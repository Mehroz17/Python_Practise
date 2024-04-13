# List Practise

'''
List is Like Array List in Java and C C++
'''

# Creation of List
# we use [] brackets for list only

list1 = ['Muhammad Mehroz','Ali Ahmed','Abdullah']
# to access we use the index
'''
print(list1[0]) # it will print Muhammad Mehroz

print("Length of the list is: "+str(len(list1))) # len function will return the length of the list and str() is the function to type cast int to string

list1.append("Haris") # append will insert a new value at the last of the list & this function can only add 1 value at one time
print(list1)

list1.insert(1,"Ahmed") # insert function needs index and the value too

list1.extend(["Muneeb","Ommer","Sohail"]) # extend function is used for inserting of more then 1 values in the list
print(list1)


x = input("Enter the Name of the Person: ")

print(x + " occurs "+str(list1.count(x))+" Times in the list") # this function will return the occurance of the values in the list

print("\nThe Position of "+ x +" in the list is "+str(list1.index(x))) # index function tells the index of the value in the list
'''
#print("\nClear Function " )
#list1.clear() # this function will remove all the elements of the list

""" Copy Function

namelist2  = list1.copy() # this is by value
namelist2 = list1 # this is by reference (means the pointer is store in the new list) so when we change the original list then new list will

list1.append("Mama")
print(namelist2)
"""

#Delete  Function
"""del list1[1] # this function wants the index only
print(list1)
"""
# Remove Function
"""remove function delete the element from the list by value
list1.remove("Ali Ahmed")
print(list1)"""

# Pop function
'''
this function will works like stack(last is first out) if we do not give any index
if we give index then it will only pop that element only

we can use this function to store the popped value in an other variable
'''
"""poped_name = list1.pop(0)
print("Popped Name is "+poped_name)
"""

# Sort Function
"""
list1.sort() # in ascending order
print("list in Ascending order"+ str(list1))

list1.sort(reverse=True) # in descending order
print("List is Descending Order"+ str(list1))

"""

## Slicing in the list
list2 = ["Mango","apple","guava","strawberry","peach","orange","peanut"]

print(list2[0:2]) # formula list[startindex: end+1] it do not include last index
print(list2[0:6:3]) # the last number represents the jump
print(list2[::5])