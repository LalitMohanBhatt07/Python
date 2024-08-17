import pandas as pd

data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles',"Chicago"]
}

# specifying index labels
indexLabels=['Person1','Person2','Person3']

df=pd.DataFrame(data,index=indexLabels)

print(df)