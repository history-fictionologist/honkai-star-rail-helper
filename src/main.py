import argparse
import re

from builders.character_builder import CharacterBuilder
from builders.character_table_builder import CharacterTableBuilder
from helpers.csv_helper import CsvHelper
from helpers.file_downloader import FileDownloader
from helpers.json_helper import JsonHelper
from builders.skill_set_builder import SkillSetBuilder


def run(version: int, skip_download: bool = False, languages: list = None) -> None:
    # Use default list of languages if none are provided
    if languages is None:
        languages = FileDownloader.get_supported_languages()
    print("Supported languages: {}".format(languages))

    if not skip_download:
        file_downloader = FileDownloader(version, languages)
        file_downloader.download_all_files()

    json_helper = JsonHelper(version)
    csv_helper = CsvHelper(version)

    character_builder = CharacterBuilder(json_helper)
    character_builder.write_characters()
    character_builder.write_cv_map()

    character_table_builder = CharacterTableBuilder(character_builder, csv_helper)
    character_table_builder.write_character_table()
    character_table_builder.update_character_table()

    for language in languages:
        CharacterBuilder(json_helper, language).write_relic_rec()
        SkillSetBuilder(json_helper, language).write_skill_sets()


def validate_version(value: str) -> str:
    # Regular expression to match x.y format, where x and y are digits
    if not re.match(r"^\d+\.\d+$", value):
        raise argparse.ArgumentTypeError(
            "Version number must be in x.y format (e.g., 2.5 or 1.0)."
        )
    return value


def convert_version(version_str: str) -> int:
    # Remove the decimal point and convert the resulting string to an integer
    return int(version_str.replace(".", ""))


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Process character data and build tables."
    )

    # Add version argument with validation
    parser.add_argument(
        "--version",
        type=validate_version,  # Validate the version format
        required=True,
        help="Version number in x.y format (e.g., 2.5 or 1.0).",
    )

    # Add skip-download argument
    parser.add_argument(
        "--skip-download", action="store_true", help="Skip downloading files."
    )

    # Add languages argument as a list (optional)
    parser.add_argument(
        "--languages",
        nargs="+",  # Allows one or more languages to be passed
        help="List of languages to process (e.g., EN JP KR). Defaults to all languages.",
    )

    args = parser.parse_args()

    # Convert the version number from x.y to xy format
    version_numeric = convert_version(args.version)

    # Run the script with the validated and converted version number
    run(version_numeric, args.skip_download, args.languages)


# Example usage:
# To run the script with version 2.5 and download the files:
# python3 main.py --version 2.5
#
# To run the script with version 2.5 and skip downloading the files:
# python3 main.py --version 2.5 --skip-download
#
# To run the script with version 2.5 and download the files for specific languages (e.g., EN and JP):
# python3 main.py --version 2.5 --languages EN JP
