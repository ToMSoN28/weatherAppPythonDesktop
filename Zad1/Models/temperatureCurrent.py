from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class Temperature:
    Metric: TempDetails
    Imperial: TempDetails

    def __post_init__(self):
        if isinstance(self.Metric, dict):
            self.Metric = TempDetails(**self.Metric)
        if isinstance(self.Imperial, dict):
            self.Imperial = TempDetails(**self.Imperial)