#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:15:28 2018

@author: ganeson
"""




import sys
import numpy as np
import math

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
    for each_ratio,no_occur in zip(rr21,vms_np[:,-1].astype(np.int)):
        rr_final_21.extend([each_ratio]*no_occur)
            
    rr_final_21 = np.array(rr_final_21)
        
        
    rr_final_32 = []
    for each_ratio,no_occur in zip(rr32,vms_np[:,-1].astype(np.int)):
        rr_final_32.extend([each_ratio]*no_occur)
            
    rr_final_32 = np.array(rr_final_32)
        
        
    rr_final_31 = []
    for each_ratio,no_occur in zip(rr31,vms_np[:,-1].astype(np.int)):
        rr_final_31.extend([each_ratio]*no_occur)
            
    rr_final_31 = np.array(rr_final_31)
        
        
    rr_final_41 = []
    for each_ratio,no_occur in zip(rr41,vms_np[:,-1].astype(np.int)):
        rr_final_41.extend([each_ratio]*no_occur)
            
    rr_final_41 = np.array(rr_final_41)
        
        
    rr_final_42 = []
    for each_ratio,no_occur in zip(rr42,vms_np[:,-1].astype(np.int)):
        rr_final_42.extend([each_ratio]*no_occur)
            
    rr_final_42 = np.array(rr_final_42)
        
        
    rr_final_43 = []
    for each_ratio,no_occur in zip(rr43,vms_np[:,-1].astype(np.int)):
        rr_final_43.extend([each_ratio]*no_occur)
            
    rr_final_43 = np.array(rr_final_43)
        
    op_each_row.extend([rr_final_21.std(),rr_final_31.std(),rr_final_41.std(),rr_final_32.std(),rr_final_42.std(),rr_final_43.std()])    
    
    
    return op_each_row

def predictor_given_list(rfc,params_list):
    out_res = np.ones(shape=(1,9))
    for i in range(9):
        out_res[0,i] = rfc[i].predict([params_list])
        
    out_res = out_res.astype(np.int)
    return out_res[0].tolist()

def expf(pm,v,f):
	alpha=[]
	cost=0
	filled=f[:]
	temp=pm[:]
	for i in range(4):
		s=0
		num=0
		for j in range(len(v)):
			s+=v[j][i]
		alpha.append(s/len(v))
	for i in range(len(v)):
		s=0
		for j in range(4):
			s+=alpha[j]*v[i][j]
		v[i].append(s)
	v.sort(reverse=True,key=lambda x:x[-1])
	#print(v,l)
	i=0
	while i<len(v):
		if v[i][4]==False and fit(v[i],pm):
			num+=1 
			v[i][4]=True
			pm[0]-=v[i][0]
			pm[1]-=v[i][1]
			pm[2]-=v[i][2]
			pm[3]-=v[i][3]
			cost+=pm[4]*v[i][0]
		i+=1
	for i in range(m):
		v[i].pop(-1)
	return sum(pm)/sum(temp),vm,cost,filled,num
def prodf(pm,v,f):
	filled=f[:]
	vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
	phy=pm[:]
	temp=pm[:]
	for i in range(len(vm)):
		vm[i].append(prodr(vm,i))
	vm.sort(reverse=True,key=lambda x:x[5])
	num=0
	cur=0
	cost=0
	m=len(vm)
	for i in range(m):
		if vm[i][4]==False and fit(vm[i],phy):
			num+=1 
			for k in range(4):
                        			phy[k]-=vm[i][k]
			vm[i][4]=True
	for i in range(m):
		vm[i].pop(-1)
	#print('PROD '+str(phy)+' '+str(temp))
	return sum(phy)/sum(temp),vm,cost,filled,num
def euclidian(pm,vm):
	adiff=abs(pm[0]-vm[0])
	bdiff=abs(pm[1]-vm[1])
	cdiff=abs(pm[2]-vm[2])
	ddiff=abs(pm[3]-vm[3])
	return math.sqrt(adiff**2+bdiff**2+cdiff**2+ddiff**2)
def arank(v,i):
	a=sorted(v,key=lambda x:x[0])
	b=sorted(v,key=lambda x:x[1])
	c=sorted(v,key=lambda x:x[2])
	d=sorted(v,key=lambda x:x[3])
	return a.index(v[i])+b.index(v[i])+c.index(v[i])+d.index(v[i])
def sumr(v,i):
	return v[i][0]+v[i][1]+v[i][2]+v[i][3]
def prodr(v,i):
	return v[i][0]*v[i][1]*v[i][2]*v[i][3]
def euclidianf(pm,vm,f):
	v=[[vm[i][j] for j in range(5)] for i in range(len(vm))]
	l=pm[:]
	temp=pm[:]
	filled=f[:]
	vin=-1
	num=0
	cost=0
	dist=0
	while(dist!=999999999999):
		dist=999999999999
		for i in range(len(vm)):
			if v[i][4]==False and fit(v[i],l):
				if dist>euclidian(l,v[i]):
					dist=euclidian(l,v[i])
					vin=i
		if dist!=999999999999:
			i=vin	
			num+=1 
			v[i][4]=True
			l[0]-=v[i][0]
			l[1]-=v[i][1]
			l[2]-=v[i][2]
			l[3]-=v[i][3]
			cost+=l[4]*v[i][0]
			break
	return sum(l)/sum(temp),v,cost,filled,num
def arankf(pm,v,f):
	filled=f[:]
	vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
	phy=pm[:]
	temp=pm[:]
	for i in range(len(vm)):
		vm[i].append(arank(vm,i))
	vm.sort(reverse=True,key=lambda x:x[5])
	num=0
	cur=0
	cost=0
	m=len(vm)
	for i in range(m):
		if vm[i][4]==False and fit(vm[i],phy):
			num+=1 
			for k in range(4):
                        			phy[k]-=vm[i][k]
			vm[i][4]=True
	for i in range(m):
		vm[i].pop(-1)
	#print('ARANK '+str(phy)+' '+str(temp))
	return sum(phy)/sum(temp),vm,cost,filled,num
def sumf(pm,v,f):
	filled=f[:]
	vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
	phy=pm[:]
	temp=pm[:]
	for i in range(len(vm)):
		vm[i].append(sumr(vm,i))
	vm.sort(reverse=True,key=lambda x:x[5])
	num=0
	cur=0
	cost=0
	m=len(vm)
	for i in range(m):
		if vm[i][4]==False and fit(vm[i],phy):
			num+=1 
			for k in range(4):
                        			phy[k]-=vm[i][k]
			vm[i][4]=True
	for i in range(m):
		vm[i].pop(-1)
	#print('SUM '+str(phy)+' '+str(temp))
	return sum(phy)/sum(temp),vm,cost,filled,num
def prodf(pm,v,f):
	filled=f[:]
	vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
	phy=pm[:]
	temp=pm[:]
	for i in range(len(vm)):
		vm[i].append(prodr(vm,i))
	vm.sort(reverse=True,key=lambda x:x[5])
	num=0
	cur=0
	cost=0
	m=len(vm)
	for i in range(m):
		if vm[i][4]==False and fit(vm[i],phy):
			num+=1 
			for k in range(4):
                        			phy[k]-=vm[i][k]
			vm[i][4]=True
	for i in range(m):
		vm[i].pop(-1)
	#print('PROD '+str(phy)+' '+str(temp))
	return sum(phy)/sum(temp),vm,cost,filled,num
def fit(vm,pm):
    for i in range(4):
        if vm[i]>pm[i]:
            return False
    return True
def vmnear(pm,v,f):
    temp=pm[:]
    vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
    filled=[f[i] for i in range(len(f))]
    num=0
    cost=0
    processed=[]
    while len(processed)< len(vm) and pm[0]>0:
            rr1=pm[3]/pm[0]
            rr2=pm[2]/pm[0]
            rr3=pm[1]/pm[0]
            curdiff1=curdiff2=curdiff3=999999999999
            vmlist=[]
            flag=0
            for i in range(len(vm)):
                if i in processed:
                    continue
                try:
                    if vm[i][4]==True:
                        processed.append(i)
                        continue
                except:
                    print(vm[i])
                if vm[i][4]==False:
                    calcrr1=vm[i][3]/vm[i][0]
                    calcrr2=vm[i][2]/vm[i][0]
                    calcrr3=vm[i][1]/vm[i][0]
                    diffa=abs(calcrr1-rr1)
                    diffb=abs(calcrr2-rr2)
                    diffc=abs(calcrr3-rr3)
                    if diffa==curdiff1:
                        if diffb==curdiff2:
                            if diffc==curdiff3:
                                vmlist.append(i)
                            elif diffc<curdiff3:
                                vmlist=[i]
                                curdiff3=diffc
                        elif diffb<curdiff2:
                            vmlist=[i]
                            curdiff2=diffb
                            curdiff3=diffc
                    elif diffa<curdiff1:
                        vmlist=[i]
                        curdiff1=diffa
                        curdiff2=diffb
                        curdiff3=diffc
            for k in vmlist:
                #flag=1
                processed.append(k)
                if fit(vm[k],pm):
                    num+=1
                    flag=1
                    vm[k][4]=True
                    for i in range(4):
                        pm[i]-=vm[k][i]
                    cost+=vm[k][0]*pm[4]
                    break
    return sum(pm)/sum(temp),vm,cost,filled,num
def vmneard(pm,v,f):
    temp=pm[:]
    vm=[[v[i][j] for j in range(5)] for i in range(len(v))]
    filled=[f[i] for i in range(len(f))]
    num=0
    cost=0
    rr1o=pm[3]/pm[0]
    rr2o=pm[2]/pm[0]
    rr3o=pm[1]/pm[0]
    flaga=flagb=flagc=0
    processed=[]
    flag=0
    while len(processed)< len(vm) and pm[0]>0:
        rr1=pm[3]/pm[0]
        rr2=pm[2]/pm[0]
        rr3=pm[1]/pm[0]
        if rr1o>rr1:
            flaga=2
            #Current Resource Ratio is lesser
            #We need to increase the Ratio
            #So, Go for Larger VMs
        else:
            flaga=1
        if rr2o>rr2:
            flagb=2
        else:
            flagb=1
        if rr2o>rr2:
            flagc=2
        else:
            flagc=1
        if flag==1:
            flaga=1 if flaga==2 else 1
            flagb=1 if flagb==2 else 1
            flagc=1 if flagc==2 else 1
        curdiff1=curdiff2=curdiff3=999999999999
        vmlist=[]
        flag=1
        for i in range(len(vm)):
                if i in processed:
                    continue
                if vm[i][4]==True:
                    processed.append(i)
                    continue
                if vm[i][4]==False:
                    calcrr1=vm[i][3]/vm[i][0]
                    calcrr2=vm[i][2]/vm[i][0]
                    calcrr3=vm[i][1]/vm[i][0]
                    if flaga==1 and calcrr1<rr1:
                        continue
                    elif flaga==2 and calcrr1>rr1:
                        continue
                    if flagb==1 and calcrr2<rr2:
                        continue
                    elif flagb==2 and calcrr2>rr2:
                        continue
                    if flagc==1 and calcrr3<rr3:
                        continue
                    elif flagc==2 and calcrr3>rr3:
                        continue
                    diffa=abs(calcrr1-rr1)
                    diffb=abs(calcrr2-rr2)
                    diffc=abs(calcrr3-rr3)
                    if diffa==curdiff1:
                        if diffb==curdiff2:
                            if diffc==curdiff3:
                                vmlist.append(i)
                            elif diffc<curdiff3:
                                vmlist=[i]
                                curdiff3=diffc
                        elif diffb<curdiff2:
                            vmlist=[i]
                            curdiff2=diffb
                            curdiff3=diffc
                    elif diffa<curdiff1:
                        vmlist=[i]
                        curdiff1=diffa
                        curdiff2=diffb
                        curdiff3=diffc
        for k in vmlist:
                flag=0
                processed.append(k)
                if fit(vm[k],pm):
                    num+=1
                    vm[k][4]=True
                    for i in range(4):
                        pm[i]-=vm[k][i]
                    cost+=vm[k][0]*pm[4]
                    break
        if flag==1:
                for k in range(len(vm)):
                    if vm[k][4]==False and fit(vm[k],pm):
                        num+=1
                        vm[k][4]=True
                        for i in range(4):
                           pm[i]-=vm[k][i]
                        cost+=vm[k][0]*pm[4]
                break 
    return sum(pm)/sum(temp),vm,cost,filled,num

#fin_outs_to_sram = []
for i_iter in range(180,250):
    input_file=open('New folder1/inputhomo_'+str(i_iter)+'.txt','r')
    op_file=open('hyperclassifierbinbybinop.txt','a')
    pm=[]
    n=1#int(input_file.readline())
    for i in range(n):
        l=(list(map(int,input_file.readline().split())))
        for j in range(l[-1]):
            pm.append(l[:-1])
    #print(pm)
    vm=[]
    #print(sumf([10,10,10,10],[[1,1,1,1,False],[2,2,2,2,False],[5,5,7,2,False],[2,2,0,5,False]],[]))
    #print(sumf([10,10,10,10],[[1,1,1,1,False],[2,2,2,2,False],[5,5,7,2,False],[2,2,0,5,False]],[]))
    #print(sumf([10,10,10,10],[[1,1,1,1,False],[2,2,2,2,False],[5,5,7,2,False],[2,2,0,5,False]],[]))
    m=int(input_file.readline())
    for i in range(m):
        l=list(map(int,input_file.readline().split()))
        for j in range(l[-1]):
            vm.append(l[:-1])
    #print(vm)
    r1=0
    r2=1
    r3=2
    r4=3
    epc=4
    num=0
    pm.sort(key=lambda x:x[4])
    #print(pm)
    en=0
    cur=0
    n=len(pm)
    m=len(vm)
    for i in range(m):
    	vm[i].append(False)
    filled=[False for i in range(m)]
    c=0
    while num!=m:
        c+=1
        phy1=pm[cur][:]
        t=vm[:]
        t_np = np.array(t)
        t_np = t_np[:,:4]
        t_added = np.ones(shape=(len(t_np),1))
        t_np = np.concatenate((t_np,t_added),axis=1)
        vms_np = t_np
        pms = phy1
        classify_op = predictor_given_list(rfc,op_op_each_row(1,pms,vms_np))
        
    #    if c%2==0:
    #    	classify_op=[0,0,0,0,0,1,0,0,0]
    #    else:
    #    	classify_op=[0,0,0,0,0,0,0,1,0]
        if classify_op[0]==1:
            	diff1,vm1,c1,f1,n1=sumf(phy1,vm,filled)
        elif classify_op[1]==1:
            	diff1,vm1,c1,f1,n1=expf(phy1,vm,filled)
        elif classify_op[2]==1:
            	diff1,vm1,c1,f1,n1=arankf(phy1,vm,filled)
        elif classify_op[4]==1:
            	diff1,vm1,c1,f1,n1=prodf(phy1,vm,filled)
        elif classify_op[5]==1:
            	diff1,vm1,c1,f1,n1=vmnear(phy1,vm,filled)
        elif classify_op[6]==1:
            	diff1,vm1,c1,f1,n1=vmneard(phy1,vm,filled)
        elif classify_op[7]==1:
            	diff1,vm1,c1,f1,n1=euclidianf(phy1,vm,filled)
        else:
            diff1,vm1,c1,f1,n1=arankf(phy1,vm,filled)
        vm=vm1[:]
        en+=c1
        filled=f1
        num+=n1
        cur+=1
        if num==m:
            break
        if cur==n:
            break
    if num!=m:
        op_file.write('999999999999\n')
    else:
        op_file.write(str(c)+'\n')
    fin_outs_to_sram.append(cur)
    
    print('processed input no :- '+str(i_iter)+"")
    
    
    #f=open('inputhomo.txt','r')
    #pm=list(map(int,f.readline().split()))
    #n=int(f.readline())
    #vm=[]
    #for i in range(n):
    #    vm.append(list(map(int,f.readline().split())))
    #sum=[0,0,0,0]
    #for i in range(n):
    #    for j in range(4):
    #        sum[j]+=vm[i][j]*vm[i][-1]
    #print(sum)
    #for i in range(4):
    #    if num==m and sum[i]>c*pm[i]:
    #        print('no')
    #        break
    #op_file.close()
    #s.close()
print(fin_outs_to_sram)