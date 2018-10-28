library(glmnet)
library(dplyr)
library(janitor)
data <- read.csv(file="/Users/Sunny/Desktop/CS498/HW7/Crusio1.csv", header=TRUE, sep=",")

#(a)
data_1 <- data[c(2,4:41)]
data_1 <- na.omit(data_1)
Y = as.matrix(data_1[c(1)])
X = as.matrix(data_1[c(2:39)])
Y[Y == "f"] <- 0
Y[Y == "m"] <- 1
reg_1 <- cv.glmnet(X, Y, family = "binomial", type.measure = "class")
plot(reg_1)


#(b)
data_2 <- data[c(1,4:41)]
data_2 <- na.omit(data_2)
str <- unique(data_2$strain)
set<-c()
for (val in str) {
    if(nrow(subset(data_2,strain == val)) < 10)
    set<-c(set, val)
}

data_2 <- data_2[which((data_2$strain %in% set) == FALSE), ]
Y_2 = as.matrix(data_2[,1])
X_2 = as.matrix(data_2[,c(2:39)])
reg_2 <- cv.glmnet(X_2, Y_2, family = "multinomial", type.measure = "class")
plot(reg_2)


