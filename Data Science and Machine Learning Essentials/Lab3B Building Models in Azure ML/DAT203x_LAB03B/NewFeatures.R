eeframe <- maml.mapInputPort(1)

library(dplyr)
eeframe = mutate(eeframe,
                 RelativeCompactnessSqred = RelativeCompactness^2,
                 SurfaceAreaSqred = SurfaceArea^2,
                 WallAreaSqred = WallArea^2,
                 RelativeCompactness3 = RelativeCompactness^3,
                 SurfaceArea3 = SurfaceArea^3,
                 WallArea3 = WallArea^3)

maml.mapOutputPort('eeframe')
