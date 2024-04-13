# For Exception Handling in Pyhton we use
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

import datetime as mt


x = 0
try:
    x = int(input("Enter Your Age: "))
except:
    print("Enter Age in Number not in text")
else:
    print("You are eligilbe")
finally:
    print("Finaly")



c = 20
b = '10'
v = c+int(b)
print(v)

n = str(c) + b
print(n)
a = 1


def my_bio():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    my_string = str(input('Enter date(yyyy-mm-dd): '))
    my_date = mt.datetime.strptime(my_string, "%Y-%m-%d")
    """
    this function will take bio data from user and shows it
    :param
    name , age , date of brith 
    """
    print("\n\nName",name,"\nAge: ",age,"\nDB",my_date)


print(my_bio.__doc__)
