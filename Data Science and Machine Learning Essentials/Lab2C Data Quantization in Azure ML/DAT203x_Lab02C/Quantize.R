frame1 <- maml.mapInputPort(1)
## Bin the wind column into 4 categories.
bins <- c(0,   2.5,   5, 7.5, 10)
frame1[, "wind_cat"] <- cut(frame1[, "wind"], breaks = bins)

## Create categorical variables from the X and Y columns.
frame1[, c("X", "Y")] <- lapply(frame1[, c("X", "Y")], as.factor)

## Output the data frame.
maml.mapOutputPort('frame1')
