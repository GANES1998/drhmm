#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:56:14 2018

@author: ganeson
"""

inp = open('outed2.txt')
line = inp.readline()
while line:
    print("'"+line.split(':')[0]+"':"+line.split(':')[1],end=',')
    line = inp.readline()