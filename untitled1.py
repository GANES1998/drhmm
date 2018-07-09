#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:15:00 2018

@author: ganeson
"""

import numpy as np

file_name = open('test1.html')

text = file_name.readlines()

text = ''.join(text)

first_split_key = '<div style="margin-top:500px;"></div>'

text_last = text.split(first_split_key)[1]

text = text.split(first_split_key)[0]

second_split_key = '<!--##################START HERE####################-->'

first_addable = len(text.split(second_split_key))[0]

text = text.split(second_split_key)[1]

new_text = text.replace('class="*"','class=""')

new_file = open('new_text.html','w')

new_file.writelines(first_addable)

new_file.writelines(second_split_key)

new_file.writelines(text)

new_file.writelines(first_split_key)

new_file.writelines(text_last)

new_file.close()


print(first_addable)

print(text)

print(first_addable)





