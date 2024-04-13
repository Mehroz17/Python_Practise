# Storing of Data in the file
with open("New File.txt","w")as fp:
    fp.write("Helloe New File")

with open("New File.txt","a") as ap:
    ap.write("Added")

with open("New File.txt","r")as r:
    c3 = r.read()

with open("New File.txt","a") as ap1:
    ap1.write("Again Added")

with open("New File.txt","r")as r2:
    c5 = r2.read()
print(c5)


# Searching from file
f3= open("New File.txt","r")
ge = input("Enter : ")
if ge in f3.read():
    print("Found")


# w+ mode
with open("New File.txt","w+") as fp:
    fp.write(" Testing W+ Mode")

    print(fp.read())


f = open("New File.txt",'r+')
p = f.tell()
print("The Position of the file", f)