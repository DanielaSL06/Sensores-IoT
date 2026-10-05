# 03. API REST e Ingesta de Datos de Sensores IoT en Tiempo Real

## Especificaciones Técnicas
* **Lenguaje de programación:** Python (v3.10 / v3.11)
* **Framework Web Backend:** Flask (v3.0)
* **Librerías principales:**
  * `requests`: Envío de solicitudes HTTP POST desde el cliente simulador.
  * `json`: Serialización, almacenamiento y lectura de estructuras de datos en formato JSON.
  * `csv`: Manipulación y persistencia de registros en hojas de cálculo planas (.csv).
  * `os`: Verificación de existencia de archivos e interacción con el sistema operativo.
  * `time` & `random`: Emulación de temporizadores, estampas de tiempo (*timestamps*) y generación de variables físicas de telemetría.
* **Formatos de Almacenamiento:** `.json` (persistencia para el sistema) y `.csv` (exportación para análisis en Excel).
* **Herramientas de entorno:** VS Code, Terminal de Python.

---

## Descripción del Proyecto
Este proyecto simula la arquitectura de recolección, ingesta y procesamiento continuo de datos en un entorno de Internet de las Cosas (IoT), dividido en dos módulos interconectados:

1. **Servidor Web de Ingesta y Persistencia Doble (`appSensores.py`):**
   * **Endpoint de Ingesta:** Expone la ruta HTTP `/sensores` mediante el método `POST` para recibir paquetes JSON de telemetría (temperatura, humedad y timestamp).
   * **Persistencia Dual Simultánea:** 
     * **JSON:** Almacena los registros en `datosSensor.json`, actualizando de forma estructurada el historial completo del sistema.
     * **CSV:** Exporta los datos al archivo `datosSensor.csv` formateado en tres columnas (*temperatura*, *humedad*, *timestamp*), facilitando la integración directa con herramientas de hoja de cálculo como Microsoft Excel.
   * **Procesamiento de Métricas:** Calcula de manera automática resúmenes estadísticos en consola (promedios, máximos y mínimos) a medida que ingresa cada nueva lectura.

2. **Emulador de Dispositivo IoT (`simuladorSensor.py`):**
   * **Generación de Telemetría:** Produce variaciones continuas de temperatura ($20^\circ\text{C} - 30^\circ\text{C}$) y humedad ($40\% - 60\%$) asignando estampas de tiempo Unix.
   * **Transmisión Asíncrona en Bucle:** Envía periódicamente los paquetes de datos cada 5 segundos hacia el servidor Flask mediante solicitudes `requests.post()`, mostrando en consola la respuesta HTTP del servidor.

---

## Instrucciones de Ejecución

1. Asegurarse de tener Python 3.x instalado.
2. Instalar las dependencias necesarias:
   ```bash
   pip install flask requests
