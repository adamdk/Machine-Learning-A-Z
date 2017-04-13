# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
#select all but the last column as input dataframe (':' = all rows, ':-1' = all rows but not last column)
x = dataset.iloc[:, :-1].values
#select only last column for output dataframe
y = dataset.iloc[:, 3]

# Takine care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)
#imputer.fit(x[:, 1:3])
#x[:, 1:3] = imputer.transform(x[:, 1:3])
#---- two lines above do the same thing as the one line below
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
#transforms to integer categories (words -> ints for example)
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
#takes a range of ints and converts to a matrix of 0 or 1 foe each category
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
#y only has two values so no need to use onehotencoder because output is alreads 1's and 0's
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and the Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
#create a scaler
sc_x = StandardScaler()
#fit the data to the training set and go ahead and transform it
x_train = sc_x.fit_transform(x_train)
#transform the test set with the same fit as the training set
x_test = sc_x.transform(x_test)