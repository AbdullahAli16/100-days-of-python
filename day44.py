# Day: 44(Import keyword)

import math             # Imports all functions

print(math.sqrt(2))

from math import floor   # For Single function
print(floor(4))

from math import floor,sinh,pi   # For Multiple functions
print(sinh(30)*pi)

from math import * #not recommended because it may cause confusion
print(sqrt(6))

import imageio as io     # as keyword

import requests
print(dir(requests))       # dir is a built-in function in python which returns a list of all the functions and     # variables defined in a module

# You can also import functions and variables from a file you made, example:
# (all the above methods can be used here too)

from day42 import wassup,Andrew

wassup()
print(Andrew)