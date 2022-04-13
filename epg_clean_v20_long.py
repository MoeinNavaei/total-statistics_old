#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:32:45 2020

@author: rastegar
"""

########################import package#####################
########################import package#####################
import pandas as pd
import numpy as np
import statistics 
from statistics import mode
#from sklearn import tree
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.svm import SVC
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score
import json
from ast import literal_eval
import difflib
#import nltk
import math
from collections import defaultdict  # For word frequency
from sklearn.feature_extraction.text import CountVectorizer
import itertools
#################################read form excell  #############################
#for i in list(range(24)):
   
 #   ch=i
  
#print(ch)  
 
iii = 0
aaa = 1
# for iii in range(0, 10, 1)
 
#while aaa < 13:

# ch=aaa

vahid = 1    
for vahid in range(25):
#     vahid = 13
    print("number of chanel", vahid)
    
    ch= vahid
    
    path  =r'C:\Users\PC\Desktop\new power bi\append\modify\modify_25-32\sarasari\in\{}.xlsx'.format(ch)
    path2 = r'C:\Users\PC\Desktop\new power bi\append\modify\modify_25-32\sarasari\out\{}.xlsx'.format(ch)

#path  = r'C:\Users\PC\Desktop\new power bi\append\khordad_99_02\khordad\Ekhtesasi\in\{}.xlsx'.format(ch)
#path2 = r'C:\Users\PC\Desktop\new power bi\append\khordad_99_02\khordad\Ekhtesasi\out\{}.xlsx'.format(ch)

#path= r'C:\Users\PC\Desktop\new power bi\append\khordad_99_02\khordad\sarasari_in\2.xlsx'
#path2= r'C:\Users\PC\Desktop\new power bi\append\khordad_99_02\khordad\sarasari_out\2.xlsx'
#    print(aaa)
 
# aaa +=1
#path  ='~/Documents/new/25-26/in/4.xlsx'
#path2 = '~/Documents/new/25-26/out/4.xlsx'
    input0= pd.read_excel (path)

    input0.reset_index()
#del input0['Unnamed: 0']
    input1=pd.DataFrame()

    input1['نام برنامه']=list(itertools.chain(*input0.iloc[:, [1]].values.tolist()))
    input1['نام برنامه']=input1['نام برنامه'].apply(str)
#input1=input0.iloc[:, [1]]
#print(input1)
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('فیلم سینمایی','سینمایی')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('سینمایی-','سینمایی  ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('سینمایی -','سینمایی  ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('سریال','مجموعه')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('قرائت','تلاوت')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('nan','')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('«',' ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('»',' ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('"',' ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('\\',' ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('ؤ','و')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('ادامه',' ')
    input1['نام برنامه'] = input1['نام برنامه'].str.replace('پشت صحنه',' ')
#input1['نام برنامه'] = input1['نام برنامه'].str.replace('خلاصه',' ')


    input2=input1.values.tolist()
#print(input2)
    Flat_list = list(itertools.chain(*input2))
    input3=Flat_list
#print(input3)
#print(len(input))
###################################pivoting process########
    lable_list=[]
    output_intersect_2=[]
    output_vag_2=[]
    output_BoW_2=[]
    similarity_vec_2=[]
    tag_list=[]
    for c in range(len(input3)): 
       lable_list.append([])
       output_intersect_2.append([])
       output_vag_2.append([])
       output_BoW_2.append([])
       similarity_vec_2.append([])
       tag_list.append([])

#####################labling processs ########################
    for i in range(len(input3)):
        print(i)
        for j in range(len(input3)):
            if(input3[i]==input3[j]):
                lable_list[i]=i
                lable_list[j]=i
            else:
                lable_list[i]=i

#print(lable_list)            

    input=input_remove_duplicate=list(dict.fromkeys(input3)) 
    lable_list_remove_duplicate=list(dict.fromkeys(lable_list))

#print(input_remove_duplicate)
####################################### Definition ##################################
    vector=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#print(len(vector))
#for c in  range(100): 
#    vector_BoW.append(0)
    output_1=pd.DataFrame()
    vec=pd.DataFrame()
    error_finding=pd.DataFrame()
    similarity_vec=[]
    return_name=[]
    super_vec = [] 
    super_list_BoW = []
    super_vec_list_BoW=[]
    vector_BoW=[]
    vector_BoW_1=[]
    output_vag=[]
    output_vag_1=[]
    output_BoW=[]
    similarity_vec_BoW=[]
    return_name_BoW=[]
    intersect_BoW=[]

    for c in range(len(input)): # create a list with nested lists
        super_vec .append([])
        similarity_vec.append([])
        similarity_vec_BoW.append([])
        return_name.append([])
        super_vec_list_BoW.append([])
        output_vag.append([])
        output_vag_1.append([])
        output_BoW.append([])
        return_name_BoW.append([])
#################################
    df0=pd.DataFrame()
    df0['name0']=input

    df0['name0'] = df0['name0'].apply(lambda x: x.split('(')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('-')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('(')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('(')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('-')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('،')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('قسمت')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('فصل')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('شبکه')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('_')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('/')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('گزیده')[0])
    df0['name0'] = df0['name0'].apply(lambda x: x.split('خلاصه')[0])
#df0['name0'] = df0['name0'].str.replace('خلاصه',' ')
#df0['name0'] = df0['name0'].str.replace('گزیده',' ')
    df0['name0'] = df0['name0'].str.replace('ادامه',' ')
    df0['name0'] = df0['name0'].str.replace('برنامه',' ')
    df0['name0'] = df0['name0'].str.replace('مجموعه',' ')

   
    
#df0['name0'] = df0['name0'].apply(lambda x: x.split('خلاصه')[0])
    input4=list(itertools.chain(*df0.values.tolist())) 
#print(input4)   
####################################### LETTER VECTORIZATION PROCESS##################################################
    p=['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ئ','ی', '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#print(len(p))   
    d=0   
    for a in input4:
        b=list(str(a))
#    print(b)/
    
        k=0     
        for j in p:
            for i in b:
                if (i==j):
                    vector[k]=b.count(i)
            k=k+1       
    #print(vector)
        super_vec[d]=vector
        d=d+1
        vector=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#print('super_vec')
#print(super_vec[0])
#print(len(super_vec[0]))
###########################################################################################
########################## similarity function #######################################    
    def cosine_similarity(f,g):
        "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
        sumxx, sumxy, sumyy = 0, 0, 0
        for e in range(len(f)):
            x = f[e]; y = g[e]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return math.acos(sumxy/math.sqrt(sumxx*sumyy))
    
##################################################################
    def sum_mul(f,g):
        sumxx = 0 
        for e in range(len(f)):
            x = f[e]; y = g[e]
            sumxx += x*y
        return sumxx
#############################length defference detection##################
    def diff_length(f,g):
        sumx=0
        sumy=0
        sumx_y=0
        for e in range(len(f)):
            sumx+=f[e]
            sumy+=g[e]
            sumx_y=sumx-sumy    
        return math.sqrt(sumx_y*sumx_y)
#############################vector length detection######
    def vector_length(f):
        sumx=0
        for e in range(len(f)):
            sumx+=f[e]
        return sumx 
###################################### intersection function ##############

    def get_intersection(s1, s2): 
        res = ''
        l_s1 = len(s1)
        for t in range(l_s1):
            for u in range(t + 1, l_s1):
                q = s1[t:u]
                if q in s2 and len(q) > len(res):
                    res = q
        return res
###################################### diff_leter_lenght detection #######################################
    def diff_leter_lenght(f,g):
        intersect_letter_len=len(list(set(f) & set(g)))
        union_letter_len=len(list(set(f)|set(g)))
        non_intersect_letter = intersect_letter_len-union_letter_len
        return math.sqrt(non_intersect_letter*non_intersect_letter)

############################ SIMILARITY DETECTION for vag and replacment #############

    for f in  range(len(super_vec)):
        for g in range(0,len(super_vec)):
            try:
                similarity=cosine_similarity(super_vec[f],super_vec[g])
            except:
                similarity=1.5

            similarity_vec[f].append(similarity)
            diff_length_1=diff_length(super_vec[f],super_vec[g])
            vector_length_1=vector_length(super_vec[f])
            diff_leter_lenght_1=diff_leter_lenght(input4[f],input4[g])  
        
            if(diff_length_1<2):
                if (diff_leter_lenght_1<3):
                    if(vector_length_1==5):
                        if (similarity <0.65):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])
                    if(vector_length_1==6):
                        if (similarity <0.59):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])
                    if(vector_length_1==7):
                        if (similarity <0.55):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])
                    if(vector_length_1==8):
                        if (similarity <0.51):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])
                    if(vector_length_1==9):
                        if (similarity <0.48):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])
                    if(vector_length_1==10): 
                        if (similarity <0.46):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g]) 
                    if(vector_length_1==11):
                        if (similarity <0.43):
                            if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                #output_vag[g]=input[f]
                                return_name[f].append(input[g])    
                    else:
                        if (similarity <0.3):
                            if(vector_length_1!=5,6,7,8,9,10,11):
                                if(len(get_intersection('aa' + input[f] + 'bb', 'cc' + input[g] + 'dd'))>2):
                                    #output_vag[g]=input[f]
                                    return_name[f].append(input[g])
       
        print(f)
#print(return_name)
    for i in range(len(return_name)):
        try:
            output_vag[i]= min(return_name[i], key = lambda x: len(x))
        except:
            output_vag[i]=input[i]   
 ###############################BAG OF WORD VECTORIZATION PROCESS#####################################

    for i in output_vag:
        tokens=str.split(str(i))
        intersect_BoW.append(i)
    #super_list_BoW.append(tokens)
       
#print('intersect_BoW')
#print(intersect_BoW)
    df=pd.DataFrame()
    df['name']=output_vag
    df['name'] = df['name'].apply(lambda x: x.split('(')[0])
    df['name'] = df['name'].apply(lambda x: x.split('-')[0])
    df['name'] = df['name'].apply(lambda x: x.split('(')[0])
    df['name'] = df['name'].apply(lambda x: x.split('(')[0])
    df['name'] = df['name'].apply(lambda x: x.split('-')[0])
    df['name'] = df['name'].apply(lambda x: x.split('قسمت')[0])
    df['name'] = df['name'].apply(lambda x: x.split('فصل')[0])
    df['name'] = df['name'].apply(lambda x: x.split('شبکه')[0])
    df['name'] = df['name'].apply(lambda x: x.split('_')[0])
    df['name'] = df['name'].apply(lambda x: x.split('؛')[0])
    df['name'] = df['name'].apply(lambda x: x.split('گزیده')[0])
    df['name'] = df['name'].apply(lambda x: x.split('خلاصه')[0])
    output_vag_1=list(itertools.chain(*df.values.tolist()))

    for i in output_vag_1:
        tokens=str.split(str(i))
    #intersect_BoW.append(i)
        super_list_BoW.append(tokens)
    BW=list(itertools.chain(*super_list_BoW))

    BW_remove_duplicates=list(dict.fromkeys(BW))
    remove_list=['برنامه','مستند','مسابقه','شبکه','سریال ','مجموعه','برنامه‌های','الفیلم','فیلم','السینمایی','سینمایی','موشن گرافیک','اخبار','زنده','بازپخش','خلاصه','هفتگی','قسمت','پخش','باز','قسمتهای','و','ادامه','ها','های']
    for i in remove_list:
        try:
            BW_remove_duplicates.remove(i)
        except:
            pass    
#BW_remove_duplicates.remove('شبکه')
#print(BW_remove_duplicates)

    for c in  range(len(BW_remove_duplicates)): 
        vector_BoW.append(0)
        vector_BoW_1.append(0)

    d=0   
    for caption in super_list_BoW:
   #print(caption)

       k=0     
       for j in BW_remove_duplicates :
       #print(j)
           for z in caption:
            #print(z)
                if (z==j):
               #print(z)
                   vector_BoW[k]=caption.count(z)
           k=k+1   
       super_vec_list_BoW[d]=vector_BoW
       super_vec_list_BoW[d]=np.array(super_vec_list_BoW[d])
       d=d+1
       vector_BoW = (np.array(vector_BoW_1))*(np.array(vector_BoW))# reset vector_BoW

#print('super_vec_list_BoW')
#print(super_vec_list_BoW)
#print(super_vec_list_BoW[299])
#print(len(super_vec_list_BoW[0]))
#################################### Intersection Function #####################################
#def intersection(lst1, lst2): 
#    return list(set(lst1) & set(alalamlst2)) 
###############################################################
#def intersection(lst1, lst2): 
#    return set(lst1).intersection(set(lst2))
################################################################

#print(output_vag)
###########################################################################
#print(intersection((super_list_BoW[3]),(super_list_BoW[4]))) 
#print(intersect_BoW)          

########################### SIMILARITY DETECTION for BoW and replacment #############
    h=0
    for f in range(0,len(super_vec_list_BoW)):
        for g in range(0,len(super_vec_list_BoW)):
            try:
                simillarity2 =cosine_similarity(super_vec_list_BoW[f],super_vec_list_BoW[g])
            except:
                simillarity2=1.501
            similarity_vec_BoW[h].append(simillarity2)
            if (simillarity2<.85):
                if(simillarity2!=0.7853981633974484):
                    output_BoW[g]=output_vag[f]
            #intersect_BoW[g]= intersection(intersect_BoW[f],intersect_BoW[g])
            #intersect_BoW[g]=intersect_BoW[f]= set(intersect_BoW[f]).intersection(set(intersect_BoW[g]))
                    if(len(get_intersection('aa' + intersect_BoW[f] + 'bb', 'cc' + intersect_BoW[g] + 'dd'))>3):
                    #intersect_BoW[f]=get_intersection('aa' + intersect_BoW[f] + 'bb', 'cc' + intersect_BoW[g] + 'dd') 
                    #intersect_BoW[g]=get_intersection('aa' + intersect_BoW[f] + 'bb', 'cc' + intersect_BoW[g] + 'dd') 
                        if(len(intersect_BoW[f])>len(intersect_BoW[g])):
                            intersect_BoW[f]=intersect_BoW[g]
                        else:
                            intersect_BoW[g]=intersect_BoW[f]

        h=h+1
        print(f)

#print(intersect_BoW)
#print(similarity_vec_BoW[0]
#print(intersect_BoW_1)

    df2=pd.DataFrame()
    df2['name1']=intersect_BoW
    df2['name1'] = df2['name1'].apply(lambda x: x.split('(')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('-')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('(')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('(')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('-')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('قسمت')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('فصل')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('شبکه')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('نیمه دوم')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('نیمه اول')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('/')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('_')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split(':')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('خلاصه')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('گزیده')[0])
#df2['name1'] = df2['name1'].str.replace('خلاصه',' ')
#df2['name1'] = df2['name1'].str.replace('گزیده',' ')

#df2['name'] = df2['name'].apply(lambda x: x.split('خلاصه')[0])
    df2['name1'] = df2['name1'].apply(lambda x: x.split('؛')[0])
    intersect_BoW_1=list(itertools.chain(*df2.values.tolist()))
    for i in range(len(intersect_BoW_1)):
        if(len(intersect_BoW_1[i])<1):
            intersect_BoW_1[i]=intersect_BoW[i]

    df3=pd.DataFrame()
    df3['name2']=intersect_BoW_1
    df3['name2'] = df3['name2'].str.replace('خلاصه',' ')
    df3['name2'] = df3['name2'].str.replace('گزیده',' ')

    intersect_BoW_1=list(itertools.chain(*df3.values.tolist()))


###################################################return process ##################
    for i in range(len(lable_list_remove_duplicate)):
        for j in range(len(lable_list)):
            if(lable_list_remove_duplicate[i]==lable_list[j]):
                output_intersect_2[j]=intersect_BoW_1[i]
                output_vag_2[j]=output_vag[i]
                output_BoW_2[j]=output_BoW[i]
            #similarity_vec_2[j] = similarity_vec_BoW[i]
#print(output_intersect_2)
#print(similarity_vec_BoW[3])
##############################

########################### GROUP SIMILAR WORD for BoW ##########
#n=0
#for m in similarity_vec_BoW:
#    for l in range(len(output_vag)):
##        print(l)3
#        if (m[l] < 1.25):
#            return_name_BoW[n].append(output_vag[l])
##            print(input[l])
#    n=n+1       
#print(return_name_BoW)
#
#return_name_BoW_1=return_name_BoW
#angle_in_radians = math.acos(cos_sim)output_BoW_dataframe.to_excel('~/Documents/output_BoW_dataframe.xlsx')
##############################replacement process for BoW ########################################
#n=0
#for m in similarity_vec_BoW:
#    for l in range(len(output_vag)):
#        print(l)
#        if (m[l] <1.25):
#            output_BoW[l]=output_vag[n]
#            print(input[l])vagoutput_vag_intersec
#   n=n+1
#    print(n)
#####################################TAG ###################################################################
    input0_tag=input0.iloc[:,[1]].values.tolist()
    input0_tag_Flat_list = list(itertools.chain(*input0_tag))
    #print(input0_tag_Flat_list)
    for i in range(len(input0_tag_Flat_list)):

        if(input0_tag_Flat_list[i]==output_intersect_2[i]):
            tag_list[i]=0
        else:
            tag_list[i]=1


#########################################

#output_BoW_dataframe=pd.DataFrame(output_BoW)
    output_1['نام شبکه']=list(itertools.chain(*input0.iloc[:,[0]].values.tolist()))

    output_1['نام برنامه اولیه']=list(itertools.chain(*input0.iloc[:,[1]].values.tolist()))
    #output_1[' output_vag_2']= output_vag_2
#output_1['output_BoW_2']=output_BoW_2
    output_1['نام برنامه']=output_intersect_2
    output_1['تاریخ شروع']=input0.iloc[:,[2]]
    output_1['تاریخ پایان']=input0.iloc[:,[3]]
    output_1['مدت بازدید']=list(itertools.chain(*input0.iloc[:,[4]].values.tolist()))
    output_1['تعداد بازدید']=list(itertools.chain(*input0.iloc[:,[5]].values.tolist()))
    output_1['میانگین']=list(itertools.chain(*input0.iloc[:,[6]].values.tolist()))
    output_1['اپراتور']=list(itertools.chain(*input0.iloc[:,[7]].values.tolist()))
    output_1['ساعت']=list(itertools.chain(*input0.iloc[:,[8]].values.tolist()))
    output_1['تاریخ']=list(itertools.chain(*input0.iloc[:,[9]].values.tolist()))
    output_1['ردیف']=list(itertools.chain(*input0.iloc[:,[10]].values.tolist()))
    output_1['جنس']=list(itertools.chain(*input0.iloc[:,[11]].values.tolist()))
    output_1['tag']=tag_list

#output_1['similarity_vec_2']=similarity_vec_2[0]

    output_1.to_excel(path2, index=False) 
    error_finding['input']=input
    error_finding['output_vag']=output_vag
    error_finding['return_name']=return_name
    error_finding['output_BoW']=output_BoW
    error_finding['intersect_BoW']=intersect_BoW
#error_finding['similarity_vec']=similarity_vec[250]
#error_finding['similarity_vec_BoW']=similarity_vec_BoW[355]
#error_finding['similarity_vec_BoW']=similarity_vec_BoW[1]
#error_finding.to_excel('~/Documents/error_ch2.xlsx')
    print('finished')
#output_1['similarity_vec']=similarity_vec[268]
#vec['BW_remove_duplicates']=BW_remove_duplicates
#vec.to_excel('~/Documents/vec.xlsx')      
#output_vag_dataframe=pd.DataFrame(output_vag)
#output_vag_dataframe.to_excel('~/Documents/output_vag_dataframe.xlsx')
#output_BoW_dataframe.to_excel('~/Documents/output_BoW_dataframe.xlsx')
