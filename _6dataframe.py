import pandas as pd

data={
    'Student Id':[556,557,558],
    'Name':['Mothi','Alice','Bob'],
    'Math Score':[84,90,78],
    'Science Score':[96,85,88],
    'English Score':[84,79,92]
}

# create dataframe
df=pd.DataFrame(data)

#print dataFrame
print("DAtaframe")
print(df)