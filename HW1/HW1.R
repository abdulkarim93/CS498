setwd('/Users/Sunny/Desktop/CS498/HW1')
raw_data<-read.csv('pima-indians-diabetes.csv', header=FALSE)
library(klaR)
library(caret)
bigx<-wdat[,-c(9)]
bigy<-wdat[,9]
trscore<-array(dim=10)
tescore<-array(dim=10)
for (wi in 1:10)
{wtd<-createDataPartition(y=bigy, p=.8, list=FALSE)
    nbx<-bigx
    ntrbx<-nbx[wtd, ]
    ntrby<-bigy[wtd]
    trposflag<-ntrby>0
    ptregs<-ntrbx[trposflag, ]
    ntregs<-ntrbx[!trposflag,]
    ntebx<-nbx[-wtd, ]
    nteby<-bigy[-wtd]
    ptrmean<-sapply(ptregs, mean, na.rm=TRUE)
    ntrmean<-sapply(ntregs, mean, na.rm=TRUE)
    ptrsd<-sapply(ptregs, sd, na.rm=TRUE)
    ntrsd<-sapply(ntregs, sd, na.rm=TRUE)
    ptroffsets<-t(t(ntrbx)-ptrmean)
    ptrscales<-t(t(ptroffsets)/ptrsd)
    ptrlogs<--(1/2)*rowSums(apply(ptrscales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ptrsd))
    ntroffsets<-t(t(ntrbx)-ntrmean)
    ntrscales<-t(t(ntroffsets)/ntrsd)
    ntrlogs<--(1/2)*rowSums(apply(ntrscales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ntrsd))
    lvwtr<-ptrlogs>ntrlogs
    gotrighttr<-lvwtr==ntrby
    trscore[wi]<-sum(gotrighttr)/(sum(gotrighttr)+sum(!gotrighttr))
    pteoffsets<-t(t(ntebx)-ptrmean)
    ptescales<-t(t(pteoffsets)/ptrsd)
    ptelogs<--(1/2)*rowSums(apply(ptescales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ptrsd))
    nteoffsets<-t(t(ntebx)-ntrmean)
    ntescales<-t(t(nteoffsets)/ntrsd)
    ntelogs<--(1/2)*rowSums(apply(ntescales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ntrsd))
    lvwte<-ptelogs>ntelogs
    gotright<-lvwte==nteby
    tescore[wi]<-sum(gotright)/(sum(gotright)+sum(!gotright))
}
    sum(tescore)/length(tescore)

setwd('/Users/Sunny/Desktop/CS498/HW1')
wdat<-read.csv('pima-indians-diabetes.csv', header=FALSE)
library(klaR)
library(caret)
bigx<-wdat[,-c(9)]
bigy<-wdat[,9]
nbx<-bigx
for (i in c(3, 4, 6, 8))
{vw<-bigx[, i]==0
    nbx[vw, i]=NA
}
trscore<-array(dim=10)
tescore<-array(dim=10)
for (wi in 1:10)
{wtd<-createDataPartition(y=bigy, p=.8, list=FALSE)
    ntrbx<-nbx[wtd, ]
    ntrby<-bigy[wtd]
    trposflag<-ntrby>0
    ptregs<-ntrbx[trposflag, ]
    ntregs<-ntrbx[!trposflag,]
    ntebx<-nbx[-wtd, ]
    nteby<-bigy[-wtd]
    ptrmean<-sapply(ptregs, mean, na.rm=TRUE)
    ntrmean<-sapply(ntregs, mean, na.rm=TRUE)
    ptrsd<-sapply(ptregs, sd, na.rm=TRUE)
    ntrsd<-sapply(ntregs, sd, na.rm=TRUE)
    ptroffsets<-t(t(ntrbx)-ptrmean)
    ptrscales<-t(t(ptroffsets)/ptrsd)
    ptrlogs<--(1/2)*rowSums(apply(ptrscales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ptrsd))
    ntroffsets<-t(t(ntrbx)-ntrmean)
    ntrscales<-t(t(ntroffsets)/ntrsd)
    ntrlogs<--(1/2)*rowSums(apply(ntrscales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ntrsd))
    lvwtr<-ptrlogs>ntrlogs
    gotrighttr<-lvwtr==ntrby
    trscore[wi]<-sum(gotrighttr)/(sum(gotrighttr)+sum(!gotrighttr))
    pteoffsets<-t(t(ntebx)-ptrmean)
    ptescales<-t(t(pteoffsets)/ptrsd)
    ptelogs<--(1/2)*rowSums(apply(ptescales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ptrsd))
    nteoffsets<-t(t(ntebx)-ntrmean)
    ntescales<-t(t(nteoffsets)/ntrsd)
    ntelogs<--(1/2)*rowSums(apply(ntescales,c(1, 2), function(x)x^2), na.rm=TRUE)-sum(log(ntrsd))
    lvwte<-ptelogs>ntelogs
    gotright<-lvwte==nteby
    tescore[wi]<-sum(gotright)/(sum(gotright)+sum(!gotright))
}
sum(tescore)/length(tescore)


setwd('/Users/Sunny/Desktop/CS498/HW1')
rm(list=ls())
wdat<-read.csv('pima-indians-diabetes.csv', header=FALSE)
library(klaR)
library(caret)
bigx<-wdat[,-c(9)]
bigx2<-apply(bigx, c(1, 2), function(x)x^2)
bigx<-cbind(bigx, bigx2)
errs<-array(dim=10)
cvs<-c(0.005, 0.01, 0.1)
for (wi in c(1:10))
{bigy<-as.factor(wdat[,9])
    wtd<-createDataPartition(y=bigy, p=.8, list=FALSE)
    wstring<-paste("-c", sprintf('%f', cvs[wi]), sep=" ")
    svm<-svmlight(bigx[wtd,], bigy[wtd], pathsvm='/Users/Sunny/Desktop/CS498/HW1/svm_light_OS10.8.4_i7/')
    labels<-predict(svm, bigx[-wtd,])
    foo<-labels$class
    errs[wi]<-sum(foo==bigy[-wtd])/(sum(foo==bigy[-wtd])+sum(!(foo==bigy[-wtd])))
}
mean(errs)

