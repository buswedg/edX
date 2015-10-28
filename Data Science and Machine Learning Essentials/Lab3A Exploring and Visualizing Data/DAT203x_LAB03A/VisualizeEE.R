## Install ggplot2 (use a personal library if  prompted!)
## install.packages('ggplot2', dep = TRUE)

## Use basic R graphics to create a pair-wise scatter plot
Azure = FALSE
if(Azure){
  eeframe <- maml.mapInputPort(1)
  maml.mapOutputPort('eeframe')
} 
pairs(~ ., data = eeframe)

## Use ggplot2 to create conditioned scatter plots
library(ggplot2)
plotCols <- c("RelativeCompactness",
              "SurfaceArea",
              "WallArea",
              "RoofArea",
              "GlazingArea",
              "GlazingAreaDistribution")
plotEE <- function(x){
  title <- paste("Heating Load vs", x, "\n conditioned on OverallHeight and Orientation")
  ggplot(eeframe, aes_string(x, "HeatingLoad")) +
    geom_point() +
    facet_grid(OverallHeight ~ Orientation) +
    ggtitle(title) +
    stat_smooth(method = "lm")
}
lapply(plotCols, plotEE)


## Create histograms
plotCols4 <- c("RelativeCompactness",
               "SurfaceArea",
               "WallArea",
               "RoofArea",
               "GlazingArea",
               "GlazingAreaDistribution",
               "HeatingLoad")
library(gridExtra)
eeHist <- function(x) {
  title <- paste("Histogram of", x, "conditioned on OverallHeight")
  ggplot(eeframe, aes_string(x)) +
    geom_histogram(aes(y = ..density..)) +
    facet_grid(. ~ OverallHeight) +
    ggtitle(title) +
    geom_density()
}
lapply(plotCols4, eeHist)


## Create box plots
eebox <- function(x) {
  title <- paste("Box plot of", x, "by OverallHeight")
  ggplot(eeframe, aes_string('OverallHeight', x)) +
    geom_boxplot() +
    ggtitle(title)
}
lapply(plotCols4, eebox)
