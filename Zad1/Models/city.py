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

    def __post_init__(self):
        if isinstance(self.Country, dict):
            self.Country = Country(**self.Country)
        if isinstance(self.AdministrativeArea, dict):
            self.AdministrativeArea = AdministrativeArea(**self.AdministrativeArea)