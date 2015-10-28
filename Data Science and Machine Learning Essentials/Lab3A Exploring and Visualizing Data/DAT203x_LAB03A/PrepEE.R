
## Load the data
dirName <- 'C:\\DAT203xLabfiles'
fileName <- "EnergyEfficiencyRegressiondata.csv"
infile <- file.path(dirName, fileName)
eeframe <- read.csv( infile, header = TRUE, stringsAsFactors = FALSE)

## Remove dots from column names.
names(eeframe) <- gsub("\\.", "", names(eeframe))

## Remove columns we are not going to use.
eeframe$CoolingLoad <- NULL

## Convert some columns to factors/categorical. 
catList <- c("OverallHeight", "Orientation")
eeframe[, catList] <- lapply(eeframe[, catList], 
                             function(x) as.factor(as.character(x)))

## Scale the numeric features. 
scaleList <- c("RelativeCompactness", "SurfaceArea",
               "WallArea", "RoofArea", "GlazingArea", 
               "GlazingAreaDistribution")
eeframe[, scaleList] <- lapply(eeframe[, scaleList], function(x) as.numeric(scale(x)))
