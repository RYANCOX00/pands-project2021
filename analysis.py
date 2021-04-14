# A program to explore and present the Fisher's Iris Data Set
# Author: Ryan Cox

import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pandas as pd

# defining the files and lists to be used in code. 
irisFile = "iris_csv.csv"
summaryFile = "species_summary.txt"
summary = []    # appending summary data to list for pushing to summary file later.  
                # needed to do this way as variable would over write the summary file otherwise


# Creating the functions that will be used in the code.  

# Function to write to summary text file.
def writing_to_summary(summary):   # pushing summary data to summary file 
    with open (summaryFile, "wt") as f: #in write mode so not added everytime its ran
        for contents in summary:  # as a for loop so contents of list uploaded seperately and not as a list itself. 
            f.write(str(contents))

# histogram from function hist() # without species breakdown
def hist(feature, species, colour, species_title): 
    sns.set_style("darkgrid")
    sns.displot(x= feature, data = species, color = colour)
    plt.ylabel("Frequency", fontsize = 14, weight ="bold")
    plt.xlabel(feature +" in cm", fontsize = 14, weight ="bold")
    plt.title(species_title, fontsize=18, weight = "bold")
    plt.show()


# histogram from function hist() # with species breakdown
def hist_species(feature):
    palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"}
    sns.set_style("darkgrid")
    sns.displot(x = feature, data = df, hue= "Species", multiple= "stack", palette=palette)
    plt.ylabel("Frequency", fontsize = 14, weight ="bold")
    plt.xlabel(feature +" in cm", fontsize = 14, weight ="bold")
    plt.title(feature + " by species", fontsize=18, weight = "bold")
    plt.show()


# Function to create scatter plots
# use sample code below to create function here 

# Reading in file from Pandas
df = pd.read_csv(irisFile) # changed reading in the file to Pandas. Below variables also changed.
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"]


# creating variables for the different species of Iris
gp = df.groupby("Species")
setosa = gp.get_group('Iris-setosa')
versicolor = gp.get_group('Iris-versicolor')
virginica = gp.get_group('Iris-virginica')


#Checking for missing value
null_values = df.isnull().values.any() #Delft Stack
if null_values == False:
    print("\nThere is no missing values in this data set.") # optional for now, main purpose to the output to summary file.
    no_null = "There is no missing values in this data set."
    summary.append(no_null)  #appending summary data to list for pushing to summary file later. 


# Manipulating the list to drop the "Iris-" and capitalize each species. The finding unique species and saving as a list.
# Outputting to the user the type of Iris species added to a string. 
df["Species"] = [i.replace("Iris-", "").capitalize() for i in df["Species"]]
species = (df['Species'].unique()) 
text = "\n\nThe species of Iris flower are being analysed are: "
species1 = ", ".join(map(str, species)) # joining the contents of the list as a string with ", " as the seperator. 
species_output = (text + species1) # adding both strings for output variable.
summary.append(species_output) 
print(species_output)


## May want to run other stats # bar chart for the total sample of each i.e. 50/50/50?

## Below running .describe() and pushing summary list and subsequently to summary file
full_summary_text = ("\n\nA summary of all the Iris species:\n")
full_summary = df.describe() 
summary.append(full_summary_text)
summary.append(full_summary)
print("\nA summary of all species has been written to text file in a single data frame.")

setosa_summary_text = ("\n\nA summary of the Setosa species:\n") 
setosa_summary = setosa.describe()
summary.append(setosa_summary_text)
summary.append(setosa_summary)
print("\nA summary of the Setosa species has been written to text file in a single data frame.")

versicolor_summary_text = ("\n\nA summary of the Versicolor species:\n") 
versicolor_summary = versicolor.describe()
summary.append(versicolor_summary_text)
summary.append(versicolor_summary)
print("\nA summary of the Versicolor species has been written to text file in a single data frame.")

virginica_summary_text = ("\n\nA summary of the Virginica species:\n") 
virginica_summary = virginica.describe()
summary.append(virginica_summary_text)
summary.append(versicolor_summary)
print("\nA summary of the Virginica species has been written to text file in a single data frame.")

writing_to_summary(summary) # calling the function as pushing to summary file.  


#histogram from function hist() # without species breakdown
#hist("Sepal Lenght", df, "red", "All Species")
#hist("Sepal Width", df, "yellow", "All Species")
#hist("Petal Lenght", df, "green", "All Species")
#hist("Petal Width", df, "orange", "All Species")


#sns.displot(x= "Sepal Lenght", data = df, hue="Species", multiple="stack")
hist_species("Sepal Lenght")
hist_species("Sepal Width")
hist_species("Petal Lenght")
hist_species("Petal Width")




# Scatter plot sample
# need to create function for these as done with hist
#plt.scatter(setosa["Sepal Lenght"], setosa["Sepal Width"] , color = "red")
#plt.scatter(versicolor["Sepal Lenght"], versicolor["Sepal Width"], color = "yellow")
#plt.scatter(virginica["Sepal Lenght"], virginica["Sepal Width"], color = "green")
#plt.show()
#
#
#sns.displot(data=df["Sepal Lenght"])
#plt.show()

