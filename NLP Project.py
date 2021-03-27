import os
import csv
from collections import defaultdict
from tkinter import *
from tkinter import filedialog

#The select file filedialog screen
def browseFiles():
    fN = filedialog.askopenfilename(initialdir = "./",
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
column = defaultdict(list)

fields = ['Course Code', 'Section Code', 'Section Display Name', 'Est. Enroll.', 'ISBN', 'Title', 'Author', 'Publisher', 'Date', 'Edition', 'Required?', 'Supplier', 'Link', 'OK to Use Newer Edition?', 'OK to Use Older Edition?', 'Section Status', 'Submitted By']

col2 = []
f = open(filename)
csv_f = csv.reader(f)

for row in csv_f:
  col2.append(row)

with open('output.csv','w', newline="") as csvfile:
  write = csv.writer(csvfile)
  write.writerow(fields)
  write.writerows(col2[1:])


print(col2[1:2])
''' EVERYTHING BELOW IS TEMP AND WILL BE REMOVED OR USED
#Opens the CSV file and puts the data into list
with open(filename,encoding="utf8") as data:
   csv_reader = csv.DictReader(data)
   for row in csv_reader:
      for (k,v) in row.items():
        column[k].append(v)'''

''' How to remove from dictonary
>>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
>>> new_dict = {}  # Create a new empty dictionary
>>> for key, value in a_dict.items():
...     # If value satisfies the condition, then store it in new_dict
...     if value <= 2:
...         new_dict[key] = value
...
>>> new_dict
{'one': 1, 'two': 2}'''

'''dicts = column['ISBN'], column['Title']

with open('output.csv', 'w') as csvfile:
    fieldnames = ['ISBN', 'Title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for e in dicts:
      writer.writerows({'ISBN': e , 'Title': e})'''
'''
'''
