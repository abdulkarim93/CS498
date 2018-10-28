library(glmnet)
I2000 = t(read.table("/Users/Sunny/Desktop/CS498/HW7/I2000.txt", header = FALSE, sep = ""))
I2000 = as.matrix(I2000)

Tissues = sign(read.table("/Users/Sunny/Desktop/CS498/HW7/tissues.txt", header = FALSE, sep = ""))
Tissues[Tissues ==1] <- TRUE
Tissues[Tissues ==-1] <- FALSE
Tissues = as.matrix(Tissues$V1)

regression <- cv.glmnet(I2000, Tissues, family = "binomial", type.measure = "class")
plot(regression)

pre = sign(predict(regression,I2000, s="lambda.min"))
pre[pre ==1] <- TRUE
pre[pre ==-1] <- FALSE

total<- sum (Tissues == pre)
err_rate<- (1 - total/dim(pre))
baseline <- max(sum(Tissues == 0), sum(Tissues == 1)) / 62

