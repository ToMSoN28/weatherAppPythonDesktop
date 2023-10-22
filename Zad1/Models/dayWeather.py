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
    Sources: List[str]
    MobileLink: str
    Link: str

    def __post_init__(self):
        if isinstance(self.Temperature, dict):
            self.Temperature = Temperature(**self.Temperature)
        if isinstance(self.Day, dict):
            self.Day = Day(**self.Day)
        if isinstance(self.Night, dict):
            self.Night = Day(**self.Night)
        if isinstance(self.Sources, list):
            for i, itm in enumerate(self.Sources):
                if isinstance(itm, dict):
                    self.Sources[i] = str(**itm)