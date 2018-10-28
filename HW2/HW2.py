import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import csv
from numpy import linalg as LA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

train_set = pd.read_csv("/Users/Sunny/Desktop/CS498/HW2/train_data.csv",header = None).as_matrix()
test_set = pd.read_csv("/Users/Sunny/Desktop/CS498/HW2/test_data.csv",header = None).as_matrix() 
train_data,val_data = train_test_split(train_set,train_size=0.1, random_state=1)
label_data = train_data[:,[14]]
label_data[label_data == ' <=50K'] = -1
label_data[label_data == ' >50K'] = 1
val_label = val_data[:,[14]]
val_label[val_label == ' <=50K'] = -1
val_label[val_label == ' >50K'] = 1
train_data = train_data[:,[0,2,4,10,11,12]]
train_data = preprocessing.scale(train_data)
val_data = val_data[:,[0,2,4,10,11,12]]
#val_data = preprocessing.scale(val_data)
test_data = test_set[:,[0,2,4,10,11,12]]
def array_to_csv(name,array):
    with open(name,'wt') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Example','Label'))
        for i in range(len(array)):
            writer.writerow(("'%s'"%str(i) , array[i]))
m = 0.01
n = 50
repu_para = np.array([1,1e-1,1e-3,1e-5,1e-7]) 
scores = []
stepresults = []
magnitudes = []
for lamda in repu_para:
    stepresult = []
    magnitude = []
    a=np.array([0,0,0,0,0,0])
    b=1
    for epoch in range(1,51):
        train,train_ho,label,label_ho= train_test_split(train_data,label_data,test_size=50,random_state = 2)
        steplength = 1/(m*epoch+n) 
        for step in range(1,301):
            rindex = random.randint(0,len(train_data)-1)
            hinge_loss = label_data[rindex]* (np.dot(a.T,train_data[rindex])+b) 
            if hinge_loss >= 1:
                a = a - steplength*lamda*a
            else:
                a = a - steplength*(lamda*a -label_data[rindex]*train_data[rindex])
                b = b - steplength*(-label_data[rindex])                
            if step % 30 == 0:
                #evaluate and plot accuracy 
                correct = 0
                for i in range(len(train_ho)):
                    temp = np.dot(train_ho[i],a.T)+b
                    if (temp>0 and label_ho[i] == 1) or (temp<0 and label_ho[i] ==-1):
                        correct += 1
                accuracy = correct/len(train_ho)
                stepresult.append(accuracy)
                magnitude.append(LA.norm(a))
    correct = 0
    for i in range(len(val_data)):
        temp = np.dot(val_data[i],a.T)+b
        if (temp>0 and val_label[i] == 1) or (temp<0 and val_label[i] ==-1):
            correct += 1
        accuracy = correct/len(val_data)
    scores.append([lamda,accuracy])
    stepresults.append(stepresult)
    magnitudes.append(magnitude)

    test_label = []
    for i in range(len(test_data)):
        hinge_loss = np.dot(a.T,test_data[i])+b
        if hinge_loss >= 0:
            test_label.append('>50K')
        else:
            test_label.append('<=50K')
    name = "%s.data " % lamda
    array_to_csv(name,test_label)
    
plt.figure(1)
plt.xlabel("Steps")
plt.ylabel("Accuracy")
for i in range(len(repu_para)):
    plt.plot(stepresults[i],label = "%s"%str(repu_para[i]))
plt.legend()

plt.figure(2)
plt.xlabel("Steps")
plt.ylabel("Magnitude of the coefficient vector")
for i in range(len(repu_para)):
    plt.plot(magnitudes[i],label = "%s"%str(repu_para[i]))
plt.legend()
plt.show()
print(scores)

