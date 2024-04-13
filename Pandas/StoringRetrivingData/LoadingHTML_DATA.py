"""
 we are loading data from HTML page or from any website
 the function we will use if read_html
"""
import pandas as pd
x = pd.ExcelFile("E:\Mehroz Personals\PIAIC\Second Time Admission\AI\Python Practise\First Part\Pandas\Book1.xlsx") # here we are loading excel file
xl = pd.read_excel("E:\Mehroz Personals\PIAIC\Second Time Admission\AI\Python Practise\First Part\Pandas\Book1.xlsx",'Sheet1') # here we are sepcifying which sheet we want to read
print(xl)

