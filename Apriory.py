# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:44:02 2019

@author: rajpu
"""
import pandas as pd
from itertools import permutations

def find_frequency_of_item(item,final_set):
        counter1 = 0
        for j in final_set:
            if set(list(item)).issubset(set(list(j))):
                counter1 += 1
        return counter1


def find_frequency(all_items,final_set):
    C = {}
    for i in all_items:
        counter = find_frequency_of_item(i,final_set)
        C.update({i:counter})
    return C


def valid_item_set(C,min_Support_numeric):
    new_C = {}
    for i in C.keys():
        if C[i] >= min_Support_numeric:
            new_C.update({i:C[i]})
    del C
    C = new_C
    del new_C
    return C


def join_sets(C):
    temp = list(C.keys())
    l = []
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            l.append("".join(sorted(list(set(list(temp[i]+temp[j]))))))
    return list(set(l))


def A_priory(dataset,min_Support,min_Confidence):
    items = dataset.iloc[:, 1].values
    final_set = []
    all_items = []
    for i in items:
        k = (i.split())
        final_set.append("".join(k))
        all_items += k
    all_items = sorted(list(set(all_items)))
    min_Support_numeric = min_Support*len(final_set)
    while True:
        C = find_frequency(all_items,final_set)
        C = valid_item_set(C,min_Support_numeric)
        if len(list(C.keys())) == 0:
            break
        temp_C = C
        all_items = join_sets(C)
    all_possible_itemset = []
    for i in temp_C.keys():
        permList = list(permutations(i))
        for j in permList:
            all_possible_itemset.append("".join(j))
    Rules = []
    for i in all_possible_itemset:
        total_support = find_frequency_of_item(i,final_set)
        for j in range(1,len(i)):
            temp =find_frequency_of_item(i[:j],final_set)
            Rules.append([i[:j],i[j:],total_support/temp])
    Final = []
    for i in Rules:
        if i[2] >= min_Confidence:
            left = ",".join(list(i[0]))
            rigtht = ",".join(list(i[1]))
            temp = "{"+left+"} => {"+rigtht+"} :Confidence="+("%.2f"%(i[2]*100.00))+"%"
            Final.append(temp)
    return Final


dataset = pd.read_csv('Apriory.csv')
min_Confidence = 0.50
min_Support = 2/9
Final_answer = A_priory(dataset,min_Support,min_Confidence)
print("Assosiation Rules Are:")
print(*Final_answer,sep="\n")