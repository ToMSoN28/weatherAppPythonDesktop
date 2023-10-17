from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class Temperature:
    Minimum: TempDetails
    Maximum: TempDetails

    def __post__init__(self):
        self.Minimum = TempDetails(**self.Minimum)
        self.Maximum = TempDetails(**self.Maximum)