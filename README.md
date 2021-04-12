# pands-project2021

Fisher's Iris data was a statisical study of three species of the Iris plant.  50 flowers of the setosa, versicolor, and virginica species were each measured totaling 150 samples.   Four features of each flower was measured: the length of the sepals; width of the sepals; lenght of the petals; and width of the petal, respectively in that order.  
https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html


SUMMARY OF CODE DEVELOPMENT

In relation to opening the file, I am currently using the Python open file function.  I might change this to PANDAS.  This will make the extraction of species more efficient as discussed above. 

I created empty lists for the raw data can be extracted to.  I originally done this by the feature of the species but ran into trouble later when designing my pilot code (unable to seperate by species when plotting).   I then decided it would be best to extract by way of species themselves using a for loop and == "the species" eg. if row[4] == "Iris-setosa":.

In relation to extracting the features of each species for plotting, later I originally extracted these into seperate lists for each species.  This essentially created 12 seperate list.  I was determined to create a more efficient way to extract this data for plotting.  I decided to create a PANDAS array for the 3 species and 1 for all of the species.  This made its easy to plot by way of indexing e.g. plt.scatter(setosa_df["Sepal Lenght"], setosa_df["Sepal Width"]).  Also the arrays including the array for total data made its easy to analyse using PANDAS functions.  


File now read in through Pandas.  Some work was involved in grouping the species and then amneding variables throughout the code. 

Also included is a check to see if there is any null/ missing data, and a output to inform the user that there is no missing data is this is the case. 

Included is a statement to the user of the species of Iris flower.  I took the unique items from the column and stripped the "Iris-" and capitalized each species before printing as a one line for loop. 



##### need to think about appending to the summary file.  Not all the data is going onto it.  Do I need to do it in one go, is only the last bit of content going to to it   -bug fixed with summary file.

Need to think about a more effecient way to write to the file.   Maybe in one go via a list of strings. 