from dataclasses import dataclass

@dataclass
class HourWeatherViewModel:
    Temp: float
    Describe: str

    def __init__(self, hourWeather):
        self.Temp = hourWeather.Temperature.Value
        self.Describe = hourWeather.IconPhrase