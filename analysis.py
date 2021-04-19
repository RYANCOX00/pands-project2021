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
summary = []    # appending summary data to list for pushing to summary file in one go later.  
               

# Function to write to summary text file.
def writing_to_summary(summary):   # pushing summary data to summary file 
    with open (summaryFile, "wt") as f: #in write mode so not added everytime its ran
        for contents in summary:  # as a for loop so contents of list uploaded seperately and not as a list itself. 
            f.write(str(contents))


# Reading in file from Pandas
df = pd.read_csv(irisFile) # changed reading in the file to Pandas. Below variables also changed.
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"]


#Checking for missing value.  Output if there is now missing data continues, or alerts the user that there is missing data and ends the programme. 
null_values = df.isnull().values.any() #Delft Stack
if null_values == False:
    no_null = "There is no missing values in this data set."
    print(no_null)
    summary.append(no_null)  #appending summary data to list for pushing to summary file later. 
else:
    print("There is missing data in the dataset. Please review. Quitting programme.\n ")
    quit()

# Manipulating the list to drop the "Iris-" and capitalize each species. Then finding unique species and saving as a list.
# Outputting to the user the type of Iris species added to a string. 
df["Species"] = [i.replace("Iris-", "").capitalize() for i in df["Species"]]
species = (df['Species'].unique()) 
species1 = ", ".join(map(str, species)) # joining the contents of the unique list as a string with ", " as the seperator. 
text = "\nThe species of Iris flower being analysed are: "
species_output = (text + species1) # adding both strings for output variable.
summary.append(species_output) 
print(species_output)


# Summarising data
full_summary_text = ("\n\nA summary of all the Iris species:\n")
full_summary = df.describe().round(2)  # an overview of the Iris data using .describe().  No breakdown of species yet. 
summary.append(full_summary_text) # appending to summary list. (Later to summary file)
summary.append(full_summary)
print("\nA summary of all species has been written to the summary file in a single data frame.")


# Comparing the features across the species
species_summary_text = "\n\nA summary of each flower features across the different species: \n"
summary.append(species_summary_text) # Appending a text heading to the summary dataframe to the summary file.
pd.options.display.width = 0  # Setting no max columns so that the summary of the features output is not truncated.
species_summary = (df.groupby('Species').describe().round(2))   # Outputing a summary of the features and comparison across the species
summary.append(species_summary)                                 # using the groupby() function and the .describe() function.
print("\nA comparison of the features across the species has been written to the summary file. ")

writing_to_summary(summary) # calling the function and pushing to summary file.  



# Plotting 
# Creating a color scheme for the species to be used across the plots.
palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"} 

# Saving the features to be plotted and their position on the subplots as a dict. (for histogram plotting) 
hist_dict = {"Sepal Lenght": (0,0), "Sepal Width" : (0,1), "Petal Lenght": (1,0), "Petal Width":(1,1)} 

# Histogram
sns.set(style="darkgrid") # setting the background of the mainplot. 
fig, axes = plt.subplots(2, 2, figsize=(15, 8), sharey=True) # subplot to be 2x2 and size.  sharey =true keeps the y axix labels the same. 
fig.suptitle('Iris Features Measurements', fontsize = 28, weight= "bold") #setting the title of the plot/ 
for key, value in hist_dict.items(): # plots are from a for loop. 
    hist =sns.histplot(ax=axes[value], x=key, data = df, hue= "Species", multiple= "stack", palette=palette, edgecolor= 'black')  # plot to be created with these arguements.  axes relates to position, x is the feature of the flower,  hue groups them by species, species stacked on oneanother, palette is the color scheme defined above and edge color is black around the bars. 
    hist.set_xlabel(key + " in cm", fontsize = 14)  # labei=ling and managign size of x axis. 
    hist.set_ylabel("Frequency", fontsize = 14) # labei=ling and managign size of y axis. 
    fig.tight_layout() # Setting tight_layout so nothing is crushed. 
plt.savefig('histogram.png')

# Scatter plot
sct = sns.pairplot(df, hue = 'Species', diag_kind = 'auto', height = 2.2, palette=palette, plot_kws= { 'edgecolor':'black' }) # Running a pairplot for the scatterplots.  Features are plotted against eachother. Diag_type will plot a line plot where the feature is plotted against itself. 
plt.suptitle('Comparing Features Across Iris Species',size = 28, weight= "bold") #title are is font adjusted.
sct._legend.remove() # removing orginal/ default legend as its was being crushed by subplots. #unable to move. 
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0) # plotting a new legend outside of the axes border. 
plt.tight_layout()
plt.savefig('scatter.png')