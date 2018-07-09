#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:16:47 2018

@author: ganeson
"""

import pandas as pd
import numpy as np

dict_diseases= {}
dict_symptoms= {}

diseases_list = ["amoebiasis","typhoid","dengue","malaria","cholera","diseases"]
symptoms_list = ["fever","cold","headache","stomach","rash","vomiting","dysentry"]

for (ind,val) in enumerate(diseases_list):
    dict_diseases[val] = ind
    

for (ind,val) in enumerate(symptoms_list):
    dict_symptoms[val] = ind

list_of_symps = {'fever-fever':37
,'fever-cold':11
,'fever-headache':6
,'fever-stomach':1
,'fever-rash':3
,'fever-vomiting':9
,'fever-dysentry':23
,'cold-fever':7
,'cold-cold':45
,'cold-headache':4
,'cold-stomach':9
,'cold-rash':2
,'cold-vomiting':11
,'headache-fever':6
,'headache-cold':3
,'headache-headache':22
,'headache-stomach':6
,'headache-rash':9
,'stomach-fever':1
,'stomach-cold':5
,'stomach-headache':4
,'stomach-stomach':40
,'stomach-vomiting':2
,'rash-fever':5
,'rash-cold':12
,'rash-headache':16
,'vomiting-fever':11
,'vomiting-cold':64
,'dysentry-fever':7}

transition_mat = np.zeros(shape=(len(symptoms_list),len(symptoms_list)))


for (i,k) in list_of_symps.items():
    lis = i.split('-')
    symp1 = lis[0]
    symp2 = lis[1]
    transition_mat[dict_symptoms[symp1]][dict_symptoms[symp2]] = transition_mat[dict_symptoms[symp2]][dict_symptoms[symp1]] = k
    

list_of_diseases = {'fever-amoebiasis':11
,'fever-typhoid':39
,'fever-dengue':63
,'fever-malaria':14
,'fever-cholera':16
,'fever-diseases':29
,'cold-amoebiasis':14
,'cold-typhoid':21
,'cold-dengue':11
,'cold-malaria':3
,'cold-cholera':0
,'cold-diseases':5
,'headache-amoebiasis':1
,'headache-typhoid':4
,'headache-dengue':7
,'headache-malaria':1
,'headache-cholera':1
,'headache-diseases':4
,'stomach-amoebiasis':11
,'stomach-typhoid':2
,'stomach-dengue':1
,'stomach-malaria':6
,'stomach-cholera':8
,'stomach-diseases':1
,'rash-amoebiasis':0
,'rash-typhoid':1
,'rash-dengue':1
,'rash-malaria':0
,'rash-cholera':0
,'rash-diseases':0
,'vomiting-amoebiasis':8
,'vomiting-typhoid':3
,'vomiting-dengue':4
,'vomiting-malaria':2
,'vomiting-cholera':7
,'vomiting-diseases':2
,'dysentry-amoebiasis':6
,'dysentry-typhoid':1
,'dysentry-dengue':0
,'dysentry-malaria':0
,'dysentry-cholera':4
,'dysentry-diseases':2}
emmision_prob = np.zeros(shape=(len(symptoms_list),len(diseases_list)))

for (i,k) in list_of_diseases.items():
    lis =i.split('-')
    symp = lis[0]
    dis = lis[1]
    emmision_prob[dict_symptoms[symp]][dict_diseases[dis]] = k 
    
emi = emmision_prob/666
trans = transition_mat/666
    
output_trans_mat_path = "./output2map/op_tras.csv"

output_emmi_mat_path = "./output2map/op_emmi.csv"

import pandas as pd

pd.DataFrame(trans).to_csv(path_or_buf = output_trans_mat_path,header = symptoms_list,index=False)


pd.DataFrame(emi).to_csv(path_or_buf = output_emmi_mat_path,header = diseases_list,index=False)




    