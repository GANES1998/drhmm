#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:23:07 2018

@author: ganeson
"""

import numpy as np
import cv2
import os

dirs = os.listdir('dataset_B_Eye_Images')

closed_left = []
closed_right = []
open_left = []
open_right = []

arrs = [closed_left,closed_right,open_left,open_right]

k = 0

for each_dir in dirs:
    
    ffolder = 'dataset_B_Eye_Images/'+each_dir
    for each_file in os.listdir(ffolder):
        fname = ffolder+'/'+each_file
        if not fname.split('.')[-1] == 'jpg':
            continue
        img = cv2.imread(fname)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        arrs[k].append(img.reshape(24*24,))
    k+=1

closed_left = np.array(closed_left)
closed_right = np.array(closed_right)
open_left = np.array(open_left)
open_right = np.array(open_right)


from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

def getCm(closed_left,open_left):
    lefts = np.zeros((closed_left.shape[0]+open_left.shape[0],closed_left.shape[1]+1))
    
    lefts[0:closed_left.shape[0],0:closed_left.shape[1]] = closed_left
            
    lefts[0:closed_left.shape[0],-1] = 0
    
    lefts[closed_left.shape[0]:,:closed_left.shape[1]] = open_left 
    
    lefts[closed_left.shape[0]:,-1] = 1
    
    np.random.shuffle(lefts)
    
    from sklearn.model_selection import train_test_split
    
    left_x_train,left_x_test,left_y_train,left_y_test = train_test_split(lefts[:,:-1],lefts[:,-1],test_size=0.2)
    
    lr.fit(left_x_train,left_y_train)
    
    pred = lr.predict(left_x_test)
    
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(pred,left_y_test)
    
    print(cm)
    
    print((cm[0,0]+cm[1,1]) /(sum(sum(cm))))
    
closed = np.concatenate((closed_left,closed_right))

open = np.concatenate((open_left,open_right))

getCm(closed,open)

    
    




