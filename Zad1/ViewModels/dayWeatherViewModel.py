from dataclasses import dataclass

@dataclass
class DailyForecastViewModel:
    TempMax: float
    TempMini: float
    Day: str
    Night: str

    def __init__(self, dayliForecast):
        if dayliForecast.Temperature.Maximum.Unit == "F":
            self.TempMax = self.fToC(dayliForecast.Temperature.Maximum.Value)
            self.TempMini = self.fToC(dayliForecast.Temperature.Minimum.Value)
        else:
            self.TempMax = dayliForecast.Temperature.Maximum.Value
            self.TempMini = dayliForecast.Temperature.Minimum.Value
        self.Day = dayliForecast.Day.IconPhrase
        self.Night = dayliForecast.Night.IconPhrase
    
    def fToC(self, value):
        tmp = (value-32)*5/9
        tmp = round(tmp, 1)
        return tmp