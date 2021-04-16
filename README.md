# Iris Fishers Dataset Exploration and Visualisation
This repository is intended as coursework submission for the Programming and Scripting Module at GMIT in 2021.



### The dataset
The Iris Fishers Dataset is a set of measurements of 150 Iris flowers.  The flowers were made up of three different species of Iris flower. A sample of 50 Iris-Setosa, 50 Iris-Versicolor and 50 Iris-Virginica were selected.  The features measured on each sample was the sepal length, sepal width, petal length and petal width.  All measurements in the data set were in centimetres. 

Where did I get the data set for this project?????!!

![Iris image](https://user-images.githubusercontent.com/77641344/115000853-10912800-9e9b-11eb-9755-df01c7bd1fc6.png)



### What was the intention of the dataset?
The dataset was used as a multivariate dataset used by Ronald Fisher, a statistician and biologist.  Fisher used the dataset to argue the Linear Discriminant Analysis method in statistics.  This method argues that two or more combinations of features can categorise or separate an object. This was published in his paper *The use of multiple measurements in taxonomic problems in 1936*.  NEED REFERENCES

![RonaldFisher1912 image](https://user-images.githubusercontent.com/77641344/115000446-ad9f9100-9e9a-11eb-9da9-66883c1f51ef.jpg)



### How is the dataset used today?
The Iris Fishers Dataset is well known today.  Many have explored the dataset and it is seen as a textbook case study for statistical classification.  Furthermore, with developments in machine learning technology the use of the dataset has become widespread in teachings of data science.  The concept of automatically categorising new entries based on the analysis of some of the features has been explored [REF].  Below I will explore the dataset to see if species of Iris flower can be distinguished based on their features. 




## Aim of this project
This repository will explore the Iris Fishers Dataset using Python.  I will firstly aim to summarise the differences of the features across the three species. A comparative table will be outputted to summarise the key differences in sizes of the species per feature.   

I will then aim to visualise the differences in features by plotting a histogram of each feature with the species as a category. This will show the user the size of each feature and frequency of each species within a particular size range.  

I will finally aim to compare the relationships between each feature on a scatter plot. This will allow one to see or not see clusters of species which may or may not distinguish their categories as held by the Discriminant Analysis Method.  

Modules that were imported for this exploration and visualisation are: 
1.	Numpy
3.  Pandas
2.	Matplotlib
3.	Seaborn
4.  CSV


![modules imported](https://user-images.githubusercontent.com/77641344/115039580-7ea01400-9ec8-11eb-9808-e831f7440079.PNG)





# Code development
### Reading in the Iris file 

To read in the data I used Pandas CSV_read function. This function seperates data from commas automatically and saves the data in a dataframe.  This main datafram is saved under the variable *df*. I then immediately renamed the columns to more suitable names that will be used throughout the code: *"Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width","Species"*

![reading in file](https://user-images.githubusercontent.com/77641344/115040934-df7c1c00-9ec9-11eb-9478-0ef04b1ded1a.PNG)


I had orginally used the built-in file opener in Python and saved the different species as variable.  This involved subdequently converting each variable to numpy arrays before further breaking them down into variables for each feature.  As identified above, it was decided the best approach was to read the data in though Panda for more effecient code, analysis and plotting. 



### Code for manipulating the data 
The data under the Species column then needed to be manipulated so that it was in a more presentable format. The intention was to drop the "Iris-" and capitalise each species under this column. The below code was used to do this.

![manipulating species](https://user-images.githubusercontent.com/77641344/115043234-31be3c80-9ecc-11eb-9eff-2ffa056e8c38.PNG)


While working on the species column I took the opportunity to find the unique names in the column and output a breakdown of all the species that is being analysed to the reader. 


![find unique](https://user-images.githubusercontent.com/77641344/115044314-4a7b2200-9ecd-11eb-82cc-cdb30dee5d9f.PNG)


Before moving onto the data exploration, I ran a check to see if there was any missing data in the dataset. This was originally done by simply teling the user that no data was missing from the dataset should that be the case.  However, it was subquently thought that this served no purpose should there be data missing from the data set.  Therefore, the below code was put in place that handles errors if data is missing by stoping the programme and alerting the user. It also tells the user that no data is missing should that be the case.  



### Data exploration code
The intention was to create summary data for the dataframe, features and the species and write this summary data to a text file called species_summary.txt.  To do this in an efficent way for multiple strings it was decided that the summary data would be appended to a list called *summary* before being written to a text file in one go.  A function was created to write the contents of the *summary* list. This was created in write mode so that the contents are overwritten each time the programme is ran. The contents of the list are added as a for loop to prevent the list to be written to the summary file itself.  

![summary file](https://user-images.githubusercontent.com/77641344/115055924-135f3d80-9eda-11eb-86fd-3e929fe7d4d4.PNG)


To get an overview of the dataset, I ran the Pandas .describe() function on the *df* dataframe.  This gave a breakdown of each feature, identifying the count, min, mean, max measurements, among other summary data.  Note that a break down of species was not sought yet.  Also included in this batch of code was a text to be used as a heading for the summary output that stated: *A summary of all the Iris species*.   Both the heading and the summary dataframe were appended to a list *summary*.  This user was also notified in the terminal that a summary of the dataframe was written to the summary file. 

![df summary](https://user-images.githubusercontent.com/77641344/115056810-2e7e7d00-9edb-11eb-9313-bec15869978b.PNG)


I hope to provide a summary of how each feature of the species compared.  The end result provided a breakdown of each feature identifying the count, min, mean, max measurements, among other summary data, comparing each specie of Iris with eachother.  The break down first provided 36 columns wide and 5 rows down.  This was a summary of the features side-by-side rather than underneath eachother.  The solution was to adust the max columns so that the summary of the features output directly under one another, see code below. 

![feature summary](https://user-images.githubusercontent.com/77641344/115058254-faa45700-9edc-11eb-9a79-8c40d81aabd3.PNG)


Initially, the code that was developed provided a summary of the features for each species seperately.  This proved difficult to compare the species against eachother.  It was therfore decided that the *df.groupby('Species').describe()* code was more practical for comparison. 



### Data visualisation code
An approach was initally taken to use matplotlib and numpy arrays to plot the data for the variables. Although it was possible to create a function with the variable names as arguements, this still required the programme to recall the function and make many seperate plots which was ineffiecent and required a lot of computation.  

However, once it was decided to use Pandas dataframe and Seaborn plotting became more efficient.  The histogram plot is designed by plotting all features as subplots (2x2 axes') The 4 features and their positions on the histogram are saved as a dict object. Once the parameters were set for the subplots, each feature was plotted using a for loop and the plot was saved outside the for loop.  This ensured that the features were placed on the same plot, rather than on sperate plots with three empety plot spaces.   The code to acheive this is below. 

![hist plot](https://user-images.githubusercontent.com/77641344/115064797-4529d180-9ee5-11eb-95c8-9f3c2bfea184.PNG)


In relation to the scatter plots, the most efficient way to plot the relationships between each variable to i.e. to achieve Fishers Linear Discriminant Analysis was to use a pairplot.  Otherwise, 9 seperate plot would have to be ran.   A pairplot will plot the columns of a dataframe against eachother so that the user can understand how each relationship behaves.  An issue that arose when programming for this plot was that the plots on the right side were crushing the default legend.  In order to workaround this, the default legend had to be removed and a new legend was added to the plot with its position manually adjusted.  See the pairplot code below. 

![scatter code](https://user-images.githubusercontent.com/77641344/115065686-57f0d600-9ee6-11eb-827a-133159ce6cfa.PNG)