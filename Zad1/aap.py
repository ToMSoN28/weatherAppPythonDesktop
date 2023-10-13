import customtkinter
import function

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

cityKey = ""
cityName = ""


def currentWeather():
    currentConditionDescribe,celciusTemp = function.getCurrentCondition(cityKey)
    tmp = "Actual weather conditions in "+cityName+": "+currentConditionDescribe+" , temperature: "+str(celciusTemp)
    return tmp

def weatherInAnHour():
    conditionDescribe,celciusTemp = function.getOneHourForecast(cityKey)
    tmp = "In an hour in "+cityName+" there will be "+conditionDescribe+" and "+str(celciusTemp)+" degrees"
    return tmp

def tomorrowWeather():
    miniTemp, maxiTemp, dayDescribe, nightDescribe = function.getOneDayForecast(str(cityKey))
    tmp = "Tomorow in "+cityName+" will be maximum: "+str(maxiTemp)+" degrees and minimum: "+str(miniTemp)+" degrees.\n It will be "+ dayDescribe+" during the day and "+nightDescribe+" at night."
    return tmp

def fiveDayWeather():
    return function.getFiveDayForecast(cityKey,cityName)

def twelfHourWeather():
    return function.getTwelfHourForecast(cityKey,cityName)



def apply():
    global cityKey
    global cityName
    city = entry.get()
    if city == "":
        return
    option = selectedOption.get()
    # print(option)

    cityKey, cityName = function.getCityKey(city)

    switch = {
        "current weather": currentWeather,
        "weather in an hour": weatherInAnHour,
        "tomorrow weather": tomorrowWeather,
        "five day forecast":fiveDayWeather,
        "twelf hour forecast":twelfHourWeather,
    }

    if option in switch:
        result = switch[option]()
    else:
        result = "Choos one of option!"

    textLabel.configure(text=result)
    return 


root = customtkinter.CTk()
root.title("Weather App")
root.geometry("400x680")

optionsToChoos = ["current weather","weather in an hour", "tomorrow weather", "five day forecast", "twelf hour forecast"]
selectedOption = customtkinter.StringVar()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Weather App", font=("Arial", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="City")
entry.pack(pady=12, padx=10)

optionMenu = customtkinter.CTkOptionMenu(master=frame, values=optionsToChoos, variable=selectedOption)
optionMenu.pack(pady=12, padx=10)
# optionMenu.set("time")

applyButton = customtkinter.CTkButton(master=frame, text="Apply", command=apply)
applyButton.pack(pady=12, padx=10)

textLabel = customtkinter.CTkLabel(master=frame, text="Write a city and choos the option.", wraplength=200)
textLabel.pack(pady=12, padx=10)

root.mainloop()

