import customtkinter
# import tkinter as tk
from collections import OrderedDict

from .cityViewModel import CityViewModel
from .currentWeatherViewModel import CurrentWeatherViewModel
from .dayWeatherViewModel import DailyForecastViewModel
from .hourViewModel import HourWeatherViewModel
import Services.accuWeatherService as fun

class MainViewModel:
    def __init__(self, accuWeatherService):
        # self.cityString = customtkinter.StringVar()
        # self.selectedCityString = customtkinter.StringVar()
        # self.selectedOptionString = customtkinter.StringVar()
        self.citySearched = None
        self.selectedCity = None
        self.weather = None
        self.weatherL = []
        self.currentWeatherView = None
        self.oneHourConditionView = None
        self.tomorowWeatherView = None
        self.fiveDayWeatherView = None
        self.twelfHourWeatherView = None

        self.accuWeatherService = accuWeatherService
        self.view = None
        # self.root = root
        self.Cities = []
        self.optionsToChoos = ["current weather","weather in an hour", "tomorrow weather", "five day forecast", "twelf hour forecast"]

    
    @property
    def city(self):
        return self.cityString.get()
    
    @city.setter
    def city(self, value):
        self.cityString.set(value)

    @property
    def selectedCity(self):
        return self.selectedCityString
    
    @selectedCity.setter
    def selectedCity(self, value):
        self.selectedCityString = value

    @property
    def selectedOption(self):
        return self.selectedOptionString
    
    @selectedOption.setter
    def selectedOption(self, value):
        self.selectedOptionString = value

    def currentString(self):
        weather = self.accuWeatherService.getCurrentCondition(self.selectedCity.Key)
        self.weather = CurrentWeatherViewModel(weather)
        string = "Currently in "+ self.selectedCity.LocalizedName + " it is " + self.weather.WeatherText + " and " + str(self.weather.TempValue) + " degrees"
        return string
    
    def tomorowString(self):
        weather = self.accuWeatherService.getOneDayForecast(self.selectedCity.Key)
        self.weather = DailyForecastViewModel(weather)
        string = "Tomorrow in "+ self.selectedCity.LocalizedName + " it will be maximum" + str(self.weather.TempMax) + " and minimum " + str(self.weather.TempMini) + " egrees.\nIt will be "+self.weather.Day+" during the day and "+self.weather.Night+" at night.\n"
        return string
    
    def oneHourString(self):
        weather = self.accuWeatherService.getOneHourForecast(self.selectedCity.Key)
        self.weather = HourWeatherViewModel(weather)
        string = "In an hour in "+self.selectedCity.LocalizedName+" there will be "+self.weather.Describe+" and "+str(self.weather.Temp)+" degree"
        return string
    
    def fiveDaysString(self):
        self.weatherL.clear()
        weather = self.accuWeatherService.getFiveDayForecast(self.selectedCity.Key)
        # self.weatherL = DailyForecastViewModel(weather)
        string = ""
        dayList = ["Tomorrow in ", "In two days in ", "In three days in ", "In four days in ", "In five days in "]
        for dailyM in weather:
            self.weatherL.append(DailyForecastViewModel(dailyM))
        for i, daily in enumerate(self.weatherL):
            string = string + dayList[i]+self.selectedCity.LocalizedName+" it will be maximum "+str(daily.TempMax) + " and minimum " +str(daily.TempMini) + " egrees.\nIt will be "+daily.Day+" during the day and "+daily.Night+" at night.\n"
        return string

    def twelfHourString(self):
        self.weatherL.clear()
        weather = self.accuWeatherService.getTwelfHourForacast(self.selectedCity.Key)
        string = ""
        numbers = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
        for hourM in weather:
            self.weatherL.append(HourWeatherViewModel(hourM))
        for i, hour in enumerate(self.weatherL):
            string += numbers[i]+" hour in "+self.selectedCity.LocalizedName+" will be "+hour.Describe+" and "+str(hour.Temp)+" degrees.\n"
        return string

    def search(self):
        self.citySearched = self.view.cityString.get()
        # print(self.citySearched)
        citis = self.accuWeatherService.getCitis(self.citySearched)
        self.Cities.clear()
        for cityObj in citis:
            # print(cityObj.LocalizedName)
            self.Cities.append(CityViewModel(cityObj))
        self.view.cityOptionMenu.configure(values = [city.LocalizedName for  city in self.Cities])        

    def apply(self):
        print(self.view.selectedCityString.get())
        for city in self.Cities:
            if self.view.selectedCityString.get() == city.LocalizedName:
                self.selectedCity = city
        self.selectedOption = self.view.selectedOptionString.get()
        print("dupa "+self.selectedOption)
        switch = {
            self.optionsToChoos[0]: self.currentString,
            self.optionsToChoos[1]: self.oneHourString,
            self.optionsToChoos[2]: self.tomorowString,
            self.optionsToChoos[3]: self.fiveDaysString,
            self.optionsToChoos[4]: self.twelfHourString,
        }
        if self.selectedOption in switch:
            weatrherText = switch[self.selectedOption]()
        else:
            weatrherText = "Choos one of option!"
        self.view.textLabel.configure(text = weatrherText)
        
        
    