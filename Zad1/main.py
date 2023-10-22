import customtkinter
from Services.accuWeatherService import AccuWeatherService
from ViewModels.mainViewModel import MainViewModel
from View.view import View

root = customtkinter.CTk()

service = AccuWeatherService()

viewModel = MainViewModel(service)
view = View(root, viewModel)
viewModel.view = view
root.mainloop()