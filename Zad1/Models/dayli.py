from dataclasses import dataclass
from typing import List
from .headLine import HeadLine
from .dayWeather import DailyForecasts

@dataclass
class Dayli:
    Hedline: HeadLine
    DayliForecast: List[DailyForecasts]

    def __posst__init__(self):
        self.Hedline = HeadLine(**self.Hedline)
        self.DayliForecast = [DailyForecasts(**tmp) for tmp in self.DayliForecast]
