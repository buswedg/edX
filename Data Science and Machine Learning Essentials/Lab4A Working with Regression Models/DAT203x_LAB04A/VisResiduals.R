frame1 <- maml.mapInputPort(1)

frame1$Resids <- frame1$HeatingLoad - frame1$ScoredLabels

## Plot of residuals vs HeatingLoad.
library(ggplot2)
ggplot(frame1, aes(x = HeatingLoad, y = Resids , by = OverallHeight)) +
  geom_point(aes(color = OverallHeight)) +
  xlab("Heating Load") + ylab("Residuals") +
  ggtitle("Residuals vs Heating Load") +
  theme(text = element_text(size=20))

  ## create some conditioned plots of the residuals
plotCols <- c("WallArea",
              "RoofArea",
              "GlazingArea")

plotEERes <- function(x){
  title <- paste("Residuals vs Heating Load conditioned by", x)
  facFormula <- paste("OverallHeight ~", x)
  ggplot(frame1, aes(Resids, HeatingLoad)) +
    geom_point() +
    facet_grid(facFormula) +
    ggtitle(title) 
}

lapply(plotCols, plotEERes)


## Conditioned histograms of the residuals
ggplot(frame1, aes(Resids)) + 
  geom_histogram(binwidth = 0.5) +
  facet_grid(. ~ OverallHeight) + 
  ggtitle('Histogram of residuals conditioned by Overall Height') +
  xlab('Residuals')

## Quantile-quantile normal plot of the residuals.
Resids35 <- frame1[frame1$OverallHeight == 3.5, ]$Resid
Resids7 <- frame1[frame1$OverallHeigh == 7, ]$Resid
par(mfrow = c(1,2))
qqnorm(Resids35)
qqnorm(Resids7)
par(mfrow = c(1,1))


rmse <- function(x){
  sqrt(sum(x^2)/length(x))
} 

outFrame <- data.frame( 
  rms_Overall = rmse(frame1$Resids),
  rms_35 = rmse(Resids35),
  rms_7 = rmse(Resids7))

maml.mapOutputPort('outFrame')
