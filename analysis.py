# A program to explore and present the Fisher's Iris Data Set
# Author: Ryan Cox

import numpy as np 
import matplotlib.pyplot as plt
import csv
import pandas as pd

irisFile = "iris_csv.csv"

setosa = []
versicolor = []
virginica = []

def iris_species():  ## Might want to replace this with Pandas version of importing csv. 
    with open(irisFile) as f:
        csvReading = csv.reader(f, delimiter=",")  #https://realpython.com/python-csv/#what-is-a-csv-file
        
        for row in csvReading:
            if row[4] == "Iris-setosa":
                features =  [row[0], row[1], row[2], row[3] ] #https://stackoverflow.com/questions/24641894/making-objects-from-a-csv-file-python
                setosa.append(features)
            if row[4] == "Iris-versicolor":
                features = [row[0], row[1], row[2], row[3]]
                versicolor.append(features)
            if row[4] == "Iris-virginica":
                features = [row[0], row[1], row[2], row[3]]
                virginica.append(features)

# Creating a function to create the data for each species as a pandas data frame. 
def Dataframe_Function(species):
    species_data = pd.DataFrame (species, columns=["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width"])
    return species_data


iris_species() 

setosaarray = np.array(setosa, float)  # converting the lists to numpy arrays  # this may be replaced later if I 
versicolorarray = np.array(versicolor, float)  # read in the csv directly to pandas. 
virginicaarray = np.array(virginica, float)


# Analysing the data. 
allspecies = np.concatenate((setosaarray, versicolorarray, virginicaarray))

# running the defined function above for each species (and total) and saving the dataframe as a variable 
setosa_df = Dataframe_Function(setosaarray)
versicolor_df = Dataframe_Function(versicolorarray)
virginica_df = Dataframe_Function(virginicaarray)
total_df = Dataframe_Function(allspecies)

## May want to run stats for each species seperately & other stats
print(total_df.describe())


 # Better plotting  # Indexing the Data Frame instead of creating many variables. 
 # will be best to create a function for these plots rather than writing below out many times. 
plt.scatter(setosa_df["Sepal Lenght"], setosa_df["Sepal Width"] , color = "red")
plt.scatter(versicolor_df["Sepal Lenght"], versicolor_df["Sepal Width"], color = "yellow")
plt.scatter(virginica_df["Sepal Lenght"], virginica_df["Sepal Width"], color = "green")
plt.show()