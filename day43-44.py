<<<<<<< HEAD
# Day: 43(Virtual Environment)

# Basically a separate environment, the one that we usually use is the global environment.

# You can install different packages on a virtual environment they won't interfere with the ones in
#  global environment or any other virtual environment.

# You can create as many virtual environments as you like.

# Often useful when you want to work on a project and are unsure of the complications you might face in the
#  future and want to avoid such complications

# You can check the version of a package in your terminal, for example: pandas.__version__

# pip freeze is a command that returns all the installed packages in your environment

# Now to make the list of all the packages that are installed in your environment stated in a separate file
#  you just need to run this command: pip freeze > requirements.txt
#    and now to store these packages all at once, just run: pip install -r requirements.txt

# Bonus tip: You can also install a specific version of a package
#       Example: pip install pandas==1.4.4


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


=======
# Day: 43(Virtual Environment)

# Basically a separate environment, the one that we usually use is the global environment.

# You can install different packages on a virtual environment they won't interfere with the ones in
#  global environment or any other virtual environment.

# You can create as many virtual environments as you like.

# Often useful when you want to work on a project and are unsure of the complications you might face in the
#  future and want to avoid such complications

# You can check the version of a package in your terminal, for example: pandas.__version__

# pip freeze is a command that returns all the installed packages in your environment

# Now to make the list of all the packages that are installed in your environment stated in a separate file
#  you just need to run this command: pip freeze > requirements.txt
#    and now to store these packages all at once, just run: pip install -r requirements.txt

# Bonus tip: You can also install a specific version of a package
#       Example: pip install pandas==1.4.4


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


>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
