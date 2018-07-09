#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:20:16 2018

@author: ganeson
"""

import keras

from keras.models import Sequential

from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units=16,input_shape=(27,),activation='relu'))

classifier.add(Dense(units=8,activation='relu'))

classifier.add(Dense(units=1,activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

