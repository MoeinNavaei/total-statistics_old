import xlsxwriter  
import pandas as pd
#from pandas imPRrt DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib as mpl
import matplotlib.ticker as tkr
import numpy as np
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D

workbook_sar = xlsxwriter.Workbook('EPG Radio.xlsx')
df_radio = pd.read_excel (r'C:\Users\PC\Desktop\total statistics\radio-tir99.xlsx', sheet_name='radio_tir_99')

worksheet_sar = workbook_sar.add_worksheet() 
 
format1 = workbook_sar.add_format({'num_format': '#,##', 'bold':True, 'font_color':'green', 'size':14, 'font_name':'B Nazanin'})
                                   
worksheet_sar.set_column('A:EZ', 12, format1)

R_eghtesad=pd.DataFrame()
R_ava=pd.DataFrame()
R_iran=pd.DataFrame()
R_payam=pd.DataFrame()
R_javan=pd.DataFrame()
R_salamat=pd.DataFrame()
R_saba=pd.DataFrame()
R_farhang=pd.DataFrame()
R_qoran=pd.DataFrame()
R_goftego=pd.DataFrame()
R_maaref=pd.DataFrame()
R_namayesh=pd.DataFrame()
R_varzesh=pd.DataFrame()

PR1=0
PR2=0
PR3=0
PR4=0
PR5=0
PR6=0
PR7=0
PR8=0
PR9=0
PR10=0
PR11=0
PR12=0
PR13=0

#df_radio=df_radio.drop(columns=['جنس','ردیف','میانگین','نام برنامه اولیه'])

df_R_sum=df_radio.groupby(['نام برنامه','نام شبکه']).sum().reset_index()
t=len(df_R_sum)
for i in range(0,t):
    f=df_R_sum.loc[i,'نام شبکه']
    
#####################################################################
######################### channels data sarasari #############################
#####################################################################

############################# شبکه 1 #################################
    if f=='رادیو اقتصاد':
        PR1=PR1+1  
        R_eghtesad.loc[PR1,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_eghtesad.loc[PR1,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_eghtesad.loc[PR1,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه 2 #################################
    if f=='رادیو آوا': 
        PR2=PR2+1 
        R_ava.loc[PR2,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_ava.loc[PR2,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_ava.loc[PR2,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه 3 #################################
    if f=='رادیو ایران':
        PR3=PR3+1  
        R_iran.loc[PR3,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_iran.loc[PR3,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_iran.loc[PR3,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه 4 #################################
    if f=='رادیو پیام': 
        PR4=PR4+1 
        R_payam.loc[PR4,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_payam.loc[PR4,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_payam.loc[PR4,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه 5 #################################
    if f=='رادیو جوان':
        PR5=PR5+1  
        R_javan.loc[PR5,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_javan.loc[PR5,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_javan.loc[PR5,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه خبر #################################
    if f=='رادیو سلامت': 
        PR6=PR6+1 
        R_salamat.loc[PR6,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_salamat.loc[PR6,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_salamat.loc[PR6,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه افق #################################
    if f=='رادیو صبا':
        PR7=PR7+1  
        R_saba.loc[PR7,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_saba.loc[PR7,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_saba.loc[PR7,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه پویا #################################
    if f=='رادیو فرهنگ':
        PR8=PR8+1 
        R_farhang.loc[PR8,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_farhang.loc[PR8,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_farhang.loc[PR8,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه امید #################################
    if f=='رادیو قرآن': 
        PR9=PR9+1  
        R_qoran.loc[PR9,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_qoran.loc[PR9,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_qoran.loc[PR9,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه آی فیلم #################################
    if f=='رادیو گفتگو':
        PR10=PR10+1 
        R_goftego.loc[PR10,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_goftego.loc[PR10,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_goftego.loc[PR10,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه نمایش #################################
    if f=='رادیو معارف': 
        PR11=PR11+1  
        R_maaref.loc[PR11,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_maaref.loc[PR11,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_maaref.loc[PR11,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
############################# شبکه تماشا #################################
    if f=='رادیو نمایش':
        PR12=PR12+1 
        R_namayesh.loc[PR12,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_namayesh.loc[PR12,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_namayesh.loc[PR12,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']

############################# شبکه مستند #################################
    if f=='رادیو ورزش': 
        PR13=PR13+1  
        R_varzesh.loc[PR13,'نام برنامه']=df_R_sum.loc[i,'نام برنامه']
        R_varzesh.loc[PR13,'تعداد بازدید']=df_R_sum.loc[i,'تعداد بازدید']
        R_varzesh.loc[PR13,'مدت بازدید']=df_R_sum.loc[i,'مدت بازدید']
  
############################# شبکه 1 #################################
R_eghtesad1=[]
R_eghtesad2=[]
R_eghtesad3=[]
R_eghtesad4=[]
R_eghtesad5=[]
R_eghtesad.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_eghtesad1=R_eghtesad["نام برنامه"].tolist()
R_eghtesad5.append(R_eghtesad1)
R_eghtesad2=R_eghtesad["تعداد بازدید"].tolist()
R_eghtesad5.append(R_eghtesad2)
R_eghtesad.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_eghtesad3=R_eghtesad["نام برنامه"].tolist()
R_eghtesad5.append(R_eghtesad3)
R_eghtesad4=R_eghtesad["مدت بازدید"].tolist()
R_eghtesad5.append(R_eghtesad4)
############################# شبکه 2 #################################
R_ava1=[]
R_ava2=[]
R_ava3=[]
R_ava4=[]
R_ava5=[]
R_ava.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_ava1=R_ava["نام برنامه"].tolist()
R_ava5.append(R_ava1)
R_ava2=R_ava["تعداد بازدید"].tolist()
R_ava5.append(R_ava2)
R_ava.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_ava3=R_ava["نام برنامه"].tolist()
R_ava5.append(R_ava3)
R_ava4=R_ava["مدت بازدید"].tolist()
R_ava5.append(R_ava4)
############################# شبکه 3 #################################
R_iran1=[]
R_iran2=[]
R_iran3=[]
R_iran4=[]
R_iran5=[]
R_iran.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_iran1=R_iran["نام برنامه"].tolist()
R_iran5.append(R_iran1)
R_iran2=R_iran["تعداد بازدید"].tolist()
R_iran5.append(R_iran2)
R_iran.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_iran3=R_iran["نام برنامه"].tolist()
R_iran5.append(R_iran3)
R_iran4=R_iran["مدت بازدید"].tolist()
R_iran5.append(R_iran4)
############################# شبکه 4 #################################
R_payam1=[]
R_payam2=[]
R_payam3=[]
R_payam4=[]
R_payam5=[]
R_payam.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_payam1=R_payam["نام برنامه"].tolist()
R_payam5.append(R_payam1)
R_payam2=R_payam["تعداد بازدید"].tolist()
R_payam5.append(R_payam2)
R_payam.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_payam3=R_payam["نام برنامه"].tolist()
R_payam5.append(R_payam3)
R_payam4=R_payam["مدت بازدید"].tolist()
R_payam5.append(R_payam4)
############################# شبکه 5 #################################
R_javan1=[]
R_javan2=[]
R_javan3=[]
R_javan4=[]
R_javan5=[]
R_javan.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_javan1=R_javan["نام برنامه"].tolist()
R_javan5.append(R_javan1)
R_javan2=R_javan["تعداد بازدید"].tolist()
R_javan5.append(R_javan2)
R_javan.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_javan3=R_javan["نام برنامه"].tolist()
R_javan5.append(R_javan3)
R_javan4=R_javan["مدت بازدید"].tolist()
R_javan5.append(R_javan4)
############################# شبکه خبر #################################
R_salamat1=[]
R_salamat2=[]
R_salamat3=[]
R_salamat4=[]
R_salamat5=[]
R_salamat.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_salamat1=R_salamat["نام برنامه"].tolist()
R_salamat5.append(R_salamat1)
R_salamat2=R_salamat["تعداد بازدید"].tolist()
R_salamat5.append(R_salamat2)
R_salamat.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_salamat3=R_salamat["نام برنامه"].tolist()
R_salamat5.append(R_salamat3)
R_salamat4=R_salamat["مدت بازدید"].tolist()
R_salamat5.append(R_salamat4)
############################# شبکه افق #################################
R_saba1=[]
R_saba2=[]
R_saba3=[]
R_saba4=[]
R_saba5=[]
R_saba.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_saba1=R_saba["نام برنامه"].tolist()
R_saba5.append(R_saba1)
R_saba2=R_saba["تعداد بازدید"].tolist()
R_saba5.append(R_saba2)
R_saba.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_saba3=R_saba["نام برنامه"].tolist()
R_saba5.append(R_saba3)
R_saba4=R_saba["مدت بازدید"].tolist()
R_saba5.append(R_saba4)
############################# شبکه پویا #################################
R_farhang1=[]
R_farhang2=[]
R_farhang3=[]
R_farhang4=[]
R_farhang5=[]
R_farhang.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_farhang1=R_farhang["نام برنامه"].tolist()
R_farhang5.append(R_farhang1)
R_farhang2=R_farhang["تعداد بازدید"].tolist()
R_farhang5.append(R_farhang2)
R_farhang.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_farhang3=R_farhang["نام برنامه"].tolist()
R_farhang5.append(R_farhang3)
R_farhang4=R_farhang["مدت بازدید"].tolist()
R_farhang5.append(R_farhang4)
############################# شبکه امید #################################
R_qoran1=[]
R_qoran2=[]
R_qoran3=[]
R_qoran4=[]
R_qoran5=[]
R_qoran.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_qoran1=R_qoran["نام برنامه"].tolist()
R_qoran5.append(R_qoran1)
R_qoran2=R_qoran["تعداد بازدید"].tolist()
R_qoran5.append(R_qoran2)
R_qoran.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_qoran3=R_qoran["نام برنامه"].tolist()
R_qoran5.append(R_qoran3)
R_qoran4=R_qoran["مدت بازدید"].tolist()
R_qoran5.append(R_qoran4)
############################# شبکه آی فیلم #################################
R_goftego1=[]
R_goftego2=[]
R_goftego3=[]
R_goftego4=[]
R_goftego5=[]
R_goftego.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_goftego1=R_goftego["نام برنامه"].tolist()
R_goftego5.append(R_goftego1)
R_goftego2=R_goftego["تعداد بازدید"].tolist()
R_goftego5.append(R_goftego2)
R_goftego.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_goftego3=R_goftego["نام برنامه"].tolist()
R_goftego5.append(R_goftego3)
R_goftego4=R_goftego["مدت بازدید"].tolist()
R_goftego5.append(R_goftego4)
############################# شبکه نمایش #################################
R_maaref1=[]
R_maaref2=[]
R_maaref3=[]
R_maaref4=[]
R_maaref5=[]
R_maaref.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_maaref1=R_maaref["نام برنامه"].tolist()
R_maaref5.append(R_maaref1)
R_maaref2=R_maaref["تعداد بازدید"].tolist()
R_maaref5.append(R_maaref2)
R_maaref.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_maaref3=R_maaref["نام برنامه"].tolist()
R_maaref5.append(R_maaref3)
R_maaref4=R_maaref["مدت بازدید"].tolist()
R_maaref5.append(R_maaref4)
############################# شبکه تماشا #################################
R_namayesh1=[]
R_namayesh2=[]
R_namayesh3=[]
R_namayesh4=[]
R_namayesh5=[]
R_namayesh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_namayesh1=R_namayesh["نام برنامه"].tolist()
R_namayesh5.append(R_namayesh1)
R_namayesh2=R_namayesh["تعداد بازدید"].tolist()
R_namayesh5.append(R_namayesh2)
R_namayesh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_namayesh3=R_namayesh["نام برنامه"].tolist()
R_namayesh5.append(R_namayesh3)
R_namayesh4=R_namayesh["مدت بازدید"].tolist()
R_namayesh5.append(R_namayesh4)
############################# شبکه مستند #################################
R_varzesh1=[]
R_varzesh2=[]
R_varzesh3=[]
R_varzesh4=[]
R_varzesh5=[]
R_varzesh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_varzesh1=R_varzesh["نام برنامه"].tolist()
R_varzesh5.append(R_varzesh1)
R_varzesh2=R_varzesh["تعداد بازدید"].tolist()
R_varzesh5.append(R_varzesh2)
R_varzesh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
R_varzesh3=R_varzesh["نام برنامه"].tolist()
R_varzesh5.append(R_varzesh3)
R_varzesh4=R_varzesh["مدت بازدید"].tolist()
R_varzesh5.append(R_varzesh4)

#####################################################################

bold = workbook_sar.add_format({'bold': 1})  
headings = ['اقتصاد بازدید', 'تعداد بازدید اقتصاد','اقتصاد (زمان)', 'زمان بازدید اقتصاد'
            ,'آوا بازدید', 'تعداد بازدید آوا','آوا (زمان)', 'زمان بازدید آوا',
            'ایران بازدید', 'تعداد بازدید ایران','ایران (زمان)', 'زمان بازدید ایران',
            'پیام بازدید', 'تعداد بازدید پیام','پیام (زمان)', 'زمان بازدید پیام',
            'جوان بازدید', 'تعداد بازدید جوان','جوان (زمان)', 'زمان بازدید جوان',
            'شبکه سلامت بازدید', 'تعداد بازدید شبکه سلامت','شبکه سلامت (زمان)', 'زمان بازدید شبکه سلامت',
            'شبکه صبا بازدید', 'تعداد بازدید شبکه صبا','شبکه صبا (زمان)', 'زمان بازدید شبکه صبا',
            'شبکه فرهنگ بازدید', 'تعداد بازدید شبکه فرهنگ','شبکه فرهنگ (زمان)', 'زمان بازدید شبکه فرهنگ',
            'شبکه قرآن بازدید', 'تعداد بازدید شبکه قرآن','شبکه قرآن (زمان)', 'زمان بازدید شبکه قرآن',
            'شبکه گفتگو بازدید', 'تعداد بازدید شبکه گفتگو','شبکه گفتگو (زمان)', 'زمان بازدید شبکه گفتگو',
            'شبکه معارف بازدید', 'تعداد بازدید شبکه معارف','شبکه معارف (زمان)', 'زمان بازدید شبکه معارف',
            'شبکه نمایش بازدید', 'تعداد بازدید شبکه نمایش','شبکه نمایش (زمان)', 'زمان بازدید شبکه نمایش',
            'شبکه ورزش بازدید', 'تعداد بازدید شبکه ورزش','شبکه ورزش (زمان)', 'زمان بازدید شبکه ورزش']       
worksheet_sar.write_row('A1', headings)  

######################### write columns #############################
#####################################################################

############################# شبکه 1 #################################
worksheet_sar.write_column('A2', R_eghtesad5[0])  
worksheet_sar.write_column('B2', R_eghtesad5[1]) 
worksheet_sar.write_column('C2', R_eghtesad5[2])  
worksheet_sar.write_column('D2', R_eghtesad5[3]) 
############################# آذربایجان غربی #################################
worksheet_sar.write_column('E2', R_ava5[0])  
worksheet_sar.write_column('F2', R_ava5[1]) 
worksheet_sar.write_column('G2', R_ava5[2])  
worksheet_sar.write_column('H2', R_ava5[3]) 
############################# شبکه 3 #################################
worksheet_sar.write_column('I2', R_iran5[0])  
worksheet_sar.write_column('J2', R_iran5[1]) 
worksheet_sar.write_column('K2', R_iran5[2])  
worksheet_sar.write_column('L2', R_iran5[3]) 
############################# شبکه 4 #################################
worksheet_sar.write_column('M2', R_payam5[0])  
worksheet_sar.write_column('N2', R_payam5[1]) 
worksheet_sar.write_column('O2', R_payam5[2])  
worksheet_sar.write_column('P2', R_payam5[3]) 
############################# شبکه 5 #################################
worksheet_sar.write_column('Q2', R_javan5[0])  
worksheet_sar.write_column('R2', R_javan5[1]) 
worksheet_sar.write_column('S2', R_javan5[2])  
worksheet_sar.write_column('T2', R_javan5[3]) 
############################# شبکه خبر #################################
worksheet_sar.write_column('U2', R_salamat5[0])  
worksheet_sar.write_column('V2', R_salamat5[1]) 
worksheet_sar.write_column('W2', R_salamat5[2])  
worksheet_sar.write_column('X2', R_salamat5[3]) 
############################# شبکه افق #################################
worksheet_sar.write_column('Y2', R_saba5[0])  
worksheet_sar.write_column('Z2', R_saba5[1]) 
worksheet_sar.write_column('AA2', R_saba5[2])  
worksheet_sar.write_column('AB2', R_saba5[3]) 
############################# شبکه پویا #################################
worksheet_sar.write_column('AC2', R_farhang5[0])  
worksheet_sar.write_column('AD2', R_farhang5[1]) 
worksheet_sar.write_column('AE2', R_farhang5[2])  
worksheet_sar.write_column('AF2', R_farhang5[3]) 
############################# شبکه امید #################################
worksheet_sar.write_column('AG2', R_qoran5[0])  
worksheet_sar.write_column('AH2', R_qoran5[1]) 
worksheet_sar.write_column('AI2', R_qoran5[2])  
worksheet_sar.write_column('AJ2', R_qoran5[3]) 
############################# شبکه آی فیلم #################################
worksheet_sar.write_column('AK2', R_goftego5[0])  
worksheet_sar.write_column('AL2', R_goftego5[1]) 
worksheet_sar.write_column('AM2', R_goftego5[2])  
worksheet_sar.write_column('AN2', R_goftego5[3]) 
############################# شبکه نمایش #################################
worksheet_sar.write_column('AO2', R_maaref5[0])  
worksheet_sar.write_column('AP2', R_maaref5[1]) 
worksheet_sar.write_column('AQ2', R_maaref5[2])  
worksheet_sar.write_column('AR2', R_maaref5[3]) 
############################# شبکه تماشا #################################
worksheet_sar.write_column('AS2', R_namayesh5[0])  
worksheet_sar.write_column('AT2', R_namayesh5[1]) 
worksheet_sar.write_column('AU2', R_namayesh5[2])  
worksheet_sar.write_column('AV2', R_namayesh5[3]) 
############################# شبکه مستند #################################
worksheet_sar.write_column('AW2', R_varzesh5[0])  
worksheet_sar.write_column('AX2', R_varzesh5[1]) 
worksheet_sar.write_column('AY2', R_varzesh5[2])  
worksheet_sar.write_column('AZ2', R_varzesh5[3]) 

workbook_sar.close()

df_radio_operator=df_radio.groupby(['اپراتور']).sum().reset_index()
radio_operators_visit={'operators_name': df_radio_operator['اپراتور'],
                       'operators_visit': df_radio_operator['تعداد بازدید']}
radio_operators_visit=pd.DataFrame(radio_operators_visit, columns=['operators_name', 'operators_visit'])
radio_operators_visit.sort_values('operators_visit', axis = 0, ascending = False, inplace = True, na_position ='last')
#####################################################################
df_radio_all_channels=df_radio.groupby(['نام شبکه']).sum().reset_index()
radio_channels_visit={'channels_names': df_radio_all_channels['نام شبکه'],
                      'channels_visit': df_radio_all_channels['تعداد بازدید']}
radio_channels_visit=pd.DataFrame(radio_channels_visit, columns=['channels_names', 'channels_visit'])
radio_channels_visit.sort_values('channels_visit', axis = 0, ascending = True, inplace = True, na_position ='last')
#####################################################################   
PRograms_all=df_radio.groupby(['نام برنامه']).sum().reset_index()
PRograms_alll=PRograms_all.sum(axis = 0, skipna = True)
PRograms_all_visits=PRograms_alll[1]
PRograms_all_duration=PRograms_alll[0]
PRograms_all_duration=round(PRograms_all_duration*60,0)
PRograms_all_contents=len(PRograms_all)
program_data={'parameters': ['visit', 'duration', 'content_number'],
              'parameters_count': [PRograms_all_visits, PRograms_all_duration, PRograms_all_contents]}
program_data=pd.DataFrame(program_data, columns=['parameters', 'parameters_count'])
#####################################################################     

def place_value(number):      # comma seperation
    return ("{:,}".format(number)) 
#####################################################################
font = {'family' : 'B Nazanin',
        'weight' : 'bold',
        'size'   : 22}

text_font = {'fontname':'B Nazanin', 'size':'12', 'color':'black', 'weight':'bold', 'verticalalignment':'center'}
num_font = {'fontname':'B Nazanin', 'size':'12', 'color':'black', 'weight':'bold', 'verticalalignment':'center','num_format': '#,##'}


Data_all_channels={'channels': [get_display(arabic_reshaper.reshape('اقتصاد')),get_display(arabic_reshaper.reshape('آوا')), 
                                get_display(arabic_reshaper.reshape('ایران')),get_display(arabic_reshaper.reshape('پیام')), 
                                get_display(arabic_reshaper.reshape('جوان')),get_display(arabic_reshaper.reshape('سلامت')), 
                                get_display(arabic_reshaper.reshape('صبا')),get_display(arabic_reshaper.reshape('فرهنگ')), 
                                get_display(arabic_reshaper.reshape('قرآن')),get_display(arabic_reshaper.reshape('گفتگو')), 
                                get_display(arabic_reshaper.reshape('معارف')),get_display(arabic_reshaper.reshape('نمایش')), 
                                get_display(arabic_reshaper.reshape('ورزش'))], 
                   'visits_channels': df_radio_all_channels['تعداد بازدید']}
############################################# شبکه یک #############################################
df_radio_barh_all_channels=pd.DataFrame(Data_all_channels, columns=['channels', 'visits_channels'])
############################################# شبکه یک #############################################
data_operators_visits={'operators':[get_display(arabic_reshaper.reshape('تیوا')), get_display(arabic_reshaper.reshape('لنز'))], 
                       'visits_operators':df_radio_operator['تعداد بازدید']}
df_radio_pie_operators=pd.DataFrame(data_operators_visits, columns=['operators', 'visits_operators'])

def func(pct, allvalues):    #values and perecentage in pie graph
         absolute = int(pct / 100.*np.sum(allvalues)) 
         return "{:.1f}%\n\n{:d}".format(pct, absolute) 
#         return "{:.1f}%\n({:d} g)".format(pct, absolute)
################################################بازدید اپراتورها به تفکیک#######################################################
tva_visits=df_radio_pie_operators.iat[0,1]
lenz_visits=df_radio_pie_operators.iat[1,1]
#televebion_visits=df_radio_pie_operators.iat[2,1]
#anten_visits=df_radio_pie_operators.iat[3,1]
#PRint(fam_visits)

 ################################# ده محتوای پربازدید ####################################
df_radio_all_content_visit=df_radio.groupby(['نام برنامه']).sum().reset_index()
df_radio_all_content_visit.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
#df_radio_all_content_visit=df_radio_all_content_visit.drop(columns=['تاریخ شروع', 'میانگین','تاریخ پایان', 'مدت بازدید','ساعت','تاریخ','ردیف','جنس','نام برنامه اولیه'])
###################### for PDF #########################
content_popular_visit=[]
content_popular_visitnumber=[]
content_popular_name=[]
content_popular_name=df_radio_all_content_visit["نام برنامه"].tolist()
content_popular_visit.append(content_popular_name)
content_popular_visitnumber=df_radio_all_content_visit["تعداد بازدید"].tolist()
content_popular_visit.append(content_popular_visitnumber)
content_popular_visit_data_pdf={'content_popular_name_data' : [get_display(arabic_reshaper.reshape(content_popular_name[0])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[1])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[2])),
                                                           get_display(arabic_reshaper.reshape(content_popular_name[3])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[4])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[5])),
                                                           get_display(arabic_reshaper.reshape(content_popular_name[6])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[7])), 
                                                           get_display(arabic_reshaper.reshape(content_popular_name[8])),
                                                           get_display(arabic_reshaper.reshape(content_popular_name[9]))],
                            'content_popular_visitnumber_data' : [content_popular_visitnumber[0], content_popular_visitnumber[1],
                                                                  content_popular_visitnumber[2], content_popular_visitnumber[3],
                                                                  content_popular_visitnumber[4], content_popular_visitnumber[5],
                                                                  content_popular_visitnumber[6], content_popular_visitnumber[7],
                                                                  content_popular_visitnumber[8], content_popular_visitnumber[9]]}
df_radio_content_popular_visit=pd.DataFrame(content_popular_visit_data_pdf, columns=['content_popular_name_data' , 'content_popular_visitnumber_data'])
###################### for excel #########################
content_popular_visit_data={'content_popular_name_data' : [content_popular_name[0], 
                                                           content_popular_name[1], 
                                                           content_popular_name[2],
                                                           content_popular_name[3], 
                                                           content_popular_name[4], 
                                                           content_popular_name[5],
                                                           content_popular_name[6], 
                                                           content_popular_name[7], 
                                                           content_popular_name[8],
                                                           content_popular_name[9]],
                            'content_popular_visitnumber_data' : [content_popular_visitnumber[0], content_popular_visitnumber[1],
                                                                  content_popular_visitnumber[2], content_popular_visitnumber[3],
                                                                  content_popular_visitnumber[4], content_popular_visitnumber[5],
                                                                  content_popular_visitnumber[6], content_popular_visitnumber[7],
                                                                  content_popular_visitnumber[8], content_popular_visitnumber[9]]}
content_popular_visit_data=pd.DataFrame(content_popular_visit_data, columns=['content_popular_name_data' , 'content_popular_visitnumber_data'])
 ################################# ده محتوای پربازدید به ازای هر قسمت ####################################
numbersection_content_1=10
numbersection_content_2=20
numbersection_content_3=10
numbersection_content_4=20
numbersection_content_5=10
numbersection_content_6=20
numbersection_content_7=10
numbersection_content_8=20
numbersection_content_9=10
numbersection_content_10=20

content_popular_visitnumber_sections_1=content_popular_visitnumber[0]/numbersection_content_1
content_popular_visitnumber_sections_2=content_popular_visitnumber[1]/numbersection_content_2
content_popular_visitnumber_sections_3=content_popular_visitnumber[2]/numbersection_content_3
content_popular_visitnumber_sections_4=content_popular_visitnumber[3]/numbersection_content_4
content_popular_visitnumber_sections_5=content_popular_visitnumber[4]/numbersection_content_5
content_popular_visitnumber_sections_6=content_popular_visitnumber[5]/numbersection_content_6
content_popular_visitnumber_sections_7=content_popular_visitnumber[6]/numbersection_content_7
content_popular_visitnumber_sections_8=content_popular_visitnumber[7]/numbersection_content_8
content_popular_visitnumber_sections_9=content_popular_visitnumber[8]/numbersection_content_9
content_popular_visitnumber_sections_10=content_popular_visitnumber[9]/numbersection_content_10

content_popular_visitnumber_sections_1=round(content_popular_visitnumber_sections_1,0)
content_popular_visitnumber_sections_2=round(content_popular_visitnumber_sections_2,0) 
content_popular_visitnumber_sections_3=round(content_popular_visitnumber_sections_3,0) 
content_popular_visitnumber_sections_4=round(content_popular_visitnumber_sections_4,0) 
content_popular_visitnumber_sections_5=round(content_popular_visitnumber_sections_5,0) 
content_popular_visitnumber_sections_6=round(content_popular_visitnumber_sections_6,0) 
content_popular_visitnumber_sections_7=round(content_popular_visitnumber_sections_7,0) 
content_popular_visitnumber_sections_8=round(content_popular_visitnumber_sections_8,0) 
content_popular_visitnumber_sections_9=round(content_popular_visitnumber_sections_9,0) 
content_popular_visitnumber_sections_10=round(content_popular_visitnumber_sections_10,0)

content_popular_visit_persection_data={'content_popular_name_persection_data' : [get_display(arabic_reshaper.reshape(content_popular_name[0])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[1])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[2])),
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[3])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[4])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[5])),
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[6])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[7])), 
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[8])),
                                                                                 get_display(arabic_reshaper.reshape(content_popular_name[9]))],
                                       'content_popular_visitnumber_persection_data' : [content_popular_visitnumber_sections_1,
                                                                                        content_popular_visitnumber_sections_2,
                                                                                        content_popular_visitnumber_sections_3,
                                                                                        content_popular_visitnumber_sections_5,
                                                                                        content_popular_visitnumber_sections_5,
                                                                                        content_popular_visitnumber_sections_6,
                                                                                        content_popular_visitnumber_sections_7,
                                                                                        content_popular_visitnumber_sections_8,
                                                                                        content_popular_visitnumber_sections_9,
                                                                                        content_popular_visitnumber_sections_10]}
df_radio_content_popular_visit_persection_data=pd.DataFrame(content_popular_visit_persection_data, columns=['content_popular_name_persection_data' , 'content_popular_visitnumber_persection_data']) 
df_radio_content_popular_visit_persection_data.sort_values('content_popular_visitnumber_persection_data', axis = 0, ascending = False, inplace = True, na_position ='last')
################################################ number of channels in operators ###################################################
number_channels_tva=df_radio.query("اپراتور == 'تیوا'")
number_channels_tva.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True) 
number_channels_tva=len(number_channels_tva)

number_channels_lenz=df_radio.query("اپراتور == 'لنز'")
number_channels_lenz.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True) 
number_channels_lenz=len(number_channels_lenz)

number_channels_televebion=df_radio.query("اپراتور == 'تلوبیون'")
number_channels_televebion.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True) 
number_channels_televebion=len(number_channels_televebion)

number_channels_anten=df_radio.query("اپراتور == 'آنتن'")
number_channels_anten.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True) 
number_channels_anten=len(number_channels_anten)

number_channels_operators={'operators_name': ['تیوا', 'لنز', 'تلوبیون', 'آنتن'],
                           'channels_number': [number_channels_tva, number_channels_lenz, number_channels_televebion, number_channels_anten]}
number_channels_operators=pd.DataFrame(number_channels_operators, columns=['operators_name', 'channels_number'])
number_channels_operators.sort_values('channels_number', axis = 0, ascending = False, inplace = True, na_position ='last')
 ################################# output excel ####################################
EPG_Radio = pd.read_excel ('EPG Radio.xlsx')

radio_channels_visit.to_excel('radio_channels_visit.xlsx')
radio_operators_visit.to_excel('radio_operators_visit.xlsx')
number_channels_operators.to_excel('number_channels_operators.xlsx')

radio_channels_visit=pd.read_excel('radio_channels_visit.xlsx')
radio_operators_visit=pd.read_excel('radio_operators_visit.xlsx')
number_channels_operators=pd.read_excel('number_channels_operators.xlsx')

del radio_channels_visit['Unnamed: 0']
del radio_operators_visit['Unnamed: 0']
del number_channels_operators['Unnamed: 0']

all_data_radio=pd.concat([radio_operators_visit,
                          radio_channels_visit,
                          program_data,
                          content_popular_visit_data,
                          number_channels_operators,], axis=1)
all_data_radio.to_excel('output\RADIO.xlsx')

#######################################################################################################
########################################### گزارش رئیس سازمان #########################################
########################################################################################################

with PdfPages(r'C:\Users\PC\Desktop\total statistics\گزارش رادیویی.pdf') as exPRrt_pdf:
    #################################### تعداد بازدید و تعداد محتوا و مدت زمان محتواها ######################################     
     firstPage = plt.figure(figsize=(10,12))
     firstPage.clf()
     txt1 = get_display(arabic_reshaper.reshape('به نام خداوند بخشنده مهربان'))
     firstPage.text(0.5,0.2,txt1, transform=firstPage.transFigure, size=24, ha="center")
     exPRrt_pdf.savefig()
     plt.close()
     df_radioall_visits=pd.DataFrame()
     df_radioall_visits[get_display(arabic_reshaper.reshape('تعداد محتوا'))]=[PRograms_all_contents]
     df_radioall_visits[get_display(arabic_reshaper.reshape('تعداد بازدید کل محتواهای رادیویی'))]=[PRograms_all_visits]
     df_radioall_visits[get_display(arabic_reshaper.reshape('مدت زمان بازدید کل محتواهای \n\n رادیویی (به دقیقه)'))]=[PRograms_all_duration]
     fig = plt.figure(figsize=(10,12))
     plt.subplot(111)
     plt.axis('off')
     plt.title(get_display(arabic_reshaper.reshape('تعداد محتوا، بازدید و مدت زمان بازدید کل شبکه های رادیویی\n')),
               fontweight ="bold",
               fontsize=18,
               loc="center") 
     plt.table(cellText=df_radioall_visits.values, 
               colLabels=df_radioall_visits.columns,
               colWidths=[1] * 3,
               bbox=[0,0,1,1], 
               edges='closed',
               rowLoc='center',
#               rowColours=["palegreen"] * 16,
               colColours=["palegreen"] * 12,
               cellLoc='center')     
     plt.subplots_adjust(left=.1, top=.8)
     exPRrt_pdf.savefig()
     plt.show()
     plt.close()
     ######################################تعداد بازدید شبکه های سازمان####################################     
     plt.figure(figsize=(10, 12))
     plt.title(get_display(arabic_reshaper.reshape('تعداد بازدید شبکه های سازمان')), 
               fontsize=18, 
               fontname='B Nazanin', 
               weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('تعداد بازدید شبکه های سازمان (به ترتیب حروف الفبا)')), 
                fontsize=12, 
                fontname='B Nazanin', 
                weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('نام محتوا')), 
                fontsize=12, 
                fontname='B Nazanin', 
                weight="bold")
     plt.rc('font', family='B Nazanin', size=12, weight="bold")
     rects1=plt.barh(df_radio_barh_all_channels['channels'], df_radio_barh_all_channels['visits_channels'], 
                     color='blue', 
                     align='center', 
                     alpha=0.5)
     for i, v in enumerate(df_radio_barh_all_channels['visits_channels']):
         plt.text(v + 3, i - 0.15, str(v), color='blue', fontweight='bold')
#     plt.bar(format=comma_fmt)
#     plt.colorbar(format=comma_fmt)
#     plt.rc('font', size=12)          # controls default text sizes
#     plt.rc('axes', titlesize=12)     # fontsize of the axes title
#     plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
#     plt.rc('legend', fontsize=12)    # legend fontsize
#     plt.rc('figure', titlesize=12)  # fontsize of the figure title
#     plt.text(-.1, ch_one2[0]+500, ch_one2[0], **text_font)
#     plt.text(0.9, ch_one2[1]+500, ch_one2[1], **text_font)
#     plt.text(1.9, ch_one2[2]+500, ch_one2[2], **text_font)
     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numPRints=1)
     exPRrt_pdf.savefig()
     plt.show()
     plt.close()
     #################################تعداد بازدید اپراتورها####################################
     colors=('aqua', 'dodgerblue', 'red', 'blue')
     plt.figure(figsize=(10, 12))
     plt.pie(df_radio_pie_operators['visits_operators'], labels=df_radio_pie_operators['operators'], shadow=False, colors=colors, explode=(0.1, 0.1), 
             startangle=50, autopct=lambda pct: func(pct, df_radio_pie_operators['visits_operators']))
     plt.title(get_display(arabic_reshaper.reshape('تعداد بازدید اپراتورها')), fontsize=22, fontname='B Nazanin', weight="bold")
     plt.legend(df_radio_pie_operators['operators'], loc="best")
     plt.axis('equal')
#     plot=df_radiooperator.plot.pie(y='radius', title=get_display(arabic_reshaper.reshape('بازدید اپراتورها')), legend=False, 
#                   autopct='%1.1f%%', explode=(0.05, 0.05, 0.05), shadow=True, startangle=0, colors=colors, figsize=(6,6))
     exPRrt_pdf.savefig()
     plt.show()
     plt.close()
 #################################تعداد کاربران فعال اپراتورها####################################
#     plt.figure(figsize=(9, 6))
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
#     plt.bar(operators_name, operators_visitors, color='aqua', width=0.75, align='center', alpha=1)
#     plt.title(get_display(arabic_reshaper.reshape('کاربران فعال ماهانه اپراتورها')), fontsize=18, fontname='B Nazanin', weight="bold")
#     plt.xlabel(get_display(arabic_reshaper.reshape('نام اپراتور')), fontsize=14, fontname='B Nazanin', weight="bold")
#     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد کاربر فعال')), fontsize=14, fontname='B Nazanin', weight="bold")
#     plt.rc('font', family='B Nazanin', size=16, weight="bold")
#     plt.text(-0.25,operators_visitors[0]+150, operators_visitors[0],  **text1_font)
#     plt.text(0.90,operators_visitors[1]+150, operators_visitors[1],  **text1_font)
#     plt.text(1.90,operators_visitors[2]+150, operators_visitors[2],  **text1_font)
#     plt.text(2.90,operators_visitors[3]+150, operators_visitors[3],  **text1_font)
#     plt.text(3.90,operators_visitors[4]+150, operators_visitors[4],  **text1_font)
#     plt.text(4.90,operators_visitors[5]+150, operators_visitors[5],  **text1_font)
#     plt.text(5.90,operators_visitors[6]+150, operators_visitors[6],  **text1_font)
##     plt.grid(True)
##     plt.legend('نمودار معین',loc='upper right', numPRints=1)
#     exPRrt_pdf.savefig()
#     plt.show()
#     plt.close() 
 ################################# ده محتوای پربازدید ####################################
     plt.figure(figsize=(10, 12))
     plt.suptitle(get_display(arabic_reshaper.reshape('محتواهای پربازدید سازمان')), fontsize=24, fontname='B Nazanin', weight="bold") 
     plt.subplot(211)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(df_radio_content_popular_visit['content_popular_name_data'], df_radio_content_popular_visit['content_popular_visitnumber_data'], 
             color='aqua', 
             width=0.25, 
             align='center', 
             alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('ده محتوای داغ سازمان')), 
               fontsize=18, 
               fontname='B Nazanin', 
               weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام  محتوا')), 
                fontsize=10, 
                fontname='B Nazanin', 
                weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), 
                fontsize=10, 
                fontname='B Nazanin', 
                weight="bold")
#     plt.rc('font', family='B Nazanin', size=10, weight="bold")
#     plt.text(-0.1,channels_visits_sPRrts[0]+10000, channels_visits_sPRrts[0],  **text1_font)
#     plt.text(0.90,channels_visits_sPRrts[1]+10000, channels_visits_sPRrts[1],  **text1_font)
#     plt.text(1.90,channels_visits_sPRrts[2]+10000, channels_visits_sPRrts[2],  **text1_font)
#     plt.text(2.90,channels_visits_sPRrts[3]+10000, channels_visits_sPRrts[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numPRints=1)
     plt.subplot(212)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(df_radio_content_popular_visit_persection_data['content_popular_name_persection_data'],df_radio_content_popular_visit_persection_data['content_popular_visitnumber_persection_data'], 
             color='aqua', 
             width=0.25, 
             align='center', 
             alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('ده محتوای پربازدید به ازای هر قسمت')), 
               fontsize=18, 
               fontname='B Nazanin', 
               weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام محتوا')), 
                fontsize=10, 
                fontname='B Nazanin', 
                weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), 
                fontsize=10, 
                fontname='B Nazanin', 
                weight="bold")
#     plt.rc('font', family='B Nazanin', size=10, weight="bold")
#     plt.text(-0.1,channels_contents_sPRrts[0]+10000, channels_contents_sPRrts[0],  **text1_font)
#     plt.text(0.90,channels_contents_sPRrts[1]+10000, channels_contents_sPRrts[1],  **text1_font)
#     plt.text(1.90,channels_contents_sPRrts[2]+10000, channels_contents_sPRrts[2],  **text1_font)
#     plt.text(2.90,channels_contents_sPRrts[3]+10000, channels_contents_sPRrts[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numPRints=1)
     exPRrt_pdf.savefig()
     plt.show()
     plt.close()
     