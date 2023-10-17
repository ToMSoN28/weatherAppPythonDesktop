import function
from Models.city import City

CITY = "roma"
cityKey = 55489

city = function.getCityKey(CITY)
print(city.name)

# cityKey,cityName = function.getCityKey(CITY)
# currentConditionDescribe,celciusTemp = function.getCurrentCondition(str(cityKey))
# miniTemp, maxiTemp, dayDescribe, nightDescribe = function.getOneDayForecast(str(cityKey))

# print(cityName)
# print(currentConditionDescribe)
# print(celciusTemp)