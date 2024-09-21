
# honkai-star-rail-helper

`honkai-star-rail-helper` es una utilidad diseñada para gestionar y procesar datos de personajes, habilidades y recomendaciones de reliquias para el videojuego [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Lee archivos de entrada, procesa varios atributos como la información de los personajes y conjuntos de habilidades, y genera los resultados en un formato organizado. Los datos de entrada provienen de los paquetes de actualización oficiales del repositorio [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) y la salida se guarda en carpetas específicas de la versión para una gestión sencilla.

## Última Tabla de Personajes
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION        | THE_HUNT | ERUDITION | HARMONY | NIHILITY      | PRESERVATION | ABUNDANCE |
| ----------- | ------ | ------------------ | -------- | --------- | ------- | ------------- | ------------ | --------- |
| PHYSICAL    | 5      | clara|player|yunli | boothill | argenti   | robin   |               |              |           |
| PHYSICAL    | 4      |                    | sushang  |           | hanya   | luka          |              | natasha   |
| FIRE        | 5      | sam                | topaz    | himeko    |         | jiaoqiu       | player2      | lingsha   |
| FIRE        | 4      | hook               |          |           | asta    | guinaifen     |              | gallagher |
| ICE         | 5      | jingliu            | yanqing  |           | ruanmei |               | gepard       |           |
| ICE         | 4      | misha              |          | herta     |         | pela          | mar7th       |           |
| LIGHTENING  | 5      |                    |          | jingyuan  |         | acheron|kafka |              | bailu     |
| LIGHTENING  | 4      | arlan              | moze     | serval    | tingyun |               |              |           |
| WIND        | 5      | blade              | feixiao  |           | bronya  | blackswan     |              | huohuo    |
| WIND        | 4      |                    | danheng  |           |         | sampo         |              |           |
| QUANTUM     | 5      |                    | seele    | jade      | sparkle | silverwolf    | fuxuan       |           |
| QUANTUM     | 4      | xueyi              |          | qingque   |         |               |              | lynx      |
| IMAGINARY   | 5      | danhengil          | drratio  |           | player3 | welt          | aventurine   | luocha    |
| IMAGINARY   | 4      |                    | mar7th2  |           | yukong  |               |              |           |
<!-- CHARACTER_TABLE_END -->

## Funciones Clave
- Descarga automáticamente datos de personajes, CVs, conjuntos de habilidades y recomendaciones de reliquias.
- Procesa y organiza los datos en directorios de entrada/salida versionados.
- Configuración desde la línea de comandos de los números de versión para cada nueva actualización.

## Requisitos

Asegúrate de tener lo siguiente:
- **Python 3.8+** (confirma con `python3 --version`).
- Paquetes de Python requeridos listados en `requirements.txt`.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Opcional) Crea y activa un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scriptsctivate
   ```

3. **Instala las dependencias (actualmente no hay dependencias adicionales):**
   ```bash
   # No es necesario instalar dependencias por ahora, pero si es necesario en el futuro:
   # pip install -r requirements.txt
   ```

## Uso

### Ejecutar la herramienta
   Navega al directorio `src/` y ejecuta el script principal con el número de versión deseado:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Reemplaza `<version_number>` con la versión actual (por ejemplo, `2.5`).
   - Si deseas omitir la descarga de los archivos, agrega la bandera `--skip-download`.

   Los archivos de entrada se descargarán en la carpeta `input/{version}`, y la salida se guardará en la carpeta `output/{version}`.

### Ejemplo de uso

- Para ejecutar el script con la versión `2.5` y descargar los archivos:
  ```bash
  python3 main.py --version 2.5
  ```

- Para ejecutar el script con la versión `2.5` y omitir la descarga de los archivos:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Para ejecutar el script con la versión 2.5 y descargar los archivos para idiomas específicos (por ejemplo, EN y JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Contribuciones

¡Aceptamos contribuciones! Puedes:
- Enviar una solicitud de extracción para nuevas funciones o corrección de errores.
- Informar cualquier problema a través del rastreador de problemas.
- Asegúrate de que todas las contribuciones incluyan pruebas y documentación relevante.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
