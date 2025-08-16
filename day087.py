# Day: 87(Shutil Module)

# Don't execute the file, before checking the content to avoid losing files

''' shutil is a module that provides a higher level interface for working with file and directories '''

import shutil

# Makes a copy of a file. Arguments:("File to copy","File name to save with") (better to use copy2
#  because it also preserves the metadata of that file such as the timestamp)
shutil.copy("day87.py","day887.py") 
    
# Makes a copy of a directory. Arguments:("directory","new directory name")
shutil.copytree("new","aslihai")

# Moves the file from its current path to the path specified. Arguments:("current path","new path")
shutil.move("new/Seylani.pdf","Seylani.pdf")

# Deletes the directory. Arguments:("Directory path")
shutil.rmtree("test")