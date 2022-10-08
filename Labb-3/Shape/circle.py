from geometry import Shapes
from math import pi
from __future__ import annotations


###KANSKE MÅSTE ÄNDRA VARIABEL NAMN PÅ X_POS OCH Y_POS FÖR DE ÄR ÄNDRADE I GEOMEtry

"""Inherets from geometry(Shapes) class"""
class Circle(Shapes):
    def __init__(self, x_pos: float, y_pos: float, radius: float):
        super().__init__(x_pos, y_pos)
        self.radius = radius
        # No value in area and circum from start
        self._circum = 0
        self._area = 0 
    
    #--- Property and decorator for radius, circum and area functions-----------------------
    @property
    def radius(self) -> (int | float):
        """Radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (float | int)):
            raise TypeError(f"Number has to be an int or float not {type(value)}")
        if value <= 0:
            raise ValueError(f"Radius must be more than 0")
        self._radius = value 


    @property
    def circum(self) -> (int | float):
        return self._circumference

    @circum.setter
    def circum(self) -> (int | float):
        """Circumference of the circle"""
        if self._circum is not None:
            return self._circum
        else:
            self._circum = 2 * pi * self._radius
            return self._circum

    @property
    def area(self) -> (int | float):
        """Area of the circle"""
        if self._area is not None:
            return self._area
        else:
            self._area = pi * self._radius ** 2

    # ------- Methods-------------------------------------------


    # String conversion
    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}{self.radius}"
    
    def __str__(self) -> None:
        return f"Circle, x position:{self.x_pos} Circle, y position: {self.y_pos}, radius is: {self.radius}, circumferene is: {self.circum}"


    # --------------------------------------------------------
    # TODO Hur checkar man så cirkel är inside e
    # TODO: Gör fel hantering av cirkel klassen igen efter att ha ändrat i koden
    # TODO: När jag gör felhantering så måste jag se till så jag importerar från rätt ställe osv...
    # TODO: Kanske måste ändra variablerna x och y nedanför bara för att jag ändrade dem i geometry(KOLLA MED KOKCHUN KANSKE?)

    def is_circle_inside(self, x , y)
