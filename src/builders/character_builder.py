import logging
import os

from helpers.json_helper import JsonHelper
from model.base_type import BaseType
from model.character import Character
from model.cv_map import CvMap
from model.damage_type import DamageType
from model.model_type import ModelType
from model.path_type import PathType
from model.relic_rec import RelicRec

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("character_builder")


class CharacterBuilder:
    DEFAULT_LANGUAGE = "EN"
    RARITY_PATTERN = r"CombatPowerAvatarRarityType([0-9])"
    UI_PATH_PATTERN = r".*Manikin_Avatar_([0-9a-zA-Z]+)_([0-9a-zA-Z_]+)\.prefab"
    TEXT_MAP_FILENAME = "TextMapEN.json"
    AVATAR_CONFIG_FILENAME = "AvatarConfig.json"
    RELIC_SET_CONFIG_FILENAME = "RelicSetConfig.json"
    BASE_TYPE_FILENAME = "AvatarBaseType.json"
    RELIC_RECOMMEND_FILENAME = "AvatarRelicRecommend.json"
    AVATAR_ATLAS_FILENAME = "AvatarAtlas.json"
    CAMP_FILENAME = "AvatarCamp.json"
    DAMAGE_TYPE_FILENAME = "DamageType.json"
    NICKNAME_PLACEHOLDER = "{NICKNAME}"
    NICKNAME_HASH = "-2090701432"

    def __init__(self, json_helper: JsonHelper, language: str = None) -> None:
        if not language:
            self.language = CharacterBuilder.DEFAULT_LANGUAGE
        else:
            self.language = language

        logger.info("Creating character builder in {}".format(self.language))

        self.json_helper = json_helper
        self.text_map = self.json_helper.read("TextMap{}.json".format(self.language))
        self.avatar_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.AVATAR_CONFIG_FILENAME, "AvatarID"
        )
        self.relic_set_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.RELIC_SET_CONFIG_FILENAME, "SetID"
        )
        self.base_type_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.BASE_TYPE_FILENAME, "ID"
        )
        self.relic_recommend_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.RELIC_RECOMMEND_FILENAME, "AvatarID"
        )
        self.avatar_atlas_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.AVATAR_ATLAS_FILENAME, "AvatarID"
        )
        self.camp_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.CAMP_FILENAME, "ID"
        )
        self.damage_type_config = self.json_helper.read_json_array_as_object(
            CharacterBuilder.DAMAGE_TYPE_FILENAME, "ID"
        )

        self.characters = self.get_characters()

    def get_characters(self) -> dict[str, Character]:
        characters = {}
        for char_id in self.avatar_config:
            name = self.get_name(char_id)
            tag = self.get_tag(char_id)
            system_name = self.get_system_name(char_id)
            rarity = self.get_rarity(char_id)
            base_type = self.get_base_type(char_id)
            path_type = self.get_path_type(char_id)
            damage_type = self.get_damage_type(char_id)
            model_type = self.get_model_type(char_id)
            cv_map = self.get_cv_map(char_id)
            camp_name = self.get_camp_names(char_id)
            relic_rec = self.get_relic_rec(char_id, tag)

            character = Character(
                char_id,
                name,
                tag,
                system_name,
                rarity,
                base_type,
                path_type,
                damage_type,
                model_type,
                cv_map,
                camp_name,
                relic_rec,
            )
            characters[char_id] = character

        return characters

    def get_name(self, char_id: str) -> str:
        name = JsonHelper.find_and_translate(
            self.avatar_config, [char_id, "AvatarName"], self.text_map
        )

        if name == CharacterBuilder.NICKNAME_PLACEHOLDER:
            return JsonHelper.translate_hash(
                CharacterBuilder.NICKNAME_HASH, self.text_map
            )

        return name

    def get_full_name(self, char_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.avatar_config, [char_id, "AvatarFullName"], self.text_map
        )

    def get_tag(self, char_id: str) -> str:
        return JsonHelper.find(self.avatar_config, [char_id, "AvatarVOTag"])

    def get_system_name(self, char_id: str) -> str:
        return JsonHelper.find_and_match(
            self.avatar_config,
            [char_id, "UIAvatarModelPath"],
            CharacterBuilder.UI_PATH_PATTERN,
            2,
        )

    def get_rarity(self, char_id: str) -> int:
        rarity = JsonHelper.find_and_match(
            self.avatar_config, [char_id, "Rarity"], CharacterBuilder.RARITY_PATTERN, 1
        )
        return int(rarity)

    def get_base_type(self, char_id: str) -> BaseType:
        base_type_str = JsonHelper.find(self.avatar_config, [char_id, "AvatarBaseType"])
        return getattr(BaseType, base_type_str.upper(), None)

    def get_path_type(self, char_id: str) -> PathType:
        base_type_str = JsonHelper.find(self.avatar_config, [char_id, "AvatarBaseType"])
        path_type_str = JsonHelper.find(
            self.base_type_config, [base_type_str, "FirstWordText"]
        )
        return getattr(PathType, path_type_str.replace(" ", "_").upper(), None)

    def get_damage_type(self, char_id: str) -> DamageType:
        damage_type_str = JsonHelper.find(self.avatar_config, [char_id, "DamageType"])
        return getattr(DamageType, damage_type_str.upper(), None)

    def get_model_type(self, char_id: str) -> ModelType:
        model_type_str = JsonHelper.find_and_match(
            self.avatar_config,
            [char_id, "UIAvatarModelPath"],
            CharacterBuilder.UI_PATH_PATTERN,
            1,
        )
        return getattr(ModelType, model_type_str.upper(), None)

    def get_camp_names(self, char_id: str) -> str:
        camp_id = JsonHelper.find(self.avatar_atlas_config, [char_id, "CampID"])
        return JsonHelper.find_and_translate(
            self.camp_config, [str(camp_id), "Name"], self.text_map
        )

    def get_cv_map(self, char_id) -> CvMap:
        if char_id not in self.avatar_atlas_config:
            logger.debug("Cannot find CV for {} in avatar atlas".format(char_id))
            return CvMap()

        cv_en = JsonHelper.find_and_translate(
            self.avatar_atlas_config, [char_id, "CV_EN"], self.text_map
        )
        cv_cn = JsonHelper.find_and_translate(
            self.avatar_atlas_config, [char_id, "CV_CN"], self.text_map
        )
        cv_jp = JsonHelper.find_and_translate(
            self.avatar_atlas_config, [char_id, "CV_JP"], self.text_map
        )
        cv_kr = JsonHelper.find_and_translate(
            self.avatar_atlas_config, [char_id, "CV_KR"], self.text_map
        )
        return CvMap(cv_en, cv_cn, cv_jp, cv_kr)

    def get_relic_rec(self, char_id: str, tag: str) -> RelicRec:
        set4_id_list = JsonHelper.find(
            self.relic_recommend_config, [char_id, "Set4IDList"]
        )
        set4 = [self.get_relic_set_name(set_id) for set_id in set4_id_list]

        set2_id_list = JsonHelper.find(
            self.relic_recommend_config, [char_id, "Set2IDList"]
        )
        set2 = [self.get_relic_set_name(set_id) for set_id in set2_id_list]

        property_list = JsonHelper.find(
            self.relic_recommend_config, [char_id, "PropertyList"]
        )
        properties = [prop["PropertyType"] for prop in property_list]
        return RelicRec(Character.to_normalized_tag(tag), set4, set2, properties)

    def get_relic_set_name(self, relic_set_id: int) -> str:
        return JsonHelper.find_and_translate(
            self.relic_set_config, [str(relic_set_id), "SetName"], self.text_map
        )

    def write_characters(self) -> None:
        character_dict = {}
        for character_id, character in self.characters.items():
            character_dict[character_id] = character.to_dict(
                skip_relic_rec=True, skip_cv_map=True
            )

        self.json_helper.write(
            os.path.join(self.language, "Character.json"), character_dict
        )

    def write_relic_rec(self) -> None:
        relic_rec_dict = {}
        for char_id, character in self.characters.items():
            relic_rec_dict[char_id] = character.relics.to_dict()

        self.json_helper.write(
            os.path.join(self.language, "RelicRec.json"),
            relic_rec_dict,
        )

    def write_cv_map(self) -> None:
        cv_map_dict = {}
        for char_id, character in self.characters.items():
            cv_map_dict[char_id] = character.cv_map.to_dict()

        self.json_helper.write("CvMap.json", cv_map_dict)
