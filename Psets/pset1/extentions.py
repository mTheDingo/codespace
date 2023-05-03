"""In a file called extensions.py,
 implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
  case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""

name = input("Name of the file : ").casefold()


if ".gif" in name:
    print("Image/GIF")
elif ".jpg" and ".jpeg" in name :
    print("Image/JPG")
elif ".png" in name:
    print("Image/PNG")
elif ".pdf" in name:
    print("APPLICATION/PDF")
elif ".txt" in name:
    print("TEXT/TXT")
elif ".zip" in name:
    print("FILE/ZIP")
else:
    print("application/octet-stream")


#This program works as expected
# however, i feel like there could be a better way to design it
# but on the other hand, each if statement has a different outcome, so i think this is pretty close to the best design or my level of knowledge is not good enough at this point.
# What if there was 120 different file extentions ?  we can't code them one by one like this

#But in the str documentation, they say if you are checking to see if a sub is in a str, you should use "in" keyword instead of str.find() function.

#str.find() function finds the locaion  of a substring in a str