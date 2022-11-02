#set working disk

setwd("D:/panepistimio/Διαχείριση Μεγάλων Δεδομένων - Τζαγκαρακης/ergasiaprwth")

#libraries
library(MASS)
library(tidyverse)

#show lines and columns
dim(Cars93)

#show some stats
head(Cars93)

# Let's take a summary of the cars data.
summary(Cars93)

#make cylinders column from factor to numeric, which will be needed later

Cars93$Cylinders <- as.numeric(Cars93$Cylinders)
str(Cars93)

# select columns with only numbers
pcaData <- select(Cars93, Min.Price, Price, Max.Price, MPG.city, MPG.highway, Cylinders, EngineSize, Horsepower, RPM, Rev.per.mile, Fuel.tank.capacity, Passengers, Length, Wheelbase, Width, Turn.circle, Rear.seat.room, Luggage.room, Weight)

# Let's take a summary of new cars data.
summary(pcaData)
pcaData

#remove lines with NAs
pcaData <- na.omit(pcaData)
dim(pcaData)
summary(pcaData)

str(pcaData)

# ready to execute PCA
## R's princomp() function is one way of executing PCA (there are also other functions available e.g. prcomp() ).
# We use princomp() because it can be configured to use the Covariance matrix to calculate Eigenvalues/Eigenvectors
# Please note that princomp() supports also performing PCA by using a Correlation matrix and SVD. This all depends
# on the parameters that you will provide.
# 

principalComponents<-princomp(pcaData,cor=FALSE, score=TRUE)
# Ok, done. Now the result of the princomp() function is a new object -that we store in a new variable
# called principalComponents- that has inside all necessary information. This object has attributes that
# you can access. 
# But first, let's see what attributes it has.
attributes(pcaData)

#You can see attributes such sdev, scores etc. You can display their values.
# Here, we display the calculated scores 
principalComponents$scores

# Or, you can display a summary, which gives you a better overview.
summary(pcaData)

# You may also plot the principal components to see the variances of each principal component 
# 
plot(pcaData)

# 
# into the 2-d plane of the biplot.
biplot(pcaData)

