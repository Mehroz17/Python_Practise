# Iloc and loc are the methods for accesing data from the dataframe
"""
The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem.
As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, loc and iloc.
For more advanced operations, these are the ones you're supposed to be using.

Index-based selection
Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical
position in the data. iloc follows this paradigm.

Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.
"""
import pandas as pd

p = pd.DataFrame({'Country':['Pakistan','india','Iran','China','England','USA','UAE'],"POP":['22.5M','2B','10M','2.5B','15M','45M','5M']})
print(p)
# using iloc
#  To get a column with iloc, we can do the following:
print("It will print the first column of the data\n",p.iloc[:,0])

#On its own, the : operator, which also comes from native Python, means "everything". When combined with other selectors
#however, it can be used to indicate a range of values. For example, to select the country column from just the first, second, and third row, we would do:
print("\nCountry from just 1st 2nd and 3rd row\n",p.iloc[:3,0]) # :3,0 means that start from 0 rows and goes to the 3rd row
#Or, to select just the second and third entries, we would do
print("\n2nd and 3rd row only\n",p.iloc[1:3,0])

# we can also pass a list of the rows
print("Using list of the rowa\n",p.iloc[[2,3,5],0]) # it will print all the rows which we pass as a list

# we can also pass negative number, it just start to count from the last and goes up
print("\nnegative 3 values of the data\n",p.iloc[-3:])



### Loc Labeled Based Selection
# in this we pass the data not its postion
#The second paradigm for attribute selection is the one followed by the loc operator: label-based selection.
# In this paradigm, it's the data index value, not its position, which matters.

# to get the first entry of the column country
print("\n\n###Using LOC####\n")
print("Geting the fist entry in the country column: ",p.loc[0,'Country'])


"""
iloc is conceptually simpler than loc because it ignores the dataset's indices.
When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position.
loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, 
it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:
"""

print("\nThis will print the columns\n",p.loc[:,["Country","POP"]]) # this is similar to the iloc in which we provide the list of the indexes but in this we pass the list of the columns

# Counditional Satement
print("\nChecking if the Country Column contains Italy\n",p.Country == "Italy")

#We can use the ampersand (&) to bring the two questions together:
print(p.loc[(p.Country == 'USA')& (p.POP >'2.5B') ])
print(p.loc[(p.Country == 'USA') | (p.POP >'2.5B') ])
