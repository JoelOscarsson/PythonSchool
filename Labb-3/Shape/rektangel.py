from __future__ import annotations
import Shapes from geometry   ### Kolla på denna det är så jag importerar allting.
import Circle from circle      ### IMPORTERA ALLTING KORREKT FÖR ATT TESTA KOD



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
 




            