import re
from typing import Dict, Any

from model.base_type import BaseType
from model.cv_map import CvMap
from model.damage_type import DamageType
from model.model_type import ModelType
from model.path_type import PathType
from model.relic_rec import RelicRec


class Character:

    def __init__(
        self,
        char_id: str,
        name: str,
        tag: str,
        system_name: str = None,
        rarity: int = 0,
        base_type: BaseType = None,
        path_type: PathType = None,
        damage_type: DamageType = None,
        model_type: ModelType = None,
        cv_map: CvMap = None,
        camp: str = None,
        relics: RelicRec = None,
    ):

        self.char_id = char_id
        self.name = name
        self.tag = tag
        self.system_name = system_name
        self.rarity = rarity
        self.base_type = base_type
        self.path_type = path_type
        self.damage_type = damage_type
        self.model_type = model_type
        self.cv_map = cv_map
        self.camp = camp
        self.relics = relics

    def group(self) -> int:
        return int(self.char_id) // 10

    def to_dict(
        self, skip_relic_rec: bool = False, skip_cv_map: bool = False
    ) -> Dict[str, Any]:
        result = {
            "Name": self.name,
            "Tag": self.tag,
            "SystemName": self.system_name,
            "Rarity": self.rarity,
            "BaseType": self.base_type.name if self.base_type else None,
            "PathType": self.path_type.name if self.path_type else None,
            "DamageType": self.damage_type.name if self.damage_type else None,
            "ModelType": self.model_type.name if self.model_type else None,
            "Camp": self.camp,
            "Group": self.group(),
        }

        if not skip_relic_rec:
            result["RelicRec"] = self.relics.to_dict() if self.relics else None

        if not skip_cv_map:
            result["CV"] = self.cv_map.to_dict() if self.cv_map else None

        return result

    @staticmethod
    def to_normalized_tag(tag: str) -> str:
        # Regular expression to match tags and capture the player number
        match = re.match(r"(playergirl|playerboy)(\d*)", tag)
        if match:
            player_number = match.group(2)
            return f"player{player_number}"

        return tag
