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
    def __repr__(self) -> str:
        return f"Shape with x_pos = {self.x_pos}, y_pos ={self.y_pos}"
    
    def __str__(self) -> str:
        return f"Shape with x_pos = {self.x_pos}, y_pos ={self.y_pos}"

    #----- Getter and Setter for x_pos
    @property
    def x_pos(self) ->(int | float):
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value: (int | float)):
        #must be a number:
        print("x_pos.setter")
        if not isinstance(value, (int, float)):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._x_pos = round(value, 1)


    #------- Getter and setter for y_pos
    @property
    def y_pos(self) -> (int | float):
    #Read and write for y_pos
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: (int | float)):
        print("y_pos.setter")
        if not isinstance(value, int, float):
            raise TypeError(f"y_pos input must be a number, not {type(value)}")
        
        #Round to 1 decimal
        self._y_pos = round(value, 1)

    #---- Overload --------------------------------------------------

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

    #--------- #Translate method ----------
    def translatemethod(self, x_other: int|float, y_other: int|float) -> Shapes:
        """Moves shape from the original position to the new position"""
        new_shape = copy(self)#KUDOS TO DOROTA FOR THIS LINE OF CODE
        if not isinstance(x_other, (int, float)):
            raise TypeError(f"Number has to be an int or float{type(x_other)}")
        if not isinstance(y_other, (int, float)):
            raise TypeError(f"Number has to be an int or float{type(y_other)}")
        self.x_center = x_other
        self.y_center = y_other
        return self

#--------------------------
"""Inherits from geometry(Shapes) class"""
class Circle(Shapes):
    def __init__(self, x_pos: int|float, y_pos: int|float, radius: int|float) -> None:
        super().__init__(x_pos, y_pos)
        self.radius = radius
        # No value in area and circum from start
        self._circum = 0
        self._area = 0 


    #--- Property and decorator for radius, circum and area functions-----------------------
    ## Getter for only radius because the rest is already fixat i shape
    @property
    def radius(self) -> (int | float):
        """Radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (int | float)):
            raise TypeError(f"Number has to be an int or float not {type(value)}")
        if value <= 0:
            raise ValueError(f"Radius must be more than 0")
        self._radius = value

    @property
    def circum(self) -> (int | float):
        """Circum = Circumference"""
        return 2 * pi * self.radius

    @property
    def area(self) -> (int | float):
        """Area of the circle"""
        return pi * self.radius**2

    # ------- Methods-------------------------------------------




    # String conversion
    def __repr__(self) -> None:
        return f"Circle with x_pos = {self.x_pos}, Circle with y_pos = {self.y_pos}, radius is = {self.radius}"
    
    def __str__(self) -> None:
        return f"Circle with x_pos = {self.x_pos} Circle with y_pos = {self.y_pos}, radius is = {self.radius}, circumference is = {self.circum}"


    # --------------- Other methods -----------------------------------------

    def is_enhetscirkel(self) -> bool:
        """ Kollar om cirkeln är en enhetscirkel med radie 1 vid origo"""
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    

    ######## KUDOS to Daniel from this code solution calculating distance between two points####################
    def is_inside_circle(self, x, y) -> bool:
        """ Kollar om en viss punkt punkt befinner sig innanför objektet """
        return (x - self.x_pos)**2 + (y - self.y_pos)**2 < self.radius**2

##_________________________________________________________________________________________________________________
## _______________________________________REKTANGEL CLASS__________________________________________________________
class Rektangel(Shapes):
    def __init__(self, x_pos: int | float, y_pos: int | float, height: int | float, width: int | float) -> list:
        super().__init__(x_pos, y_pos)
        self.height = height
        self.width = width
        self._area = 0
        self._circum = 0
        #------------------- Property and decorators ------------------------
    @property
    def height(self) -> (int | float):
        """Height rektangel"""
        return self._height

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Height must be an int or float ok? Not {type(value)}")
        if value <= 0:
            raise ValueError("Height must be larger than zero")
        self._height = value

    @property
    def width(self) -> (int | float):
        """Width rektangel"""
        return self._width

    ### ISÅFALL HÄR DET FELAR SENARE OM DET ÄR FEL med tanke på (int | float)
    @width.setter
    def width(self, value: (int | float)):
        if not isinstance(value):
            raise TypeError(f"Width must be an int or float ok? Not {type(value)}")
        if value <= 0:
            raise ValueError("Width must be larger than zero")
        self._width = value

    @property
    def area(self) -> (int | float):
        """Area rektangel"""
        return self.width * self.height
    
    @property
    def circum(self) -> (int | float):
        """Circumference rektangel"""
        return self.width * 2 + self.height * 2


    #------------------------------------------------

    ### KANSKE FLYTTA NER ÄNNU MER
    # String conversion
    def __str__(self) -> str:
        """Self as string"""
        return f"Rektangel center position: {self.x_pos}, {self.y_pos}, height:({self.height}) area:({self.area}) circumference:({self.circum})"

    def __repr__(self) -> (str):
        return "Rektangel x_pos:{self.x_pos}, y_pos:{self.x_pos}, height:({self.height} width:({self.width})"

    ############### KAN BEHÖVA EN EQ HÄR

###################################
    def is_it_square(self) -> bool:
        """Is rektangel a square?"""
        if self._width == self._height:
            return True
        else:
            return False
    
    def is_it_inside(self, x_other: (int | float), y_other: (int | float)) -> bool:
        """Checks if rectangle contains a given point"""
        if not isinstance(x_other, (int, float)):
            raise TypeError(f"Must be an int or float and not {type(x_other)}")
        if not isinstance(y_other, (int, float)):
            raise TypeError(f"Must be an int or float and not{type(y_other)}")

        x_min = self.x_other - (self.width / 2)
        x_max = self.x_other + (self.width / 2)
        y_min = self.y_other - (self.height / 2)
        y_max = self.y_other + (self.height /2)

        if x_other <= x_max and x_point >= x_min and y_other <= y_max and y_other >= y_min:
            return True
        else:
            return False