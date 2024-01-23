import pandas as pd

proteinconc = pd.read_csv(r"C:\Users\KELVIN\OneDrive\Desktop\data_science\proteinconc.csv", header=0, sep=",")

proteinconc.dropna(axis=0, inplace=True)

#We can use the info() function to list the data types within our data set

print(proteinconc)
print(proteinconc.info())
print(proteinconc.describe())
