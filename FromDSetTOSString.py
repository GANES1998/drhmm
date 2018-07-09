#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:14:56 2018

@author: ganeson
"""

import pandas as pd
dset = pd.read_csv('result_latest_disease.csv')


out = dset['text'].tolist()


new_out = []
for each_str in out:
    new_out.append(str(each_str).replace('\n','.'))


file_op = open('String_tweets.txt','w')

file_op.write('\!@123456789@!'.join(new_out))

file_op.close() 











