import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read the dataset from csv fiel using pandas library
dataset = pd.read_csv('Dataset1.csv')
X1 = dataset.iloc[:, 1].values
X2 = dataset.iloc[:, 2].values
X3 = dataset.iloc[:, 3].values
X4 = dataset.iloc[:, 4].values
X5 = dataset.iloc[:, 5].values 
labelencoder_X = LabelEncoder()
Y2 = labelencoder_X.fit_transform(X2)
Y3 = labelencoder_X.fit_transform(X3)
Y4 = labelencoder_X.fit_transform(X4)
Y5 = labelencoder_X.fit_transform(X5)
l1 = []
labels_x1 = ['sunny', 'overcast', 'rain']
for i in range(0,3):
    temp = []
    temp.append(labels_x1[i])
    k = 0
    t = 0
    for j in range(0,len(Y5)):
        if labels_x1[i] == X1[j]:
            t += 1
            k += Y5[j]
    temp += [k, t-k]
    l1.append(temp)
Outlook = l1.copy()
del(l1)
del(temp)
l1 = []
labels_x2 = ['hot', 'mild', 'cool']
for i in range(0,3):
    temp = []
    temp.append(labels_x2[i])
    k = 0
    t = 0
    for j in range(0,len(Y5)):
        if labels_x2[i] == X2[j]:
            t += 1
            k += Y5[j]
    temp += [k, t-k]
    l1.append(temp)
Tempurature = l1.copy()
del(l1)
del(temp)
l1 = []
labels_x3 = ['high', 'normal']
for i in range(0,2):
    temp = []
    temp.append(labels_x3[i])
    k = 0
    t = 0
    for j in range(0,len(Y5)):
        if labels_x3[i] == X3[j]:
            t += 1
            k += Y5[j]
    temp += [k, t-k]
    l1.append(temp)
Humidity = l1.copy()
del(l1)
del(temp)
l1 = []
labels_x4 = ['weak', 'strong']
for i in range(0,2):
    temp = []
    temp.append(labels_x4[i])
    k = 0
    t = 0
    for j in range(0,len(Y5)):
        if labels_x4[i] == X4[j]:
            t += 1
            k += Y5[j]
    temp += [k, t-k]
    l1.append(temp)
Wind = l1.copy()
del(l1)
del(temp)
del(k)
del(j)
del(t)
del(i)
