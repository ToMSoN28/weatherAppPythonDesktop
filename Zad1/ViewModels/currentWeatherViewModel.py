from dataclasses import dataclass

@dataclass
class CurrentWeatherViewModel:
    WeatherText: str
    TempValue: float

    def __init__(self, currentWeather):
        self.WeatherText = currentWeather.WeatherText
        self.TempValue = currentWeather.Temperature.Metric.Value