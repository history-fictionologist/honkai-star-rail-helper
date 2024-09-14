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
    def get_table_string(
        character_table: list[list[str]], color: bool = False, markdown: bool = False
    ) -> str:
        # Step 1: Determine the maximum width of content for each column
        column_widths = [
            max(len(str(item)) for item in column) for column in zip(*character_table)
        ]

        # Markdown-style separator and formatting
        if markdown:
            # Create a Markdown formatted header and separator line
            header = character_table[0]
            header_row = (
                "| "
                + " | ".join(
                    str(item).ljust(width) for item, width in zip(header, column_widths)
                )
                + " |"
            )
            separator_row = (
                "| " + " | ".join("-" * width for width in column_widths) + " |"
            )

            # Generate all data rows
            data_rows = [
                "| "
                + " | ".join(
                    str(item).ljust(width) for item, width in zip(row, column_widths)
                )
                + " |"
                for row in character_table[1:]
            ]

            # Combine header, separator, and data rows
            table_string = "\n".join([header_row, separator_row] + data_rows)
            return table_string

        # Step 2: Construct the separator line for terminal output
        separator = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"

        # Initialize a list to hold all rows and separators
        table_string = []

        # Add the first separator
        table_string.append(separator)

        for i, row in enumerate(character_table):
            # Step 3: Construct each row with the appropriate padding
            row_str = (
                "| "
                + " | ".join(
                    str(item).center(width) for item, width in zip(row, column_widths)
                )
                + " |"
            )

            # Append the row with or without colors based on the 'color' flag
            if color:
                if i == 0:
                    table_string.append(row_str)
                elif i % 2 == 1:
                    table_string.append(f"{CsvHelper.YELLOW}{row_str}{CsvHelper.RESET}")
                else:
                    table_string.append(f"{CsvHelper.PURPLE}{row_str}{CsvHelper.RESET}")
            else:
                table_string.append(row_str)

            # Add separator after the header and every other row
            if i % 2 == 0:
                table_string.append(separator)

        # Return the full table as a single string
        return "\n".join(table_string)
