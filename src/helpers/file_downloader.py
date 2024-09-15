import os
import re
import requests


class FileDownloader:

    # Common prefix for the URLs
    GITHUB_BASE_URL = "https://github.com/Dimbreath/StarRailData/raw/master/"
    GITHUB_API_URL = "https://api.github.com/repos/Dimbreath/StarRailData/contents/"

    # List of common file paths to download (non-language-specific)
    GITHUB_COMMON_FILE_LIST = [
        "ExcelOutput/AvatarAtlas.json",
        "ExcelOutput/AvatarBaseType.json",
        "ExcelOutput/AvatarCamp.json",
        "ExcelOutput/AvatarConfig.json",
        "ExcelOutput/AvatarRelicRecommend.json",
        "ExcelOutput/AvatarSkillConfig.json",
        "ExcelOutput/AvatarSkillTreeConfig.json",
        "ExcelOutput/DamageType.json",
        "ExcelOutput/RelicSetConfig.json",
    ]

    # Base path for language-specific TextMap files
    TEXT_MAP_DIR = "TextMap/"

    def __init__(self, version: int, languages: list = None) -> None:
        self.version = version
        self.languages = languages or FileDownloader.get_supported_languages()

        # Path where the files will be saved
        self.save_path = os.path.join("..", "input", f"v{self.version}")

    # Function to download a file from a URL
    def download_file(self, url):
        # Extract the file name from the URL
        file_name = url.split("/")[-1]
        # Full path for the file
        file_path = os.path.join(self.save_path, file_name)

        # Download the file
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"File {file_name} downloaded and saved to {file_path}")
        else:
            print(
                f"Failed to download {file_name}. Status code: {response.status_code}"
            )

    def download_all_files(self):
        # Ensure the directory exists
        os.makedirs(self.save_path, exist_ok=True)

        # Download common files
        for file in FileDownloader.GITHUB_COMMON_FILE_LIST:
            url = FileDownloader.GITHUB_BASE_URL + file
            self.download_file(url)

        # Download language-specific TextMap files
        for language in self.languages:
            text_map_file = f"{FileDownloader.TEXT_MAP_DIR}TextMap{language}.json"
            url = FileDownloader.GITHUB_BASE_URL + text_map_file
            self.download_file(url)

    @staticmethod
    def get_supported_languages() -> list:
        """Fetch the list of available language abbreviations by listing files in the TextMap directory."""
        response = requests.get(
            FileDownloader.GITHUB_API_URL + FileDownloader.TEXT_MAP_DIR
        )

        if response.status_code == 200:
            # Extract filenames from the API response
            files = response.json()
            language_set = set()
            pattern = r"TextMap(Main)?([A-Z]+)\.json"

            # Loop through files and extract language abbreviations
            for file in files:
                match = re.search(pattern, file["name"])
                if match:
                    language_set.add(match.group(2))

            # Return the sorted list of unique languages
            return sorted(language_set)
        else:
            print(
                f"Failed to fetch directory content. Status code: {response.status_code}"
            )
            return []
