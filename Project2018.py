#Store Project 2018 codes in this file
import pandas as pd # What is Pandas https://pandas.pydata.org/pandas-docs/stable/
iris= pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data') # This is how the data is pulled to my PC
iris_cols=['Sepal Length','Sepal Width','Petal Length', 'Petal Width','Class'] #The raw data from UCI doesn't contain column name, this line will give a name to each of the columns
iris.columns = iris_cols # This line will executes and assigns each of the names in the List to each column
iris.describe() # provides summary satistics of the dataset, (this line isn't executed in Visual Studio code, I run this in Jupyter notebook)
iris.shape     # shows number of rows and columns
iris.head() # prints only the first 5 rows of the dataset 
iris.tail() # prints only the last 5 rows of the dataset
print (iris) # prints the data 
