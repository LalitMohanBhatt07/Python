import pandas as pd;
import numpy as np

def createAndDisplayArray():
    
    # create a numpy array : 
    data=np.array([[1,2,3],[4,5,6],[7,8,9]])
    
    # create a dataframe
    df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

# display the dataframe
    print("DataFrame createed form Numpy Array")
    print(df)
    
    
def main():
    createAndDisplayArray()

main()