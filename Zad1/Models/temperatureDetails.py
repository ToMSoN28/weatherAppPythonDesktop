from dataclasses import dataclass

@dataclass
class TempDetails:
    Value: float
    Unit: str
    UnitType: int