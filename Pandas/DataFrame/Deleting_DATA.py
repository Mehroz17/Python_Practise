import pandas as pd

revi = pd.DataFrame({"Countries":['Afganistan','Pakistan','India','America','UAE','UK'],'POP':[0,1,2,3,4,5]})
print(revi.drop('Countries',axis=1))