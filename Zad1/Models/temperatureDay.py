from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class Temperature:
    Minimum: TempDetails
    Maximum: TempDetails

    def __post_init__(self):
        if isinstance(self.Minimum, dict):
            self.Minimum = TempDetails(**self.Minimum)
        if isinstance(self.Maximum, dict):
            self.Maximum = TempDetails(**self.Maximum)