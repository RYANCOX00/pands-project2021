# A program to explore and present the Fisher's Iris Data Set
# Author: Ryan Cox

import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pandas as pd

# Defining the files and lists to be used in code. 
irisFile = "iris_csv.csv"
summaryFile = "species_summary.txt"
summary = []    # Using a list to push to summary of data to text file in one go later.  
               

# Function to write to summary text file.
def writing_to_summary(summary):   # Pushing summary data to summary file.
    with open (summaryFile, "wt") as f: # In write mode so not added everytime its ran.
        for contents in summary:  # As a for loop so contents of list uploaded seperately and not as a list itself. 
            f.write(str(contents))


# Reading in file from Pandas
df = pd.read_csv(irisFile) # Reading in the file with Pandas. REF[5]
df.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"] # Column names amended. 


# Checking for missing values in the dataset. 
null_values = df.isnull().values.any() # REF[6]
if null_values == False: # If no missing values i.e. false, then print such and continue with code.  
    no_null = "There is no missing values in this data set."
    print(no_null)
    summary.append(no_null)  # Appending summary data to list for pushing to summary file later. 
else:       # Otherwise, alert the user that there is missing data and quit the programme.
    print("There is missing data in the dataset. Please review. Quitting programme.\n ")
    quit()

# Manipulating the list to drop the "Iris-" and capitalize each species. Then finding unique species and saving as a list.
# Outputting to the user the type of Iris species added to a string. 
df["Species"] = [i.replace("Iris-", "").capitalize() for i in df["Species"]] # Dropping the "Iris-" and capitalising the each species name. REF[7]
species = (df['Species'].unique())  # Finding unique species' names and saving them as variable. [8]
species1 = ", ".join(map(str, species)) # Joining the contents of the unique list as a string with ", " as the seperator. REF[9]
text = "\nThe species of Iris flower being analysed are: "
species_output = (text + species1) # Adding both strings for output variable.
summary.append(species_output) # Appending species_output to summary list to write to summary file later. 
print(species_output)


# Summarising data
full_summary_text = ("\n\nA summary of all the Iris species:\n")
full_summary = df.describe().round(2)  # An overview of all the Iris data using .describe(). REF[10] 
summary.append(full_summary_text) # Appending to summary list.
summary.append(full_summary)
print("\nA summary of all species has been written to the summary file in a single data frame.")

# Creating dataframe to compare the features across the species
species_summary_text = "\n\nA summary of each flower features across the different species: \n"
summary.append(species_summary_text) # Appending a text heading to the summary dataframe to the summary file.
pd.options.display.width = 0  # Setting no max columns so that the summary of the features output is not truncated. REF[11]
species_summary = (df.groupby('Species').describe().round(2))   # Outputing a summary of the features and comparison across the species
summary.append(species_summary)                                 # Using the groupby() function and the .describe() function.
print("\nA comparison of the features across the species has been written to the summary file. ")

writing_to_summary(summary) # Calling the function and pushing to summary file.  


# Plotting 
# Creating a color scheme for the species to be used across the plots.
palette = {"Setosa": "green", "Versicolor":"yellow", "Virginica": "orange"} 

# Saving the features to be plotted and their position on the subplots as a dict. (for the histogram plotting) 
hist_dict = {"Sepal Lenght": (0,0), "Sepal Width" : (0,1), "Petal Lenght": (1,0), "Petal Width":(1,1)} 

# Histogram
sns.set(style="darkgrid") # Setting the background of the mainplot. 
fig, axes = plt.subplots(2, 2, figsize=(15, 8), sharey=True) # Subplot to be 2x2 and size. REF[12]  sharey =true uses a common y axix for the plots. 
fig.suptitle('Iris Features Measurements', fontsize = 28, weight= "bold") # Setting the title of the plot. 
for key, value in hist_dict.items(): # Plots are from a for loop so they go on one plot. REF [14]
    hist =sns.histplot(ax=axes[value], x=key, data = df, hue= "Species", multiple= "stack", palette=palette, edgecolor= 'black')  # REF[13][14] Axes relates to position, x is the feature of the flower,  hue groups them by species, species stacked on oneanother, palette is the color scheme defined above and edge color is black around the bars. 
    hist.set_xlabel(key + " in cm", fontsize = 14)  # Labeling and managing size of x axis font. 
    hist.set_ylabel("Frequency", fontsize = 14) # Labeling and managing size of y axis font. 
    fig.tight_layout() # Setting tight_layout so nothing is crushed. 
plt.savefig('histogram.png')

# Scatter plot
sct = sns.pairplot(df, hue = 'Species', diag_kind = 'auto', height = 2.2, palette=palette, plot_kws= { 'edgecolor':'black' }) # REF[15] Running a pairplot for the scatterplots.  Features are plotted against eachother. Diag_type will plot a line plot where the feature is plotted against itself. 
plt.suptitle('Comparing Features Across Iris Species',size = 28, weight= "bold") # Title are is font adjusted.
sct._legend.remove() # Removing orginal/ default legend as its was being crushed by subplots. #unable to move. REF[16]
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0) # Plotting a new legend outside of the axes border. 
plt.tight_layout() # Tight layout will plot within the figure areas cleanly.  
plt.savefig('scatter.png')