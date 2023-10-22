import requests
from Models.city import City
from Models.currentWeather import CurrentWeather
from Models.hour import HourWeather
from Models.dayli import Dayli

BASE_URL = "http://dataservice.accuweather.com"
# API_KEY = "L9CE93Lw6aehXlK1FZeE0V7AFRbUstbR"
# API_KEY = "qCtdDGd8DAGrbJPFRF6u1Hn1EAN09WTb"
API_KEY = "fczx5bWlQev7L9f8AKB5FXRike7Y31Xw"

CITY = "sopot"
LANGUAGE = "en"

AUTOCOMPLITE_ENDPOINT = "/locations/v1/cities/autocomplete"
CURRENT_CONDITIONS_ENDPOINT = "/currentconditions/v1"
ONE_HOUR_FORECAST_ENDPOINT = "/forecasts/v1/hourly/1hour"
ONE_DAY_FORECASTS_ENDPOINT = "/forecasts/v1/daily/1day"
FIVE_DAY_FORECAST_ENDPOINT = "/forecasts/v1/daily/5day"
TWELF_HOUR_RORECAS_ENDPOIT = "/forecasts/v1/hourly/12hour"

def fToC(value):
    tmp = (value-32)*5/9
    tmp = round(tmp, 1)
    return tmp

def getCityKey(city):
    url = BASE_URL + AUTOCOMPLITE_ENDPOINT + "?apikey=" + API_KEY + "&q=" + city + "&language=" + LANGUAGE
    response = requests.get(url).json()
    print(response)
    city_models = []
    for city_data in response:
        city_back = City(**city_data)
        city_models.append(city_back)
        print(city_back.Country.LocalizedName)
    # return city_back
    return city_models[0].Key,response[0]['LocalizedName']

# testy = getCityKey(CITY)

def getCurrentCondition(cityKey):
    url = BASE_URL + CURRENT_CONDITIONS_ENDPOINT +"/"+ cityKey + "?apikey=" + API_KEY + "&language=" + LANGUAGE
    response = requests.get(url).json()
    print(response)
    currentWeather_model = CurrentWeather(**response[0])
    print(currentWeather_model.Temperature.Metric.Value)
    return response[0]['WeatherText'], fToC(response[0]['Temperature']['Metric']['Value'])

def getOneHourForecast(cityKey):
    url = BASE_URL + ONE_HOUR_FORECAST_ENDPOINT + "/" + cityKey + "?apikey=" + API_KEY + "&language=" + LANGUAGE
    response = requests.get(url).json()
    hour_model = HourWeather(**response[0])
    print(hour_model.Temperature.Value)
    return response[0]["IconPhrase"], fToC(response[0]["Temperature"]["Value"])

def getOneDayForecast(cityKey):
    url = BASE_URL + ONE_DAY_FORECASTS_ENDPOINT + "/" + cityKey + "?apikey=" + API_KEY + "&language=" + LANGUAGE
    response = requests.get(url).json()
    print(response)
    dayli_model = Dayli(**response)
    print(dayli_model.DailyForecasts[0].Temperature.Maximum.Value)
    miniValue = response["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    maxiValue = response["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    return fToC(miniValue), fToC(maxiValue), response["DailyForecasts"][0]["Day"]["IconPhrase"], response["DailyForecasts"][0]["Night"]["IconPhrase"]

def getFiveDayForecast(cityKey, cityName):
    url = BASE_URL + FIVE_DAY_FORECAST_ENDPOINT + "/" + cityKey + "?apikey=" + API_KEY + "&language=" + LANGUAGE
    response = requests.get(url).json()
    print(response)
    dayli_model = Dayli(**response)
    print(dayli_model.DailyForecasts[4].Temperature.Maximum.Value)
    minTemperatures = []
    maxTemperatures = []
    dayIcons = []
    nightIcons = []

    for forecast in response["DailyForecasts"]:

        minTmp = fToC(forecast["Temperature"]["Minimum"]["Value"])
        maxTemp = fToC(forecast["Temperature"]["Maximum"]["Value"])
        minTemperatures.append(minTmp)
        maxTemperatures.append(maxTemp)
        
        # Ikony
        dayIcon = forecast["Day"]["IconPhrase"]
        nightIcon = forecast["Night"]["IconPhrase"]
        dayIcons.append(dayIcon)
        nightIcons.append(nightIcon)


    tmp = "Tomorow in "+cityName+" will be maximum: "+str(maxTemperatures[0])+" degrees and minimum: "+str(minTemperatures[0])+" degrees.\n It will be "+ dayIcons[0]+" during the day and "+nightIcons[0]+" at night.\n"+"In two days in "+cityName+" will be maximum: "+str(maxTemperatures[1])+" degrees and minimum: "+str(minTemperatures[1])+" degrees.\n It will be "+ dayIcons[1]+" during the day and "+nightIcons[1]+" at night.\n"+"In  three days in "+cityName+" will be maximum: "+str(maxTemperatures[2])+" degrees and minimum: "+str(minTemperatures[2])+" degrees.\n It will be "+ dayIcons[2]+" during the day and "+nightIcons[2]+" at night.\n"+"In  four days in "+cityName+" will be maximum: "+str(maxTemperatures[3])+" degrees and minimum: "+str(minTemperatures[3])+" degrees.\n It will be "+ dayIcons[3]+" during the day and "+nightIcons[3]+" at night.\n"+"In  five days in "+cityName+" will be maximum: "+str(maxTemperatures[4])+" degrees and minimum: "+str(minTemperatures[4])+" degrees.\n It will be "+ dayIcons[4]+" during the day and "+nightIcons[4]+" at night.\n"
    return tmp

def getTwelfHourForecast(cityKey, CityName):
    url = BASE_URL + TWELF_HOUR_RORECAS_ENDPOIT + "/" + cityKey + "?apikey=" + API_KEY + "&language=" + LANGUAGE
    response = requests.get(url).json()
    print(response)
    hour_models = []
    for model in response:
        hour_model = HourWeather(**model)
        hour_models.append(hour_model)
        print(hour_model.Temperature.Value)
    hourWeather = []
    for hour_data in response:
        hourWeather.append(HourWeather(**hour_data))
    print(hourWeather[11].Temperature.Value)
    iconPhrases = []
    temperatures = []
    numbers = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]


    for hourData in response:
        iconPhrase = hourData["IconPhrase"]
        temperature = fToC(hourData["Temperature"]["Value"])
        
        iconPhrases.append(iconPhrase)
        temperatures.append(temperature)

    tmp=""
    for i in range(12):
        tmp = tmp+ numbers[i]+" hour in "+CityName+" will be "+iconPhrases[i]+" and "+str(temperatures[i])+" degrees.\n"

    return tmp
    
