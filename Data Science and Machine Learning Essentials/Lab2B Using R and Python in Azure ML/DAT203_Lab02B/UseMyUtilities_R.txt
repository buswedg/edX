frame1 <- maml.mapInputPort(1)
source("src/myutilities.R")

numCols <- c("Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod", "Total.Prod")
## Call the round2 function in the myutilities.R script
frame1[, numCols] <- lapply(frame1[, numCols], round2)
maml.mapOutputPort('frame1')
