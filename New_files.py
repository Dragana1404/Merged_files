import os
import pandas as pd
from glob import glob
import inspect


path = "C:/Users/Nenad/Desktop/Data"
EXT = "data1.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(path)
                 for file in glob(os.path.join(path, EXT))]

for f in all_csv_files:
    df1 = pd.read_csv(f, header=None)
    df2 = pd.read_csv(f, header=None)
    df3 = pd.read_csv(f, header=None)
    combined_csv_data =pd.concat([pd.read_csv(f, header=None) for f in all_csv_files])

print("File from Folder 1: ")
print(df1)
print("The number of rows is: ", df1.shape[0])
print('\n')
print("File from Folder 2: ")
print(df2)
print("The number of rows is: ", df2.shape[0])
print('\n')
print("File from Folder 3: ")
print(df3)
print("The number of rows is: ", df3.shape[0])
print('\n')
combined_csv_data.to_csv('combined_data.csv')
print("Combined CSV file: ")
print(combined_csv_data)
print("The number of rows is: ", combined_csv_data.shape[0])
print('\n')
exe='combined_data.csv'
print("The path from file is: ")
print(os.path.abspath(exe))