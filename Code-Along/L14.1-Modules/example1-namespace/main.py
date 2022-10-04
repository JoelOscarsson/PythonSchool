import os, sys

x = 5 

os.system("cls||clear")  # Rensar terminalen

print(f"{'='*30}main.py{'='*30}")    #30 st lika med tecken, main.py, 30 st lika med tecken

# code imported from another module is executed when imported
import module1 as m1

# note __name__ is module1 when ran from outside of module1.py
# when module.py is ran -> __name__= "__main__"

# when importing a module - a reference will be created to sys.modules
print("globals namespace")
print(globals()["module1"])

# when importing a module - it will be stored in sys.modules
print("sys.modules")
print(sys.modules["module1"])

print(f"\n{'='*30}end main{'='*30}") 