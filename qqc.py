import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import time

qcc = importr("qcc")
r = robjects.r


#R part
robjects.r('''
MyData <- read.csv(file="data_diana.csv", header = FALSE, sep = ",")
myData <- MyData[1:1700,]

#XBar Charts
a <- myData$V3
b <- myData$V1
V3 <- qcc.groups(myData$V3, myData$V1)
q1 <- qcc(V3, type="xbar")
pl <- plot(q1, chart.all=FALSE)
plsum <- summary(q1)

#S chart
q2 <- qcc(V3, type="S")

#cusum
q3 <- cusum(V3, decision.interval = 4, se.shift = 1 )

#ewma
q4 <- ewma(V3, lambda = 0.3, nsigmas=2)

 ''')

#Look for the outliers for things because they mess up the rest of the model -- very important for cusum
r_data = robjects.globalenv['q1']
r.plot(r_data)
time.sleep(20)

r_dev = robjects.globalenv['q2']
r.plot(r_dev)
time.sleep(20)

r_cusum = robjects.globalenv['q3']
r.plot(r_cusum)
time.sleep(20)

r_ewma = robjects.globalenv['q4']
r.plot(r_ewma)
time.sleep(20)
