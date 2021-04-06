import os
import csv
import re
from collections import defaultdict
from tkinter import *
from tkinter import filedialog

#The select file filedialog screen
def browseFiles(fileType):
    fN = filedialog.askopenfilename(initialdir = "./",
                                          title = f"Select a {fileType} File",
                                          filetypes = (("All files",
                                                        "*.*"),
                                                       ("Text Files",
                                                        "*.txt*")))
    return fN

#Gets all the indexs of the words that should be removed
def findindexes(dataFile, whatToDelete):
  index = []
  i = 0
  for word in dataFile:
    i += 1
    for item in word:
      if re.search(f'(?:{whatToDelete})', item, re.IGNORECASE):
        index.append(i)
  return index

#Prints out the what should be removeds text and how many
def removeFrom(removeText, dataFile):
  indexOf = findindexes(dataFile, removeText)
  print(f'Total number of Books with "{removeText}" in the title: {str(len(indexOf))}')
  return indexOf

#Outputs to new CSV file that has the reduced data
def makeReducedCSV(filename, dataFile, fields):
  with open(filename+'REDUCED.csv','w', newline="") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(fields)
    write.writerows(dataFile[1:])
    csvfile.close()

#Hides the Tk UI so that its not shown when the the file browser opens to load the files
Tk().withdraw()

#Returns the filename from the fileDialog window.
filename = browseFiles('CSV')

#Gets the data out of the original CSV file
dataFile = []
f = open(filename)
csv_f = csv.reader(f)
for row in csv_f:
  dataFile.append(row)

#Gets the text document that contains key words not to included
indexestonotinclude = []
textFile = browseFiles('TXT')
textFileRead = open(textFile, 'r')
Lines = textFileRead.readlines()
Lines = [x.strip() for x in Lines]
for line in Lines:
  if not line.startswith("#"):
    indexestonotinclude.extend(removeFrom(line, dataFile))

#prints how many items shouldnt be included contains duplicates
print(len(indexestonotinclude))

#Sorts the list of indexes that shouldnt be included
indexestonotinclude.sort()

#Removes duplicates
finalIndexToRemove = [i for n, i in enumerate(indexestonotinclude,start=0) if i not in indexestonotinclude[:n]]

#DEBUG: prints out all the indexes that should be removed from the file
print("Total amount to be removed without duplicates: " + str(len(finalIndexToRemove)))
#print(finalIndexToRemove) #<----SHOULD BE COMMENTED OUT FOR DEBUG PURPOSES ONLY

#Column headers should be changed to programatically at some point from the original file
fields = ['Course Code', 'Section Code', 'Section Display Name', 'Est. Enroll.', 'ISBN', 'Title', 'Author', 'Publisher', 'Date', 'Edition', 'Required?', 'Supplier', 'Link', 'OK to Use Newer Edition?', 'OK to Use Older Edition?', 'Section Status', 'Submitted By']

reducedData = [element for i, element in enumerate(dataFile, start=1) if i not in finalIndexToRemove]

#Outputs to new CSV file named output
makeReducedCSV(filename, reducedData, fields)

#Closing all files
textFileRead.close()
f.close()
