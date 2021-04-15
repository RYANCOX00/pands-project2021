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


# Reading in file from Pandas
df = pd.read_csv(irisFile) # changed reading in the file to Pandas. Below variables also changed.
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"]


# Manipulating the list to drop the "Iris-" and capitalize each species. The finding unique species and saving as a list.
# Outputting to the user the type of Iris species added to a string. 
df["Species"] = [i.replace("Iris-", "").capitalize() for i in df["Species"]]
species = (df['Species'].unique()) 
text = "\nThe species of Iris flower are being analysed are: "
species1 = ", ".join(map(str, species)) # joining the contents of the list as a string with ", " as the seperator. 
species_output = (text + species1) # adding both strings for output variable.
summary.append(species_output) 
print(species_output)


#Checking for missing value
null_values = df.isnull().values.any() #Delft Stack
if null_values == False:
    no_null = "\n\nThere is no missing values in this data set."
    print(no_null)
    summary.append(no_null)  #appending summary data to list for pushing to summary file later. 


# Grouping species and creating variables for the different species of Iris
# No need for these anymore as the the summary obtained differently.
#gp = df.groupby("Species")
#setosa = gp.get_group('Setosa')
#versicolor = gp.get_group('Versicolor')
#virginica = gp.get_group('Virginica')


# Below running .describe() and pushing summary list and subsequently to summary file
full_summary_text = ("\n\nA summary of all the Iris species:\n")
full_summary = df.describe() 
summary.append(full_summary_text)
summary.append(full_summary)
print("\nA summary of all species has been written to the summary file in a single data frame.")


species_summary_text = "\n\nA summary of each flower feature across the different species: \n"
summary.append(species_summary_text) # Appending a text heading to the summary dataframe to the summary file.
pd.options.display.max_columns = 999  # Setting the max columns so that the summary of the features output directly under one another. 
species_summary = (df.groupby('Species').describe())  # Outputing a summary of the features and comparison across the species, using the groupby() function and the .describe() function.
summary.append(species_summary)
print("\nA summary of the flower features and comparison across the species has been written to the summary file. ")

writing_to_summary(summary) # calling the function and pushing to summary file.  


# Plotting the histogram as subplots on one plot. Can't plot within my own function as they plot seperately. 

hist_dict = {"Sepal Lenght": (0,0), "Sepal Width" : (0,1), "Petal Lenght": (1,0), "Petal Width":(1,1)}
palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"}


sns.set(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 8), sharey=True) # sharey =true keeps the y axix labels the same #may want to remove for easier reading of plot
fig.suptitle('Iris Features Measurements', fontsize = 28, weight= "bold")
for key, value in hist_dict.items(): # running the plot as a for loop with the plt.show() outside the for loop
    hist =sns.histplot(ax=axes[value], x=key, data = df, hue= "Species", multiple= "stack", palette=palette, edgecolor= 'black') 
    hist.set_xlabel(key + " in cm", fontsize = 14) 
    hist.set_ylabel("Frequency", fontsize = 14)
    fig.tight_layout()


sct = sns.pairplot(df, hue = 'Species', diag_kind = 'auto', height = 2.2, palette=palette, plot_kws= { 'edgecolor':'black' } )
plt.suptitle('Comparing Features Across Iris Species',size = 28, weight= "bold")
sct._legend.remove() # removing orginal/ default legend as its was being crushed by subplots. #unable to move. 
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0) # plotting a new legend outside of the axes border. 
plt.tight_layout()

plt.show() 