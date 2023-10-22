from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class HourWeather:
    DateTime: str
    EpochDateTime: int
    WeatherIcon: int
    IconPhrase: str
    HasPrecipitation: bool
    Temperature: TempDetails
    PrecipitationProbability: str
    MobileLink: str
    Link: str
    PrecipitationType: str = ""
    PrecipitationIntensity: str = ""
    IsDaylight: bool = False
    print("init")

    def __post_init__(self):
        print("post init")
        if isinstance(self.Temperature, dict):
            print("hour TempDiteils")
            self.Temperature = TempDetails(**self.Temperature)