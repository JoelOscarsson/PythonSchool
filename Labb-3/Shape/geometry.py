from __future__ import annotations
from math import pi
from copy import copy 

# Super class Shapes
class Shapes:

    def __init__(self, x_pos: (int | float), y_pos: (int | float)):
        print("__init__")
        self.x_pos = x_pos
        self.y_pos = y_pos


    # String represantation
    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}"
    
    def __str__(self) -> None:
        return f"X-pos is: {self.x_pos} and Y-pos is: {self.y_pos}"

    #----- Getter and Setter for x_pos
    @property
    def x_pos(self):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value: int | float):
        #must be a number:
        print("x_pos.setter")
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._x_pos = round(value, 1)


    #------- Getter and setter for y_pos
    @property
    def y_pos(self):
    #Read and write for y_pos
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: int | float):
        print("y_pos.setter")
        if not isinstance(value, int, float):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._y_pos = round(value, 1)

    #---- Overload ----

    def __lt__(self, other: Shapes) -> bool:
        """Checks lesser than operator for all shapes"""
        return self.area > other.area

    def __gt__(self, other: Shapes) -> bool:
        """Checks if greater than to all shapes"""
        return self.area <= other.area

    def __ge__(self, other: Shapes) -> bool:
        """Checks if greater or equal to operator to all shapes"""
        return self.area >= other.area
    
    def __le__(self, other: Shapes) -> bool:
        """Checks if lesser than or equal to all shapes"""
        return self.area <= other.area
    
    def __eq__(self, other: Shapes) -> bool:
        """Checks if its equal to all shapes"""
        return self.area == other.area

    #--------- #KUDOS TO DOROTA FOR THIS LINE OF CODE----------
    def translatemethod(self, x_other: int|float, y_other: int|float) -> None:
        """Moves shape from the original position to the new position"""
        new_shape = copy(self)
        if not isinstance(x_other, (int, float)):
            raise TypeError(f"Number has to be an int or float{type(x_other)}")
        if not isinstance(y_other, (int, float)):
            raise TypeError(f"Number has to be an int or float{type(y_other)}")
        self.x_center = x_other
        self.y_center = y_other
        return self


    #-------------------------------------------------------------------------------

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
    def radius(self) -> int | float:
        """Radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, value) -> int | float:
        if not isinstance(value, (int | float)):
            raise TypeError(f"Number has to be an int or float not {type(value)}")
        if value <= 0:
            raise ValueError(f"Radius must be more than 0")
        self._radius = value 


    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._radius = value 


    @property
    def circum(self) -> (int | float):
        return self._circum

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

    def is_it_enhetscirkel(self) -> bool:
        """ Kollar om cirkeln är en enhetscirkel med radie1 vid origo"""
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    
    ######## KUDOS to Daniel from this code solution calculating distance between two points####################
    def is_inside_cirle(self, x, y):
        """ Kollar om en viss punkt punkt befinner sig innanför objektet """
        return (x - self.x_pos)**2 + (y - self.y_pos)**2 < self.radius**2


## _______________________________________REKTANGEL CLASS__________________________________________________________
class Rektangel(Shapes):
    def __init__(self, x_pos, y_pos, height: int | float, width: int | float):
        super().__init__(x_pos, y_pos)
        self.height = height
        self.width = width


    def __str__(self):
        """Override for string"""
        return "This is Rektangel x position: " + str(self.x_pos) + "and y postion of " + str(self.y_pos) + ". Height is " + str(self.height) + " and width is " + str(self.width)

    ## Titta till detta sedan
    def __repr__(self) -> (str):
        return "Rektangels position x = " + str(self.x_pos) + ", position y = " + str(self.y_pos) + ", width = " + str(self.width) + ", height =" + str(self.height) + ")"



    #------------- Propertys and decorators ----------------------------------
    
    @property
    def height(self) -> (int | float):
        """For height"""
        return self._height

    @height.setter
    def height(self, value: int | float):
        if isinstance(value, str):
            raise TypeError(f"y pos must be an int or float ok? Not {type(value)}")
        self._height = value
    
    @property
    def width(self) -> (int | float):
        return self._width
    ##### KIKA IN DEN HÄR IGEN!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @width.setter
    def width(self, value: int | float):
        if isinstance(value, str):
            raise TypeError(f"y position must be an int or float ok? Not {type(value)}")
        self.width = value


    # Logic for width * height = area
    @ property
    def area(self) -> float:
        return self.height * self.width
    
    # circum = Circumference
    @property
    def circum(self) -> float:
        return (self.width * 2) + (self.height * 2)
    
    @property
    def is_it_square(self) -> True:
        if self._width == self._height:
            return print("Yes, it is a square")
        else:
            return print("No, this is not a square")
    
    def is_it_inside(self, x_pos, y_pos):
        x_min = self.x_pos - (self.width / 2)
        x_max = self.x_pos + (self.width / 2)
        y_min = self.y_pos - (self.height / 2)
        y_max = self.y_pos + (self.height /2)

        if x_min < x_pos <x_max and y_min < y_pos < y_max:
            return True
        return False

