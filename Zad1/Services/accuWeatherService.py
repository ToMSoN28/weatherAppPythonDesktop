import requests
from Models.city import City
from Models.currentWeather import CurrentWeather
from Models.hour import HourWeather
from Models.dayli import Dayli


class AccuWeatherService:

    def __init__(self):
        self.BASE_URL = "http://dataservice.accuweather.com"
        self.API_KEY = "L9CE93Lw6aehXlK1FZeE0V7AFRbUstbR"
        # self.API_KEY = "qCtdDGd8DAGrbJPFRF6u1Hn1EAN09WTb"

        self.CITY = "sopot"
        self.LANGUAGE = "en"

        self.AUTOCOMPLITE_ENDPOINT = "/locations/v1/cities/autocomplete"
        self.CURRENT_CONDITIONS_ENDPOINT = "/currentconditions/v1"
        self.ONE_HOUR_FORECAST_ENDPOINT = "/forecasts/v1/hourly/1hour"
        self.ONE_DAY_FORECASTS_ENDPOINT = "/forecasts/v1/daily/1day"
        self.FIVE_DAY_FORECAST_ENDPOINT = "/forecasts/v1/daily/5day"
        self.TWELF_HOUR_RORECAS_ENDPOIT = "/forecasts/v1/hourly/12hour"

    def getCitis(self, lokacionName):
        url = self.BASE_URL + self.AUTOCOMPLITE_ENDPOINT + "?apikey=" + self.API_KEY + "&q=" + lokacionName + "&language=" + self.LANGUAGE
        response = requests.get(url).json()
        city_models = []
        for city_data in response:
            city_models.append(City(**city_data))
        return city_models
    
    def getCurrentCondition(self, cityKey):
         url = self.BASE_URL + self.CURRENT_CONDITIONS_ENDPOINT +"/"+ cityKey + "?apikey=" + self.API_KEY + "&language=" + self.LANGUAGE
         response = requests.get(url).json()
         print(response)
         currentWeather_model = CurrentWeather(**response[0])
         return currentWeather_model
    

    def getOneHourForecast(self, cityKey):
        url = self.BASE_URL + self.ONE_HOUR_FORECAST_ENDPOINT + "/" + cityKey + "?apikey=" + self.API_KEY + "&language=" + self.LANGUAGE
        response = requests.get(url).json()
        print(response)
        print("service")
        hour_model = HourWeather(**response[0])
        print("service1")
        return hour_model
    
    def getOneDayForecast(self, cityKey):
        url = self.BASE_URL + self.ONE_DAY_FORECASTS_ENDPOINT + "/" + cityKey + "?apikey=" + self.API_KEY + "&language=" + self.LANGUAGE
        response = requests.get(url).json()
        print(response)
        dayli_model = Dayli(**response)
        return dayli_model.DailyForecasts[0]

    def getFiveDayForecast(self, cityKey):
        url = self.BASE_URL + self.FIVE_DAY_FORECAST_ENDPOINT + "/" + cityKey + "?apikey=" + self.API_KEY + "&language=" + self.LANGUAGE
        response = requests.get(url).json()
        print(response)
        dayli_model = Dayli(**response)
        return dayli_model.DailyForecasts

    def getTwelfHourForacast(self, cityKey):
        url = self.BASE_URL + self.TWELF_HOUR_RORECAS_ENDPOIT + "/" + cityKey + "?apikey=" + self.API_KEY + "&language=" + self.LANGUAGE
        response = requests.get(url).json()
        print(response)
        hourWeather = []
        for hour_data in response:
            hourWeather.append(HourWeather(**hour_data))
        return hourWeather