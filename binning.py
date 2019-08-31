# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:13:42 2019

@author: rajpu
"""

def Equi_width(lower_bound, width, quantity):    
    bins = []
    for low in range(lower_bound, 
                     lower_bound + quantity*width + 1, width):
        bins.append((low, low+width))
    return bins

bins = Equi_width(lower_bound=10,width=10,quantity=5)
print("Equal Width Bins:")
print(*bins,sep="\n")
def Equi_depth(l):
    return int((max(l)-min(l))/2+0.5)
l = [4,8,9,15,21,21,24,25,26,28,29,34]
width = Equi_depth(l)
print("Equi_depth Bins:")
for i in range(0,len(l),3):
    print(l[i:i+3])