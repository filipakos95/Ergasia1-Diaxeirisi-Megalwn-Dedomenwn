
# Reading csv files with pandas
#

# The pandas library offers you a way to easily read data from a .csv file
# and handle the red data via a data.frame just like
# in R. Well not exactly like in R, but in a similar way with some
# syntactic differences.
import pandas as pd
import numpy as np


# Read the csv dataset from the file
# The variable wineData is a data.frame that is provided by pandas
# NOTE: header=0 means that the file HAS a header and is located at line 0 of
# the file i.e. at the start.
# Files without header should be read with header=None
wineData = pd.read_csv("winequality-white.csv", header=0, sep=";", engine='python')


# Print out the data type of each variable to see if everything has been read fine from the file
print(wineData.dtypes)

# Print dimensions of the data frame in the form of (number of rows, number of columns)
print(wineData.shape)

# Check if each column of the data frame is numeric
for col in wineData.columns:
    if pd.api.types.is_numeric_dtype(wineData[col]):
        print ('Column', col, 'is numberic (', wineData[col].dtype, ')')
    else:
        print ('Column', col, 'is NOT numberic. It is', wineData[col].dtype)
        print('This error is FATAL. Program should terminate.')
        


# Remove entire rows, if at least one variable in row has a missing value.
# Store the "cleaned" data.frame in variable wineData
wineData = wineData.dropna()

# Get a peek at the data. Look at the first rows of the data frame
print('\nFirst 2 rows')
print( wineData.head(2) )
print('\nLast 2 rows')
print( wineData.tail(2) )

# Indexing using .iloc
# E.g. all rows (:) fifth column (remember, column numbering starts at 0)
print("Printing firth column (column at position 4) for all rows:")
print(wineData.iloc[:, 4])



#
# PCA
# 

# Next two lines required to properly use the PCA function
from sklearn import decomposition
from sklearn.decomposition import PCA



# Create the PCA object from the sklearn library
# Take a look at the documentation:
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
# HINT: ALWAYS look at the documentation to see what parameters to pass and what the
# return values are.
pca = decomposition.PCA(n_components=wineData.shape[1])

# Initialize the PCA function of the sklearn module.
pca = decomposition.PCA(n_components=2)

# Show now the eingenvectors.
pca.fit(wineData)
print("Eigenvectors:")
print(pca.components_)
transformedwineDataset = pca.transform(wineData)

# Print out the new data when the original data
# is mapped onto the Eigenvectors.
print("\nNew data points, on the space defined by the Eigenvectors")
print( transformedwineDataset)

#variance
X = np.array ([[-1, 1]])
pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)

print(pca.explained_variance_ratio_)

print(pca.singular_values_)

