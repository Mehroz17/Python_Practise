import  pandas as pd

d = pd.DataFrame({"Name":['Mehroz','Abdullah'],'Roll #':['FA20-BSe-071','FA20-BSe-075']})

print("original Data Frame: \n",d)

v = d.rename(columns={'Name':'Friends','Roll':'registration #'}) # changing name of  columns
s = d.rename(index={0:'First Friend',1:'Second Friend'}) # changing name of indexes

print(v)
print(s)

# joining 2 dataframe

first = pd.DataFrame({"Students":['Mehroz','Abdullah','Moeez'],'Reg#':['Fa20-BSE-071','Fa20-BSe-075','FA20-BSE-078']})
print(first)
second =pd.DataFrame({"Students":['Mehroz','Abdullah','Saim'],'Reg#':['Fa20-BSE-071','Fa20-BSe-075','FA20-BSE-005']})
combine = pd.concat([first,second])
print("Concatinating")
print(combine)
c = first.merge(second,how='right')# merge is used to update record of one dataframe with the record of other dataframe , it will work only when we have same name of columns
print(c)
