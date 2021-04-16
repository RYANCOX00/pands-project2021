# Iris Fishers Dataset Exploration and Visualisation
This repository is intended as coursework submission for the Programming and Scripting Module at GMIT in 2021.


### The dataset
The Iris Fishers Dataset is a set of measurements of 150 Iris flowers.  The flowers were made up of three different species of Iris flower. A sample of 50 Iris-Setosa, 50 Iris-Versicolor and 50 Iris-Virginica were selected.  The features measured on each sample was the sepal length, sepal width, petal length and petal width.  All measurements in the data set were in centimetres. 

![Iris image](https://user-images.githubusercontent.com/77641344/115000853-10912800-9e9b-11eb-9755-df01c7bd1fc6.png)


### What was the intention of the dataset?
The dataset was used as a multivariate data set used by Ronald Fisher, a statistician and biologist.  Fisher used the dataset to argue the linear Discriminant Analysis Method in statistics.  This method argues that two or more combinations of features can categorise or separate an object. This was published in his paper: The use of multiple measurements in taxonomic problems in 1936.

![RonaldFisher1912 image](https://user-images.githubusercontent.com/77641344/115000446-ad9f9100-9e9a-11eb-9da9-66883c1f51ef.jpg)


### How is the dataset used today?
The Iris Fishers Dataset is well known today.  Many have explored the dataset and it is seen as a textbook case study for statistical classification.  Furthermore, with developments in machine learning technology, the use of the dataset has become widespread in teachings of data science.  The concept of automatically categorising new entries based on the analysis of some of the features has been explored [REF].  Below I will explore the dataset to see if species of Iris flower can be distinguished based on their features. 



## Aim of this project
This repository will explore the Iris Fishers Dataset using Python.  I will firstly aim to summarise the differences of the features across the three species. A comparative table will be outputted to summarise the key differences in sizes of the species per feature.   
I will then aim to visualise the differences in features by plotting a histogram of each feature with the species as a category. This will show the user the size of each feature and frequency of each species within a particular size range.  
I will finally aim to compare the relationships between each feature on a scatter plot. This will allow one to see or not see clusters of species which may or may not distinguish their categories.  
Tools that will be used in the exploration and visualisation include: 
1.	Pandas
2.	Matplotlib
3.	Seaborn
