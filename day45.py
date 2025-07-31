# Day: 45(if__name__=="__main__")

# When we import a self-made made, we get all the functions and variables in that file BUT we also
#  get those functions executions or operations performed in that file
#    For example:

import day42
print(day42.Andrew)             # In output we get all these funcitons executions and operations that are being
                            # performed in day42.py file instead of just the wassap function.

# How do we solve it ???

print(__name__)              #__name__ is basically a predefined variable which returns the value "__main__"
                                 # ONLY When it is run by the file itself and not from any other file
                                
# So, we can use this to prevent all the stuff of the file we imported and just the ones we need by using
#  the expression (if __name__=="__main__") in the file which is imported and in that we put the content that
#   we don't want to run in our very own file.

# It is often a good practice to make a function named "main" in the start of your file, so in the end you can just:
# if(__name__=="__main__"):
#    main()