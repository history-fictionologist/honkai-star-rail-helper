from typing import Dict, Any


class RelicRec:

    def __init__(self, tag, set4, set2, properties):
        self.tag = tag
        self.set4 = set4
        self.set2 = set2
        self.properties = properties

    def to_dict(self) -> Dict[str, Any]:
        return {
            "Tag": self.tag,
            "Set4": self.set4,
            "Set2": self.set2,
            "Body": self.properties[0],
            "Foot": self.properties[1],
            "Sphere": self.properties[2],
            "Rope": self.properties[3],
        }
