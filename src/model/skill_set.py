from typing import Optional, Any

from model.skill import Skill


class SkillSet:

    def __init__(self, char_id: str, tag: str, skills: list[Skill] = None):
        if not skills:
            skills = []

        self.char_id = char_id
        self.tag = tag
        self.skills = skills

    def add_skill(self, skill: Skill) -> None:
        self.skills.append(skill)

    def contains_skill(self, skill_id: str) -> bool:
        return any([skill_id == s.skill_id for s in self.skills])

    def get_skill(self, skill_id: str) -> Optional[Skill]:
        for skill in self.skills:
            if skill.skill_id == skill_id:
                return skill

        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "Tag": self.tag,
            "Skills": [
                skill.to_dict()
                for skill in sorted(self.skills, key=lambda s: s.skill_id)
            ],
        }
