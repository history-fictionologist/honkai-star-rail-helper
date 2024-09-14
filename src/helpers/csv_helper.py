import csv
import os


class CsvHelper:

    YELLOW = "\033[33m"
    PURPLE = "\033[35m"
    RESET = "\033[0m"

    def __init__(self, version: int) -> None:
        self.version = version
        self.output_path = os.path.join("..", "output", "v{}".format(self.version))

    def write_table(self, character_table: list[list[str]]) -> None:
        output_filename = os.path.join(self.output_path, "CharacterTable.csv")
        with open(output_filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(character_table)

    @staticmethod
    def print_table(character_table: list[list[str]]):
        # Step 1: Determine the maximum width of content for each column
        column_widths = [
            max(len(str(item)) for item in column) for column in zip(*character_table)
        ]

        # Step 2: Construct the separator line
        separator = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
        print(separator)

        for i, row in enumerate(character_table):
            # Step 3: Print each row with the appropriate padding
            row_str = (
                "| "
                + " | ".join(
                    str(item).center(width) for item, width in zip(row, column_widths)
                )
                + " |"
            )

            if i == 0:
                print(row_str)
            elif i % 2 == 1:
                print(f"{CsvHelper.YELLOW}{row_str}{CsvHelper.RESET}")
            else:
                print(f"{CsvHelper.PURPLE}{row_str}{CsvHelper.RESET}")

            # Step 4: Print the separator line after the header and after the table
            if i % 2 == 0:
                print(separator)
