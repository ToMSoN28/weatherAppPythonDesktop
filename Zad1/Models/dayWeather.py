from dataclasses import dataclass
from typing import List
from .temperatureDay import Temperature
from .day import Day

@dataclass
class DailyForecasts:
    Date: str
    EpochDate:str
    Temperature: Temperature
    Day: Day
    Night: Day
    Source: List[str]
    MobileLink: str
    Link: str

    def __post__init__(self):
        self.Temperature = Temperature(**self.Temperature)
        self.Day = Day(**self.Day)
        self.Night = Day(**self.Night)
        self.Source = [str(**source) for source in self.Source]