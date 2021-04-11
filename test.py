# A program to explore and present the Fisher's Iris Data Set
# Author: Ryan Cox

import numpy as np 
import matplotlib.pyplot as plt
import csv
import pandas as pd

irisFile = "iris_csv.csv"
summaryFile = "species_summary.txt"

def writing_to_file(summary):
    with open (summaryFile, "wt") as f:
        f.write(str(summary))


df = pd.read_csv(irisFile) # changed reading in the file to Pandas. Below variables also changed.
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"]


#Checking for missing value
null_values = df.isnull().values.any() #Delft Stack
if null_values == False:
    print("There is no missing values in this data set. \n")


gp = df.groupby("Species")
setosa = gp.get_group('Iris-setosa')
versicolor = gp.get_group('Iris-versicolor')
virginica = gp.get_group('Iris-virginica')


    
species = (df['Species'].unique())
species = [i.replace("Iris-", "").capitalize() for i in species]
the_species = print ("The species of Irish flower are being analysed are: ", *species, sep = "\n")


print("\n")


## May want to run stats for each species seperately & other stats # bar chart for the total sample of each i.e. 50/50/50?
print("Full summary has been written to text file. \n")
full_summary = df.describe() # May not need to print. rather output to text file 
writing_to_file(full_summary)


print("A summary of the Setosa species:")
print(setosa.describe())

print("\nA summary of the Versicolor species")
print(versicolor.describe())

print("\nA summary of the Virginica species")
print(virginica.describe())




## Better plotting  # Indexing the Data Frame instead of creating many variables. 
## will be best to create a function for these plots rather than writing below out many times. 
plt.scatter(setosa["Sepal Lenght"], setosa["Sepal Width"] , color = "red")
plt.scatter(versicolor["Sepal Lenght"], versicolor["Sepal Width"], color = "yellow")
plt.scatter(virginica["Sepal Lenght"], virginica["Sepal Width"], color = "green")
plt.show()