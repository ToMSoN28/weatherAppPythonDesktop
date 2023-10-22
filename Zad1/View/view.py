import customtkinter


class View:
    def __init__(self, root, viewModel):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("420x350")
        self.root.grid_columnconfigure((0, 1), weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.view_model = viewModel

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.cityString = customtkinter.StringVar()
        self.selectedCityString = customtkinter.StringVar()
        self.selectedOptionString = customtkinter.StringVar()
        self.cityList = []

        self.frame = customtkinter.CTkFrame(master=root)
        self.frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.label = customtkinter.CTkLabel(master=self.frame, text="Weather App", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="City", textvariable = self.cityString)
        self.entry.pack(pady=12, padx=10)

        self.searchButton = customtkinter.CTkButton(master=self.frame, text="Search", command = self.search_button_click)
        self.searchButton.pack(pady=12, padx=10)

        self.cityOptionMenu = customtkinter.CTkOptionMenu(master=self.frame, values=[], variable = self.selectedCityString)
        self.cityOptionMenu.pack(pady=12, padx=10)
        self.cityOptionMenu.set("choos city")

        self.optionMenu = customtkinter.CTkOptionMenu(master=self.frame, values = self.view_model.optionsToChoos, variable = self.selectedOptionString)
        self.optionMenu.pack(pady=12, padx=10)
        self.optionMenu.set("choos option type")

        self.applyButton = customtkinter.CTkButton(master=self.frame, text="Apply", command=self.apply_button_click)
        self.applyButton.pack(pady=12, padx=10)

        self.frame1 = customtkinter.CTkFrame(master=root)
        self.frame1.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsw")

        self.label = customtkinter.CTkLabel(master=self.frame1, text="Weather App", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)

        self.textLabel = customtkinter.CTkLabel(master=self.frame1, text="Write a city and choos the option.", wraplength=180)
        self.textLabel.pack(pady=12, padx=20)

    def search_button_click(self):
        self.view_model.search()

    def apply_button_click(self):
        self.view_model.apply()

