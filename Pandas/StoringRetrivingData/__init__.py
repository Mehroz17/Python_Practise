# Data Loading and File Formats
# to Read Csv file : read_csv  in csv we can use any other thing as a delimetor
# to read excel file : read_excel
# to read htm file : read_htm



# we use read_csv function we have some options like
'''
indexing: means we can treat more than 1 or more columns as returned DataFrame

Type Infernce and data conversion:
we can change the type of the data like int to string and string to int after retrieval

Unclean data issues: skipping rows or a folder comments or other minor



'''

import pandas as pd


sample = pd.read_csv("/First Part/Pandas/StoringRetrivingData/sample.csv", header= None) # header none means that first rows is also used as a record
print(sample)




# reading train file
"""s = pd.read_csv("E:\Mehroz Personals\PIAIC\Second Time Admission\AI\Python Practise\First Part\PTrain.csv", nrows=50)
print("\n")
print(s)
"""

# reading data in chunks
chunks = pd.read_csv("E:\Mehroz Personals\PIAIC\Second Time Admission\AI\Python Practise\First Part\PTrain.csv", chunksize=50)
print("\n")
print(type(chunks),print(chunks)) # if we want to access the chunk we have to use loop , we do not have access to it directly

chunklist = []
# printing chunks of the data and each chunk contains data of about 200 rows
for ch in chunks:
    #print(ch)
    # MERGING THE CHUNKS in a list
    chunklist.append(ch)
# we merge the chunks in the list and then we give the number to acces the first second or any chunk to work on
print(chunklist[0]) # it will return the first chunk of the dataframe







