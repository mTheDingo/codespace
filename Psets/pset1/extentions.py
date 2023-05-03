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
