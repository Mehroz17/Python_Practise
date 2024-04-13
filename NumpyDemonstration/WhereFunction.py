# Where Function
"""
Where acts like a ternary operator we have in java C
"""
# Syntax
"""
np.where(condition,optionA,optionB)

"""


import  numpy as np

a = np.array([["Muhammad Mehroz","Moeez Khan"],["Saim Hafeez","Arslan"]])
x = input("Enter the name u want to search: ")
print(np.where(a == x,"Found","Not Found"))


salary = np.array([-0,100,-5,200])
print(np.where(salary<=0,"Not Ok","OK"))




