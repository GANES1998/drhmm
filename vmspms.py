#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:40:17 2018

@author: ganeson
"""

import numpy as np

final_mat = []

index_rows = []

col_names = ['problem_no','no_pm_div_no_vm','vm_type_cnt','res_1per_vm_lt25','res_1per_vm_lt50','res_1per_vm_lt75','res_2per_vm_lt25','res_2per_vm_lt50','res_2per_vm_lt75','res_3per_vm_lt25','res_3per_vm_lt50','res_3per_vm_lt75','res_4per_vm_lt25','res_4per_vm_lt50','res_4per_vm_lt75','rr21','rr31','rr41','rr32','rr42','rr43','rr21inc_no','rr31inc_no','rr41inc_no','rr32inc_no','rr42inc_no','rr43inc_no']
        

def op_op_each_row(iii,pms,vms_np):

    totol_no_vms = sum(vms_np[:,-1])
         
    op_each_row = []
        
    op_each_row.extend([iii,sum(vms_np[:,-1])/totol_no_vms,nos])
        
    for i in range(4):
        no_vm_lt_25 = sum(vms_np[vms_np[:,i]<=(0.25*pms[i]),-1])
            
        per_vm_lt_25 = no_vm_lt_25 / sum(vms_np[:,-1])
            
        no_vm_lt_50 = sum(vms_np[vms_np[:,i]<=(0.50*pms[i]),-1])
            
        per_vm_lt_50 = no_vm_lt_50 / sum(vms_np[:,-1])
            
        no_vm_lt_75 = sum(vms_np[vms_np[:,i]<=(0.75*pms[0]),-1])
            
        per_vm_lt_75 = no_vm_lt_75 / sum(vms_np[:,-1])
            
        op_each_row.extend([per_vm_lt_25,per_vm_lt_50,per_vm_lt_75])
        
    rr21 = vms_np[:,1]/vms_np[:,0]
        
    rr31 = vms_np[:,2]/vms_np[:,0]
        
    rr41 = vms_np[:,3]/vms_np[:,0]
        
    rr32 = vms_np[:,2]/vms_np[:,1]
        
    rr42 = vms_np[:,3]/vms_np[:,1]
        
    rr43 = vms_np[:,3]/vms_np[:,2]
        
    op_each_row.extend([rr21.std(),rr31.std(),rr41.std(),rr41.std(),rr42.std(),rr43.std()])
       
    rr_final_21 = []
    for each_ratio,no_occur in zip(rr21,vms_np[:,-1]):
        rr_final_21.extend([each_ratio]*no_occur)
            
    rr_final_21 = np.array(rr_final_21)
        
        
    rr_final_32 = []
    for each_ratio,no_occur in zip(rr32,vms_np[:,-1]):
        rr_final_32.extend([each_ratio]*no_occur)
            
    rr_final_32 = np.array(rr_final_32)
        
        
    rr_final_31 = []
    for each_ratio,no_occur in zip(rr31,vms_np[:,-1]):
        rr_final_31.extend([each_ratio]*no_occur)
            
    rr_final_31 = np.array(rr_final_31)
        
        
    rr_final_41 = []
    for each_ratio,no_occur in zip(rr41,vms_np[:,-1]):
        rr_final_41.extend([each_ratio]*no_occur)
            
    rr_final_41 = np.array(rr_final_41)
        
        
    rr_final_42 = []
    for each_ratio,no_occur in zip(rr42,vms_np[:,-1]):
        rr_final_42.extend([each_ratio]*no_occur)
            
    rr_final_42 = np.array(rr_final_42)
        
        
    rr_final_43 = []
    for each_ratio,no_occur in zip(rr43,vms_np[:,-1]):
        rr_final_43.extend([each_ratio]*no_occur)
            
    rr_final_43 = np.array(rr_final_43)
        
    op_each_row.extend([rr_final_21.std(),rr_final_31.std(),rr_final_41.std(),rr_final_32.std(),rr_final_42.std(),rr_final_43.std()])    
    
    
    return op_each_row

for iii in range(2000):
    if True :
        directory = "New folder1/inputhomo_"+str(iii)+".txt"
        
        index_rows.append('input_homo'+str(iii))
        
        file = open(directory)
        
        if(iii>=250):
            file.readline()
        
        pms = list(map(int,file.readline().split()))
        
        pms = pms[:-2]
        
        nos = int(file.readline())
        
        vms = []
        
        for i in range(nos):
            
            vms.append(list(map(int,file.readline().split())))
            
        vms_np = np.array(vms)
        
#        totol_no_vms = sum(vms_np[:,-1])
#        
#        
#        op_each_row = []
#        
#        op_each_row.extend([iii,sum(vms_np[:,-1])/totol_no_vms,nos])
#        
#        for i in range(4):
#            no_vm_lt_25 = sum(vms_np[vms_np[:,i]<=(0.25*pms[i]),-1])
#            
#            per_vm_lt_25 = no_vm_lt_25 / sum(vms_np[:,-1])
#            
#            no_vm_lt_50 = sum(vms_np[vms_np[:,i]<=(0.50*pms[i]),-1])
#            
#            per_vm_lt_50 = no_vm_lt_50 / sum(vms_np[:,-1])
#            
#            no_vm_lt_75 = sum(vms_np[vms_np[:,i]<=(0.75*pms[0]),-1])
#            
#            per_vm_lt_75 = no_vm_lt_75 / sum(vms_np[:,-1])
#            
#            op_each_row.extend([per_vm_lt_25,per_vm_lt_50,per_vm_lt_75])
#        
#        rr21 = vms_np[:,1]/vms_np[:,0]
#        
#        rr31 = vms_np[:,2]/vms_np[:,0]
#        
#        rr41 = vms_np[:,3]/vms_np[:,0]
#        
#        rr32 = vms_np[:,2]/vms_np[:,1]
#        
#        rr42 = vms_np[:,3]/vms_np[:,1]
#        
#        rr43 = vms_np[:,3]/vms_np[:,2]
#        
#        op_each_row.extend([rr21.std(),rr31.std(),rr41.std(),rr41.std(),rr42.std(),rr43.std()])
#       
#        rr_final_21 = []
#        for each_ratio,no_occur in zip(rr21,vms_np[:,-1]):
#            rr_final_21.extend([each_ratio]*no_occur)
#            
#        rr_final_21 = np.array(rr_final_21)
#        
#        
#        rr_final_32 = []
#        for each_ratio,no_occur in zip(rr32,vms_np[:,-1]):
#            rr_final_32.extend([each_ratio]*no_occur)
#            
#        rr_final_32 = np.array(rr_final_32)
#        
#        
#        rr_final_31 = []
#        for each_ratio,no_occur in zip(rr31,vms_np[:,-1]):
#            rr_final_31.extend([each_ratio]*no_occur)
#            
#        rr_final_31 = np.array(rr_final_31)
#        
#        
#        rr_final_41 = []
#        for each_ratio,no_occur in zip(rr41,vms_np[:,-1]):
#            rr_final_41.extend([each_ratio]*no_occur)
#            
#        rr_final_41 = np.array(rr_final_41)
#        
#        
#        rr_final_42 = []
#        for each_ratio,no_occur in zip(rr42,vms_np[:,-1]):
#            rr_final_42.extend([each_ratio]*no_occur)
#            
#        rr_final_42 = np.array(rr_final_42)
#        
#        
#        rr_final_43 = []
#        for each_ratio,no_occur in zip(rr43,vms_np[:,-1]):
#            rr_final_43.extend([each_ratio]*no_occur)
#            
#        rr_final_43 = np.array(rr_final_43)
#        
#        op_each_row.extend([rr_final_21.std(),rr_final_31.std(),rr_final_41.std(),rr_final_32.std(),rr_final_42.std(),rr_final_43.std()])    
#        
        final_mat.append(op_op_each_row(iii,pms,vms_np))
        
np_data = np.array(final_mat)

import pandas as pd

pd_df = pd.DataFrame(data = np_data,index=index_rows,columns=col_names)

new_df_to_sk_sir = pd_df.iloc[:15,:]

new_df_to_sk_sir.to_csv('df_head_15.csv')

y_vals = pd.read_excel('hyper.xlsx')

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=400)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

pd_tf_np = pd_df.iloc[:,:].values

from sklearn.cross_validation import train_test_split

i=0

from imblearn.over_sampling.smote import SMOTE

sm = SMOTE()

pd_tf_np = ss.fit_transform(pd_tf_np)

out = np.ones(shape=(250,9))

rfc = []
for i in range(9):
    rfc.append(RandomForestClassifier(n_estimators=400))

res = []



for i in range(9):

    #x_train,x_test,y_train,y_test = train_test_split(pd_tf_np,y_vals.iloc[:,i].values)
    
    x_train ,x_test = pd_tf_np[250:,:],pd_tf_np[:250,:]
    
    y_train,y_test = y_vals.iloc[:,i].values[250:],y_vals.iloc[:,i].values[:250]
    
    #ss = StandardScaler()
    
    #x_train = ss.fit_transform(x_train)
    
    print(x_train.shape,y_train.shape)
    
    x_train , y_train = sm.fit_sample(x_train,y_train)
    
    rfc[i].fit(X = x_train,y = y_train)
    
    from sklearn.metrics import confusion_matrix
    
   # x_test = ss.transform(x_test)
    
    pred_ed = rfc[i].predict(x_test)
    
    out[:,i] = pred_ed
    
    cm = confusion_matrix(y_test,pred_ed)
    
    print(y_vals.columns[i])
    
    print(cm)
    
    accur = (cm[0,0]+cm[1,1])/sum(sum(cm))
    
    res.append(accur)
    
    print(accur)
    
res

print(np.array(res).mean())

def predictor_given_list(rfc,params_list):
    out_res = np.ones(shape=(1,9))
    for i in range(9):
        out_res[0,i] = rfc[i].predict([params_list])
        
    out_res = out_res.astype(np.int)
    return out_res[0].tolist()


out = out.astype(np.int)

res_to_sriram = pd.DataFrame(out,columns=y_vals.columns)

res_to_sriram.head()

res_to_sriram.to_csv('final_output_250.csv')


##Out is the final dataset output



