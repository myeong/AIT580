###Hypothesis Testing
###------------------
#Question: Examine if the mean heights for males is greater than females.
#Define Null and Alternative Hypothesis and choose the one based on your results (See the Examples-HypothesisTesting-R.pdf) 
#Answer is "reject null hypothesis and accept alternative hypothesis" but make sure to explain your results in detail.

rm(list=ls())

data <- read.csv('height.csv')

males <- which(data$Gender=='M')
females <- which(data$Gender=='F')

t.test(data$Height[males],data$Height[females], alternative="greater",var.equal=T)