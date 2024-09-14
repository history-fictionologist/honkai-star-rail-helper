import json
import logging
import os
import re
from typing import Any, Optional, Union

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("json_helper")


class JsonHelper:
    def __init__(self, version: int) -> None:
        self.version = version
        self.input_path = os.path.join("..", "input", "v{}".format(self.version))
        self.output_path = os.path.join("..", "output", "v{}".format(self.version))
        self.jsona_indent = 2
        self.mode = 0o755

        os.makedirs(self.input_path, mode=self.mode, exist_ok=True)
        os.makedirs(self.output_path, mode=self.mode, exist_ok=True)

    def read(self, filename: str) -> Union[dict[str, Any], list[dict[str, Any]]]:
        with open(os.path.join(self.input_path, filename), "r") as file:
            data = json.load(file)

        return data

    def read_json_array_as_object(self, filename: str, key_attr: str) -> dict[str, Any]:
        data = self.read(filename)
        if isinstance(data, dict):
            return data

        json_object = {}
        for item in data:
            if key_attr in item and str(item[key_attr]) not in json_object:
                json_object[str(item[key_attr])] = item

        return json_object

    def write(
        self, filename: str, json_data: dict[str, Any], debug: bool = False
    ) -> None:
        if debug:
            self.print_json(json_data)

        # Full path including directories from filename
        full_path = os.path.join(self.output_path, filename)

        # Ensure the directory for the full path exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Write the JSON data to the file
        with open(full_path, "w") as file:
            json.dump(json_data, file, ensure_ascii=False, indent=self.jsona_indent)

    def print_json(self, json_data: dict[str, Any]) -> None:
        pretty_dict = json.dumps(
            json_data, ensure_ascii=False, indent=self.jsona_indent
        )
        print(pretty_dict)

    @staticmethod
    def find(data: dict[str, Any], keys: list[str]) -> Any:
        current_data = data
        for key in keys:
            if key not in current_data:
                logging.debug("Cannot find key {} in json".format(key))
                return None

            current_data = current_data[key]

        return current_data

    @staticmethod
    def upsert(data: dict[str, Any], keys: list[str], value: Any) -> None:
        current_data = data
        for key in keys[:-1]:
            if key not in current_data:
                current_data[key] = {}

            current_data = current_data[key]

        current_data[keys[-1]] = value

    @staticmethod
    def append(data: dict[str, Any], keys: list[str], value: Any) -> None:
        current_data = data
        for key in keys[:-1]:
            if key not in current_data:
                current_data[key] = {}

            current_data = current_data[key]

        last_key = keys[-1]
        if last_key not in current_data:
            current_data[last_key] = []

        current_data[last_key].append(value)

    @staticmethod
    def translate_hash(hash_str: str, text_map: dict[str, Any]):
        if hash_str == "None":
            logging.debug("Cannot find hash None in text map")
            return ""

        if hash_str in text_map:
            return text_map[hash_str]

        stable_hash_str = JsonHelper.get_stable_hash(hash_str)
        if stable_hash_str in text_map:
            return text_map[stable_hash_str]

        logging.debug("Cannot find hash {} in text map".format(hash_str))
        return ""

    @staticmethod
    def find_and_translate(
        data: dict[str, Any], keys: list[str], text_map: dict[str, Any]
    ) -> str:
        if keys[-1] != "Hash":
            keys.append("Hash")

        hash_str = str(JsonHelper.find(data, keys))
        return JsonHelper.translate_hash(hash_str, text_map)

    @staticmethod
    def match_regex(text: str, pattern: Optional[str], group_index: int) -> str:
        if not pattern:
            return text

        match = re.search(pattern, text)
        if not match:
            raise Exception(
                "Text and pattern do not match, text: {}, pattern: {}".format(
                    text, pattern
                )
            )

        return match.group(group_index)

    @staticmethod
    def find_and_match(
        data: dict[str, Any], keys: list[str], pattern: Optional[str], group_index: int
    ) -> str:
        text = JsonHelper.find(data, keys)
        return JsonHelper.match_regex(text, pattern, group_index)

    @staticmethod
    def get_stable_hash(hash_str: str) -> str:
        if hash_str.startswith("-"):
            return JsonHelper.get_stable_hash(str(abs(int(hash_str))))

        hash1 = 5381
        hash2 = hash1

        i = 0
        while i < len(hash_str):
            hash1 = ((hash1 << 5) + hash1) ^ int(hash_str[i])
            if i == len(hash_str) - 1:
                break

            hash2 = ((hash2 << 5) + hash2) ^ int(hash_str[i + 1])
            i += 2

        return str(hash1 + (hash2 * 1566083941))
