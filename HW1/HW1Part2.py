import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import csv
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
def bounding_box(u):
    minx = 27
    miny = 27
    maxx = 0
    maxy = 0
    u = np.reshape(u, (28, 28))
    for x in range (28):
        for y in range (28):
            if u[x][y] > 0:
                if x < minx:
                    minx = x
                if y < miny:
                    miny = y
                if x > maxx:
                    maxx = x
                if y > maxy:
                    maxy = y
    v = u[minx:maxx+1][miny:maxy+1]
    v = np.resize(v,(20,20))
    v = np.reshape(v, (400))
    return v
def array_to_csv(name,array):
    with open(name,'wt') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('ImageId','Label'))
        for i in range(len(array)):
            writer.writerow((i , array[i]))
def Gaussian_NB(train_set,train_label,test_set,val_set,val_label):
    classifier = GaussianNB()
    classifier.fit(train_set,train_label)
    accuracy = accuracy_score(val_label, classifier.predict(val_set))
    print(accuracy)
    return classifier.predict(test_set)
def Bernoulli_NB(train_set,train_label,test_set,val_set,val_label):
    classifier = BernoulliNB()
    classifier.fit(train_set,train_label)
    accuracy = accuracy_score(val_label, classifier.predict(val_set))
    print(accuracy)
    return classifier.predict(test_set)
def Decision_Forest(train_set,train_label,test_set,trees,depth,val_set,val_label):
    classifier = RandomForestClassifier(n_estimators =trees, max_depth=depth)
    classifier.fit(train_set,train_label)
    accuracy = accuracy_score(val_label, classifier.predict(val_set))
    print(accuracy)
    return classifier.predict(test_set)
def drawpic(test_label, test_data):
    num = []
    array = np.zeros((10, 28*28))
    count = Counter(test_label)
    for i in range(10):
        num.append(count[i])
        
    for i in range(20000):
        label = test_label[i]
        for j in range(28*28):
            if(test_data[i][j] > 0):
                array[label][j] += int(test_data[i][j])/(num[label]*255)
    draw_figure =plt.figure(figsize=(10,10))
    for i in range(10):
        draw_figure.add_subplot(1, 10, i+1)        
        plt.imshow(array[i].reshape((28,28)), cmap="gray")
    plt.show()
train_set = pd.read_csv("/Users/Sunny/Desktop/CS498/HW1/train.csv").as_matrix()
test_set = pd.read_csv("/Users/Sunny/Desktop/CS498/HW1/test.csv",header=None).as_matrix()
val_set = pd.read_csv("/Users/Sunny/Desktop/CS498/HW1/val.csv").as_matrix()
train_label = train_set[:,1]
train_untouched =train_set[:,2:]
train_stretched = [bounding_box(row) for row in train_untouched]
test_stretched = [bounding_box(row.reshape(784)) for row in test_set]
val_label = val_set[:,0]
val_untouched = val_set[:,1:]
val_stretched = [bounding_box(row.reshape(784)) for row in val_untouched]
Gaussian_untouched  = Gaussian_NB(train_untouched,train_label,test_set,val_untouched,val_label)
Gaussian_stretched  = Gaussian_NB(train_stretched,train_label,test_stretched,val_stretched,val_label)
Bernoulli_untouched = Bernoulli_NB(train_untouched,train_label,test_set,val_untouched,val_label)
Bernoulli_stretched = Bernoulli_NB(train_stretched,train_label,test_stretched,val_stretched,val_label)
Decision_Forest_untouched104 = Decision_Forest(train_untouched,train_label,test_set,10,4,val_untouched,val_label)
Decision_Forest_stretched104 = Decision_Forest(train_stretched,train_label,test_stretched,10,4,val_stretched,val_label)
Decision_Forest_untouched1016 = Decision_Forest(train_untouched,train_label,test_set,10,16,val_untouched,val_label)
Decision_Forest_stretched1016 = Decision_Forest(train_stretched,train_label,test_stretched,10,16,val_stretched,val_label)
Decision_Forest_untouched304 = Decision_Forest(train_untouched,train_label,test_set,30,4,val_untouched,val_label)
Decision_Forest_stretched304 = Decision_Forest(train_stretched,train_label,test_stretched,30,4,val_stretched,val_label)
Decision_Forest_untouched3016 = Decision_Forest(train_untouched,train_label,test_set,30,16,val_untouched,val_label)
Decision_Forest_stretched3016 = Decision_Forest(train_stretched,train_label,test_stretched,30,16,val_stretched,val_label)

drawpic(Gaussian_untouched, test_set)
drawpic(Gaussian_stretched, test_set)
drawpic(Bernoulli_untouched, test_set)
drawpic(Bernoulli_stretched, test_set)
array_to_csv('xinyigu2_1.csv',Gaussian_untouched)
array_to_csv('xinyigu2_2.csv',Gaussian_stretched)
array_to_csv('xinyigu2_3.csv',Bernoulli_untouched)
array_to_csv('xinyigu2_4.csv',Bernoulli_stretched)

array_to_csv('xinyigu2_5.csv',Decision_Forest_untouched104)
array_to_csv('xinyigu2_6.csv',Decision_Forest_stretched104)
array_to_csv('xinyigu2_7.csv',Decision_Forest_untouched1016)
array_to_csv('xinyigu2_8.csv',Decision_Forest_stretched1016)
array_to_csv('xinyigu2_9.csv',Decision_Forest_untouched304)
array_to_csv('xinyigu2_10.csv',Decision_Forest_stretched304)
array_to_csv('xinyigu2_11.csv',Decision_Forest_untouched3016)
array_to_csv('xinyigu2_12.csv',Decision_Forest_stretched3016)

