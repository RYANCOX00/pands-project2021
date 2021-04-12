# A program to explore and present the Fisher's Iris Data Set
# Author: Ryan Cox

import numpy as np 
import matplotlib.pyplot as plt
import csv
import pandas as pd

irisFile = "iris_csv.csv"
summaryFile = "species_summary.txt"


def writing_to_summary(summary):
    with open (summaryFile, "at") as f:
        f.write(str(summary))


df = pd.read_csv(irisFile) # changed reading in the file to Pandas. Below variables also changed.
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"]


#Checking for missing value
null_values = df.isnull().values.any() #Delft Stack
if null_values == False:
    print("\nThere is no missing values in this data set.") # optional for now, main purpose to the output to summary file.
    no_null = "There is no missing values in this data set."
    writing_to_summary(no_null)


gp = df.groupby("Species")
setosa = gp.get_group('Iris-setosa')
versicolor = gp.get_group('Iris-versicolor')
virginica = gp.get_group('Iris-virginica')


# Find unique species and saving as a list. Manipulating the list to drop the "Iris-" and capitalize each species. 
# Outputting to the user the type of Iris species added to a string. 
species = (df['Species'].unique()) 
species = [i.replace("Iris-", "").capitalize() for i in species]
text = "\n\nThe species of Iris flower are being analysed are: "
species1 = ", ".join(map(str, species)) # joining the contents of the list as a string with ", " as the seperator. 
species_output = (text + species1)
writing_to_summary(species_output)
print(species_output)




## May want to run other stats # bar chart for the total sample of each i.e. 50/50/50?

full_summary_text = ("\n\nFull summary of all the Iris species:\n")
full_summary = df.describe() 
writing_to_summary(full_summary_text)
writing_to_summary(full_summary)
print("\nFull summary has been written to text file.")


setosa_summary_text = ("\n\nA summary of the Setosa species:\n") 
setosa_summary = setosa.describe()
writing_to_summary(setosa_summary_text)
writing_to_summary(setosa_summary)
print("\nSetosa summary has been written to text file.")


versicolor_summary_text = ("\n\nA summary of the Versicolor species:\n") 
versicolor_summary = versicolor.describe()
writing_to_summary(versicolor_summary_text)
writing_to_summary(versicolor_summary)
print("\nVersicolor summary has been written to text file.")


virginica_summary_text = ("\n\nA summary of the Virginica species:\n") 
virginica_summary = virginica.describe()
writing_to_summary(virginica_summary_text)
writing_to_summary(virginica_summary)
print("\nVirginica summary has been written to text file.")


## Better plotting  # Indexing the Data Frame instead of creating many variables. 
## will be best to create a function for these plots rather than writing below out many times. 
plt.scatter(setosa["Sepal Lenght"], setosa["Sepal Width"] , color = "red")
plt.scatter(versicolor["Sepal Lenght"], versicolor["Sepal Width"], color = "yellow")
plt.scatter(virginica["Sepal Lenght"], virginica["Sepal Width"], color = "green")
plt.show()