#Import the Pandas library as pd
import pandas as pd
import numpy as np

#Define data with column and rows in a variable named d
d = {'col1': [1, 2, 4, 6, 8], 'col2': [7, 8, 9, 7, 8], 'col3': [5, 6, 8, 9, 7]}

#Create a data frame using the function pd.DataFrame()
df = pd.DataFrame(data=d)

print(df)

#counting columns in python
count_column = df.shape[1]
print(count_column)

#counting rows in python
count_rows = df.shape[0]
print(count_rows)

#Functions
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print (Average_pulse_max)

#Minnimum Function
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print (Average_pulse_min)

#Mean funvtion

calorie_burnage = [240, 500,120, 344, 233, 223, 102, 120, 112, 220]

Average_calorie_burnage = np.mean(calorie_burnage)    #Note: We write np. in front of mean to let Python know that we want to activate the mean function from the Numpy library.

print("ACB:", Average_calorie_burnage)
