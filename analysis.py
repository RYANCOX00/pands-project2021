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

def iris_species():
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

iris_species() 

setosaarray = np.array(setosa, float)  # converting the lists to numpy arrays
versicolorarray = np.array(versicolor, float)
virginicaarray = np.array(virginica, float)



# Need to analyse the data.  Think about PANDAs.  May need to import data above using PANDAS instead. 



# Setosa contents for plotting  There has to be a more efficient way to do this!   Can I index it directly from the plotting code?? Unable to do so so far.  
# Will get it working first and then think about efficentcy afterwards.  Might be better to use pandas .loc
setosa_sepals_lenght = [item[0] for item in setosaarray]  #https://stackoverflow.com/questions/29934201/using-every-first-element-in-a-multidimensional-array
setosa_sepals_width = [item[1] for item in setosaarray]
setosa_petals_lenght = [item[2] for item in setosaarray]
setosa_petals_width =  [item[3] for item in setosaarray]

versicolor_sepals_lenght = [item[0] for item in versicolorarray]  
versicolor_sepals_width = [item[1] for item in versicolorarray]
versicolor_petals_lenght = [item[2] for item in versicolorarray]
versicolor_petals_width =  [item[3] for item in versicolorarray]

virginica_sepals_lenght = [item[0] for item in virginicaarray]  
virginica_sepals_width = [item[1] for item in virginicaarray]
virginica_petals_lenght = [item[2] for item in virginicaarray]
virginica_petals_width =  [item[3] for item in virginicaarray]


# Plotting data 
# Sepal lenght X width
plt.scatter(setosa_sepals_lenght, setosa_sepals_width, color = "red")
plt.scatter(versicolor_sepals_lenght, versicolor_sepals_width, color = "yellow" )
plt.scatter(virginica_sepals_lenght, virginica_sepals_width, color = "green")
plt.show()