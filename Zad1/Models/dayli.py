from dataclasses import dataclass
from typing import List
from .headLine import HeadLine
from .dayWeather import DailyForecasts

@dataclass
class Dayli:
    Headline: HeadLine
    DailyForecasts: List[DailyForecasts]

    def __post_init__(self):
        print("sex")
        if isinstance(self.Headline, dict):
            self.Headline = HeadLine(**self.Headline)
            print("cycki")
        if isinstance(self.DailyForecasts, list):
            print("dupaDUPAdupa")
            for i, item in enumerate(self.DailyForecasts):
                if isinstance(item, dict):
                    self.DailyForecasts[i] = DailyForecasts(**item)
                    print("chuj")