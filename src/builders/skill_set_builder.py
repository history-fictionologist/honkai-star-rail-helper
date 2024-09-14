import logging
import os
from typing import Any

from helpers.json_helper import JsonHelper
from model.character import Character
from model.skill import Skill
from model.skill_set import SkillSet

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("skill_set_builder")


class SkillSetBuilder:

    DEFAULT_LANGUAGE = "EN"
    SKILL_CONFIG_FILENAME = "AvatarSkillConfig.json"
    AVATAR_CONFIG_FILENAME = "AvatarConfig.json"

    def __init__(self, json_helper: JsonHelper, language: str = None) -> None:
        if not language:
            self.language = SkillSetBuilder.DEFAULT_LANGUAGE
        else:
            self.language = language

        self.json_helper = json_helper
        self.text_map = self.json_helper.read("TextMap{}.json".format(self.language))
        self.skill_config = self.json_helper.read_json_array_as_object(
            SkillSetBuilder.SKILL_CONFIG_FILENAME, "SkillID"
        )
        self.avatar_config = self.json_helper.read_json_array_as_object(
            SkillSetBuilder.AVATAR_CONFIG_FILENAME, "AvatarID"
        )

    def write_skill_sets(self) -> None:
        skill_set_by_char = {}

        for skill_id in self.skill_config:
            char_id = str(int(skill_id) // 100)
            tag = Character.to_normalized_tag(
                JsonHelper.find(self.avatar_config, [char_id, "AvatarVOTag"])
            )

            skill_name = self.get_skill_name(skill_id)
            skill_tag = self.get_skill_tag(skill_id)
            skill_type_desc = self.get_skill_type_desc(skill_id)
            level = self.get_level(skill_id)
            max_level = self.get_max_level(skill_id)
            skill_desc = self.get_skill_desc(skill_id)
            simple_skill_desc = self.get_simple_skill_desc(skill_id)
            stance_damage_type = self.get_stance_damage_type(skill_id)
            attack_type = self.get_attack_type(skill_id)
            skill_effect = self.get_skill_effect(skill_id)

            skill = Skill(
                skill_id,
                skill_name,
                skill_tag,
                skill_type_desc,
                level,
                max_level,
                skill_desc,
                simple_skill_desc,
                stance_damage_type,
                attack_type,
                skill_effect,
            )

            SkillSetBuilder.add_skill(skill_set_by_char, char_id, tag, skill)

        skill_set_dict = SkillSetBuilder.transform_and_sort(skill_set_by_char)
        self.json_helper.write(
            os.path.join(self.language, "SkillSet.json"),
            skill_set_dict,
        )

    def get_skill_name(self, skill_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.skill_config,
            [skill_id, "SkillName"],
            self.text_map,
        )

    def get_skill_tag(self, skill_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.skill_config,
            [skill_id, "SkillTag"],
            self.text_map,
        )

    def get_skill_type_desc(self, skill_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.skill_config,
            [skill_id, "SkillTypeDesc"],
            self.text_map,
        )

    def get_level(self, skill_id: str) -> int:
        return JsonHelper.find(self.skill_config, [skill_id, "Level"])

    def get_max_level(self, skill_id: str) -> int:
        return JsonHelper.find(
            self.skill_config,
            [skill_id, "MaxLevel"],
        )

    def get_skill_desc(self, skill_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.skill_config,
            [skill_id, "SkillDesc"],
            self.text_map,
        )

    def get_simple_skill_desc(self, skill_id: str) -> str:
        return JsonHelper.find_and_translate(
            self.skill_config,
            [skill_id, "SimpleSkillDesc"],
            self.text_map,
        )

    def get_stance_damage_type(self, skill_id: str) -> str:
        return JsonHelper.find(
            self.skill_config,
            [skill_id, "StanceDamageType"],
        )

    def get_attack_type(self, skill_id: str) -> str:
        return JsonHelper.find(
            self.skill_config,
            [skill_id, "AttackType"],
        )

    def get_skill_effect(self, skill_id: str) -> str:
        return JsonHelper.find(
            self.skill_config,
            [skill_id, "SkillEffect"],
        )

    @staticmethod
    def add_skill(
        skill_sets: dict[str, SkillSet],
        char_id: str,
        tag: str,
        skill: Skill,
    ) -> None:
        if char_id not in skill_sets:
            skill_sets[char_id] = SkillSet(char_id, tag)

        skill_sets[char_id].add_skill(skill)

    @staticmethod
    def transform_and_sort(
        skill_sets: dict[str, SkillSet]
    ) -> dict[str, dict[str, Any]]:
        return {
            char_id: skill_set.to_dict()
            for char_id, skill_set in sorted(skill_sets.items())
        }
