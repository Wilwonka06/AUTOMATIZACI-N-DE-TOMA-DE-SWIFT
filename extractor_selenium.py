from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from time import sleep
import os

# ==============================
# CONFIG SELENIUM
# ==============================
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ==============================
# LISTA DE PAÍSES
# ==============================
COUNTRIES = [
    "Albania", "Argelia", "Andorra", "Angola", "Argentina", "Armenia", "Aruba", "Australia", "Austria", 
    "Azerbaiyán", "Bahamas", "Bahrain", "Bangladés", "Barbados", "Bélgica", "Benin", "islas Bermudas", 
    "Bután", "Bolivia", "Botswana", "Brasil","Brunei", "Bulgaria", "Burkina Faso", "Camboya", "Canadá", 
    "Cabo Verde", "Islas Caimán", "Chile", "China", "Colombia", "Costa Rica", "Croacia", "Chipre", 
    "República Checa", "Dinamarca", "Dominio", "República Dominicana", "Ecuador", "Egipto", "El Salvador", 
    "Estonia", "Etiopía", "Fiji", "Finlandia", "Francia", "Polinesia francés", "Gabón", "Gambia", "Georgia", 
    "Alemania", "Ghana", "Grecia", "Granada", "Guatemala", "Guinea", "Guinea Bissau", "Guayana", "Haití", 
    "Honduras", "Hong Kong", "Hungría", "Islandia", "India", "Indonesia", "Irlanda", "Israel", "Italia", 
    "Jamaica", "Japón", "Kazajstán", "Kenia", "Kosovo", "Kuwait", "Kirguistán", "Laos", "Letonia", "Líbano", 
    "Lesoto", "Liberia", "Liechtenstein", "Lituania", "Luxemburgo", "Macaomacedonia", "Malawi", "Malasia", 
    "Maldivas", "Mali", "Malta", "Mauritania", "Mauricio", "México", "Moldava", "Mónaco", "Mongolia", "Montenegro", 
    "Marruecos", "Mozambique", "Namibia", "Nepal", "Países Bajos", "Nueva Zelanda", "Nicaragua", "Níger", 
    "Nigeria", "Noruega", "Omán", "Pakistán", "Palau", "Panamá", "Papúa Nueva Guinea", "Paraguay" "Perú",
    "Filipinas", "Polonia", "Portugal", "Katar", "Rumanía", "Rusia", "Ruanda", "Santa Lucía", "Samoa", "San Marino", 
    "Arabia Saudita", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Eslovaquia", "Eslovenia", 
    "Sudáfrica", "Corea del Sur", "España", "Sri Lanka", "Surinam", "Suecia", "Suiza", "Taiwán", "Tayikistán", 
    "Tanzania", "Tailandia", "Tonga", "Túnez", "Turquía", "Tuvalu", "Uganda", "Ucrania", "Emiratos Árabes Unidos", 
    "Reino Unido", "Estados Unidos", "Uruguay", "Uzbekistán", "Vanuatu", "Ciudad del Vaticano", "Vietnam", "Zambia"
 ]

# ==============================
# SCRAPER POR PAÍS
# ==============================
def scrape_country(driver, country):
    slug = country.lower().replace(" ", "-")
    page = 1
    results = []

    print(f"🚀 {country}")

    while True:
        if page == 1:
            url = f"https://bank.codes/swift-code/{slug}/"
        else:
            url = f"https://bank.codes/swift-code/{slug}/page/{page}/"

        driver.get(url)

        try:
            WebDriverWait(driver, 8).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "table.swift-country tbody tr")
                )
            )
        except TimeoutException:
            break

        rows = driver.find_elements(By.CSS_SELECTOR, "table.swift-country tbody tr")

        if not rows:
            break

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) == 5:
                results.append({
                    "country": country,
                    "bank_name": cols[1].text.strip(),
                    "city": cols[2].text.strip(),
                    "branch": cols[3].text.strip(),
                    "swift_code": cols[4].text.strip()
                })

        page += 1
        sleep(0.7)

    return results

# ==============================
# EJECUCIÓN + CHECKPOINT
# ==============================
OUTPUT_DIR = "countries_excel"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for country in COUNTRIES:
    filename = f"{country.replace(' ', '_')}.xlsx"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        print(f"⏭️ {country} ya existe, se omite")
        continue

    data = scrape_country(driver, country)

    if data:
        pd.DataFrame(data).to_excel(filepath, index=False)
        print(f"Guardado {filepath}")
    else:
        print(f"Sin datos {country}")

driver.quit()
print("\nSCRAPING FINALIZADO POR PAÍS")