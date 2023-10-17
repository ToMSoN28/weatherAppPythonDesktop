from dataclasses import dataclass
from .country import Country
from .administrativeArea import AdministrativeArea


@dataclass
class City:
    Version: int
    Key: int
    Type: str
    Rank: int
    LocalizedName: str
    Country: Country
    AdministrativeArea: AdministrativeArea

    def __post__init__(self):
        self.Country = Country(**self.Country)
        self.AdministrativeArea = AdministrativeArea(**self.AdministrativeArea)