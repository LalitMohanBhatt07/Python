import numpy as np
import pandas as pd

def convert(array):
    series=pd.Series(array)
    print("Original Numpy array : ")
    print(array)
    print("Converted panda series: ")
    print(series)
    
def main():
    array=np.array([10,20,30,40])
    convert(array)
    
main()