#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:56:21 2018

@author: ganeson
"""

import numpy as np


from hmm import Model

states = diseases_list
symbols = symptoms_list
start_prob = {}
for i in states:
    start_prob[i] = 0.5 

trans_prob = {}
for i in range(len(trans)):
    for j in range(len(trans)):
        if symbols[i] not in trans_prob.keys():
            trans_prob[symbols[i]]={}
        trans_prob[symbols[i]][symbols[j]] = trans[i][j]
trans_prob
emit_prob = {}
for i in range(len(trans)):
    for j in range(len(emi[0])):
        if symbols[i] not in emit_prob.keys():
            emit_prob[symbols[i]]={}
        emit_prob[symbols[i]][states[j]] = emi[i][j]
emit_prob
sequence = ['vomiting','dysentry','stomach']
model = Model(states, symbols, start_prob, trans_prob, emit_prob)

print(model.evaluate(sequence))
print(model.decode(sequence))







