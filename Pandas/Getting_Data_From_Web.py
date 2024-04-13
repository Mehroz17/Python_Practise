## we are going to learn how to get data from an web page and then use it in pandas as a dataframe
import pandas as pd

# from wiki pedia page
page = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
wiki = pd.read_html(page, attrs={'class':'wikitable'})
print(wiki[0].head())


#extract information from non wiki page
page2 = "https://stats.espncricinfo.com/c/content/records/284175.html"
non_wiki = pd.read_html(page2, attrs={'class':'engineTable'}) # here class is the type of table used in html language

# to check it go to that page inspect element and search table class
print(non_wiki[0].head()) # [0] means that we are accessing the first table of the page
# if the page has more than one table then we can use [1] for the 2nd table and so on

# now saving the data from webpage to csv file
# save_file_name = "./cricketerswithmostCenturies.csv" # this is the path where we want to save the file
# non_wiki[0].to_csv(save_file_name  ,index= False)

# now i am replacing the name of player
read = pd.read_csv("cricketerswithmostCenturies.csv")
read["Player"] = read['Player'].replace({"SR Tendulkar (INDIA)":"Baber Azam (PAKISTAN)"})
print(read.head())

# to convert it into pdf format
#Firstly, We convert our CSV file to HTML using the Pandas
#In the Second Step, we use PDFkit Python API to convert our HTML file to the PDF file format.

# saving again to csv
save_again = "./savaagain.csv"
read.to_csv(save_again,index=False)

#now converting to html
read.to_html("MYsave.html")
# now from the webpage we can use ctrl-p to save as pdf