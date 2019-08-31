# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:06:33 2019

@author: rajpu
"""

import pandas as pd


df = pd.read_csv('Dataset1.csv')
Outlook = dict()
Temp = dict()
Humidity = dict()
Windy = dict()

yes = len(df.loc[df['PlayTennis'] == 'yes'])
no = len(df.loc[df['PlayTennis'] == 'no'])

def find_prob(column, value):
    final = dict()
    final[value] = list()
    final[value].append(len(df.loc[(df[column] == value) & (df['PlayTennis'] == 'yes')])/yes)
    final[value].append(len(df.loc[(df[column] == value) & (df['PlayTennis'] == 'no')])/no)
    return final

Outlook.update(find_prob('Outlook', 'sunny'))
Outlook.update(find_prob('Outlook', 'overcast'))
Outlook.update(find_prob('Outlook', 'rainy'))

Temp.update(find_prob('Temp', 'hot'))
Temp.update(find_prob('Temp', 'mild'))
Temp.update(find_prob('Temp', 'cool'))

Humidity.update(find_prob('Humidity', 'high'))
Humidity.update(find_prob('Humidity', 'normal'))

Windy.update(find_prob('Wind', 'weak'))
Windy.update(find_prob('Wind', 'strong'))

data = ['sunny', 'mild', 'normal', 'strong']

answer = dict()

total = yes + no
answer['yes'] = (Outlook[data[0]][0] * Temp[data[1]][0] * Humidity[data[2]][0] * Windy[data[3]][0])*(yes/total)
answer['no'] = (Outlook[data[0]][1] * Temp[data[1]][1] * Humidity[data[2]][1] * Windy[data[3]][1])*(no/total)

answer['yes'] = answer['yes']/(answer['yes']+ answer['no'])
answer['no'] = 1 - answer['yes']

print("Play Tennis:")
if answer['yes']>answer['no']:
    print("YES :)")
else:
    print("NO ;(")