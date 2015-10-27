# Map 1-based optional input ports to variables
dataset1 <- maml.mapInputPort(1) # class: data.frame

## remove columns
cols <- c("X", "Y", "month", "day")
dataset1 <- dataset1[, !(names(dataset1)) %in% cols]

## Create a pairs plot. 
pairs(dataset1)
