from __future__ import annotations
import sys, os  #Man kan importera flera saker samtidigt
import unittest

print(__file__)

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))# Ändrar directory vart jag ska befinna mig. Jag befinner mig efter changen i mappen tests

# We define path that is one step up
path_to_vector_module = os.path.abspath("../")  #../ hoppar upp ett steg/hoppar upp i mappen

# Nu har vi lagt till path to vector i sys.path, den letar efter alla moduler du har installerat i den mappen
sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector

class TestVector(unittest.TestCase):
    # Om vi ska använda flera vectorer så kan man använda en form utav setup
    # setUp gives attributes that we can use later on
    # this is to avoid repeating too much
    def setUp(self):
        self.x, self.y = 1, 2

    # Can be used to create default 2D vector for testing
    def create_2D_vector(self) -> Vector:
        #v = Vector(1,2)
        self.assertEqual(v.numbers, (self.x, self.y))
        return Vector(self.x, self.y)

    def test_create_2D_vector(self):
        """Testing numbers property"""
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_create_3D_vector(self):
        v = Vector(1,2,3)
        self.assertEqual(v.numbers, (1,2,3))

    def test_create_empty_vector(self):
        # If we get a raised ValueError -> the test is OK
        with self.assertRaises(ValueError):
            v = Vector()


    def test_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1, v2)

    def test__not_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(-1, -2)
        self.assertNotEqual(v1, v2)

    def test_add_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,3)
        self.assertEqual(v1+v2, Vector(self.x+1, self.y+3))

    def test_getitem(self):
        v1 = self.create_2D_vector()

        # this approach is tedious when we have many elements in vector
        #self.assertEqual(v1[0], self.x)
        #self.assertEqual(v1[1], self.y)

        # i = 0, number = 1 
        # i = 1, number = 2
        for i, number in enumerate((1,2)):
            self.assertEqual(v1[i], number)

    #TODO: Many more tests to be performed
    

class TestVector2(unittest.TestCase):
    def test_create_2D_vector(self):
        v = Vector(1, 2)
        self.assertEqual(v.numbers, (1, 2))

if __name__ == "__main__":
    unittest.main()
