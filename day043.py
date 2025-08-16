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