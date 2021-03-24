import os
from csv import reader
from tkinter import *
from tkinter import filedialog

#The select file filedialog screen
def browseFiles():
    fN = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("All files",
                                                        "*.*"),
                                                       ("Text Files",
                                                        "*.txt*")))
    return fN
#Hides the Tk UI so that its not shown when the the file browser opens to load the files
Tk().withdraw()

#Returns the filename from the fileDialog window.
filename = browseFiles()

#Opens the CSV file and puts the data into list
with open(filename,encoding="utf8") as data:
   csv_reader = reader(data)
   listRows = list(csv_reader)

print ("Total Data: ", len(listRows))
#print all rows of data
#print (listRows)

#Print out just one row of data
for i in listRows[:10]:
    print(" " .join(map(str, i)))
    #print("\n") #<-- prints out each row on a single line


