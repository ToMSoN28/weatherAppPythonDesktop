from dataclasses import dataclass

@dataclass
class CityViewModel:
    Key: int
    LocalizedName: str

    def __init__(self, city):
        self.Key = city.Key
        self.LocalizedName = city.LocalizedName
