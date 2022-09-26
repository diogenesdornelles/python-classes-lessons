from dataclasses import dataclass
from typing import Type
from .. import model

FormalInterface = Type[model.FormalInterface]


@dataclass
class Engineer:
    name: str

    def measure_perimeter(self, land: [FormalInterface]) -> str:
        perimeter = land.get_perimeter()
        return f'Engineer {self.name} measured perimeter of {perimeter} m².'

    def measure_area(self, land: [FormalInterface]) -> str:
        area = land.get_area()
        return f'Engineer {self.name} measured area of {area} m².'
