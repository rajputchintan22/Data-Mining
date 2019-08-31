# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:01:26 2019

@author: rajpu
"""

import numpy as np
import pandas as pd
df = pd.read_csv('KNN.csv')
X = df.drop('Result',axis=1).values
y = df['Result'].values
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X, y)
age = float(input("Enter Age:"))
location = float(input("Enter Location:")) 
data = np.asarray([[age, location]], dtype=np.float32)
Ans_predict = list(knn.predict(data))
print("Predicted Results are:")
print(*Ans_predict)