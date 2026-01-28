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
    "Albania","Algeria","Andorra","Angola","Argentina","Armenia","Aruba","Australia",
    "Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belgium",
    "Benin","Bermuda","Bhutan","Bolivia","Botswana","Brazil","Brunei","Bulgaria",
    "Burkina Faso","Cambodia","Canada","Cape Verde","Cayman Islands","Chile","China",
    "Colombia","Costa Rica","Croatia","Cyprus","Czech Republic","Denmark","Dominica",
    "Dominican Republic","Ecuador","Egypt","El Salvador","Estonia","Ethiopia","Fiji",
    "Finland","France","French Polynesia","Gabon","Gambia","Georgia","Germany","Ghana",
    "Greece","Grenada","Guatemala","Guinea","Guinea Bissau","Guyana","Haiti","Honduras",
    "Hong Kong","Hungary","Iceland","India","Indonesia","Ireland","Israel","Italy",
    "Jamaica","Japan","Kazakhstan","Kenya","Kosovo","Kuwait","Kyrgyzstan","Laos",
    "Latvia","Lebanon","Lesotho","Liberia","Liechtenstein","Lithuania","Luxembourg",
    "Macao","Macedonia","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania",
    "Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Morocco",
    "Mozambique","Namibia","Nepal","Netherlands","New Zealand","Nicaragua","Niger",
    "Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea",
    "Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia",
    "Rwanda","Saint Lucia","Samoa","San Marino","Saudi Arabia","Senegal","Serbia",
    "Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa",
    "South Korea","Spain","Sri Lanka","Suriname","Sweden","Switzerland","Taiwan",
    "Tajikistan","Tanzania","Thailand","Tonga","Tunisia","Turkey","Tuvalu","Uganda",
    "Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay",
    "Uzbekistan","Vanuatu","Vatican City","Vietnam","Zambia"
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