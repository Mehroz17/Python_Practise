# Making and using of CSV file
import  csv

# Wirint the file
with open("CSVFile.csv","w",newline= "")as f:
    data_handler =csv.writer(f)
    data_handler.writerow(["Ahmed","25","65Kg"])
    data_handler.writerow(["Arif","21","67Kg"])

# Appending
with open("CSVFile.csv","a",newline= "")as f2:
    data_handler =csv.writer(f2)
    data_handler.writerow(["Muhammad Mehroz","20","50kg"])
    data_handler.writerow(["Muhammad Moeez","18","52Kg"])


# Reading the file
with open("CSVFile.csv") as f1:
    c = csv.reader(f1)
    o = input("Enter Name: ")
    for i in c:
        if o == c:
            print("Found")
            break
        else:
            continue