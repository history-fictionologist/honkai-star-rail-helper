import os

import requests


class FileDownloader:

    # Common prefix for the URLs
    GITHUB_BASE_URL = "https://github.com/Dimbreath/StarRailData/raw/master/"

    # List of file paths to download
    GITHUB_FILE_LIST = [
        "ExcelOutput/AvatarAtlas.json",
        "ExcelOutput/AvatarBaseType.json",
        "ExcelOutput/AvatarCamp.json",
        "ExcelOutput/AvatarConfig.json",
        "ExcelOutput/AvatarRelicRecommend.json",
        "ExcelOutput/AvatarSkillConfig.json",
        "ExcelOutput/AvatarSkillTreeConfig.json",
        "ExcelOutput/DamageType.json",
        "ExcelOutput/RelicSetConfig.json",
        "TextMap/TextMapEN.json",
        "TextMap/TextMapES.json",
        "TextMap/TextMapCHS.json",
        "TextMap/TextMapCHT.json",
        "TextMap/TextMapJP.json",
        "TextMap/TextMapKR.json",
    ]

    def __init__(self, version: int) -> None:
        self.version = version

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

        # Combine the base URL with each file path to create the full URLs
        urls = [
            FileDownloader.GITHUB_BASE_URL + file
            for file in FileDownloader.GITHUB_FILE_LIST
        ]

        # Download each file in the list
        for url in urls:
            self.download_file(url)
