from dataclasses import dataclass

@dataclass
class HeadLine:
    EffectiveDate: str
    EffectiveEpochDate: str
    Severity: int
    Text: str
    Category: str
    EndDate: str
    EndEpochDate: str
    MobileLink: str
    Link: str

