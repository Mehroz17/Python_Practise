# using functions as a variables
# example
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

result = add(4, 0) - sub(2,6)
print("result = ",result)


a = input("enter y/n")
while a.upper()!="N":
    print("Hello G")
    a = input("enter y/n")