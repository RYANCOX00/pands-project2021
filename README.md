# need background and summary of the data set itself 

# pands-project2021

Fisher's Iris data was a statisical study of three species of the Iris plant.  50 flowers of the setosa, versicolor, and virginica species were each measured totaling 150 samples.   Four features of each flower was measured: the length of the sepals; width of the sepals; lenght of the petals; and width of the petal, respectively in that order.  
https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html


SUMMARY OF CODE DEVELOPMENT

In relation to opening the file, I am currently using the Python open file function.  I might change this to PANDAS.  This will make the extraction of species more efficient as discussed above. 

I created empty lists for the raw data can be extracted to.  I originally done this by the feature of the species but ran into trouble later when designing my pilot code (unable to seperate by species when plotting).   I then decided it would be best to extract by way of species themselves using a for loop and == "the species" eg. if row[4] == "Iris-setosa":.

In relation to extracting the features of each species for plotting, later I originally extracted these into seperate lists for each species.  This essentially created 12 seperate list.  I was determined to create a more efficient way to extract this data for plotting.  I decided to create a PANDAS array for the 3 species and 1 for all of the species.  This made its easy to plot by way of indexing e.g. plt.scatter(setosa_df["Sepal Lenght"], setosa_df["Sepal Width"]).  Also the arrays including the array for total data made its easy to analyse using PANDAS functions.  


# Reading csv via Pandas
File now read in through Pandas.  Some work was involved in grouping the species and then amneding variables throughout the code. 


# null data
Also included is a check to see if there is any null/ missing data, and a output to inform the user that there is no missing data is this is the case. 

# types of species
Included is a statement to the user of the species of Iris flower.  I took the unique items from the column and stripped the "Iris-" and capitalized each species before printing as a one line for loop. 


# summary file
need to think about appending to the summary file.  Not all the data is going onto it.  Do I need to do it in one go, is only the last bit of content going to to it   -bug fixed with summary file.

Need to change the wrting mode to over write, this will prevent the contents to being appended each time I run it.
However, if I change to write, only the last variable is pushed to the summary file.  
If I append all the variables to a list and add the contents of a list as a for loop it fixed this. 
Its pushed in one go and not overwritten by the last variable.  *** summary file fixed and in correct mode ***

I have amended the method to summaries the data.  No point in providing a summary of the individual species on seperate dataframes.  Difficult to compare has serves little purpose the way it is. 
Instead I have summarised with the species grouped and the features of the flowers compared. 
Done by using this function, however I had to set the columns as the data was outputing incorrectly.  pd.options.display.max_columns = 999
species_summary = (df.groupby('Species').describe())



# Plotting
I have taken the approach to index the dataframe of each species to plot the required data. 
This was on Matplotlip.  I have subsequently changed to seaborn.  Dataframe and columns are inputted seperately. 
First I created a histplot with plots and  labels/ font. 
Once I got it working I created my own function so that I could run plots for the different features.
I then decided to use a hue, so that the categories could be told apart on the plot.  
I also included a color palatte and 'darkgrid' background. 
# UPDATE ON PLOTTING :
histogram 
Plan to do a total for the 4 features  and do 4 features again with the the frequesncy of each species
*** Unable to use a function to plot the histograms and with the subplot method, the plots were going onto seperate figures.  
I had to create a dict and do a for loop to plot 4 hostograms on one main plot. 
No need to create my own funtion as it was handy enough to do a for loop and keep the same specs

With scatter plots, I done a Pairplot so all scatter plots are plotted as sub plots on one main plot. 

Consider changing to normal scatter plots and using (0,2) in a sub plot format. 
Use the bubble size as frequency?  

# TO DO:
Need to save plots as pngs. 
Write the read me file and researach summary / report. 