# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:55:36 2022

@author: DELL
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

## read csv file
r1s13 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R1 s1 113.csv',engine='python',encoding='UTF-8-sig')
r1s13 = r1s13.set_index('Accession',drop=False)

r1s17 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R1 s1 117.csv',engine='python',encoding='UTF-8-sig')
r1s17 = r1s17.set_index('Accession',drop=False)

r1s23 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R1 s2 113.csv',engine='python',encoding='UTF-8-sig')
r1s23 = r1s23.set_index('Accession',drop=False)

r1s27 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R1 s2 117.csv',engine='python',encoding='UTF-8-sig')
r1s27 = r1s27.set_index('Accession',drop=False)

r2s13 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R2 s1 113.csv',engine='python',encoding='UTF-8-sig')
r2s13 = r2s13.set_index('Accession',drop=False)

r2s17 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R2 s1 117.csv',engine='python',encoding='UTF-8-sig')
r2s17 = r2s17.set_index('Accession',drop=False)

r2s23 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R2 s2 113.csv',engine='python',encoding='UTF-8-sig')
r2s23 = r2s23.set_index('Accession',drop=False)

r2s27 = pd.read_csv('E:\sirebrowser\zhoulei\GDM_2ndBatch_raw\R2 s2 117.csv',engine='python',encoding='UTF-8-sig')
r2s27 = r2s27.set_index('Accession',drop=False)

r1s13 = r1s13[~r1s13.index.duplicated()]
r1s17 = r1s17[~r1s17.index.duplicated()]
r1s23 = r1s23[~r1s23.index.duplicated()]
r1s27 = r1s27[~r1s27.index.duplicated()]
r2s13 = r2s13[~r2s13.index.duplicated()]
r2s17 = r2s17[~r2s17.index.duplicated()]
r2s23 = r2s23[~r2s23.index.duplicated()]
r2s27 = r2s27[~r2s27.index.duplicated()]

## select useful info
r1s13 = r1s13.iloc[:,[6,7,12,17,22,27,32,37,42]]
r1s17 = r1s17.iloc[:,[6,7,12,17,22,27,32,37,42]]
r1s23 = r1s23.iloc[:,[6,7,12,17,22,27,32,37,42]]
r1s27 = r1s27.iloc[:,[6,7,12,17,22,27,32,37,42]]

r2s13 = r2s13.iloc[:,[6,7,12,17,22,27,32,37,42]]
r2s17 = r2s17.iloc[:,[6,7,12,17,22,27,32,37,42]]
r2s23 = r2s23.iloc[:,[6,7,12,17,22,27,32,37,42]]
r2s27 = r2s27.iloc[:,[4,5,8,9,10]]

# Accession name combination
r1s13.insert(0,'ID',-1)
r1s13['ID'] = r1s13.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r1s17.insert(0,'ID',-1)
r1s17['ID'] = r1s17.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r1s23.insert(0,'ID',-1)
r1s23['ID'] = r1s23.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r1s27.insert(0,'ID',-1)
r1s27['ID'] = r1s27.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r2s13.insert(0,'ID',-1)
r2s13['ID'] = r2s13.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r2s17.insert(0,'ID',-1)
r2s17['ID'] = r2s17.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r2s23.insert(0,'ID',-1)
r2s23['ID'] = r2s23.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)
r2s27.insert(0,'ID',-1)
r2s27['ID'] = r2s27.apply(lambda x: x['Accession'] + '~' + x['Name'],axis=1)

r1s13 = r1s13.set_index('ID',drop=True)
r1s13 = r1s13.drop(['Accession','Name'],axis=1)
r1s17 = r1s17.set_index('ID',drop=True)
r1s17 = r1s17.drop(['Accession','Name'],axis=1)
r1s23 = r1s23.set_index('ID',drop=True)
r1s23 = r1s23.drop(['Accession','Name'],axis=1)
r1s27 = r1s27.set_index('ID',drop=True)
r1s27 = r1s27.drop(['Accession','Name'],axis=1)
r2s13 = r2s13.set_index('ID',drop=True)
r2s13 = r2s13.drop(['Accession','Name'],axis=1)
r2s17 = r2s17.set_index('ID',drop=True)
r2s17 = r2s17.drop(['Accession','Name'],axis=1)
r2s23 = r2s23.set_index('ID',drop=True)
r2s23 = r2s23.drop(['Accession','Name'],axis=1)
r2s27 = r2s27.set_index('ID',drop=True)
r2s27 = r2s27.drop(['Accession','Name'],axis=1)

# set1
# 3
s13 = pd.concat([r1s13['114:113'],r2s13['114:113'],r1s13['118:113'],r2s13['118:113'],
                  r1s13['115:113'],r2s13['115:113'],r1s13['119:113'],r2s13['119:113'],
                  r1s13['116:113'],r2s13['116:113'],r1s13['121:113'],r2s13['121:113'],],axis=1,sort=False)

# 7
s17 = pd.concat([r1s17['114:117'],r2s17['114:117'],r1s17['118:117'],r2s17['118:117'],
                  r1s17['115:117'],r2s17['115:117'],r1s17['119:117'],r2s17['119:117'],
                  r1s17['116:117'],r2s17['116:117'],r1s17['121:117'],r2s17['121:117'],],axis=1,sort=False)

# set2
# 3
s23 = pd.concat([r1s23['114:113'],r2s23['114:113'],r1s23['118:113'],r2s23['118:113'],
                  r1s23['115:113'],r2s23['115:113'],r1s23['119:113'],r2s23['119:113'],
                  r1s23['116:113'],r2s23['116:113'],r1s23['121:113'],r2s23['121:113'],],axis=1,sort=False)

# 7
s27 = pd.concat([r1s27['114:117'],r1s27['118:117'],r2s27['118:117'],
                  r1s27['115:117'],r1s27['119:117'],r2s27['119:117'],
                  r1s27['116:117'],r1s27['121:117'],r2s27['121:117'],],axis=1,sort=False)

result1 = pd.concat([s13,s17,s23,s27],axis=1,sort=False)

s13.to_csv('E:\\sirebrowser\\泪液标志物\\data\\s13.csv')
s17.to_csv('E:\\sirebrowser\\泪液标志物\\data\\s17.csv')
s23.to_csv('E:\\sirebrowser\\泪液标志物\\data\\s23.csv')
s27.to_csv('E:\\sirebrowser\\泪液标志物\\data\\s27.csv')
result1.to_csv('E:\\sirebrowser\\泪液标志物\\data\\result1.csv')

# 只取113
result2 = pd.concat([s13,s23],axis=1,sort=False)
result2.to_csv('E:\\sirebrowser\\泪液标志物\\data\\result2.csv')
# mean cv
result2.columns = ['E11','E12','E21','E22','M11','M12','M21','M22','G11','G12','G21','G22',
                   'E31','E32','E41','E42','M31','M32','M41','M42','G31','G32','G41','G42']

result2.insert(2,'E1mean',-1)
result2.insert(3,'E1cv',-1)
result2.insert(6,'E2mean',-1)
result2.insert(7,'E2cv',-1)
result2.insert(10,'M1mean',-1)
result2.insert(11,'M1cv',-1)
result2.insert(14,'M2mean',-1)
result2.insert(15,'M2cv',-1)
result2.insert(18,'G1mean',-1)
result2.insert(19,'G1cv',-1)
result2.insert(22,'G2mean',-1)
result2.insert(23,'G2cv',-1)

result2.insert(26,'E3mean',-1)
result2.insert(27,'E3cv',-1)
result2.insert(30,'E4mean',-1)
result2.insert(31,'E4cv',-1)
result2.insert(34,'M3mean',-1)
result2.insert(35,'M3cv',-1)
result2.insert(38,'M4mean',-1)
result2.insert(39,'M4cv',-1)
result2.insert(42,'G3mean',-1)
result2.insert(43,'G3cv',-1)
result2.insert(46,'G4mean',-1)
result2.insert(47,'G4cv',-1)

result2.insert(2,'E1',-1)
result2.insert(7,'E2',-1)
result2.insert(12,'M1',-1)
result2.insert(17,'M2',-1)
result2.insert(22,'G1',-1)
result2.insert(27,'G2',-1)
result2.insert(32,'E3',-1)
result2.insert(37,'E4',-1)
result2.insert(42,'M3',-1)
result2.insert(47,'M4',-1)
result2.insert(52,'G3',-1)
result2.insert(57,'G4',-1)

for i in range(0,result2.shape[0]): # i=13
    print(i)
    result2.iloc[i,2] = sum(result2.iloc[i,[0,1]].isnull())
    result2.iloc[i,7] = sum(result2.iloc[i,[5,6]].isnull())
    result2.iloc[i,12] = sum(result2.iloc[i,[10,11]].isnull())
    result2.iloc[i,17] = sum(result2.iloc[i,[15,16]].isnull())
    result2.iloc[i,22] = sum(result2.iloc[i,[20,21]].isnull())
    result2.iloc[i,27] = sum(result2.iloc[i,[25,26]].isnull())
    result2.iloc[i,32] = sum(result2.iloc[i,[30,31]].isnull())
    result2.iloc[i,37] = sum(result2.iloc[i,[35,36]].isnull())
    result2.iloc[i,42] = sum(result2.iloc[i,[40,41]].isnull())
    result2.iloc[i,47] = sum(result2.iloc[i,[45,46]].isnull())
    result2.iloc[i,52] = sum(result2.iloc[i,[50,51]].isnull())
    result2.iloc[i,57] = sum(result2.iloc[i,[55,56]].isnull())
    
#sum(result2[['E11','E12']].isnull() == True)
#
#result2 = result2.replace(0,np.nan)
#result2 = result2.replace(np.nan,99999)
#
#np.nanstd(result2[['E11','E12']],axis=1)
#[result2['E11'],result2['E11']]

result2['E1mean'] = result2[['E11','E12']].mean(axis=1)
result2['E1cv'] = (np.nanstd(result2[['E11','E12']],axis=1))/result2['E1mean']
result2['E2mean'] = result2[['E21','E22']].mean(axis=1)
result2['E2cv'] = (result2[['E21','E22']].std(axis=1,ddof=0))/result2['E2mean']
result2['M1mean'] = result2[['M11','M12']].mean(axis=1)
result2['M1cv'] = (result2[['M11','M12']].std(axis=1,ddof=0))/result2['M1mean']
result2['M2mean'] = result2[['M21','M22']].mean(axis=1)
result2['M2cv'] = (result2[['M21','M22']].std(axis=1,ddof=0))/result2['M2mean']
result2['G1mean'] = result2[['G11','G12']].mean(axis=1)
result2['G1cv'] = (result2[['G11','G12']].std(axis=1,ddof=0))/result2['G1mean']
result2['G2mean'] = result2[['G21','G22']].mean(axis=1)
result2['G2cv'] = (result2[['G21','G22']].std(axis=1,ddof=0))/result2['G2mean']

result2['E3mean'] = result2[['E31','E32']].mean(axis=1)
result2['E3cv'] = (result2[['E31','E32']].std(axis=1,ddof=0))/result2['E3mean']
result2['E4mean'] = result2[['E41','E42']].mean(axis=1)
result2['E4cv'] = (result2[['E41','E42']].std(axis=1,ddof=0))/result2['E4mean']
result2['M3mean'] = result2[['M31','M32']].mean(axis=1)
result2['M3cv'] = (result2[['M31','M32']].std(axis=1,ddof=0))/result2['M3mean']
result2['M4mean'] = result2[['M41','M42']].mean(axis=1)
result2['M4cv'] = (result2[['M41','M42']].std(axis=1,ddof=0))/result2['M4mean']
result2['G3mean'] = result2[['G31','G32']].mean(axis=1)
result2['G3cv'] = (result2[['G31','G32']].std(axis=1,ddof=0))/result2['G3mean']
result2['G4mean'] = result2[['G41','G42']].mean(axis=1)
result2['G4cv'] = (result2[['G41','G42']].std(axis=1,ddof=0))/result2['G4mean']
result2.to_csv('E:\\sirebrowser\\泪液标志物\\data\\result2 mean cv.csv')

#result3 = pd.concat([result2[result2['E1cv']<0.3][['E11','E12','E1mean','E1cv']],
#                     result2[result2['E2cv']<0.3][['E21','E22','E2mean','E2cv']],
#                     result2[result2['M1cv']<0.3][['M11','M12','M1mean','M1cv']],
#                     result2[result2['M2cv']<0.3][['M21','M22','M2mean','M2cv']],
#                     result2[result2['G1cv']<0.3][['G11','G12','G1mean','G1cv']],
#                     result2[result2['G2cv']<0.3][['G21','G22','G2mean','G2cv']],
#                     result2[result2['E3cv']<0.3][['E31','E32','E3mean','E3cv']],
#                     result2[result2['E4cv']<0.3][['E41','E42','E4mean','E4cv']],
#                     result2[result2['M3cv']<0.3][['M31','M32','M3mean','M3cv']],
#                     result2[result2['M4cv']<0.3][['M41','M42','M4mean','M4cv']],
#                     result2[result2['G3cv']<0.3][['G31','G32','G3mean','G3cv']],
#                     result2[result2['G4cv']<0.3][['G41','G42','G4mean','G4cv']],
#                     ],axis=1,sort=False)
#result2['E1cv'] = result2['E1cv'].replace(0,1)
#result2['E2cv'] = result2['E2cv'].replace(0,1)
#result2['M1cv'] = result2['M1cv'].replace(0,1)
#result2['M2cv'] = result2['M2cv'].replace(0,1)
#result2['G1cv'] = result2['G1cv'].replace(0,1)
#result2['G2cv'] = result2['G2cv'].replace(0,1)
#
#result2['E3cv'] = result2['E3cv'].replace(0,1)
#result2['E4cv'] = result2['E4cv'].replace(0,1)
#result2['M3cv'] = result2['M3cv'].replace(0,1)
#result2['M4cv'] = result2['M4cv'].replace(0,1)
#result2['G3cv'] = result2['G3cv'].replace(0,1)
#result2['G4cv'] = result2['G4cv'].replace(0,1)

result3 = pd.concat([result2[result2['E1']==0][result2['E1cv']<0.3][['E1mean','E1cv']],
                     result2[result2['E2']==0][result2['E2cv']<0.3][['E2mean','E2cv']],
                     result2[result2['M1']==0][result2['M1cv']<0.3][['M1mean','M1cv']],
                     result2[result2['M1']==0][result2['M2cv']<0.3][['M2mean','M2cv']],
                     result2[result2['G1']==0][result2['G1cv']<0.3][['G1mean','G1cv']],
                     result2[result2['G1']==0][result2['G2cv']<0.3][['G2mean','G2cv']],
                     result2[result2['E3']==0][result2['E3cv']<0.3][['E3mean','E3cv']],
                     result2[result2['E4']==0][result2['E4cv']<0.3][['E4mean','E4cv']],
                     result2[result2['M3']==0][result2['M3cv']<0.3][['M3mean','M3cv']],
                     result2[result2['M4']==0][result2['M4cv']<0.3][['M4mean','M4cv']],
                     result2[result2['G3']==0][result2['G3cv']<0.3][['G3mean','G3cv']],
                     result2[result2['G4']==0][result2['G4cv']<0.3][['G4mean','G4cv']],
                     ],axis=1,sort=False)
result3.to_csv('E:\\sirebrowser\\泪液标志物\\data\\result3.csv')

# EC
ec = pd.concat([result2[result2['E1']==0][result2['E1cv']<0.3][['E1mean','E1cv']],
                     result2[result2['E2']==0][result2['E2cv']<0.3][['E2mean','E2cv']],
                     result2[result2['E3']==0][result2['E3cv']<0.3][['E3mean','E3cv']],
                     result2[result2['E4']==0][result2['E4cv']<0.3][['E4mean','E4cv']]
                     ],axis=1,sort=False)
#ec = ec[~ec['E1cv'].isnull()][~ec['E2cv'].isnull()][~ec['E3cv'].isnull()][~ec['E4cv'].isnull()]
ec.to_csv('E:\\sirebrowser\\泪液标志物\\data\\ec.csv')

# MC
mc = pd.concat([result2[result2['M1']==0][result2['M1cv']<0.3][['M1mean','M1cv']],
                     result2[result2['M2']==0][result2['M2cv']<0.3][['M2mean','M2cv']],
                     result2[result2['M3']==0][result2['M3cv']<0.3][['M3mean','M3cv']],
                     result2[result2['M4']==0][result2['M4cv']<0.3][['M4mean','M4cv']]
                     ],axis=1,sort=False)
#mc = mc[~mc['M1cv'].isnull()][~mc['M2cv'].isnull()][~mc['M3cv'].isnull()][~mc['M4cv'].isnull()]
mc.to_csv('E:\\sirebrowser\\泪液标志物\\data\\mc.csv')

# GC
gc = pd.concat([result2[result2['G1']==0][result2['G1cv']<0.3][['G1mean','G1cv']],
                     result2[result2['G2']==0][result2['G2cv']<0.3][['G2mean','G2cv']],
                     result2[result2['G3']==0][result2['G3cv']<0.3][['G3mean','G3cv']],
                     result2[result2['G4']==0][result2['G4cv']<0.3][['G4mean','G4cv']]
                     ],axis=1,sort=False)
#gc = gc[~gc['G1cv'].isnull()][~gc['G2cv'].isnull()][~gc['G3cv'].isnull()][~gc['G4cv'].isnull()]
gc.to_csv('E:\\sirebrowser\\泪液标志物\\data\\gc.csv')

# ec trend screen
ec = ec.drop(['E1cv','E2cv','E3cv','E4cv'],axis=1)
ec.fillna(88888,inplace=True)
ec.insert(4,'t1',np.nan)
ec.insert(5,'t2',np.nan)
ec.insert(6,'t3',np.nan)
ec.insert(7,'t4',np.nan)
for i in range(0,ec.shape[0]): # i=11
    print(i)
    if ec.iloc[i,0] >= 1:
        ec.iloc[i,4] = 1
    if ec.iloc[i,0] < 1:
        ec.iloc[i,4] = -1
    if ec.iloc[i,0] == 88888:
        ec.iloc[i,4] = 0
for i in range(0,ec.shape[0]): # i=0
    print(i)
    if ec.iloc[i,1] >= 1:
        ec.iloc[i,5] = 1
    if ec.iloc[i,1] < 1:
        ec.iloc[i,5] = -1
    if ec.iloc[i,1] == 88888:
        ec.iloc[i,5] = 0    
for i in range(0,ec.shape[0]): # i=0
    print(i)
    if ec.iloc[i,2] >= 1:
        ec.iloc[i,6] = 1
    if ec.iloc[i,2] < 1:
        ec.iloc[i,6] = -1
    if ec.iloc[i,2] == 88888:
        ec.iloc[i,6] = 0 
for i in range(0,ec.shape[0]): # i=0
    print(i)
    if ec.iloc[i,3] >= 1:
        ec.iloc[i,7] = 1
    if ec.iloc[i,3] < 1:
        ec.iloc[i,7] = -1
    if ec.iloc[i,3] == 88888:
        ec.iloc[i,7] = 0  
ec['sum'] = abs(ec['t1'])+abs(ec['t2'])+abs(ec['t3'])+abs(ec['t4'])
# remove
ec.insert(6,'sum1',np.nan)
ec.insert(9,'sum2',np.nan)
ec['sum1'] = ec['t1']+ec['t2']
ec['sum2'] = ec['t3']+ec['t4']

ec = ec[(ec['sum1'] != 0)|(ec['sum2'] != 0)]
ec = ec[(ec['sum1'] == 2)&(ec['sum2'] == -2) == False]
ec = ec[(ec['sum1'] == -2)&(ec['sum2'] == 2) == False]
ec = ec[(ec['sum1'] == 2)&(ec['sum2'] == -1) == False]
ec = ec[(ec['sum1'] == -2)&(ec['sum2'] == 1) == False]
ec = ec[(ec['sum2'] == 2)&(ec['sum1'] == -1) == False]
ec = ec[(ec['sum2'] == -2)&(ec['sum1'] == 1) == False]
ec = ec[(ec['sum1'] == 1)&(ec['sum2'] == -1) == False]
ec = ec[(ec['sum1'] == -1)&(ec['sum2'] == 1) == False]
ec = ec[(ec['sum1'] == -1)&(ec['sum2'] == 0) == False]
ec = ec[(ec['sum1'] == 1)&(ec['sum2'] == 0) == False]
ec = ec[(ec['sum2'] == -1)&(ec['sum1'] == 0) == False]
ec = ec[(ec['sum2'] == 1)&(ec['sum1'] == 0) == False]
ec = ec[ec['sum'] != 1]
ec.to_csv('E:\\sirebrowser\\泪液标志物\\data\\ecscreen.csv')

for i in range(0,ec.shape[0]):
    print(i)
    if ec.iloc[i,10] == 4:
        if ec.iloc[i,6] == 2:
            if ec.iloc[i,9] == 0:
                if ec.iloc[i,7] == -1:
                    ec.iloc[i,2] = 88888
                if ec.iloc[i,8] == -1:
                    ec.iloc[i,3] = 88888
        if ec.iloc[i,6] == -2:
            if ec.iloc[i,9] == 0:
                if ec.iloc[i,7] == 1:
                    ec.iloc[i,2] = 88888
                if ec.iloc[i,8] == 1:
                    ec.iloc[i,3] = 88888
        if ec.iloc[i,9] == 2:
            if ec.iloc[i,6] == 0:
                if ec.iloc[i,4] == -1:
                    ec.iloc[i,0] = 88888
                if ec.iloc[i,5] == -1:
                    ec.iloc[i,1] = 88888
        if ec.iloc[i,9] == -2:
            if ec.iloc[i,6] == 0:
                if ec.iloc[i,4] == 1:
                    ec.iloc[i,0] = 88888
                if ec.iloc[i,5] == 1:
                    ec.iloc[i,1] = 88888
                
    
ec = ec.replace(88888,np.nan)
ecfill = ec[['E1mean','E2mean','E3mean','E4mean']]
ecfill = pd.DataFrame(ecfill.values.T, index=ecfill.columns, columns=ecfill.index)
ecfill.fillna(ecfill.mean(axis=0), inplace=True)
ecfill = pd.DataFrame(ecfill.values.T, index=ecfill.columns, columns=ecfill.index)
ecfill.to_csv('E:\\sirebrowser\\泪液标志物\\data\\ecfill.csv')

# mc trend screen
mc = mc.drop(['M1cv','M2cv','M3cv','M4cv'],axis=1)
mc.fillna(88888,inplace=True)
mc.insert(4,'t1',np.nan)
mc.insert(5,'t2',np.nan)
mc.insert(6,'t3',np.nan)
mc.insert(7,'t4',np.nan)
for i in range(0,mc.shape[0]): # i=11
    print(i)
    if mc.iloc[i,0] >= 1:
        mc.iloc[i,4] = 1
    if mc.iloc[i,0] < 1:
        mc.iloc[i,4] = -1
    if mc.iloc[i,0] == 88888:
        mc.iloc[i,4] = 0
for i in range(0,mc.shape[0]): # i=0
    print(i)
    if mc.iloc[i,1] >= 1:
        mc.iloc[i,5] = 1
    if mc.iloc[i,1] < 1:
        mc.iloc[i,5] = -1
    if mc.iloc[i,1] == 88888:
        mc.iloc[i,5] = 0    
for i in range(0,mc.shape[0]): # i=0
    print(i)
    if mc.iloc[i,2] >= 1:
        mc.iloc[i,6] = 1
    if mc.iloc[i,2] < 1:
        mc.iloc[i,6] = -1
    if mc.iloc[i,2] == 88888:
        mc.iloc[i,6] = 0 
for i in range(0,mc.shape[0]): # i=0
    print(i)
    if mc.iloc[i,3] >= 1:
        mc.iloc[i,7] = 1
    if mc.iloc[i,3] < 1:
        mc.iloc[i,7] = -1
    if mc.iloc[i,3] == 88888:
        mc.iloc[i,7] = 0  
mc['sum'] = abs(mc['t1'])+abs(mc['t2'])+abs(mc['t3'])+abs(mc['t4'])
# remove
mc.insert(6,'sum1',np.nan)
mc.insert(9,'sum2',np.nan)
mc['sum1'] = mc['t1']+mc['t2']
mc['sum2'] = mc['t3']+mc['t4']

mc = mc[(mc['sum1'] != 0)|(mc['sum2'] != 0)]
mc = mc[(mc['sum1'] == 2)&(mc['sum2'] == -2) == False]
mc = mc[(mc['sum1'] == -2)&(mc['sum2'] == 2) == False]
mc = mc[(mc['sum1'] == 2)&(mc['sum2'] == -1) == False]
mc = mc[(mc['sum1'] == -2)&(mc['sum2'] == 1) == False]
mc = mc[(mc['sum2'] == 2)&(mc['sum1'] == -1) == False]
mc = mc[(mc['sum2'] == -2)&(mc['sum1'] == 1) == False]
mc = mc[(mc['sum1'] == 1)&(mc['sum2'] == -1) == False]
mc = mc[(mc['sum1'] == -1)&(mc['sum2'] == 1) == False]
mc = mc[(mc['sum1'] == -1)&(mc['sum2'] == 0) == False]
mc = mc[(mc['sum1'] == 1)&(mc['sum2'] == 0) == False]
mc = mc[(mc['sum2'] == -1)&(mc['sum1'] == 0) == False]
mc = mc[(mc['sum2'] == 1)&(mc['sum1'] == 0) == False]
mc = mc[mc['sum'] != 1]
mc.to_csv('E:\\sirebrowser\\泪液标志物\\data\\mcscreen.csv')

for i in range(0,mc.shape[0]):
    print(i)
    if mc.iloc[i,10] == 4:
        if mc.iloc[i,6] == 2:
            if mc.iloc[i,9] == 0:
                if mc.iloc[i,7] == -1:
                    mc.iloc[i,2] = 88888
                if mc.iloc[i,8] == -1:
                    mc.iloc[i,3] = 88888
        if mc.iloc[i,6] == -2:
            if mc.iloc[i,9] == 0:
                if mc.iloc[i,7] == 1:
                    mc.iloc[i,2] = 88888
                if mc.iloc[i,8] == 1:
                    mc.iloc[i,3] = 88888
        if mc.iloc[i,9] == 2:
            if mc.iloc[i,6] == 0:
                if mc.iloc[i,4] == -1:
                    mc.iloc[i,0] = 88888
                if mc.iloc[i,5] == -1:
                    mc.iloc[i,1] = 88888
        if mc.iloc[i,9] == -2:
            if mc.iloc[i,6] == 0:
                if mc.iloc[i,4] == 1:
                    mc.iloc[i,0] = 88888
                if mc.iloc[i,5] == 1:
                    mc.iloc[i,1] = 88888

mc = mc.replace(88888,np.nan)
mcfill = mc[['M1mean','M2mean','M3mean','M4mean']]
mcfill = pd.DataFrame(mcfill.values.T, index=mcfill.columns, columns=mcfill.index)
mcfill.fillna(mcfill.mean(axis=0), inplace=True)
mcfill = pd.DataFrame(mcfill.values.T, index=mcfill.columns, columns=mcfill.index)
mcfill.to_csv('E:\\sirebrowser\\泪液标志物\\data\\mcfill.csv')

# gc trend screen
gc = gc.drop(['G1cv','G2cv','G3cv','G4cv'],axis=1)
gc.fillna(88888,inplace=True)
gc.insert(4,'t1',np.nan)
gc.insert(5,'t2',np.nan)
gc.insert(6,'t3',np.nan)
gc.insert(7,'t4',np.nan)
for i in range(0,gc.shape[0]): # i=11
    print(i)
    if gc.iloc[i,0] >= 1:
        gc.iloc[i,4] = 1
    if gc.iloc[i,0] < 1:
        gc.iloc[i,4] = -1
    if gc.iloc[i,0] == 88888:
        gc.iloc[i,4] = 0
for i in range(0,gc.shape[0]): # i=0
    print(i)
    if gc.iloc[i,1] >= 1:
        gc.iloc[i,5] = 1
    if gc.iloc[i,1] < 1:
        gc.iloc[i,5] = -1
    if gc.iloc[i,1] == 88888:
        gc.iloc[i,5] = 0    
for i in range(0,gc.shape[0]): # i=0
    print(i)
    if gc.iloc[i,2] >= 1:
        gc.iloc[i,6] = 1
    if gc.iloc[i,2] < 1:
        gc.iloc[i,6] = -1
    if gc.iloc[i,2] == 88888:
        gc.iloc[i,6] = 0 
for i in range(0,gc.shape[0]): # i=0
    print(i)
    if gc.iloc[i,3] >= 1:
        gc.iloc[i,7] = 1
    if gc.iloc[i,3] < 1:
        gc.iloc[i,7] = -1
    if gc.iloc[i,3] == 88888:
        gc.iloc[i,7] = 0  
gc['sum'] = abs(gc['t1'])+abs(gc['t2'])+abs(gc['t3'])+abs(gc['t4'])
# remove
gc.insert(6,'sum1',np.nan)
gc.insert(9,'sum2',np.nan)
gc['sum1'] = gc['t1']+gc['t2']
gc['sum2'] = gc['t3']+gc['t4']

gc = gc[(gc['sum1'] != 0)|(gc['sum2'] != 0)]
gc = gc[(gc['sum1'] == 2)&(gc['sum2'] == -2) == False]
gc = gc[(gc['sum1'] == -2)&(gc['sum2'] == 2) == False]
gc = gc[(gc['sum1'] == 2)&(gc['sum2'] == -1) == False]
gc = gc[(gc['sum1'] == -2)&(gc['sum2'] == 1) == False]
gc = gc[(gc['sum2'] == 2)&(gc['sum1'] == -1) == False]
gc = gc[(gc['sum2'] == -2)&(gc['sum1'] == 1) == False]
gc = gc[(gc['sum1'] == 1)&(gc['sum2'] == -1) == False]
gc = gc[(gc['sum1'] == -1)&(gc['sum2'] == 1) == False]
gc = gc[(gc['sum1'] == -1)&(gc['sum2'] == 0) == False]
gc = gc[(gc['sum1'] == 1)&(gc['sum2'] == 0) == False]
gc = gc[(gc['sum2'] == -1)&(gc['sum1'] == 0) == False]
gc = gc[(gc['sum2'] == 1)&(gc['sum1'] == 0) == False]
gc = gc[gc['sum'] != 1]
gc.to_csv('E:\\sirebrowser\\泪液标志物\\data\\gcscreen.csv')

for i in range(0,gc.shape[0]):
    print(i)
    if gc.iloc[i,10] == 4:
        if gc.iloc[i,6] == 2:
            if gc.iloc[i,9] == 0:
                if gc.iloc[i,7] == -1:
                    gc.iloc[i,2] = 88888
                if gc.iloc[i,8] == -1:
                    gc.iloc[i,3] = 88888
        if gc.iloc[i,6] == -2:
            if gc.iloc[i,9] == 0:
                if gc.iloc[i,7] == 1:
                    gc.iloc[i,2] = 88888
                if gc.iloc[i,8] == 1:
                    gc.iloc[i,3] = 88888
        if gc.iloc[i,9] == 2:
            if gc.iloc[i,6] == 0:
                if gc.iloc[i,4] == -1:
                    gc.iloc[i,0] = 88888
                if gc.iloc[i,5] == -1:
                    gc.iloc[i,1] = 88888
        if gc.iloc[i,9] == -2:
            if gc.iloc[i,6] == 0:
                if gc.iloc[i,4] == 1:
                    gc.iloc[i,0] = 88888
                if gc.iloc[i,5] == 1:
                    gc.iloc[i,1] = 88888

gc = gc.replace(88888,np.nan)
gcfill = gc[['G1mean','G2mean','G3mean','G4mean']]
gcfill = pd.DataFrame(gcfill.values.T, index=gcfill.columns, columns=gcfill.index)
gcfill.fillna(gcfill.mean(axis=0), inplace=True)
gcfill = pd.DataFrame(gcfill.values.T, index=gcfill.columns, columns=gcfill.index)
gcfill.to_csv('E:\\sirebrowser\\泪液标志物\\data\\gcfill.csv')

result4 = pd.concat([ecfill,mcfill,gcfill],axis=1,sort=False)
# 交集
result4 = result4[~result4['E1mean'].isnull()]
result4 = result4[~result4['M1mean'].isnull()]
result4 = result4[~result4['G1mean'].isnull()]
result4.to_csv('E:\\sirebrowser\\泪液标志物\\data\\result4.csv')

# result5
result5 = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='Sheet4')
result5 = result5.set_index('Protein name',drop=True)
result5 = result5.drop(np.nan,axis=0)
result5 = result5.drop('Unnamed: 4',axis=1)
result5 = result5.drop('Unnamed: 5',axis=1)

result5.insert(3,'GM≥1.5&ME≥1.5&EC≥1.5',-1)
result5.insert(4,'GM<1.5&ME<1.5&EC<1.5',-1)
result5.insert(5,'GM<1.5&ME<1.5&EC≥1.5',-1)
result5.insert(6,'GM>1.5&ME>1.5&EC>1.5',-1)
result5.insert(7,'GM>1.5&ME>1.5&EC>1.5',-1)           
result5.insert(8,'GM>1.5&ME>1.5&EC>1.5',-1)                  
result5.insert(9,'GM>1.5&ME>1.5&EC>1.5',-1)
result5.insert(10,'GM>1.5&ME>1.5&EC>1.5',-1)

# 折线图
import matplotlib.pyplot as plt
fontt={'color': 'k',
      'size': 30,
      'family': 'Arial'}
fonttt={'color': 'k',
      'size': 20,
      'family': 'Arial'}
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='Sheet3')
data = data.set_index('Feature',drop=True)

for i in range(0,data.shape[0]): #i=0
    print(i)
    x = [1,2,3,4]
    y = data.iloc[i,:].values
    plt.plot(x,y,linewidth=5,markersize=10,marker='o',color='#9932CC')
    plt.xlim(0, 5) 
    plt.ylim(-0.5, 12,2)
    plt.title(data.index[i],fontdict=fontt)
    
    ax = plt.gca()
    plt.tick_params(width=4,length=8)
    ax.spines['bottom'].set_linewidth('4')
    ax.spines['top'].set_linewidth('0')
    ax.spines['left'].set_linewidth('4')
    ax.spines['right'].set_linewidth('0')
    plt.yticks(fontproperties = 'Arial', size = 25)
    plt.xticks(fontproperties = 'Arial', size = 25)
    ax.set_xticklabels(['','C','E','M','G'])
    plt.hlines(1,xmin=1,xmax=4,color='k',linewidth=2,ls = '--') 
    plt.vlines(2,ymin=1,ymax=y[1],color='k',linewidth=2,ls = '--') 
    plt.vlines(3,ymin=1,ymax=y[2],color='k',linewidth=2,ls = '--') 
    plt.vlines(4,ymin=1,ymax=y[3],color='k',linewidth=2,ls = '--') 
    plt.text(0.5, 1.8, "%.3f"%y[0], fontdict=fonttt, color='k')
    plt.text(1.5, round(y[1],2)+0.8, "%.3f"%y[1], fontdict=fonttt, color='k')
    plt.text(2.5, round(y[2],2)+0.8, "%.3f"%y[2], fontdict=fonttt, color='k')
    plt.text(3.5, round(y[3],2)+0.8, "%.3f"%y[3], fontdict=fonttt, color='k')
    plt.savefig(fname='E:\\sirebrowser\\泪液标志物\\plot\\%s.png'%data.index[i],dpi=300, bbox_inches='tight')
    plt.close('all')

# heatmap
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
result5 = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='heatmap')
#result5 = result5.set_index('Protein name',drop=True)   type(data.iloc[1,1])
result5 = np.log2(result5)
my_colormap = LinearSegmentedColormap.from_list("", ["navy",'white', "red"])
plt.figure(figsize=(40,50),dpi=100)
sns.set(font_scale=1.4)
sns.set_theme(font='Arial',font_scale=1.7)
g = sns.clustermap(data=result5,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap=my_colormap,center=0,vmax=3,vmin=-3,figsize=(30,50))
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)
    
# 可用数据heatmap
col = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 
 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 
 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r',
 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 
 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 
 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 
 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr',
 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 
 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 
 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 
 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 
 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg',
 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 
 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako',
 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 
 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 
 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c',
 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 
 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']
data = pd.read_csv('E:\\sirebrowser\\泪液标志物\\data\\mcfill.csv',engine='python',encoding='UTF-8-sig')
data.rename(columns={'Unnamed: 0':'Feature'},inplace=True)
data = data.set_index('Feature',drop=True)  
data = np.log2(data)

sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='Spectral_r',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\mcfill.png',dpi=300, bbox_inches='tight')
plt.close('all') 

# cor
data = pd.read_csv('E:\\sirebrowser\\泪液标志物\\data\\gcfill.csv',engine='python',encoding='UTF-8-sig')
data.rename(columns={'Unnamed: 0':'Feature'},inplace=True)
data = data.set_index('Feature',drop=True)  
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='Spectral_r',center=0,linewidths=1,linecolor='grey',figsize=(82,82),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\gcfill corr.png',dpi=300, bbox_inches='tight')
plt.close('all')    

# common heatmap    
# 绝对值
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='Sheet3')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\common abs.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='Sheet3')
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\common abs corr.png',dpi=300, bbox_inches='tight')
plt.close('all')  
  
# 比值
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='heatmap')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\common ratio.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液差异蛋白分析.xlsx',sheet_name='heatmap')
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\common ratio corr.png',dpi=300, bbox_inches='tight')
plt.close('all')     
    
# pr
# 
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet3')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\pr.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet3')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\pr corr.png',dpi=300, bbox_inches='tight')
plt.close('all')    

# gr
# 
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet4')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\gr.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet4')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(5)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(5) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\gr corr.png',dpi=300, bbox_inches='tight')
plt.close('all')   

# common c ec mc gm
# 
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet5')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=data,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*data.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\75 abs+ratio.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet5')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\75 abs+ratio corr.png',dpi=300, bbox_inches='tight')
plt.close('all')    

# pr gr com
pr = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet3')
pr = np.log2(pr)
gr = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet4')
gr = np.log2(gr)   
com = pd.concat([pr,gr.iloc[:,1:]],axis=1,sort=False)
com.to_csv('E:\\sirebrowser\\泪液标志物\\data\\pr gr com.csv')
com = com.replace(np.nan,0)
sns.set_theme(font='Arial',font_scale=1.7)

g = sns.clustermap(data=com,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=False,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',figsize=(5,150*com.shape[0]/225),
               cbar=True,vmax=3,vmin=-3)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\54 abs+ratio.png',dpi=300, bbox_inches='tight')
plt.close('all')  

com = pd.read_csv('E:\\sirebrowser\\泪液标志物\\data\\pr gr com.csv',engine='python',encoding='UTF-8-sig')
com.rename(columns={'Unnamed: 0':'Feature'},inplace=True)
com = com.set_index('Feature',drop=True)
com = com.iloc[:,:4]
com = pd.DataFrame(com.values.T, index=com.columns, columns=com.index)
corr = com.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*com.shape[1]/225,100*com.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(5)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(5) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\54 corr.png',dpi=300, bbox_inches='tight')
plt.close('all')  

# 7-17 common  
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet6')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)
plt.figure(figsize=(5,150*data.shape[0]/225),dpi=300)
g = sns.heatmap(data=data,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',
               cbar=True,vmax=3,vmin=-3)
#for a in g.ax_row_dendrogram.collections:
#    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 common.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet6')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 common corr.png',dpi=300, bbox_inches='tight')
plt.close('all')  

#g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
#               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
#               cbar=True,vmax=1,vmin=-1,mask=mask)
#mask = np.tril(np.ones_like(corr))
#values = g.ax_heatmap.collections[0].get_array().reshape(corr.shape)
#new_values = np.ma.array(values, mask=mask)
#g.ax_heatmap.collections[0].set_array(new_values)
#plt.show()

##以corr的形状生成一个全为0的矩阵 
#mask = np.ones_like(corr)
##将mask的对角线及以上设置为True
#mask[np.triu_indices_from(mask)] = False
#with sns.axes_style("white"):
#    sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
#               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
#               cbar=True,vmax=1,vmin=-1,mask=mask)
# pr
# 
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet3')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)
plt.figure(figsize=(5,150*data.shape[0]/225),dpi=300)
g = sns.heatmap(data=data,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',
               cbar=True,vmax=3,vmin=-3)
#for a in g.ax_row_dendrogram.collections:
#    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 pr.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet3')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(7)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(7) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 pr corr.png',dpi=300, bbox_inches='tight')
plt.close('all')    

# gr
# 
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet4')
data = np.log2(data)
sns.set_theme(font='Arial',font_scale=1.7)
plt.figure(figsize=(2.5,150*data.shape[0]/225),dpi=300)
g = sns.heatmap(data=data,cmap='coolwarm',center=0,linewidths=0.5,linecolor='grey',
               cbar=True,vmax=3,vmin=-3)
#for a in g.ax_row_dendrogram.collections:
#    a.set_linewidth(3)  
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 gr.png',dpi=300, bbox_inches='tight')
plt.close('all')  
    
# cor
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet4')
data = np.log2(data)
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
corr = data.corr(method='spearman')
sns.set_theme(font='Arial',font_scale=1.2)
g = sns.clustermap(data=corr,method='ward',metric='euclidean',row_cluster=True,
               col_cluster=True,cmap='coolwarm',center=0,linewidths=1,linecolor='grey',figsize=(100*data.shape[1]/225,100*data.shape[1]/225),
               cbar=True,vmax=1,vmin=-1)
for a in g.ax_row_dendrogram.collections:
    a.set_linewidth(5)  
for a in g.ax_col_dendrogram.collections:
    a.set_linewidth(5) 
        
plt.savefig('E:\\sirebrowser\\泪液标志物\\plot\\0717 gr corr.png',dpi=300, bbox_inches='tight')
plt.close('all')   

# 折线图
import matplotlib.pyplot as plt
fontt={'color': 'k',
      'size': 30,
      'family': 'Arial'}
fonttt={'color': 'k',
      'size': 20,
      'family': 'Arial'}
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet6')
sd = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet1')
sd = sd[['ESD','MSD','GSD']]
sd.insert(0,'CSD',0)
#data['GDM/MS'] = data['MS/C']*data['GDM/MS']
for i in range(0,data.shape[0]):    i=24
    print(i)
    x = [1,2,3,4]
    y = data.iloc[i,:].values
    e = sd.iloc[i,:].values
    plt.plot(x,[y[0],y[1],y[2],y[2]*y[3]],linewidth=4,markersize=10,marker='o',color='#9932CC')
    plt.fill_between(x,[y[0],y[1],y[2],y[2]*y[3]]-e,[y[0],y[1],y[2],y[2]*y[3]]+e,alpha=0.5,color='#0000FF')
    plt.xlim(0, 5) 
    plt.title(data.index[i],fontdict=fontt)
    plt.tick_params(width=2,length=4,color='k')    
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth('2')
    ax.spines['bottom'].set_color('k')
    ax.spines['top'].set_linewidth('2')
    ax.spines['top'].set_color('k')
    ax.spines['left'].set_linewidth('2')
    ax.spines['left'].set_color('k')
    ax.spines['right'].set_linewidth('2')
    ax.spines['right'].set_color('k')
    plt.yticks(fontproperties = 'Arial', size = 25)
    plt.xticks(fontproperties = 'Arial', size = 25,rotation=65)
    ax.set_xticklabels(['','C','ES/C','MS/C','GDM/MS'])
    h = max([y[0],y[1],y[2],y[2]*y[3]])
    eh = [y[0],y[1],y[2],y[2]*y[3]].index(h)
    eh = e[eh]
    h = h+eh
    r = [1.02,1.04,1.15,1.17,1.19]
    plt.ylim(0, int(h*r[4])+1.5,10) ###################
    plt.vlines(1,ymin=h,ymax=h*r[0],color='k',linewidth=2) 
    plt.hlines(h*r[0],xmin=1,xmax=2,color='k',linewidth=2) 
    plt.vlines(2,ymin=h,ymax=h*r[0],color='k',linewidth=2)
    plt.text(1.1, h*r[1], "%.3f"%y[1], fontdict=fonttt, color='k')
    if y[1]>1.5:
        plt.fill_between([1,2],0,136,alpha=0.4,color='#800000')
    if y[1]<0.666667:
        plt.fill_between([1,2],0,136,alpha=0.4,color='#006400')
    else:
        plt.fill_between([1,2],0,136,alpha=0.2,color='w')

    plt.vlines(1,ymin=h*r[2],ymax=h*r[3],color='k',linewidth=2) 
    plt.hlines(h*r[3],xmin=1,xmax=3,color='k',linewidth=2) 
    plt.vlines(3,ymin=h*r[2],ymax=h*r[3],color='k',linewidth=2)
    plt.text(1.6, h*r[4], "%.3f"%y[2], fontdict=fonttt, color='k')  
    if y[2]>1.5:
        plt.fill_between([1,3],0,136,alpha=0.4,color='#DC143C')
    if y[2]<0.666667:
        plt.fill_between([1,3],0,136,alpha=0.4,color='#32CD32')
    else:
        plt.fill_between([1,3],0,136,alpha=0.2,color='w')
            
    plt.vlines(3,ymin=h*r[2],ymax=h*r[3],color='k',linewidth=2) 
    plt.hlines(h*r[3],xmin=3,xmax=4,color='k',linewidth=2) 
    plt.vlines(4,ymin=h*r[2],ymax=h*r[3],color='k',linewidth=2)
    plt.text(3.1, h*r[4], "%.3f"%y[3], fontdict=fonttt, color='k')
    if y[3]>1.5:
        plt.fill_between([3,4],0,136,alpha=0.4,color='#F08080')
    if y[3]<0.666667:
        plt.fill_between([3,4],0,136,alpha=0.4,color='#98FB98')
    else:
        plt.fill_between([3,4],0,136,alpha=0.2,color='w')
    
    plt.savefig(fname='E:\\sirebrowser\\泪液标志物\\errorplot1\\%s.png'%data.index[i],dpi=300, bbox_inches='tight')
    
#    if y[1] > 1:
#        plt.vlines(1,ymin=h,ymax=h+0.5,color='k',linewidth=2) 
#        plt.hlines(h+0.5,xmin=1,xmax=2,color='k',linewidth=2) 
#        plt.vlines(2,ymin=h,ymax=h+0.5,color='k',linewidth=2)
#        plt.text(1.1, h+1, "%.3f"%y[1], fontdict=fonttt, color='k')
#        if y[2]>y[1]:
#            plt.vlines(1,ymin=h+3.5,ymax=h+4,color='k',linewidth=2) 
#            plt.hlines(h+4,xmin=1,xmax=3,color='k',linewidth=2) 
#            plt.vlines(3,ymin=h+3.5,ymax=h+4,color='k',linewidth=2)
#            plt.text(1.6, h+4.5, "%.3f"%y[2], fontdict=fonttt, color='k')   
#            if y[3]*y[2]>y[2]:
#                plt.vlines(3,ymin=h+3.5,ymax=h+4,color='k',linewidth=2) 
#                plt.hlines(h+4,xmin=3,xmax=4,color='k',linewidth=2) 
#                plt.vlines(4,ymin=h+3.5,ymax=h+4,color='k',linewidth=2)
#                plt.text(3.1, h+4.5, "%.3f"%y[3], fontdict=fonttt, color='k')
#            if y[3]*y[2]<y[2]:
#                plt.vlines(3,ymin=h+3.5,ymax=h+4,color='k',linewidth=2) 
#                plt.hlines(h+4,xmin=3,xmax=4,color='k',linewidth=2) 
#                plt.vlines(4,ymin=h+3.5,ymax=h+4,color='k',linewidth=2)
#                plt.text(3.1, h+4.5, "%.3f"%y[3], fontdict=fonttt, color='k')
            
#        if y[2]<y[1]:
#            plt.vlines(1,ymin=y[1]+abs(y[2]-y[1])*1.3,ymax=y[1]+abs(y[2]-y[1])*1.5,color='k',linewidth=2) 
#            plt.hlines(y[1]+abs(y[2]-y[1])*1.5,xmin=1,xmax=3,color='k',linewidth=2) 
#            plt.vlines(3,ymin=y[1]+abs(y[2]-y[1])*1.3,ymax=y[1]+abs(y[2]-y[1])*1.5,color='k',linewidth=2)
#            plt.text(1.6, y[1]+abs(y[2]-y[1])*1.55, "%.3f"%y[2], fontdict=fonttt, color='k')
#            
#            
#    if y[1] < 1:
#        plt.vlines(1,ymin=y[0]+abs(y[1]-y[0])*0.1,ymax=y[0]+abs(y[1]-y[0])*0.2,color='k',linewidth=2) 
#        plt.hlines(y[0]+abs(y[1]-y[0])*0.2,xmin=1,xmax=2,color='k',linewidth=2) 
#        plt.vlines(2,ymin=y[0]+abs(y[1]-y[0])*0.1,ymax=y[0]+abs(y[1]-y[0])*0.2,color='k',linewidth=2)
#        plt.text(1.1, y[0]+abs(y[1]-y[0])*0.25, "%.3f"%y[1], fontdict=fonttt, color='k')
#        
#        plt.vlines(1,ymin=y[0]+abs(y[1]-y[0])*0.4,ymax=y[0]+abs(y[1]-y[0])*0.55,color='k',linewidth=2) 
#        plt.hlines(y[0]+abs(y[1]-y[0])*0.55,xmin=1,xmax=3,color='k',linewidth=2) 
#        plt.vlines(3,ymin=y[0]+abs(y[1]-y[0])*0.4,ymax=y[0]+abs(y[1]-y[0])*0.55,color='k',linewidth=2)
#        plt.text(1.6, y[0]+abs(y[1]-y[0])*0.6, "%.3f"%y[2], fontdict=fonttt, color='k')   
#
#        
#    
#    plt.vlines(1,ymin=1+1,ymax=y[0]+abs(y[1]-y[0])+1,color='k',linewidth=2) 
#    plt.hlines(y[1]+1,xmin=1,xmax=2,color='k',linewidth=2) 
#    plt.vlines(2,ymin=y[1]+1,ymax=y[1]+2*abs(y[1]-y[0])+1,color='k',linewidth=2)
#    plt.text(1.1, round(y[1]+1,2)+0.8, "%.3f"%y[1], fontdict=fonttt, color='k')
#    
#    plt.vlines(1,ymin=y[1]+3,ymax=y[1]+abs(y[2]-y[1])+1,color='k',linewidth=2) 
#    plt.hlines(y[1]+abs(y[2]-y[1])+1,xmin=1,xmax=3,color='k',linewidth=2) 
#    plt.vlines(3,ymin=y[2]+1,ymax=y[1]+abs(y[2]-y[1])+1,color='k',linewidth=2)
#    plt.text(1.6, round(y[1]+abs(y[2]-y[1])+1,2)+0.8, "%.3f"%y[2], fontdict=fonttt, color='k')
#    
#    plt.vlines(3,ymin=y[2]+3,ymax=y[2]+abs(y[3]-y[2])+1,color='k',linewidth=2) 
#    plt.hlines(y[2]+abs(y[3]-y[2])+1,xmin=3,xmax=4,color='k',linewidth=2) 
#    plt.vlines(4,ymin=y[3]+1,ymax=y[1]+abs(y[2]-y[1])+1,color='k',linewidth=2)
#    plt.text(1.6, round(y[1]+abs(y[2]-y[1])+1,2)+0.8, "%.3f"%y[2], fontdict=fonttt, color='k')
#
#
#
#    plt.hlines(1,xmin=1,xmax=4,color='k',linewidth=2,ls = '--') 
#    plt.vlines(2,ymin=1,ymax=y[1],color='k',linewidth=2,ls = '--') 
#    plt.vlines(3,ymin=1,ymax=y[2],color='k',linewidth=2,ls = '--') 
#    plt.vlines(4,ymin=1,ymax=y[3],color='k',linewidth=2,ls = '--') 
#    
#    plt.text(0.5, 1.8, "%.3f"%y[0], fontdict=fonttt, color='k')
#    plt.text(1.5, round(y[1],2)+0.8, "%.3f"%y[1], fontdict=fonttt, color='k')
#    plt.text(2.5, round(y[2],2)+0.8, "%.3f"%y[2], fontdict=fonttt, color='k')
#    plt.text(3.5, round(y[3],2)+0.8, "%.3f"%y[3], fontdict=fonttt, color='k')
#    plt.savefig(fname='E:\\sirebrowser\\泪液标志物\\plot\\%s.png'%data.index[i],dpi=300, bbox_inches='tight')
#    plt.close('all')
    
# pca
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
# pr
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet1')
data = data.drop(['ESD','MSD','GSD'],axis=1)
data = data.iloc[:,:12]
data.insert(0,'C1',1)
data.insert(1,'C2',1)
data.insert(2,'C3',1)
data.insert(3,'C4',1)

data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)

# 2
pca = PCA(n_components=2) #选择降维数量
pca = pca.fit(data) #建模
data_pca = pca.transform(data)

x1,y1 = [],[]
for i in range(0,4):
    print(i)
    x1.append(data_pca[i][0])
    y1.append(data_pca[i][1])
    
x2,y2 = [],[]
for i in range(4,8):
    x2.append(data_pca[i][0])
    y2.append(data_pca[i][1])

x3,y3 = [],[]
for i in range(8,12):
    x3.append(data_pca[i][0])
    y3.append(data_pca[i][1])

x4,y4 = [],[]
for i in range(12,16):
    x4.append(data_pca[i][0])
    y4.append(data_pca[i][1])
    
plt.scatter(x1, y1, c='green')
plt.scatter(x2, y2, c='blue')
plt.scatter(x3, y3, c='orange')
plt.scatter(x4, y4, c='red')

# 3
pca = PCA(n_components=3) #选择降维数量
pca = pca.fit(data) #建模
data2_pca = pca.transform(data)

x1,y1,z1 = [],[],[]
for i in range(0,4):
    x1.append(data2_pca[i][0])
    y1.append(data2_pca[i][1])
    z1.append(data2_pca[i][2])
    
x2,y2,z2 = [],[],[]
for i in range(4,8):
    x2.append(data2_pca[i][0])
    y2.append(data2_pca[i][1])
    z2.append(data2_pca[i][2])

x3,y3,z3 = [],[],[]
for i in range(8,12):
    x3.append(data2_pca[i][0])
    y3.append(data2_pca[i][1])
    z3.append(data2_pca[i][2])

#x4,y4,z4 = [],[],[]
#for i in range(12,16):
#    x4.append(data2_pca[i][0])
#    y4.append(data2_pca[i][1])
#    z4.append(data2_pca[i][2])
plt.rcParams['font.size'] = 30
plt.rcParams['font.sans-serif'] = ['Arial']
fontt={'color': 'k',
      'size': 30,
      'family': 'Arial'}
plt.figure(figsize= (10, 10))
ax3d = plt.gca(projection="3d")  # 创建三维坐标
#plt.title('3D Scatter', fontsize=20)
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
#ax3d.view_init(180, 100)
#plt.tick_params(labelsize=30)
ax3d.scatter(x1, y1, z1, s=150, color="#00FF7F", marker="o")
ax3d.scatter(x2, y2, z2, s=150, color="#6495ED", marker="o")
ax3d.scatter(x3, y3, z3, s=150, color="#DC143C", marker="o")
ax3d.legend(['C','ES/C','MS/C'], loc=(1,1))
#ax3d.set_xlabel("X axis", fontdict=fontt)
#ax3d.set_ylabel("Y axis", fontdict=fontt)
#ax3d.set_zlabel("Z axis", fontdict=fontt)
#ax3d.scatter(x4, y4, z4, s=50, color="red", marker="o")
plt.tick_params(width=2,length=4,color='k')    
#ax = plt.gca()
#ax.spines['bottom'].set_linewidth('2')
#ax.spines['bottom'].set_color('k')
#ax.spines['top'].set_linewidth('2')
#ax.spines['top'].set_color('k')
#ax.spines['left'].set_linewidth('2')
#ax.spines['left'].set_color('k')
#ax.spines['right'].set_linewidth('2')
#ax.spines['right'].set_color('k')
#plt.yticks(fontproperties = 'Arial', size = 25)
#plt.xticks(fontproperties = 'Arial', size = 25)

plt.show()

# g m
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet1')
data = data.iloc[:,[5,6,7,8,16,17,18,19]]
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)

pca = PCA(n_components=3) #选择降维数量
pca = pca.fit(data) #建模
data2_pca = pca.transform(data)

x1,y1,z1 = [],[],[]
for i in range(0,4):
    x1.append(data2_pca[i][0])
    y1.append(data2_pca[i][1])
    z1.append(data2_pca[i][2])
    
x2,y2,z2 = [],[],[]
for i in range(4,8):
    x2.append(data2_pca[i][0])
    y2.append(data2_pca[i][1])
    z2.append(data2_pca[i][2])


plt.rcParams['font.size'] = 30
plt.rcParams['font.sans-serif'] = ['Arial']
fontt={'color': 'k',
      'size': 30,
      'family': 'Arial'}
plt.figure(figsize= (10, 10))
ax3d = plt.gca(projection="3d")  # 创建三维坐标
#plt.title('3D Scatter', fontsize=20)
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
#ax3d.view_init(20, 0)
#plt.tick_params(labelsize=30)
ax3d.scatter(x1, y1, z1, s=150, color="#DC143C", marker="o")
ax3d.scatter(x2, y2, z2, s=150, color="#9400D3", marker="o")
ax3d.legend(['ES/C','MS/C'], loc=(1,1))
#ax3d.set_xlabel("X axis", fontdict=fontt)
#ax3d.set_ylabel("Y axis", fontdict=fontt)
#ax3d.set_zlabel("Z axis", fontdict=fontt)
#ax3d.scatter(x4, y4, z4, s=50, color="red", marker="o")
plt.tick_params(width=2,length=4,color='k')    
#ax = plt.gca()
#ax.spines['bottom'].set_linewidth('2')
#ax.spines['bottom'].set_color('k')
#ax.spines['top'].set_linewidth('2')
#ax.spines['top'].set_color('k')
#ax.spines['left'].set_linewidth('2')
#ax.spines['left'].set_color('k')
#ax.spines['right'].set_linewidth('2')
#ax.spines['right'].set_color('k')
#plt.yticks(fontproperties = 'Arial', size = 25)
#plt.xticks(fontproperties = 'Arial', size = 25)

plt.show()

# C ES MS GDM
data = pd.read_excel('E:\\sirebrowser\\泪液标志物\\泪液蛋白整理.xlsx',sheet_name='Sheet2')
data = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)

pca = PCA(n_components=3) #选择降维数量
pca = pca.fit(data) #建模
data2_pca = pca.transform(data)

x1,y1,z1 = [],[],[]
for i in range(0,4):
    x1.append(data2_pca[i][0])
    y1.append(data2_pca[i][1])
    z1.append(data2_pca[i][2])
    
x2,y2,z2 = [],[],[]
for i in range(4,8):
    x2.append(data2_pca[i][0])
    y2.append(data2_pca[i][1])
    z2.append(data2_pca[i][2])

x3,y3,z3 = [],[],[]
for i in range(8,12):
    x3.append(data2_pca[i][0])
    y3.append(data2_pca[i][1])
    z3.append(data2_pca[i][2])

x4,y4,z4 = [],[],[]
for i in range(12,16):
    x4.append(data2_pca[i][0])
    y4.append(data2_pca[i][1])
    z4.append(data2_pca[i][2])
plt.rcParams['font.size'] = 0
plt.rcParams['font.sans-serif'] = ['Arial']
fontt={'color': 'k',
      'size': 30,
      'family': 'Arial'}
plt.figure(figsize= (10, 10))
ax3d = plt.gca(projection="3d")  # 创建三维坐标
#plt.title('3D Scatter', fontsize=20)
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
ax3d.view_init(10, 115)
#plt.tick_params(labelsize=30)
ax3d.scatter(x1, y1, z1, s=150, color="#00FF7F", marker="o")
ax3d.scatter(x2, y2, z2, s=150, color="#6495ED", marker="o")
ax3d.scatter(x3, y3, z3, s=150, color="#DC143C", marker="o")
ax3d.scatter(x4, y4, z4, s=150, color="#9400D3", marker="o")

ax3d.legend(['C','ES/C','MS/C','GDM/C'], loc=(1,1))
#ax3d.set_xlabel("X axis", fontdict=fontt)
#ax3d.set_ylabel("Y axis", fontdict=fontt)
#ax3d.set_zlabel("Z axis", fontdict=fontt)
#ax3d.scatter(x4, y4, z4, s=50, color="red", marker="o")
plt.tick_params(width=2,length=4,color='k')    
#ax = plt.gca()
#ax.spines['bottom'].set_linewidth('2')
#ax.spines['bottom'].set_color('k')
#ax.spines['top'].set_linewidth('2')
#ax.spines['top'].set_color('k')
#ax.spines['left'].set_linewidth('2')
#ax.spines['left'].set_color('k')
#ax.spines['right'].set_linewidth('2')
#ax.spines['right'].set_color('k')
#plt.yticks(fontproperties = 'Arial', size = 25)
#plt.xticks(fontproperties = 'Arial', size = 25)

plt.show()