#(a)
library(glmnet)
library(e1071)
library(data.table)  

train_data = read.csv("/Users/Sunny/Desktop/CS498/HW7/blogData_train.csv")
X<-as.matrix(data.frame(train_data[1:280]))
Y<-as.matrix(data.frame(train_data[281]))
regression <- cv.glmnet(X, Y, alpha=1, family="poisson")
plot(regression)
#(b)
pre_2 <- predict(regression,X,s='lamda.min',type ="response")
plot(Y,floor(pre))
#(c)

test_data

X_3<-as.matrix(data.frame(test_data[1:280]))
Y_3<-as.matrix(data.frame(test_data[281]))
pre_3<-predict(regression,X_3,s='lamda.min',type="response")
plot(Y_3,floor(pre_3))
#(d)
#Why is this regression difficult?
