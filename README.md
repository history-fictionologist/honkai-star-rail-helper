
# honkai-star-rail-helper

`honkai-star-rail-helper` is a utility designed to manage and process character data, skills, and relic recommendations for video  game [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). It reads input files, processes various attributes such as character information and skill sets, and outputs the results in an organized format. The input data is sourced from the official update packages in [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) repository and the output is stored in version-specific folders for easy management.

## Latest Character Table
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

## Key Features
- Automatically downloads character data, CVs, skill sets, and relic recommendations.
- Processes and organizes data into versioned input/output directories.
- Command-line configuration of version numbers for each new update.

## Requirements

Make sure you have the following:
- **Python 3.8+** (confirm with `python3 --version`).
- Required Python packages listed in `requirements.txt`.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies (currently no additional dependencies required):**
   ```bash
   # No need to install dependencies for now, but if needed in the future:
   # pip install -r requirements.txt
   ```

## Usage

### Run the Tool
   Navigate to the `src/` directory and run the main script with the desired version number:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Replace `<version_number>` with the current version (e.g., `2.5`).
   - If you want to skip downloading the files, add the `--skip-download` flag.

   The input files will be downloaded into the `input/{version}` folder, and the output will be saved in the `output/{version}` folder.

### Example Usage

- To run the script with version `2.5` and download the files:
  ```bash
  python3 main.py --version 2.5
  ```

- To run the script with version `2.5` and skip downloading the files:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

## Contributing

We welcome contributions! You can:
- Submit a pull request for new features or bug fixes.
- Report any issues via the issue tracker.
- Ensure that all contributions include tests and relevant documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
