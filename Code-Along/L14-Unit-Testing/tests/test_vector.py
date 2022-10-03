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
    def test_create_2D_vector(self):
        v = Vector(1,2)
        self.assertEqual(v.numbers, (1,2))

    def test_create_3D_vector(self):
        v = Vector(1,2,3)
        self.assertEqual(v.numbers, (1,2,3))


if __name__ == "__main__":
    unittest.main()
