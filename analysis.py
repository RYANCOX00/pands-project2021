import numpy as np 
import matplotlib.pyplot as plt
import csv


irisFile = "iris.data.txt"

sepalLength =[]
sepalwidth = []
petalLength = []
petalWidth = []
irisSpecies = []

def iris_specs(index, object_name):
    with open(irisFile) as f:
        csvReading = csv.reader(f, delimiter=",")  #https://realpython.com/python-csv/#what-is-a-csv-file
        for line in csvReading:
            w = float(line[index])
            object_name.append(w)
            
def iris_species(index, object_name):
    with open(irisFile) as f:
        csvReading = csv.reader(f, delimiter=",")  #https://realpython.com/python-csv/#what-is-a-csv-file
        for line in csvReading:
            x = line[index]
            object_name.append(x)


iris_specs(0, sepalLength)  # index, object_name
iris_specs(1,sepalwidth)
iris_specs(2,petalLength)
iris_specs(3,petalWidth)
iris_species(4,petalWidth)

 
plt.scatter (sepalLength,sepalwidth)
plt.show()

# The species need to be linked together somehow in a dict and each specie plotted seperately.  Need to do more research on
# exploration and visualisation. 