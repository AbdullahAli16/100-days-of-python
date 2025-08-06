# Day: 67(Ex: 6 Library Management System solution)

# Day: 68(Ex: 7 Clear the clutter )

import os
i=1             #starting number

for file in os.listdir("new"):                      # Changes the file of all formats in a directory
        extension=file.split(".")[-1]
        os.rename(f"new/{file}",f"new/file{i}.{extension}")
        i+=1
        
        
''' If you want to change the files of a specific format use if statement. Just be careful of the formats and
    yeah, windows treats 'png' and 'PNG' separately just keep that in mind'''