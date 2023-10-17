from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class HourWeather:
    DateTime: str
    EpochDateTime: int
    WeatherIcon: int
    IconPhrase: str
    HasPrecipitation: bool
    IsDaylight: bool
    Temperature: TempDetails
    PrecipitationProbability: str
    MobileLink: str
    Link: str

    def __post__init__(self):
        self.Temperature = TempDetails(**self.Temperature)