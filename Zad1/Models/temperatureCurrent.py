from dataclasses import dataclass
from .temperatureDetails import TempDetails

@dataclass
class Temperature:
    Metric: TempDetails
    Imperial: TempDetails

    def __post__init__(self):
        self.Metric = TempDetails(**self.Metric)
        self,Imperial = TempDetails(**self.Imperial)