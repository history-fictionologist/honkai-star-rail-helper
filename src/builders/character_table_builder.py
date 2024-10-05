import bisect
import os
import re

from builders.character_builder import CharacterBuilder
from helpers.csv_helper import CsvHelper
from model.character import Character
from model.damage_type import DamageType
from model.path_type import PathType


class CharacterTableBuilder:
    def __init__(
        self, character_builder: CharacterBuilder, csv_helper: CsvHelper
    ) -> None:
        self.character_builder = character_builder
        self.csv_helper = csv_helper
        self.character_list = self.get_character_list()

    def get_character_dict(self) -> dict[str, dict]:
        character_dict = self.character_builder.get_characters()

        nested_character_dict = {}
        for damage_type in DamageType:
            nested_character_dict[damage_type.name] = {}
            for path_type in list(PathType)[:-1]:
                nested_character_dict[damage_type.name][path_type.name] = {}
                for rarity in [5, 4]:
                    nested_character_dict[damage_type.name][path_type.name][rarity] = []

        for character_id, character in character_dict.items():
            name = character.name
            damage_type = character.damage_type.name
            path_type = character.path_type.name
            rarity = character.rarity

            name_list = nested_character_dict[damage_type][path_type][rarity]
            if name not in name_list:
                bisect.insort(
                    nested_character_dict[damage_type][path_type][rarity], name
                )

        return CharacterTableBuilder.sort_character_dict(nested_character_dict)

    def get_character_list(self) -> list[list[str]]:
        cells = self.get_cells()
        lines = [CharacterTableBuilder.get_header()]
        index = 0

        for damage_type in DamageType:
            damage_type_name = DamageType.to_normalized_damage_type(damage_type)
            for rarity in [5, 4]:
                line = [damage_type_name, rarity]
                for _ in range(7):
                    line.append(cells[index])
                    index += 1
                lines.append(line)

        return lines

    def get_cells(self) -> list[str]:
        character_dict = self.get_character_dict()
        cells = []
        for damage_type in DamageType:
            for rarity in [5, 4]:
                for path_type in list(PathType)[:-1]:
                    cell_text = "|".join(
                        character_dict[damage_type.name][path_type.name][rarity]
                    )
                    cells.append(cell_text)

        return cells

    def write_character_table(self):
        self.csv_helper.write_table(self.character_list)

    def update_character_table(self):
        print(CsvHelper.get_table_string(self.character_list, True, False))

        # Define the start and end markers in the README
        start_marker = "<!-- CHARACTER_TABLE_START -->"
        end_marker = "<!-- CHARACTER_TABLE_END -->"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        readme_path = os.path.join(script_dir, "../../README.md")

        # Read the current README content
        with open(readme_path, "r") as file:
            readme_content = file.read()

        # Get the new character table string
        new_table_string = CsvHelper.get_table_string(self.character_list, False, True)

        # Find the current table section (between the markers) and replace it
        updated_content = re.sub(
            f"{start_marker}.*?{end_marker}",
            f"{start_marker}\n{new_table_string}\n{end_marker}",
            readme_content,
            flags=re.DOTALL,
        )

        # Write the updated content back to the README
        with open(readme_path, "w") as file:
            file.write(updated_content)

    @staticmethod
    def sort_character_dict(nested_character_dict: dict[str, dict]) -> dict[str, dict]:
        sorted_character_dict = {}
        for damage_type, damage_dict in nested_character_dict.items():
            sorted_character_dict[damage_type] = dict(
                sorted(damage_dict.items(), key=lambda item: item[0])
            )

        sorted_character_dict = dict(
            sorted(sorted_character_dict.items(), key=lambda item: item[0])
        )

        return sorted_character_dict

    @staticmethod
    def get_header():
        header = ["DAMAGE_TYPE", "RARITY"]
        for path_type in list(PathType)[:-1]:
            header.append(path_type.name)

        return header
