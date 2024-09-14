from enum import Enum


class DamageType(Enum):
    PHYSICAL = 1
    FIRE = 2
    ICE = 3
    THUNDER = 4
    WIND = 5
    QUANTUM = 6
    IMAGINARY = 7

    LIGHTENING = 4  # alias of thunder

    @staticmethod
    def to_normalized_damage_type(damage_type: "DamageType") -> str:
        if damage_type == DamageType.THUNDER:
            return "LIGHTENING"
        else:
            return damage_type.name
