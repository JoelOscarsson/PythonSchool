from __future__ import annotations
import Shapes from geometry   ### Kolla på denna det är så jag importerar allting.
import Circle from circle


class Rektangel(Shapes):
    """Rectangle with defined sides (side a along x-axis, side b along y-axis) and thus area and circumference"""
    
    def __init__(self, x_pos: float|int, y_pos: float|int, area: float|int, circum: float|int) -> None:
        super().__init__(x_pos, y_pos)
        self.area = area
        self.circum = circum
        self._area = None
        self._circumference = None
    
    # getters
    @property
    def area(self) -> (int | float):
        print("R area getter körs")
        return self._area
    
    @property
    def circum(self) -> (int | float):
        print("R circum getter körs")
        return self._circum
    
    @property
    def area(self) -> float|int:
        print("R area getter körs")
        if self._area is not None:
            return self._area
        else:
            self._area = self.area * self.circum
            return self._area
    
    @property
    def circumference(self) -> float|int:
        print("R circumference getter körs")
        if self._circumference is not None:
            return self._circumference
        else:
            self._circumference = 2 * (self.area + self.circum)
            return self._circumference
    
    #setters
    @area.setter
    def area(self, value) -> float|int:
        print("R area setter körs")
        if not isinstance (value, (float, int)):
            raise TypeError (f"Side must be a float or an int and not {type(value)}")
        if value <= 0:
            raise ValueError ("Side must be larger than 0")
        self._area = value
    
    @circum.setter
    def circum(self, value) -> float|int:
        print("R circum setter körs")
        if not isinstance (value, (float, int)):
            raise TypeError (f"Side must be a float or an int and not {type(value)}")
        if value <= 0:
            raise ValueError ("Side must be larger than 0")
        self._circum = value
    
    # no setters for area or circumference as they are read-only

    def __repr__(self) -> str:
        return f"Rectancgle ({self.x_pos}, {self.y_pos}, {self.area}, {self.circum})"
    
    def __str__(self) -> str:
        return f"Rectangle: center (x,y) = ({self.x_pos},{self.y_pos}), sides = ({self.area}, {self.circum}), area = {self.area}, circumference = {self.circumference}"
    
    def __eq__(self, other: float) -> bool:
        """Returns True if shapes are of the same type, have the same area and the same side lenghts"""
        eq_GeomFig_result = super().__eq__(other)
        if eq_GeomFig_result and self.area == other.area:
            return True
        else:
            return False
    
    def is_inside(self, x_point: float|int, y_point: float|int) -> bool:
        """Checks if a given point is within the circumference of the shape"""
        if not isinstance(x_point, (float, int)):
            raise TypeError (f"x_point must be int or float and not {type(x_point)}")
        if not isinstance(y_point, (float, int)):
            raise TypeError (f"y_point must be int or float and not {type(y_point)}")

        x_max = self.x_pos + self.area/2
        x_min = self.x_pos - self.area/2
        y_max = self.y_pos + self.circum/2
        y_min = self.y_pos - self.circum/2

        if x_point <= x_max and x_point >= x_min and y_point <= y_max and y_point >= y_min:
            return True
        else:
            return False
    
    def is_square(self) -> bool:
        """Checks if the rectangle is a square"""
        if self.area == self.circum:
            return True
        else:
            return False


            