from typing import Any


class Skill:

    def __init__(
        self,
        skill_id: str,
        skill_name: str,
        skill_tag: str,
        skill_type_desc: str,
        level: int = 0,
        max_level: int = 0,
        skill_desc: str = None,
        simple_skill_desc: str = None,
        stance_damage_type: str = None,
        attack_type: str = None,
        skill_effect: str = None,
    ):

        self.skill_id = skill_id
        self.skill_name = skill_name
        self.skill_tag = skill_tag
        self.skill_type_desc = skill_type_desc
        self.level = level
        self.max_level = max_level
        self.skill_desc = skill_desc
        self.simple_skill_desc = simple_skill_desc
        self.stance_damage_type = stance_damage_type
        self.attack_type = attack_type
        self.skill_effect = skill_effect

    def to_dict(self) -> dict[str, Any]:
        return {
            "SkillID": int(self.skill_id),
            "SkillName": self.skill_name,
            "SkillTag": self.skill_tag,
            "SkillTypeDesc": self.skill_type_desc,
            "MinLevel": self.level,
            "MaxLevel": self.max_level,
            "StanceDamageType": self.stance_damage_type,
            "AttackType": self.attack_type,
            "SkillEffect": self.skill_effect,
            "SkillDesc": self.skill_desc,
            "SimpleSkillDesc": self.simple_skill_desc,
        }
