from dataclasses import dataclass
from .temperatureCurrent import Temperature

@dataclass
class CurrentWeather:
    LocalObservationDateTime: str
    EpochTime: int
    WeatherText: str
    WeatherIcon: int
    HasPrecipitation: bool
    PrecipitationType: bool
    IsDayTime: bool
    Temperature: Temperature
    MobileLink: str
    Link: str

    def __post__init__(self):
        self.Temperature = Temperature(**self.Temperature)