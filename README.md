# EXTRACTOR DE CÓDIGOS SWIFT - SELENIUM

## 📋 Descripción
Este proyecto contiene scripts en Python diseñados para extraer códigos SWIFT (BIC) de bancos de múltiples países utilizando **Selenium** para realizar web scraping automatizado desde el sitio `bank.codes`.

El flujo de trabajo consiste en extraer la información país por país y luego consolidar todos los datos en un único archivo Excel maestro.

## 📦 Archivos del Proyecto

1. **extractor_selenium.py**: Script principal que navega por la web, extrae los datos de bancos (Nombre, Ciudad, Rama, Código SWIFT) y genera un archivo Excel individual por cada país.
2. **unir_swift.py**: Script de utilidad que toma todos los archivos Excel generados en la carpeta `countries_excel` y los une en un único archivo final llamado `SWIFT_ALL_COUNTRIES_FINAL.xlsx`.
3. **requirements.txt**: Lista de dependencias necesarias.

## 🔧 Requisitos Previos

### Software
- **Python 3.x** instalado.
- **Google Chrome** instalado (el script usa Chrome WebDriver).

### Bibliotecas de Python
Es necesario instalar las bibliotecas requeridas. Puede hacerlo ejecutando:

```bash
pip install pandas openpyxl selenium webdriver-manager
```

> **Nota:** Aunque existe un archivo `requirements.txt`, asegúrese de tener instaladas `selenium` y `webdriver-manager` que son críticas para este script.

## 🚀 Instrucciones de Uso

### Paso 1: Extracción de Datos
Ejecute el script de extracción. Este proceso abrirá una ventana de navegador controlada automáticamente y comenzará a navegar por las páginas de códigos SWIFT de los países configurados.

```bash
python extractor_selenium.py
```

- El script creará automáticamente una carpeta llamada `countries_excel`.
- Guardará un archivo Excel por cada país (ej. `Espana.xlsx`, `Alemania.xlsx`).
- Si se interrumpe, puede volver a ejecutarlo; el script detectará los archivos ya creados y saltará esos países para continuar con los faltantes.

### Paso 2: Consolidación de Datos
Una vez finalizada la extracción (o cuando desee unir lo que lleva procesado), ejecute el script de unión:

```bash
python unir_swift.py
```

- Este script leerá todos los archivos `.xlsx` dentro de `countries_excel`.
- Generará un archivo maestro llamado **`SWIFT_ALL_COUNTRIES_FINAL.xlsx`** en la carpeta raíz.

## 📄 Estructura de los Datos
El archivo final contendrá las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| **country** | País del banco |
| **bank_name** | Nombre de la entidad bancaria |
| **city** | Ciudad de la sucursal |
| **branch** | Nombre o detalle de la sucursal |
| **swift_code** | Código SWIFT/BIC (8 u 11 caracteres) |

## ⚙️ Configuración
Si desea modificar la lista de países a buscar, edite la lista `COUNTRIES` dentro del archivo `extractor_selenium.py`.

```python
COUNTRIES = [
    "Albania", "Argelia", "Andorra", ...
]
```

## ⚠️ Notas Importantes
- **Tiempo de ejecución**: El scraping puede tomar tiempo dependiendo de la cantidad de países y páginas por país.
- **Estabilidad**: El script incluye esperas (`sleep`) para no saturar el servidor y dar tiempo a que carguen los elementos.
- **Archivos temporales**: No borre la carpeta `countries_excel` hasta que haya generado el archivo final consolidado.
