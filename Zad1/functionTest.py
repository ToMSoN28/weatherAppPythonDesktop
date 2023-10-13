import datetime as dt
import requests
import json
import function

CITY = "roma"
cityKey = 55489

# cityKey,cityName = function.getCityKey(CITY)
# currentConditionDescribe,celciusTemp = function.getCurrentCondition(str(cityKey))
miniTemp, maxiTemp, dayDescribe, nightDescribe = function.getOneDayForecast(str(cityKey))

# print(cityName)
# print(currentConditionDescribe)
# print(celciusTemp)