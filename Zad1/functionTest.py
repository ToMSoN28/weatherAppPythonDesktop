import function
from Models.city import City
from typing import List

CITY = "roma"
cityKey = 55489

# city = function.getCityKey(CITY)
# print(city.name)

# cityKey,cityName = function.getCityKey(CITY)
# currentConditionDescribe,celciusTemp = function.getCurrentCondition(str(cityKey))
# miniTemp, maxiTemp, dayDescribe, nightDescribe = function.getOneDayForecast(str(cityKey))
# function.getOneDayForecast(str(cityKey))
# function.getFiveDayForecast(str(cityKey), CITY)
function.getTwelfHourForecast(str(cityKey), CITY)
# print(cityName)
# print(currentConditionDescribe)
# print(celciusTemp)


# obj = [{'Date': '2023-10-18T07:00:00+02:00', 'EpochDate': 1697605200, 'Temperature': {'Minimum': {'Value': 36.0, 'Unit': 'F', 'UnitType': 18}, 'Maximum': {'Value': 52.0, 'Unit': 'F', 'UnitType': 18}}, 'Day': {'Icon': 13, 'IconPhrase': 'Mostly cloudy w/ showers', 'HasPrecipitation': True, 'PrecipitationType': 'Rain', 'PrecipitationIntensity': 'Light'}, 'Night': {'Icon': 38, 'IconPhrase': 'Mostly cloudy', 'HasPrecipitation': False}, 'Sources': ['AccuWeather'], 'MobileLink': 'http://www.accuweather.com/en/pl/brajniki/1413583/daily-weather-forecast/1413583?day=1&lang=en-us', 'Link': 'http://www.accuweather.com/en/pl/brajniki/1413583/daily-weather-forecast/1413583?day=1&lang=en-us'}]
# if isinstance(obj, list):
#     print("cycki")

