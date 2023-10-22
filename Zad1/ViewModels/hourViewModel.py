from dataclasses import dataclass

@dataclass
class HourWeatherViewModel:
    Temp: float
    Describe: str

    def __init__(self, hourWeather):
        if hourWeather.Temperature.Unit == "F":
            self.Temp = self.fToC(hourWeather.Temperature.Value)
        self.Describe = hourWeather.IconPhrase

    def fToC(self, value):
        tmp = (value-32)*5/9
        tmp = round(tmp, 1)
        return tmp