from typing import Dict, Any


class CvMap:

    def __init__(
        self, cv_en: str = None, cv_cn: str = None, cv_jp: str = None, cv_kr: str = None
    ) -> None:
        self.cv_en = cv_en
        self.cv_cn = cv_cn
        self.cv_jp = cv_jp
        self.cv_kr = cv_kr

    def to_dict(self) -> Dict[str, Any]:
        return {
            "CV_EN": self.cv_en,
            "CV_CN": self.cv_cn,
            "CV_JP": self.cv_jp,
            "CV_KR": self.cv_kr,
        }
