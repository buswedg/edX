frame1 <- maml.mapInputPort(1)

## Remove outliers 
library(dplyr)
frame1 <- frame1 %>% filter(FFMC > 40) %>% 
                     filter(ISI < 30) %>% 
                     filter(rain < 3)

## Output the data frame
maml.mapOutputPort('frame1')
