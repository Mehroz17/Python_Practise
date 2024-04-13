# Dictionary

dict = {"First Name": "Muhammad ","Last Name":"Mehroz","Grade":"45"}

dict["City"] = "Multan"

#iterating through Dict
print("Keys")
for key_only in dict.keys():
    print(key_only)

# for value only
print("\nValues")
for valueonly in dict.values():
    print(valueonly)

print("\n")
# for Both
for x , y in dict.items():
    print(x,y)
