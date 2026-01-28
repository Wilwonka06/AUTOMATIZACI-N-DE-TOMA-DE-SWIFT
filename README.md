# EXTRACTOR DE CÓDIGOS SWIFT - API NINJAS

## 📋 Descripción
Scripts en Python para extraer códigos SWIFT de bancos de todo el mundo usando la API de API Ninjas y guardarlos en archivos Excel con formato profesional.

## 📦 Archivos Incluidos

1. **extractor_swift_codes.py** - Versión línea de comandos
2. **extractor_swift_gui.py** - Versión con interfaz gráfica (recomendada)
3. **INSTRUCCIONES.md** - Este archivo

## 🔧 Requisitos Previos

### Bibliotecas de Python
Instale las siguientes bibliotecas:

```bash
pip install requests pandas openpyxl
```

Para la versión GUI, también necesita:
```bash
pip install tkcalendar
```

### API Key de API Ninjas

1. Regístrese en: https://api-ninjas.com/
2. Cree una cuenta gratuita (no requiere tarjeta de crédito)
3. Obtenga su API Key desde el dashboard
4. Guarde su API Key en un lugar seguro

## 🚀 Uso

### Opción 1: Versión con Interfaz Gráfica (Recomendada)

```bash
python extractor_swift_gui.py
```

**Pasos:**
1. Se abrirá una ventana gráfica
2. Ingrese su API Key de API Ninjas
3. (Opcional) Ajuste el delay entre requests
4. Haga clic en "INICIAR EXTRACCIÓN"
5. Espere a que el proceso termine (puede tomar varios minutos)
6. El archivo Excel se guardará automáticamente

**Características de la GUI:**
- Visualización del progreso en tiempo real
- Barra de progreso
- Log detallado de la extracción
- Estadísticas al finalizar
- Fácil de usar

### Opción 2: Versión Línea de Comandos

```bash
python extractor_swift_codes.py
```

**Pasos:**
1. El script le pedirá su API Key
2. Ingrese la API Key y presione Enter
3. El proceso comenzará automáticamente
4. Verá el progreso en la consola
5. Al finalizar, se guardará el archivo Excel

## 📊 Estrategia de Extracción

Debido a que la API requiere al menos un parámetro de búsqueda, el script:

1. **Búsqueda por países**: Itera sobre ~100 códigos de países (US, GB, DE, FR, etc.)
2. **Paginación**: Para cada país, obtiene hasta 100 registros por página
3. **Eliminación de duplicados**: Filtra códigos SWIFT duplicados
4. **Rate limiting**: Respeta los límites de la API con delays configurables

## 📄 Estructura del Excel Generado

El archivo Excel incluye las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| **swift_code** | Código SWIFT/BIC del banco |
| **bank_name** | Nombre completo del banco |
| **address** | Dirección de la sucursal |
| **city** | Ciudad |
| **region** | Estado/Región |
| **country** | Nombre del país |
| **country_code** | Código ISO del país (2 letras) |

**Formato aplicado:**
- Encabezados con fondo azul y texto blanco
- Bordes en todas las celdas
- Primera fila congelada
- Anchos de columna optimizados
- Datos ordenados por país y banco

## ⚙️ Configuración Avanzada

### Ajustar Delay entre Requests

Para evitar rate limiting, puede ajustar el delay:

**En la GUI:** Use el control deslizante (0.1 - 5.0 segundos)

**En línea de comandos:** Modifique esta línea:
```python
extractor.extraer_todos_los_registros(delay=0.5)  # Cambiar 0.5 por el valor deseado
```

**Recomendaciones:**
- Cuenta gratuita: 0.5 - 1.0 segundos
- Muchos requests: 0.2 - 0.3 segundos (más rápido pero puede alcanzar límites)
- Si obtiene error 429: Aumente el delay

### Agregar Más Países

Edite la lista `paises_busqueda` en el código:

```python
paises_busqueda = [
    'US', 'GB', 'DE', 'FR', 'IT', 'ES', 'CA', 'AU', 'JP', 'CN',
    # ... agregar más códigos ISO de países aquí
    'EC', 'PA', 'CR'  # Ecuador, Panamá, Costa Rica
]
```

Códigos ISO: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

## ⚠️ Limitaciones del Tier Gratuito

- **Rate Limiting**: Puede haber límites de requests por minuto/hora
- **Timeout**: Si ve error 429, el script esperará 60 segundos automáticamente
- **Datos**: La versión gratuita tiene acceso completo a la API de SWIFT codes

## 🔍 Solución de Problemas

### Error: "No se obtuvieron registros"
- Verifique que su API Key sea correcta
- Pruebe con menos países inicialmente
- Revise su conexión a internet

### Error 403: "Forbidden"
- Su API Key es incorrecta o ha expirado
- Genere una nueva API Key en api-ninjas.com

### Error 429: "Rate Limit"
- El script pausará automáticamente por 60 segundos
- Aumente el delay entre requests
- Considere usar menos países simultáneamente

### La extracción es muy lenta
- Es normal, puede tomar 10-30 minutos dependiendo de la cantidad de países
- Reduzca el delay si su cuenta lo permite
- Reduzca la lista de países si solo necesita algunos

## 💡 Consejos

1. **Primera vez**: Use la GUI y configure delay de 1.0 segundo
2. **Prueba**: Comience con 5-10 países para probar
3. **Producción**: Una vez configurado, puede ejecutar la extracción completa
4. **Interrupciones**: Puede detener con Ctrl+C - el script ofrecerá guardar lo extraído
5. **Backups**: Guarde los archivos Excel generados como respaldo

## 📈 Estadísticas Esperadas

Con la configuración por defecto (~100 países):
- **Tiempo estimado**: 15-40 minutos
- **Registros esperados**: 50,000 - 200,000+ códigos SWIFT
- **Tamaño del archivo**: 5-30 MB

## 📞 Soporte

Para problemas con la API de API Ninjas:
- Documentación: https://api-ninjas.com/api/swiftcode
- Soporte: support@api-ninjas.com

## 📝 Notas Técnicas

- Los registros se extraen en tiempo real (no hay base de datos local)
- La API retorna máximo 100 resultados por request
- El script elimina duplicados basándose en el campo `swift_code`
- Los datos se ordenan alfabéticamente por país y banco
- El formato Excel usa openpyxl (compatible con todas las versiones de Excel)

## ✅ Lista de Verificación Pre-Ejecución

- [ ] Instaladas todas las bibliotecas necesarias
- [ ] API Key de API Ninjas obtenida y probada
- [ ] Conexión a internet estable
- [ ] Espacio en disco suficiente (~100 MB libres)
- [ ] Tiempo disponible para la extracción (15-40 min)
- [ ] (GUI) Bibliotecas tkinter instaladas

---

**¡Listo para usar!** Ejecute el script y obtenga su base de datos de códigos SWIFT en minutos.
