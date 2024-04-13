import pandas as pd
import csv

"""
working with different delimited formats

"""



f = open("working.csv")
r = csv.reader(f)
for line in r:
    print(line)