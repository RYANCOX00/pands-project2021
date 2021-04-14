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
hist_data = []


# Creating the functions that will be used in the code.  

# Function to write to summary text file.
def writing_to_summary(summary):   # pushing summary data to summary file 
    with open (summaryFile, "wt") as f: #in write mode so not added everytime its ran
        for contents in summary:  # as a for loop so contents of list uploaded seperately and not as a list itself. 
            f.write(str(contents))


# histogram from function hist() # with species breakdown
#def hist_species(feature):
    #palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"}
    #sns.set_style("darkgrid")
   # hist = sns.pairplot(x = feature, data = df, hue= "Species", multiple= "stack", palette=palette)
   # hist.set_axis_labels(feature + "in cm","Frequency",fontsize = 14, weight ="bold")
    

def hist (feature, count):
    fig, axes = plt.subplots(2, 2, figsize=(15, 5), sharey=True)
    palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"}
    sns.set_style("darkgrid")
    fig.suptitle('test')
    hist =sns.histplot(ax=axes[count], x=feature, data = df, hue= "Species", multiple= "stack", palette=palette)
    #hist.set_axis_labels(feature + "in cm","Frequency",fontsize = 14, weight ="bold")
    axes[count].set_title(feature)
    fig.tight_layout()
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

writing_to_summary(summary) # calling the function and pushing to summary file.  



# Histograms from the function hist with species breakdown by hue.   # function wont work as they plot on seperate figures.
#hist("Sepal Lenght", (0,0))
#hist("Sepal Width", (0,1))
#hist("Petal Lenght", (1,0))
#hist("Petal Width", (1,1))

hist_list = {"Sepal Lenght": (0,0), "Sepal Width" : (0,1), "Petal Lenght": (1,0), "Petal Width":(1,1)}

sns.set(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 8), sharey=True) # sharey =true keeps the y axix labels the same 
palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"}
fig.suptitle('Iris Features Measurements', fontsize = 20, weight= "bold")
for key, value in hist_list.items(): # running the plot as a for loop with the plt.show() outside the for loop
    hist =sns.histplot(ax=axes[value], x=key, data = df, hue= "Species", multiple= "stack", palette=palette, edgecolor= 'black')
    hist.set_xlabel(key + " in cm", fontsize = 14) 
    hist.set_ylabel("Frequency", fontsize = 14)
    fig.tight_layout()
plt.show()



#sns.pairplot(df, hue = 'Species', diag_kind = 'hist') # consider changing the diag_kind
#plot_kws = {'multiple':'stack', 'palette': 'palette'})
#plt.show()

# Scatter plot sample
# need to create function for these as done with hist
#plt.scatter(setosa["Sepal Lenght"], setosa["Sepal Width"] , color = "red")
#plt.scatter(versicolor["Sepal Lenght"], versicolor["Sepal Width"], color = "yellow")
#plt.scatter(virginica["Sepal Lenght"], virginica["Sepal Width"], color = "green")
#plt.show()

#sns.displot(data=df["Sepal Lenght"])
#plt.show()