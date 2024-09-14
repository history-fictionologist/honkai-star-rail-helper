from builders.character_builder import CharacterBuilder
from builders.character_table_builder import CharacterTableBuilder
from helpers.csv_helper import CsvHelper
from helpers.file_downloader import FileDownloader
from helpers.json_helper import JsonHelper
from builders.skill_set_builder import SkillSetBuilder


def run(version: int, skip_download: bool = False) -> None:
    if not skip_download:
        file_downloader = FileDownloader(version)
        file_downloader.download_all_files()

    json_helper = JsonHelper(version)
    csv_helper = CsvHelper(version)

    character_builder = CharacterBuilder(json_helper)
    character_builder.write_characters()
    character_builder.write_cv_map()

    character_table_builder = CharacterTableBuilder(character_builder, csv_helper)
    character_table_builder.write_character_table()
    character_table_builder.print_character_table()

    languages = ["EN", "ES", "CHS", "CHT", "JP", "KR"]
    for language in languages:
        CharacterBuilder(json_helper, language).write_relic_rec()
        SkillSetBuilder(json_helper, language).write_skill_sets()


if __name__ == "__main__":
    run(25, True)
