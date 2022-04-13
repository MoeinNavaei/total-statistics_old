import xlsxwriter  
import pandas as pd
#from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib as mpl
import matplotlib.ticker as tkr
import numpy as np
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D

workbook_sar = xlsxwriter.Workbook('EPG Sarasari.xlsx')
workbook_ekh = xlsxwriter.Workbook('EPG Ekhtesasi.xlsx')
#df_sar = pd.read_excel (r'C:\Users\PC\Desktop\EPG Ordibehesh.xlsx', sheet_name='test')  
df_sar = pd.read_excel (r'C:\Users\PC\Desktop\total statistics\sarasari.xlsx', sheet_name='Sheet1')
df_ekh = pd.read_excel (r'C:\Users\PC\Desktop\total statistics\ekhtesasi.xlsx', sheet_name='Sheet1')

worksheet_sar = workbook_sar.add_worksheet() 
worksheet_ekh = workbook_ekh.add_worksheet() 
 
format1 = workbook_sar.add_format({'num_format': '#,##', 'bold':True, 'font_color':'green', 'size':14, 'font_name':'B Nazanin'})
format2 = workbook_ekh.add_format({'num_format': '#,##', 'bold':True, 'font_color':'green', 'size':14, 'font_name':'B Nazanin'})
                                   
worksheet_sar.set_column('A:EZ', 12, format1)
worksheet_ekh.set_column('A:EZ', 12, format2)

ch_one=pd.DataFrame()
ch_two=pd.DataFrame()
ch_three=pd.DataFrame()
ch_four=pd.DataFrame()
ch_five=pd.DataFrame()
ch_khabar=pd.DataFrame()
ch_ofogh=pd.DataFrame()
ch_pooya=pd.DataFrame()
ch_omid=pd.DataFrame()
ch_ifilm=pd.DataFrame()
ch_namayesh=pd.DataFrame()
ch_tamasha=pd.DataFrame()
ch_mostanad=pd.DataFrame()
ch_shoma=pd.DataFrame()
ch_amozesh=pd.DataFrame()
ch_varzesh=pd.DataFrame()
ch_nasim=pd.DataFrame()
ch_qoran=pd.DataFrame()
ch_salamat=pd.DataFrame()
ch_irankala=pd.DataFrame()
ch_alalam=pd.DataFrame()
ch_alkosar=pd.DataFrame()
ch_presstv=pd.DataFrame()
ch_sepehr=pd.DataFrame()
ch_jamejam=pd.DataFrame()

ch_tva_sport=pd.DataFrame()
ch_tva_sport_two=pd.DataFrame()
ch_tva_avand=pd.DataFrame()
ch_tva_two=pd.DataFrame()
ch_tva_film=pd.DataFrame()
ch_tva_kodak=pd.DataFrame()
ch_tva_nava=pd.DataFrame()
ch_tva_one=pd.DataFrame()
ch_sarbaz_maher=pd.DataFrame()
ch_shaparak=pd.DataFrame()
ch_kodak_digiton=pd.DataFrame()
ch_lenz_sport_plus=pd.DataFrame()
ch_lenz_sport=pd.DataFrame()
ch_mahfel=pd.DataFrame()


p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
p9=0
p10=0
p11=0
p12=0
p13=0
p14=0
p15=0
p16=0
p17=0
p18=0
p19=0
p20=0
p21=0
p22=0
p23=0
p24=0
p25=0

p1_ekh=0
p2_ekh=0
p3_ekh=0
p4_ekh=0
p5_ekh=0
p6_ekh=0
p7_ekh=0
p8_ekh=0
p9_ekh=0
p10_ekh=0
p11_ekh=0
p12_ekh=0
p13_ekh=0
p14_ekh=0
p15_ekh=0
p16_ekh=0
p17_ekh=0
p18_ekh=0
p19_ekh=0
p20_ekh=0
p21_ekh=0
p22_ekh=0
p23_ekh=0
p24_ekh=0
p25_ekh=0

#df_sar=df_sar.drop(columns=['جنس','ردیف','میانگین','نام برنامه اولیه'])

df_sar_sum=df_sar.groupby(['نام برنامه','نام شبکه']).sum().reset_index()
t=len(df_sar_sum)
for i in range(0,t):
    f=df_sar_sum.loc[i,'نام شبکه']
    
#####################################################################
######################### channels data sarasari #############################
#####################################################################

############################# شبکه 1 #################################
    if f=='شبکه 1':
        p1=p1+1  
        ch_one.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_one.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_one.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه 2 #################################
    if f=='شبکه 2': 
        p2=p2+1 
        ch_two.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_two.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_two.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه 3 #################################
    if f=='شبکه 3':
        p3=p3+1  
        ch_three.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_three.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_three.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه 4 #################################
    if f=='شبکه 4': 
        p4=p4+1 
        ch_four.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_four.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_four.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه 5 #################################
    if f=='شبکه 5':
        p5=p5+1  
        ch_five.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_five.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_five.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه خبر #################################
    if f=='خبر': 
        p6=p6+1 
        ch_khabar.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_khabar.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_khabar.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه افق #################################
    if f=='افق':
        p7=p7+1  
        ch_ofogh.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_ofogh.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_ofogh.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه پویا #################################
    if f=='پویا':
        p8=p8+1 
        ch_pooya.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_pooya.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_pooya.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه امید #################################
    if f=='امید': 
        p9=p9+1  
        ch_omid.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_omid.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_omid.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه آی فیلم #################################
    if f=='آی فیلم':
        p10=p10+1 
        ch_ifilm.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_ifilm.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_ifilm.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه نمایش #################################
    if f=='نمایش': 
        p11=p11+1  
        ch_namayesh.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_namayesh.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_namayesh.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه تماشا #################################
    if f=='تماشا':
        p12=p12+1 
        ch_tamasha.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_tamasha.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_tamasha.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه مستند #################################
    if f=='مستند': 
        p13=p13+1  
        ch_mostanad.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_mostanad.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_mostanad.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه شما #################################
    if f=='شما':
        p14=p14+1 
        ch_shoma.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_shoma.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_shoma.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']

############################# شبکه آموزش #################################
    if f=='آموزش': 
        p15=p15+1  
        ch_amozesh.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_amozesh.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_amozesh.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه ورزش #################################
    if f=='ورزش':
        p16=p16+1 
        ch_varzesh.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_varzesh.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_varzesh.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه نسیم #################################
    if f=='نسیم': 
        p17=p17+1  
        ch_nasim.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_nasim.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_nasim.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه قرآن #################################
    if f=='قرآن':
        p18=p18+1 
        ch_qoran.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_qoran.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_qoran.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه سلامت #################################
    if f=='سلامت': 
        p19=p19+1  
        ch_salamat.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_salamat.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_salamat.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه ایران کالا #################################
    if f=='ایران کالا':
        p20=p20+1 
        ch_irankala.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_irankala.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_irankala.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه العالم #################################
    if f=='العالم': 
        p21=p21+1  
        ch_alalam.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_alalam.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_alalam.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه الکوثر #################################
    if f=='الکوثر':
        p22=p22+1 
        ch_alkosar.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_alkosar.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_alkosar.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه پرس تی وی #################################
    if f=='پرس تی وی': 
        p23=p23+1  
        ch_presstv.loc[p1,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_presstv.loc[p1,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_presstv.loc[p1,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه سپهر #################################
    if f=='سپهر': 
        p24=p24+1 
        ch_sepehr.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_sepehr.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_sepehr.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']
############################# شبکه جام جم 1 #################################
    if f=='جام جم 1': 
        p25=p25+1 
        ch_jamejam.loc[p2,'نام برنامه']=df_sar_sum.loc[i,'نام برنامه']
        ch_jamejam.loc[p2,'تعداد بازدید']=df_sar_sum.loc[i,'تعداد بازدید']
        ch_jamejam.loc[p2,'مدت بازدید']=df_sar_sum.loc[i,'مدت بازدید']        
#####################################################################
############################# شبکه 1 #################################
ch_one1=[]
ch_one2=[]
ch_one3=[]
ch_one4=[]
ch_one5=[]
ch_one.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_one1=ch_one["نام برنامه"].tolist()
ch_one5.append(ch_one1)
ch_one2=ch_one["تعداد بازدید"].tolist()
ch_one5.append(ch_one2)
ch_one.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_one3=ch_one["نام برنامه"].tolist()
ch_one5.append(ch_one3)
ch_one4=ch_one["مدت بازدید"].tolist()
ch_one5.append(ch_one4)
############################# شبکه 2 #################################
ch_two1=[]
ch_two2=[]
ch_two3=[]
ch_two4=[]
ch_two5=[]
ch_two.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_two1=ch_two["نام برنامه"].tolist()
ch_two5.append(ch_two1)
ch_two2=ch_two["تعداد بازدید"].tolist()
ch_two5.append(ch_two2)
ch_two.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_two3=ch_two["نام برنامه"].tolist()
ch_two5.append(ch_two3)
ch_two4=ch_two["مدت بازدید"].tolist()
ch_two5.append(ch_two4)
############################# شبکه 3 #################################
ch_three1=[]
ch_three2=[]
ch_three3=[]
ch_three4=[]
ch_three5=[]
ch_three.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_three1=ch_three["نام برنامه"].tolist()
ch_three5.append(ch_three1)
ch_three2=ch_three["تعداد بازدید"].tolist()
ch_three5.append(ch_three2)
ch_three.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_three3=ch_three["نام برنامه"].tolist()
ch_three5.append(ch_three3)
ch_three4=ch_three["مدت بازدید"].tolist()
ch_three5.append(ch_three4)
############################# شبکه 4 #################################
ch_four1=[]
ch_four2=[]
ch_four3=[]
ch_four4=[]
ch_four5=[]
ch_four.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_four1=ch_four["نام برنامه"].tolist()
ch_four5.append(ch_four1)
ch_four2=ch_four["تعداد بازدید"].tolist()
ch_four5.append(ch_four2)
ch_four.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_four3=ch_four["نام برنامه"].tolist()
ch_four5.append(ch_four3)
ch_four4=ch_four["مدت بازدید"].tolist()
ch_four5.append(ch_four4)
############################# شبکه 5 #################################
ch_five1=[]
ch_five2=[]
ch_five3=[]
ch_five4=[]
ch_five5=[]
ch_five.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_five1=ch_five["نام برنامه"].tolist()
ch_five5.append(ch_five1)
ch_five2=ch_five["تعداد بازدید"].tolist()
ch_five5.append(ch_five2)
ch_five.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_five3=ch_five["نام برنامه"].tolist()
ch_five5.append(ch_five3)
ch_five4=ch_five["مدت بازدید"].tolist()
ch_five5.append(ch_five4)
############################# شبکه خبر #################################
ch_khabar1=[]
ch_khabar2=[]
ch_khabar3=[]
ch_khabar4=[]
ch_khabar5=[]
ch_khabar.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_khabar1=ch_khabar["نام برنامه"].tolist()
ch_khabar5.append(ch_khabar1)
ch_khabar2=ch_khabar["تعداد بازدید"].tolist()
ch_khabar5.append(ch_khabar2)
ch_khabar.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_khabar3=ch_khabar["نام برنامه"].tolist()
ch_khabar5.append(ch_khabar3)
ch_khabar4=ch_khabar["مدت بازدید"].tolist()
ch_khabar5.append(ch_khabar4)
############################# شبکه افق #################################
ch_ofogh1=[]
ch_ofogh2=[]
ch_ofogh3=[]
ch_ofogh4=[]
ch_ofogh5=[]
ch_ofogh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_ofogh1=ch_ofogh["نام برنامه"].tolist()
ch_ofogh5.append(ch_ofogh1)
ch_ofogh2=ch_ofogh["تعداد بازدید"].tolist()
ch_ofogh5.append(ch_ofogh2)
ch_ofogh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_ofogh3=ch_ofogh["نام برنامه"].tolist()
ch_ofogh5.append(ch_ofogh3)
ch_ofogh4=ch_ofogh["مدت بازدید"].tolist()
ch_ofogh5.append(ch_ofogh4)
############################# شبکه پویا #################################
ch_pooya1=[]
ch_pooya2=[]
ch_pooya3=[]
ch_pooya4=[]
ch_pooya5=[]
ch_pooya.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_pooya1=ch_pooya["نام برنامه"].tolist()
ch_pooya5.append(ch_pooya1)
ch_pooya2=ch_pooya["تعداد بازدید"].tolist()
ch_pooya5.append(ch_pooya2)
ch_pooya.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_pooya3=ch_pooya["نام برنامه"].tolist()
ch_pooya5.append(ch_pooya3)
ch_pooya4=ch_pooya["مدت بازدید"].tolist()
ch_pooya5.append(ch_pooya4)
############################# شبکه امید #################################
ch_omid1=[]
ch_omid2=[]
ch_omid3=[]
ch_omid4=[]
ch_omid5=[]
ch_omid.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_omid1=ch_omid["نام برنامه"].tolist()
ch_omid5.append(ch_omid1)
ch_omid2=ch_omid["تعداد بازدید"].tolist()
ch_omid5.append(ch_omid2)
ch_omid.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_omid3=ch_omid["نام برنامه"].tolist()
ch_omid5.append(ch_omid3)
ch_omid4=ch_omid["مدت بازدید"].tolist()
ch_omid5.append(ch_omid4)
############################# شبکه آی فیلم #################################
ch_ifilm1=[]
ch_ifilm2=[]
ch_ifilm3=[]
ch_ifilm4=[]
ch_ifilm5=[]
ch_ifilm.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_ifilm1=ch_ifilm["نام برنامه"].tolist()
ch_ifilm5.append(ch_ifilm1)
ch_ifilm2=ch_ifilm["تعداد بازدید"].tolist()
ch_ifilm5.append(ch_ifilm2)
ch_ifilm.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_ifilm3=ch_ifilm["نام برنامه"].tolist()
ch_ifilm5.append(ch_ifilm3)
ch_ifilm4=ch_ifilm["مدت بازدید"].tolist()
ch_ifilm5.append(ch_ifilm4)
############################# شبکه نمایش #################################
ch_namayesh1=[]
ch_namayesh2=[]
ch_namayesh3=[]
ch_namayesh4=[]
ch_namayesh5=[]
ch_namayesh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_namayesh1=ch_namayesh["نام برنامه"].tolist()
ch_namayesh5.append(ch_namayesh1)
ch_namayesh2=ch_namayesh["تعداد بازدید"].tolist()
ch_namayesh5.append(ch_namayesh2)
ch_namayesh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_namayesh3=ch_namayesh["نام برنامه"].tolist()
ch_namayesh5.append(ch_namayesh3)
ch_namayesh4=ch_namayesh["مدت بازدید"].tolist()
ch_namayesh5.append(ch_namayesh4)
############################# شبکه تماشا #################################
ch_tamasha1=[]
ch_tamasha2=[]
ch_tamasha3=[]
ch_tamasha4=[]
ch_tamasha5=[]
ch_tamasha.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tamasha1=ch_tamasha["نام برنامه"].tolist()
ch_tamasha5.append(ch_tamasha1)
ch_tamasha2=ch_tamasha["تعداد بازدید"].tolist()
ch_tamasha5.append(ch_tamasha2)
ch_tamasha.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tamasha3=ch_tamasha["نام برنامه"].tolist()
ch_tamasha5.append(ch_tamasha3)
ch_tamasha4=ch_tamasha["مدت بازدید"].tolist()
ch_tamasha5.append(ch_tamasha4)
############################# شبکه مستند #################################
ch_mostanad1=[]
ch_mostanad2=[]
ch_mostanad3=[]
ch_mostanad4=[]
ch_mostanad5=[]
ch_mostanad.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_mostanad1=ch_mostanad["نام برنامه"].tolist()
ch_mostanad5.append(ch_mostanad1)
ch_mostanad2=ch_mostanad["تعداد بازدید"].tolist()
ch_mostanad5.append(ch_mostanad2)
ch_mostanad.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_mostanad3=ch_mostanad["نام برنامه"].tolist()
ch_mostanad5.append(ch_mostanad3)
ch_mostanad4=ch_mostanad["مدت بازدید"].tolist()
ch_mostanad5.append(ch_mostanad4)
############################# شبکه شما #################################
ch_shoma1=[]
ch_shoma2=[]
ch_shoma3=[]
ch_shoma4=[]
ch_shoma5=[]
ch_shoma.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_shoma1=ch_shoma["نام برنامه"].tolist()
ch_shoma5.append(ch_shoma1)
ch_shoma2=ch_shoma["تعداد بازدید"].tolist()
ch_shoma5.append(ch_shoma2)
ch_shoma.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_shoma3=ch_shoma["نام برنامه"].tolist()
ch_shoma5.append(ch_shoma3)
ch_shoma4=ch_shoma["مدت بازدید"].tolist()
ch_shoma5.append(ch_shoma4)
############################# شبکه آموزش #################################
ch_amozesh1=[]
ch_amozesh2=[]
ch_amozesh3=[]
ch_amozesh4=[]
ch_amozesh5=[]
ch_amozesh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_amozesh1=ch_amozesh["نام برنامه"].tolist()
ch_amozesh5.append(ch_amozesh1)
ch_amozesh2=ch_amozesh["تعداد بازدید"].tolist()
ch_amozesh5.append(ch_amozesh2)
ch_amozesh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_amozesh3=ch_amozesh["نام برنامه"].tolist()
ch_amozesh5.append(ch_amozesh3)
ch_amozesh4=ch_amozesh["مدت بازدید"].tolist()
ch_amozesh5.append(ch_amozesh4)
############################# شبکه ورزش #################################
ch_varzesh1=[]
ch_varzesh2=[]
ch_varzesh3=[]
ch_varzesh4=[]
ch_varzesh5=[]
ch_varzesh.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_varzesh1=ch_varzesh["نام برنامه"].tolist()
ch_varzesh5.append(ch_varzesh1)
ch_varzesh2=ch_varzesh["تعداد بازدید"].tolist()
ch_varzesh5.append(ch_varzesh2)
ch_varzesh.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_varzesh3=ch_varzesh["نام برنامه"].tolist()
ch_varzesh5.append(ch_varzesh3)
ch_varzesh4=ch_varzesh["مدت بازدید"].tolist()
ch_varzesh5.append(ch_varzesh4)
############################# شبکه نسیم #################################
ch_nasim1=[]
ch_nasim2=[]
ch_nasim3=[]
ch_nasim4=[]
ch_nasim5=[]
ch_nasim.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_nasim1=ch_nasim["نام برنامه"].tolist()
ch_nasim5.append(ch_nasim1)
ch_nasim2=ch_nasim["تعداد بازدید"].tolist()
ch_nasim5.append(ch_nasim2)
ch_nasim.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_nasim3=ch_nasim["نام برنامه"].tolist()
ch_nasim5.append(ch_nasim3)
ch_nasim4=ch_nasim["مدت بازدید"].tolist()
ch_nasim5.append(ch_nasim4)
############################# شبکه قرآن #################################
ch_qoran1=[]
ch_qoran2=[]
ch_qoran3=[]
ch_qoran4=[]
ch_qoran5=[]
ch_qoran.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_qoran1=ch_qoran["نام برنامه"].tolist()
ch_qoran5.append(ch_qoran1)
ch_qoran2=ch_qoran["تعداد بازدید"].tolist()
ch_qoran5.append(ch_qoran2)
ch_qoran.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_qoran3=ch_qoran["نام برنامه"].tolist()
ch_qoran5.append(ch_qoran3)
ch_qoran4=ch_qoran["مدت بازدید"].tolist()
ch_qoran5.append(ch_qoran4)
############################# شبکه سلامت #################################
ch_salamat1=[]
ch_salamat2=[]
ch_salamat3=[]
ch_salamat4=[]
ch_salamat5=[]
ch_salamat.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_salamat1=ch_salamat["نام برنامه"].tolist()
ch_salamat5.append(ch_salamat1)
ch_salamat2=ch_salamat["تعداد بازدید"].tolist()
ch_salamat5.append(ch_salamat2)
ch_salamat.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_salamat3=ch_salamat["نام برنامه"].tolist()
ch_salamat5.append(ch_salamat3)
ch_salamat4=ch_salamat["مدت بازدید"].tolist()
ch_salamat5.append(ch_salamat4)
############################# شبکه ایران کالا #################################
ch_irankala1=[]
ch_irankala2=[]
ch_irankala3=[]
ch_irankala4=[]
ch_irankala5=[]
ch_irankala.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_irankala1=ch_irankala["نام برنامه"].tolist()
ch_irankala5.append(ch_irankala1)
ch_irankala2=ch_irankala["تعداد بازدید"].tolist()
ch_irankala5.append(ch_irankala2)
ch_irankala.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_irankala3=ch_irankala["نام برنامه"].tolist()
ch_irankala5.append(ch_irankala3)
ch_irankala4=ch_irankala["مدت بازدید"].tolist()
ch_irankala5.append(ch_irankala4)
############################# شبکه العالم #################################
ch_alalam1=[]
ch_alalam2=[]
ch_alalam3=[]
ch_alalam4=[]
ch_alalam5=[]
ch_alalam.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_alalam1=ch_alalam["نام برنامه"].tolist()
ch_alalam5.append(ch_alalam1)
ch_alalam2=ch_alalam["تعداد بازدید"].tolist()
ch_alalam5.append(ch_alalam2)
ch_alalam.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_alalam3=ch_alalam["نام برنامه"].tolist()
ch_alalam5.append(ch_alalam3)
ch_alalam4=ch_alalam["مدت بازدید"].tolist()
ch_alalam5.append(ch_alalam4)
############################# شبکه الکوثر #################################
ch_alkosar1=[]
ch_alkosar2=[]
ch_alkosar3=[]
ch_alkosar4=[]
ch_alkosar5=[]
ch_alkosar.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_alkosar1=ch_alkosar["نام برنامه"].tolist()
ch_alkosar5.append(ch_alkosar1)
ch_alkosar2=ch_alkosar["تعداد بازدید"].tolist()
ch_alkosar5.append(ch_alkosar2)
ch_alkosar.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_alkosar3=ch_alkosar["نام برنامه"].tolist()
ch_alkosar5.append(ch_alkosar3)
ch_alkosar4=ch_alkosar["مدت بازدید"].tolist()
ch_alkosar5.append(ch_alkosar4)
############################# شبکه پرس تی وی #################################
ch_presstv1=[]
ch_presstv2=[]
ch_presstv3=[]
ch_presstv4=[]
ch_presstv5=[]
ch_presstv.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_presstv1=ch_presstv["نام برنامه"].tolist()
ch_presstv5.append(ch_presstv1)
ch_presstv2=ch_presstv["تعداد بازدید"].tolist()
ch_presstv5.append(ch_presstv2)
ch_presstv.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_presstv3=ch_presstv["نام برنامه"].tolist()
ch_presstv5.append(ch_presstv3)
ch_presstv4=ch_presstv["مدت بازدید"].tolist()
ch_presstv5.append(ch_presstv4)
############################# شبکه سپهر #################################
ch_sepehr1=[]
ch_sepehr2=[]
ch_sepehr3=[]
ch_sepehr4=[]
ch_sepehr5=[]
ch_sepehr.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_sepehr1=ch_sepehr["نام برنامه"].tolist()
ch_sepehr5.append(ch_sepehr1)
ch_sepehr2=ch_sepehr["تعداد بازدید"].tolist()
ch_sepehr5.append(ch_sepehr2)
ch_sepehr.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_sepehr3=ch_sepehr["نام برنامه"].tolist()
ch_sepehr5.append(ch_sepehr3)
ch_sepehr4=ch_sepehr["مدت بازدید"].tolist()
ch_sepehr5.append(ch_sepehr4)
############################# شبکه جام جم #################################
ch_jamejam1=[]
ch_jamejam2=[]
ch_jamejam3=[]
ch_jamejam4=[]
ch_jamejam5=[]
ch_jamejam.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_jamejam1=ch_jamejam["نام برنامه"].tolist()
ch_jamejam5.append(ch_jamejam1)
ch_jamejam2=ch_jamejam["تعداد بازدید"].tolist()
ch_jamejam5.append(ch_jamejam2)
ch_jamejam.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_jamejam3=ch_jamejam["نام برنامه"].tolist()
ch_jamejam5.append(ch_jamejam3)
ch_jamejam4=ch_jamejam["مدت بازدید"].tolist()
ch_jamejam5.append(ch_jamejam4)
#####################################################################

bold = workbook_sar.add_format({'bold': 1})  
headings = ['شبکه 1 بازدید', 'تعداد بازدید شبکه 1','شبکه 1 (زمان)', 'زمان بازدید شبکه 1'
            ,'شبکه 2 بازدید', 'تعداد بازدید شبکه 2','شبکه 2 (زمان)', 'زمان بازدید شبکه 2',
            'شبکه 3 بازدید', 'تعداد بازدید شبکه 3','شبکه 3 (زمان)', 'زمان بازدید شبکه 3',
            'شبکه 4 بازدید', 'تعداد بازدید شبکه 4','شبکه 4 (زمان)', 'زمان بازدید شبکه 4',
            'شبکه 5 بازدید', 'تعداد بازدید شبکه 5','شبکه 5 (زمان)', 'زمان بازدید شبکه 5',
            'شبکه خبر بازدید', 'تعداد بازدید شبکه خبر','شبکه خبر (زمان)', 'زمان بازدید شبکه خبر',
            'شبکه افق بازدید', 'تعداد بازدید شبکه افق','شبکه افق (زمان)', 'زمان بازدید شبکه افق',
            'شبکه پویا بازدید', 'تعداد بازدید شبکه پویا','شبکه پویا (زمان)', 'زمان بازدید شبکه پویا',
            'شبکه امید بازدید', 'تعداد بازدید شبکه امید','شبکه امید (زمان)', 'زمان بازدید شبکه امید',
            'شبکه آی فیلم بازدید', 'تعداد بازدید شبکه آی فیلم','شبکه آی فیلم (زمان)', 'زمان بازدید شبکه آی فیلم',
            'شبکه نمایش بازدید', 'تعداد بازدید شبکه نمایش','شبکه نمایش (زمان)', 'زمان بازدید شبکه نمایش',
            'شبکه تماشا بازدید', 'تعداد بازدید شبکه تماشا','شبکه تماشا (زمان)', 'زمان بازدید شبکه تماشا',
            'شبکه مستند بازدید', 'تعداد بازدید شبکه مستند','شبکه مستند (زمان)', 'زمان بازدید شبکه مستند',
            'شبکه شما بازدید', 'تعداد بازدید شبکه شما','شبکه شما (زمان)', 'زمان بازدید شبکه شما',
            'شبکه آموزش بازدید', 'تعداد بازدید شبکه آموزش','شبکه آموزش (زمان)', 'زمان بازدید شبکه آموزش',
            'شبکه ورزش بازدید', 'تعداد بازدید شبکه ورزش','شبکه ورزش (زمان)', 'زمان بازدید شبکه ورزش',
            'شبکه نسیم بازدید', 'تعداد بازدید شبکه نسیم','شبکه نسیم (زمان)', 'زمان بازدید شبکه نسیم',
            'شبکه قرآن بازدید', 'تعداد بازدید شبکه قرآن','شبکه قرآن (زمان)', 'زمان بازدید شبکه قرآن',
            'شبکه سلامت بازدید', 'تعداد بازدید شبکه سلامت','شبکه سلامت (زمان)', 'زمان بازدید شبکه سلامت',
            'شبکه ایران کالا بازدید', 'تعداد بازدید شبکه ایران کالا','شبکه ایران کالا (زمان)', 'زمان بازدید شبکه ایران کالا',
            'شبکه العالم بازدید', 'تعداد بازدید شبکه العالم','شبکه العالم (زمان)', 'زمان بازدید شبکه العالم',
            'شبکه الکوثر بازدید', 'تعداد بازدید شبکه الکوثر','شبکه الکوثر (زمان)', 'زمان بازدید شبکه الکوثر',
             'شبکه پرس تی وی بازدید', 'تعداد بازدید شبکه پرس تی وی','شبکه پرس تی وی (زمان)', 'زمان بازدید شبکه پرس تی وی',
               'شبکه سپهر بازدید', 'تعداد بازدید شبکه سپهر','شبکه سپهر (زمان)', 'زمان بازدید شبکه سپهر',
            'شبکه جام جم بازدید', 'تعداد بازدید شبکه جام جم','شبکه جام جم (زمان)', 'زمان بازدید شبکه جام جم']       
worksheet_sar.write_row('A1', headings)  

######################### write columns #############################
#####################################################################

############################# شبکه 1 #################################
worksheet_sar.write_column('A2', ch_one5[0])  
worksheet_sar.write_column('B2', ch_one5[1]) 
worksheet_sar.write_column('C2', ch_one5[2])  
worksheet_sar.write_column('D2', ch_one5[3]) 
############################# شبکه 2 #################################
worksheet_sar.write_column('E2', ch_two5[0])  
worksheet_sar.write_column('F2', ch_two5[1]) 
worksheet_sar.write_column('G2', ch_two5[2])  
worksheet_sar.write_column('H2', ch_two5[3]) 
############################# شبکه 3 #################################
worksheet_sar.write_column('I2', ch_three5[0])  
worksheet_sar.write_column('J2', ch_three5[1]) 
worksheet_sar.write_column('K2', ch_three5[2])  
worksheet_sar.write_column('L2', ch_three5[3]) 
############################# شبکه 4 #################################
worksheet_sar.write_column('M2', ch_four5[0])  
worksheet_sar.write_column('N2', ch_four5[1]) 
worksheet_sar.write_column('O2', ch_four5[2])  
worksheet_sar.write_column('P2', ch_four5[3]) 
############################# شبکه 5 #################################
worksheet_sar.write_column('Q2', ch_five5[0])  
worksheet_sar.write_column('R2', ch_five5[1]) 
worksheet_sar.write_column('S2', ch_five5[2])  
worksheet_sar.write_column('T2', ch_five5[3]) 
############################# شبکه خبر #################################
worksheet_sar.write_column('U2', ch_khabar5[0])  
worksheet_sar.write_column('V2', ch_khabar5[1]) 
worksheet_sar.write_column('W2', ch_khabar5[2])  
worksheet_sar.write_column('X2', ch_khabar5[3]) 
############################# شبکه افق #################################
worksheet_sar.write_column('Y2', ch_ofogh5[0])  
worksheet_sar.write_column('Z2', ch_ofogh5[1]) 
worksheet_sar.write_column('AA2', ch_ofogh5[2])  
worksheet_sar.write_column('AB2', ch_ofogh5[3]) 
############################# شبکه پویا #################################
worksheet_sar.write_column('AC2', ch_pooya5[0])  
worksheet_sar.write_column('AD2', ch_pooya5[1]) 
worksheet_sar.write_column('AE2', ch_pooya5[2])  
worksheet_sar.write_column('AF2', ch_pooya5[3]) 
############################# شبکه امید #################################
worksheet_sar.write_column('AG2', ch_omid5[0])  
worksheet_sar.write_column('AH2', ch_omid5[1]) 
worksheet_sar.write_column('AI2', ch_omid5[2])  
worksheet_sar.write_column('AJ2', ch_omid5[3]) 
############################# شبکه آی فیلم #################################
worksheet_sar.write_column('AK2', ch_ifilm5[0])  
worksheet_sar.write_column('AL2', ch_ifilm5[1]) 
worksheet_sar.write_column('AM2', ch_ifilm5[2])  
worksheet_sar.write_column('AN2', ch_ifilm5[3]) 
############################# شبکه نمایش #################################
worksheet_sar.write_column('AO2', ch_namayesh5[0])  
worksheet_sar.write_column('AP2', ch_namayesh5[1]) 
worksheet_sar.write_column('AQ2', ch_namayesh5[2])  
worksheet_sar.write_column('AR2', ch_namayesh5[3]) 
############################# شبکه تماشا #################################
worksheet_sar.write_column('AS2', ch_tamasha5[0])  
worksheet_sar.write_column('AT2', ch_tamasha5[1]) 
worksheet_sar.write_column('AU2', ch_tamasha5[2])  
worksheet_sar.write_column('AV2', ch_tamasha5[3]) 
############################# شبکه مستند #################################
worksheet_sar.write_column('AW2', ch_mostanad5[0])  
worksheet_sar.write_column('AX2', ch_mostanad5[1]) 
worksheet_sar.write_column('AY2', ch_mostanad5[2])  
worksheet_sar.write_column('AZ2', ch_mostanad5[3]) 
############################# شبکه شما #################################
worksheet_sar.write_column('BA2', ch_shoma5[0])  
worksheet_sar.write_column('BB2', ch_shoma5[1]) 
worksheet_sar.write_column('BC2', ch_shoma5[2])  
worksheet_sar.write_column('BD2', ch_shoma5[3]) 
############################# شبکه آموزش #################################
worksheet_sar.write_column('BE2', ch_amozesh5[0])  
worksheet_sar.write_column('BF2', ch_amozesh5[1]) 
worksheet_sar.write_column('BG2', ch_amozesh5[2])  
worksheet_sar.write_column('BH2', ch_amozesh5[3]) 
############################# شبکه ورزش #################################
worksheet_sar.write_column('BI2', ch_varzesh5[0])  
worksheet_sar.write_column('BJ2', ch_varzesh5[1]) 
worksheet_sar.write_column('BK2', ch_varzesh5[2])  
worksheet_sar.write_column('BL2', ch_varzesh5[3]) 
############################# شبکه نسیم #################################
worksheet_sar.write_column('BM2', ch_nasim5[0])  
worksheet_sar.write_column('BN2', ch_nasim5[1]) 
worksheet_sar.write_column('BO2', ch_nasim5[2])  
worksheet_sar.write_column('BP2', ch_nasim5[3]) 
############################# شبکه قرآن #################################
worksheet_sar.write_column('BQ2', ch_qoran5[0])  
worksheet_sar.write_column('BR2', ch_qoran5[1]) 
worksheet_sar.write_column('BS2', ch_qoran5[2])  
worksheet_sar.write_column('BT2', ch_qoran5[3]) 
############################# شبکه سلامت #################################
worksheet_sar.write_column('BU2', ch_salamat5[0])  
worksheet_sar.write_column('BV2', ch_salamat5[1]) 
worksheet_sar.write_column('BW2', ch_salamat5[2])  
worksheet_sar.write_column('BX2', ch_salamat5[3]) 
############################# شبکه ایران کالا #################################
worksheet_sar.write_column('BY2', ch_irankala5[0])  
worksheet_sar.write_column('BZ2', ch_irankala5[1]) 
worksheet_sar.write_column('CA2', ch_irankala5[2])  
worksheet_sar.write_column('CB2', ch_irankala5[3]) 
############################# شبکه العالم #################################
worksheet_sar.write_column('CC2', ch_alalam5[0])  
worksheet_sar.write_column('CD2', ch_alalam5[1]) 
worksheet_sar.write_column('CE2', ch_alalam5[2])  
worksheet_sar.write_column('CF2', ch_alalam5[3]) 
############################# شبکه الکوثر #################################
worksheet_sar.write_column('CG2', ch_alkosar5[0])  
worksheet_sar.write_column('CH2', ch_alkosar5[1]) 
worksheet_sar.write_column('CI2', ch_alkosar5[2])  
worksheet_sar.write_column('CJ2', ch_alkosar5[3]) 
############################# شبکه پرس تی وی #################################
worksheet_sar.write_column('CK2', ch_presstv5[0])  
worksheet_sar.write_column('CL2', ch_presstv5[1]) 
worksheet_sar.write_column('CM2', ch_presstv5[2])  
worksheet_sar.write_column('CN2', ch_presstv5[3]) 
############################# شبکه سپهر #################################
worksheet_sar.write_column('CO2', ch_sepehr5[0])  
worksheet_sar.write_column('CP2', ch_sepehr5[1]) 
worksheet_sar.write_column('CQ2', ch_sepehr5[2])  
worksheet_sar.write_column('CR2', ch_sepehr5[3]) 
############################# شبکه جام جم #################################
worksheet_sar.write_column('CS2', ch_jamejam5[0])  
worksheet_sar.write_column('CT2', ch_jamejam5[1]) 
worksheet_sar.write_column('CU2', ch_jamejam5[2])  
worksheet_sar.write_column('CV2', ch_jamejam5[3]) 

workbook_sar.close()

#####################################################################
######################### channels data ekhtesasi #############################
#####################################################################

df_ekh_sum=df_ekh.groupby(['نام برنامه','نام شبکه']).sum().reset_index()
tt=len(df_ekh_sum)
for ii in range(0,tt):
    ff=df_ekh_sum.loc[ii,'نام شبکه']
############################# شبکه تیوا اسپورت #################################
    if ff=='تیوا اسپورت':
        p1_ekh=p1_ekh+1  
        ch_tva_sport.loc[p1_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_sport.loc[p1_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_sport.loc[p1_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
############################# شبکه تیوا اسپورت دو #################################
    if ff=='تیوا اسپورت دو': 
        p2_ekh=p2_ekh+1 
        ch_tva_sport_two.loc[p2_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_sport_two.loc[p2_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_sport_two.loc[p2_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
        ############################# شبکه تیوا آوند #################################
    if ff=='تیوا آوند': 
        p3_ekh=p3_ekh+1 
        ch_tva_avand.loc[p3_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_avand.loc[p3_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_avand.loc[p3_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
        ############################# شبکه تیوا دو #################################
    if ff=='تیوا دو': 
        p4_ekh=p4_ekh+1 
        ch_tva_two.loc[p4_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_two.loc[p4_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_two.loc[p4_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه تیوا فیلم #################################
    if ff=='تیوا فیلم': 
        p5_ekh=p5_ekh+1 
        ch_tva_film.loc[p5_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_film.loc[p5_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_film.loc[p5_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه تیوا کودک #################################
    if ff=='تیوا کودک': 
        p6_ekh=p6_ekh+1 
        ch_tva_kodak.loc[p6_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_kodak.loc[p6_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_kodak.loc[p6_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه تیوا نوا #################################
    if ff=='تیوا نوا': 
        p7_ekh=p7_ekh+1 
        ch_tva_nava.loc[p7_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_nava.loc[p7_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_nava.loc[p7_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه تیوا یک #################################
    if ff=='تیوا یک': 
        p8_ekh=p8_ekh+1 
        ch_tva_one.loc[p8_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_tva_one.loc[p8_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_tva_one.loc[p8_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه سرباز ماهر #################################
    if ff=='سرباز ماهر': 
        p9_ekh=p9_ekh+1 
        ch_sarbaz_maher.loc[p9_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_sarbaz_maher.loc[p9_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_sarbaz_maher.loc[p9_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه شاپرک #################################
    if ff=='شاپرک': 
        p10_ekh=p10_ekh+1 
        ch_shaparak.loc[p10_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_shaparak.loc[p10_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_shaparak.loc[p10_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه کودک دیجیتون #################################
    if ff=='کودک دیجیتون': 
        p11_ekh=p11_ekh+1 
        ch_kodak_digiton.loc[p11_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_kodak_digiton.loc[p11_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_kodak_digiton.loc[p11_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه لنز اسپورت پلاس #################################
    if ff=='لنز اسپورت پلاس': 
        p12_ekh=p12_ekh+1 
        ch_lenz_sport_plus.loc[p12_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_lenz_sport_plus.loc[p12_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_lenz_sport_plus.loc[p12_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه لنزاسپورت #################################
    if ff=='لنزاسپورت': 
        p13_ekh=p13_ekh+1 
        ch_lenz_sport.loc[p13_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_lenz_sport.loc[p13_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_lenz_sport.loc[p13_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
#        ############################# شبکه محفل #################################
    if ff=='محفل': 
        p14_ekh=p14_ekh+1 
        ch_mahfel.loc[p14_ekh,'نام برنامه']=df_ekh_sum.loc[ii,'نام برنامه']
        ch_mahfel.loc[p14_ekh,'تعداد بازدید']=df_ekh_sum.loc[ii,'تعداد بازدید']
        ch_mahfel.loc[p14_ekh,'مدت بازدید']=df_ekh_sum.loc[ii,'مدت بازدید']
############################# شبکه تیوا اسپورت #################################
ch_tva_sport1=[]
ch_tva_sport2=[]
ch_tva_sport3=[]
ch_tva_sport4=[]
ch_tva_sport5=[]
ch_tva_sport.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_sport1=ch_tva_sport["نام برنامه"].tolist()
ch_tva_sport5.append(ch_tva_sport1)
ch_tva_sport2=ch_tva_sport["تعداد بازدید"].tolist()
ch_tva_sport5.append(ch_tva_sport2)
ch_tva_sport.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_sport3=ch_tva_sport["نام برنامه"].tolist()
ch_tva_sport5.append(ch_tva_sport3)
ch_tva_sport4=ch_tva_sport["مدت بازدید"].tolist()
ch_tva_sport5.append(ch_tva_sport4)
############################# شبکه تیوا اسپورت دو #################################
ch_tva_sport_two1=[]
ch_tva_sport_two2=[]
ch_tva_sport_two3=[]
ch_tva_sport_two4=[]
ch_tva_sport_two5=[]
ch_tva_sport_two.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_sport_two1=ch_tva_sport_two["نام برنامه"].tolist()
ch_tva_sport_two5.append(ch_tva_sport_two1)
ch_tva_sport_two2=ch_tva_sport_two["تعداد بازدید"].tolist()
ch_tva_sport_two5.append(ch_tva_sport_two2)
ch_tva_sport_two.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_sport_two3=ch_tva_sport_two["نام برنامه"].tolist()
ch_tva_sport_two5.append(ch_tva_sport_two3)
ch_tva_sport_two4=ch_tva_sport_two["مدت بازدید"].tolist()
ch_tva_sport_two5.append(ch_tva_sport_two4)
############################# شبکه تیوا آوند #################################
ch_tva_avand1=[]
ch_tva_avand2=[]
ch_tva_avand3=[]
ch_tva_avand4=[]
ch_tva_avand5=[]
ch_tva_avand.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_avand1=ch_tva_avand["نام برنامه"].tolist()
ch_tva_avand5.append(ch_tva_avand1)
ch_tva_avand2=ch_tva_avand["تعداد بازدید"].tolist()
ch_tva_avand5.append(ch_tva_avand2)
ch_tva_avand.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_avand3=ch_tva_avand["نام برنامه"].tolist()
ch_tva_avand5.append(ch_tva_avand3)
ch_tva_avand4=ch_tva_avand["مدت بازدید"].tolist()
ch_tva_avand5.append(ch_tva_avand4)
############################# شبکه تیوا دو #################################
ch_tva_two1=[]
ch_tva_two2=[]
ch_tva_two3=[]
ch_tva_two4=[]
ch_tva_two5=[]
ch_tva_two.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_two1=ch_tva_two["نام برنامه"].tolist()
ch_tva_two5.append(ch_tva_two1)
ch_tva_two2=ch_tva_two["تعداد بازدید"].tolist()
ch_tva_two5.append(ch_tva_two2)
ch_tva_two.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_two3=ch_tva_two["نام برنامه"].tolist()
ch_tva_two5.append(ch_tva_two3)
ch_tva_two4=ch_tva_two["مدت بازدید"].tolist()
ch_tva_two5.append(ch_tva_two4)
############################## شبکه تیوا فیلم #################################
ch_tva_film1=[]
ch_tva_film2=[]
ch_tva_film3=[]
ch_tva_film4=[]
ch_tva_film5=[]
ch_tva_film.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_film1=ch_tva_film["نام برنامه"].tolist()
ch_tva_film5.append(ch_tva_film1)
ch_tva_film2=ch_tva_film["تعداد بازدید"].tolist()
ch_tva_film5.append(ch_tva_film2)
ch_tva_film.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_film3=ch_tva_film["نام برنامه"].tolist()
ch_tva_film5.append(ch_tva_film3)
ch_tva_film4=ch_tva_film["مدت بازدید"].tolist()
ch_tva_film5.append(ch_tva_film4)
############################## شبکه تیوا کودک #################################
ch_tva_kodak1=[]
ch_tva_kodak2=[]
ch_tva_kodak3=[]
ch_tva_kodak4=[]
ch_tva_kodak5=[]
ch_tva_kodak.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_kodak1=ch_tva_kodak["نام برنامه"].tolist()
ch_tva_kodak5.append(ch_tva_kodak1)
ch_tva_kodak2=ch_tva_kodak["تعداد بازدید"].tolist()
ch_tva_kodak5.append(ch_tva_kodak2)
ch_tva_kodak.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_kodak3=ch_tva_kodak["نام برنامه"].tolist()
ch_tva_kodak5.append(ch_tva_kodak3)
ch_tva_kodak4=ch_tva_kodak["مدت بازدید"].tolist()
ch_tva_kodak5.append(ch_tva_kodak4)
############################## شبکه تیوا نوا #################################
ch_tva_nava1=[]
ch_tva_nava2=[]
ch_tva_nava3=[]
ch_tva_nava4=[]
ch_tva_nava5=[]
ch_tva_nava.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_nava1=ch_tva_nava["نام برنامه"].tolist()
ch_tva_nava5.append(ch_tva_nava1)
ch_tva_nava2=ch_tva_nava["تعداد بازدید"].tolist()
ch_tva_nava5.append(ch_tva_nava2)
ch_tva_nava.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_nava3=ch_tva_nava["نام برنامه"].tolist()
ch_tva_nava5.append(ch_tva_nava3)
ch_tva_nava4=ch_tva_nava["مدت بازدید"].tolist()
ch_tva_nava5.append(ch_tva_nava4)
############################## شبکه تیوا یک #################################
ch_tva_one1=[]
ch_tva_one2=[]
ch_tva_one3=[]
ch_tva_one4=[]
ch_tva_one5=[]
ch_tva_one.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_one1=ch_tva_one["نام برنامه"].tolist()
ch_tva_one5.append(ch_tva_one1)
ch_tva_one2=ch_tva_one["تعداد بازدید"].tolist()
ch_tva_one5.append(ch_tva_one2)
ch_tva_one.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_tva_one3=ch_tva_one["نام برنامه"].tolist()
ch_tva_one5.append(ch_tva_one3)
ch_tva_one4=ch_tva_one["مدت بازدید"].tolist()
ch_tva_one5.append(ch_tva_one4)
############################## شبکه سرباز ماهر #################################
ch_sarbaz_maher1=[]
ch_sarbaz_maher2=[]
ch_sarbaz_maher3=[]
ch_sarbaz_maher4=[]
ch_sarbaz_maher5=[]
ch_sarbaz_maher.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_sarbaz_maher1=ch_sarbaz_maher["نام برنامه"].tolist()
ch_sarbaz_maher5.append(ch_sarbaz_maher1)
ch_sarbaz_maher2=ch_sarbaz_maher["تعداد بازدید"].tolist()
ch_sarbaz_maher5.append(ch_sarbaz_maher2)
ch_sarbaz_maher.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_sarbaz_maher3=ch_sarbaz_maher["نام برنامه"].tolist()
ch_sarbaz_maher5.append(ch_sarbaz_maher3)
ch_sarbaz_maher4=ch_sarbaz_maher["مدت بازدید"].tolist()
ch_sarbaz_maher5.append(ch_sarbaz_maher4)
############################## شبکه شاپرک #################################
ch_shaparak1=[]
ch_shaparak2=[]
ch_shaparak3=[]
ch_shaparak4=[]
ch_shaparak5=[]
ch_shaparak.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_shaparak1=ch_shaparak["نام برنامه"].tolist()
ch_shaparak5.append(ch_shaparak1)
ch_shaparak2=ch_shaparak["تعداد بازدید"].tolist()
ch_shaparak5.append(ch_shaparak2)
ch_shaparak.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_shaparak3=ch_shaparak["نام برنامه"].tolist()
ch_shaparak5.append(ch_shaparak3)
ch_shaparak4=ch_shaparak["مدت بازدید"].tolist()
ch_shaparak5.append(ch_shaparak4)
############################## شبکه کودک دیجیتون #################################
ch_shaparak1=[]
ch_kodak_digiton2=[]
ch_kodak_digiton3=[]
ch_kodak_digiton4=[]
ch_kodak_digiton5=[]
ch_kodak_digiton.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_kodak_digiton1=ch_kodak_digiton["نام برنامه"].tolist()
ch_kodak_digiton5.append(ch_kodak_digiton1)
ch_kodak_digiton2=ch_kodak_digiton["تعداد بازدید"].tolist()
ch_kodak_digiton5.append(ch_kodak_digiton2)
ch_kodak_digiton.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_kodak_digiton3=ch_kodak_digiton["نام برنامه"].tolist()
ch_kodak_digiton5.append(ch_kodak_digiton3)
ch_kodak_digiton4=ch_kodak_digiton["مدت بازدید"].tolist()
ch_kodak_digiton5.append(ch_kodak_digiton4)
############################## شبکه لنز اسپورت پلاس #################################
ch_lenz_sport_plus1=[]
ch_lenz_sport_plus2=[]
ch_lenz_sport_plus3=[]
ch_lenz_sport_plus4=[]
ch_lenz_sport_plus5=[]
ch_lenz_sport_plus.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_lenz_sport_plus1=ch_lenz_sport_plus["نام برنامه"].tolist()
ch_lenz_sport_plus5.append(ch_lenz_sport_plus1)
ch_lenz_sport_plus2=ch_lenz_sport_plus["تعداد بازدید"].tolist()
ch_lenz_sport_plus5.append(ch_lenz_sport_plus2)
ch_lenz_sport_plus.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_lenz_sport_plus3=ch_lenz_sport_plus["نام برنامه"].tolist()
ch_lenz_sport_plus5.append(ch_lenz_sport_plus3)
ch_lenz_sport_plus4=ch_lenz_sport_plus["مدت بازدید"].tolist()
ch_lenz_sport_plus5.append(ch_lenz_sport_plus4)
############################## شبکه لنزاسپورت #################################
ch_lenz_sport1=[]
ch_lenz_sport2=[]
ch_lenz_sport3=[]
ch_lenz_sport4=[]
ch_lenz_sport5=[]
ch_lenz_sport.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_lenz_sport1=ch_lenz_sport["نام برنامه"].tolist()
ch_lenz_sport5.append(ch_lenz_sport1)
ch_lenz_sport2=ch_lenz_sport["تعداد بازدید"].tolist()
ch_lenz_sport5.append(ch_lenz_sport2)
ch_lenz_sport.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_lenz_sport3=ch_lenz_sport["نام برنامه"].tolist()
ch_lenz_sport5.append(ch_lenz_sport3)
ch_lenz_sport4=ch_lenz_sport["مدت بازدید"].tolist()
ch_lenz_sport5.append(ch_lenz_sport4)
############################## شبکه محفل #################################
ch_mahfel1=[]
ch_mahfel2=[]
ch_mahfel3=[]
ch_mahfel4=[]
ch_mahfel5=[]
ch_mahfel.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_mahfel1=ch_mahfel["نام برنامه"].tolist()
ch_mahfel5.append(ch_mahfel1)
ch_mahfel2=ch_mahfel["تعداد بازدید"].tolist()
ch_mahfel5.append(ch_mahfel2)
ch_mahfel.sort_values('مدت بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
ch_mahfel3=ch_mahfel["نام برنامه"].tolist()
ch_mahfel5.append(ch_mahfel3)
ch_mahfel4=ch_mahfel["مدت بازدید"].tolist()
ch_mahfel5.append(ch_mahfel4)
#####################################################################

bold = workbook_ekh.add_format({'bold': 1})  
headings = ['شبکه تیوا اسپرت بازدید', 'تعداد بازدید شبکه تیوا اسپرت','شبکه تیوا اسپرت (زمان)', 'زمان بازدید شبکه تیوا اسپرت'
            ,'شبکه تیوا اسپرت 2 بازدید', 'تعداد بازدید شبکه تیوا اسپرت 2','شبکه تیوا اسپرت 2 (زمان)', 'زمان بازدید شبکه تیوا اسپرت 2',
            'شبکه تیوا آوند بازدید', 'تعداد بازدید شبکه تیوا آوند','شبکه تیوا آوند (زمان)', 'زمان بازدید شبکه تیوا آوند',
            'شبکه تیوا دو بازدید', 'تعداد بازدید شبکه تیوا دو','شبکه تیوا دو (زمان)', 'زمان بازدید شبکه تیوا دو',
            'تیوا فیلم بازدید', 'تعداد بازدید تیوا فیلم','تیوا فیلم (زمان)', 'زمان بازدید تیوا فیلم',
            'تیوا کودک بازدید', 'تعداد بازدید تیوا کودک','تیوا کودک (زمان)', 'زمان بازدید تیوا کودک',
            'تیوا نوا بازدید', 'تعداد بازدید تیوا نوا','تیوا نوا (زمان)', 'زمان بازدید تیوا نوا',
            'تیوا یک بازدید', 'تعداد بازدید تیوا یک','تیوا یک (زمان)', 'زمان بازدید تیوا یک',
            'سرباز ماهر بازدید', 'تعداد بازدید سرباز ماهر','سرباز ماهر (زمان)', 'زمان بازدید سرباز ماهر',
            'شاپرک بازدید', 'تعداد بازدید شاپرک','شاپرک (زمان)', 'زمان بازدید شاپرک',
            'کودک دیجیتون بازدید', 'تعداد بازدید کودک دیجیتون','کودک دیجیتون (زمان)', 'زمان بازدید کودک دیجیتون',
            'لنز اسپرت پلاس بازدید', 'تعداد بازدید لنز اسپرت پلاس','لنز اسپرت پلاس (زمان)', 'زمان بازدید لنز اسپرت پلاس',
            'لنز اسپرت بازدید', 'تعداد بازدید لنز اسپرت','لنز اسپرت (زمان)', 'زمان بازدید لنز اسپرت',
            'محفل بازدید', 'تعداد بازدید محفل','محفل (زمان)', 'زمان بازدید محفل']       
worksheet_ekh.write_row('A1', headings)  
#####################################################################
######################### write columns #############################
#####################################################################

############################# شبکه تیوا اسپرت #################################
worksheet_ekh.write_column('A2', ch_tva_sport5[0])  
worksheet_ekh.write_column('B2', ch_tva_sport5[1]) 
worksheet_ekh.write_column('C2', ch_tva_sport5[2])  
worksheet_ekh.write_column('D2', ch_tva_sport5[3]) 
############################# شبکه تیوا اسپرت 2 #################################
worksheet_ekh.write_column('E2', ch_tva_sport_two5[0])  
worksheet_ekh.write_column('F2', ch_tva_sport_two5[1]) 
worksheet_ekh.write_column('G2', ch_tva_sport_two5[2])  
worksheet_ekh.write_column('H2', ch_tva_sport_two5[3]) 
############################# شبکه تیوا آوند #################################
worksheet_ekh.write_column('I2', ch_tva_avand5[0])  
worksheet_ekh.write_column('J2', ch_tva_avand5[1]) 
worksheet_ekh.write_column('K2', ch_tva_avand5[2])  
worksheet_ekh.write_column('L2', ch_tva_avand5[3]) 
############################# شبکه تیوا دو #################################
worksheet_ekh.write_column('M2', ch_tva_two5[0])  
worksheet_ekh.write_column('N2', ch_tva_two5[1]) 
worksheet_ekh.write_column('O2', ch_tva_two5[2])  
worksheet_ekh.write_column('P2', ch_tva_two5[3]) 
############################## شبکه تیوا فیلم #################################
worksheet_ekh.write_column('Q2', ch_tva_film5[0])  
worksheet_ekh.write_column('R2', ch_tva_film5[1]) 
worksheet_ekh.write_column('S2', ch_tva_film5[2])  
worksheet_ekh.write_column('T2', ch_tva_film5[3]) 
############################## شبکه تیوا کودک #################################
worksheet_ekh.write_column('U2', ch_tva_kodak5[0])  
worksheet_ekh.write_column('V2', ch_tva_kodak5[1]) 
worksheet_ekh.write_column('W2', ch_tva_kodak5[2])  
worksheet_ekh.write_column('X2', ch_tva_kodak5[3]) 
############################## شبکه تیوا نوا #################################
worksheet_ekh.write_column('Y2', ch_tva_nava5[0])  
worksheet_ekh.write_column('Z2', ch_tva_nava5[1]) 
worksheet_ekh.write_column('AA2', ch_tva_nava5[2])  
worksheet_ekh.write_column('AB2', ch_tva_nava5[3]) 
############################## شبکه تیوا یک #################################
worksheet_ekh.write_column('AC2', ch_tva_one5[0])  
worksheet_ekh.write_column('AD2', ch_tva_one5[1]) 
worksheet_ekh.write_column('AE2', ch_tva_one5[2])  
worksheet_ekh.write_column('AF2', ch_tva_one5[3]) 
############################## شبکه سرباز ماهر #################################
worksheet_ekh.write_column('AG2', ch_sarbaz_maher5[0])  
worksheet_ekh.write_column('AH2', ch_sarbaz_maher5[1]) 
worksheet_ekh.write_column('AI2', ch_sarbaz_maher5[2])  
worksheet_ekh.write_column('AJ2', ch_sarbaz_maher5[3]) 
############################## شبکه شاپرک #################################
worksheet_ekh.write_column('AK2', ch_shaparak5[0])  
worksheet_ekh.write_column('AL2', ch_shaparak5[1]) 
worksheet_ekh.write_column('AM2', ch_shaparak5[2])  
worksheet_ekh.write_column('AN2', ch_shaparak5[3]) 
############################## شبکه کودک دیجیتون #################################
worksheet_ekh.write_column('AO2', ch_kodak_digiton5[0])  
worksheet_ekh.write_column('AP2', ch_kodak_digiton5[1]) 
worksheet_ekh.write_column('AQ2', ch_kodak_digiton5[2])  
worksheet_ekh.write_column('AR2', ch_kodak_digiton5[3]) 
############################## شبکه لنز اسپرت پلاس #################################
worksheet_ekh.write_column('AS2', ch_lenz_sport_plus5[0])  
worksheet_ekh.write_column('AT2', ch_lenz_sport_plus5[1]) 
worksheet_ekh.write_column('AU2', ch_lenz_sport_plus5[2])  
worksheet_ekh.write_column('AV2', ch_lenz_sport_plus5[3]) 
############################## شبکه لنز اسپرت #################################
worksheet_ekh.write_column('AW2', ch_lenz_sport5[0])  
worksheet_ekh.write_column('AX2', ch_lenz_sport5[1]) 
worksheet_ekh.write_column('AY2', ch_lenz_sport5[2])  
worksheet_ekh.write_column('AZ2', ch_lenz_sport5[3]) 
############################## شبکه محفل #################################
worksheet_ekh.write_column('BA2', ch_mahfel5[0])  
worksheet_ekh.write_column('BB2', ch_mahfel5[1]) 
worksheet_ekh.write_column('BC2', ch_mahfel5[2])  
worksheet_ekh.write_column('BD2', ch_mahfel5[3]) 

workbook_ekh.close()

df_sar_operator=df_sar.groupby(['اپراتور']).sum().reset_index()
sima_operators_visit={'operators_name': df_sar_operator['اپراتور'],
                       'operators_visit': df_sar_operator['تعداد بازدید']}
sima_operators_visit=pd.DataFrame(sima_operators_visit, columns=['operators_name', 'operators_visit'])
#####################################################################
df_sar_all_channels=df_sar.groupby(['نام شبکه']).sum().reset_index()
sima_channels_visit={'channels_names': df_sar_all_channels['نام شبکه'],
                      'channels_visit': df_sar_all_channels['تعداد بازدید']}
sima_channels_visit=pd.DataFrame(sima_channels_visit, columns=['channels_names', 'channels_visit'])
sima_channels_visit.sort_values('channels_visit', axis = 0, ascending = True, inplace = True, na_position ='last')
#####################################################################   
programs_all=df_sar.groupby(['نام برنامه']).sum().reset_index()
programs_alll=programs_all.sum(axis = 0, skipna = True)
programs_all_visits=programs_alll[5]
programs_all_duration=programs_alll[4]
programs_all_duration=round(programs_all_duration*60,0)
programs_all_contents=len(programs_all)
program_data={'parameters': ['visit', 'duration', 'content_number'],
              'parameters_count': [programs_all_visits, programs_all_duration, programs_all_contents]}
program_data=pd.DataFrame(program_data, columns=['parameters', 'parameters_count'])

################################# monthly visitors ####################################
operators_name=[get_display(arabic_reshaper.reshape('آنتن')),
                                        get_display(arabic_reshaper.reshape('تلوبیون')),
                                        get_display(arabic_reshaper.reshape('تیوا')),
                                        get_display(arabic_reshaper.reshape('سایت شبکه ها')),
                                        get_display(arabic_reshaper.reshape('سپهر')),
                                        get_display(arabic_reshaper.reshape('شیما')),
                                        get_display(arabic_reshaper.reshape('لنز'))]
operators_visitors= [5245,425,421,4253,533,35,3233]
################################# شبکه اختصاصی کودک ####################################
ch_one_visit=ch_one.sum(axis = 0, skipna = True)              # شبکه اختصاصی اول
ch_two_visit=ch_one.sum(axis = 0, skipna = True)              # شبکه اختصاصی دوم
ch_lenz_sport_visit=ch_one.sum(axis = 0, skipna = True)       # شبکه اختصاصی سوم
ch_shaparak_visit=ch_one.sum(axis = 0, skipna = True)         # شبکه اختصاصی چهارم
channels_name_child=[get_display(arabic_reshaper.reshape('پویا')),
                     get_display(arabic_reshaper.reshape('دیجیتون')),
                     get_display(arabic_reshaper.reshape('شاپرک')),
                     get_display(arabic_reshaper.reshape('تیوا کودک'))]
channels_visits_child=[ch_one_visit[1],ch_two_visit[1], ch_lenz_sport_visit[1], ch_shaparak_visit[1]]
ch_one_contents=len(ch_one1)
ch_two_contents=len(ch_one3)
ch_lenz_sport_contents=len(ch_two1)
ch_shaparak_contents=len(ch_two3)
channels_contents_child=[ch_one_contents, ch_two_contents, ch_lenz_sport_contents, ch_shaparak_contents]

################################# شبکه اختصاصی ورزش ####################################
ch_one_visit=ch_one.sum(axis = 0, skipna = True)              # شبکه اختصاصی اول
ch_two_visit=ch_one.sum(axis = 0, skipna = True)              # شبکه اختصاصی دوم
ch_lenz_sport_visit=ch_one.sum(axis = 0, skipna = True)       # شبکه اختصاصی سوم
ch_shaparak_visit=ch_one.sum(axis = 0, skipna = True)         # شبکه اختصاصی چهارم
channels_name_sports=[get_display(arabic_reshaper.reshape('ورزش')),
                     get_display(arabic_reshaper.reshape('لنز اسپرت')),
                     get_display(arabic_reshaper.reshape('لنز اسپرت پلاس')),
                     get_display(arabic_reshaper.reshape('استقلال'))]
channels_visits_sports=[ch_one_visit[1],ch_two_visit[1], ch_lenz_sport_visit[1], ch_shaparak_visit[1]]
ch_one_contents=len(ch_one1)
ch_two_contents=len(ch_one3)
ch_lenz_sport_contents=len(ch_two1)
ch_shaparak_contents=len(ch_two3)
channels_contents_sports=[ch_one_contents, ch_two_contents, ch_lenz_sport_contents, ch_shaparak_contents]
##################################################################### 
#####################################################################     

def place_value(number):      # comma seperation
    return ("{:,}".format(number)) 
#####################################################################
font = {'family' : 'B Nazanin',
        'weight' : 'bold',
        'size'   : 22}

text_font = {'fontname':'B Nazanin', 'size':'12', 'color':'black', 'weight':'bold', 'verticalalignment':'center'}
num_font = {'fontname':'B Nazanin', 'size':'12', 'color':'black', 'weight':'bold', 'verticalalignment':'center','num_format': '#,##'}


Data_all_channels={'channels': [get_display(arabic_reshaper.reshape('افق')),get_display(arabic_reshaper.reshape('العالم')), 
                                get_display(arabic_reshaper.reshape('الکوثر')),get_display(arabic_reshaper.reshape('امید')), 
                                get_display(arabic_reshaper.reshape('ایران کالا')),get_display(arabic_reshaper.reshape('آموزش')), 
                                get_display(arabic_reshaper.reshape('آی فیلم')),get_display(arabic_reshaper.reshape('پرس تی وی')), 
                                get_display(arabic_reshaper.reshape('پویا')),get_display(arabic_reshaper.reshape('تماشا')), 
                                get_display(arabic_reshaper.reshape('خبر')),get_display(arabic_reshaper.reshape('سلامت')), 
                                get_display(arabic_reshaper.reshape('شبکه 1')),get_display(arabic_reshaper.reshape('شبکه 2')), 
                                get_display(arabic_reshaper.reshape('شبکه 3')),get_display(arabic_reshaper.reshape('شبکه 4')), 
                                get_display(arabic_reshaper.reshape('شبکه 5')),get_display(arabic_reshaper.reshape('شما')), 
                                get_display(arabic_reshaper.reshape('قرآن')),get_display(arabic_reshaper.reshape('مستند')), 
                                get_display(arabic_reshaper.reshape('نسیم')),get_display(arabic_reshaper.reshape('نمایش')), 
                                get_display(arabic_reshaper.reshape('ورزش')),get_display(arabic_reshaper.reshape('سپهر')),
                                get_display(arabic_reshaper.reshape('جام جم 1'))], 
                   'visits_channels': df_sar_all_channels['تعداد بازدید']}
############################################# شبکه یک #############################################
df_sar_barh_all_channels=pd.DataFrame(Data_all_channels, columns=['channels', 'visits_channels'])
#Data_ch_one={'shabake1': [get_display(arabic_reshaper.reshape(ch_one1[0])),get_display(arabic_reshaper.reshape(ch_one1[1])),get_display(arabic_reshaper.reshape(ch_one1[2]))],
#       'shabake11': [ch_one2[0],ch_one2[1],ch_one2[2]]
#       }
#df_sar_ch_one = pd.DataFrame(Data_ch_one,columns=['shabake1','shabake11'])
############################################# شبکه دو #############################################
#Data_ch_two={'shabake2': [get_display(arabic_reshaper.reshape(ch_two1[0])),get_display(arabic_reshaper.reshape(ch_two1[1])),get_display(arabic_reshaper.reshape(ch_two1[2]))],
#       'shabake22': [ch_two2[0],ch_two2[1],ch_two2[2]]
#       }
#df_sar_ch_two = pd.DataFrame(Data_ch_two,columns=['shabake2','shabake22'])
############################################# شبکه یک #############################################
data_operators_visits={'operators':[get_display(arabic_reshaper.reshape('لنز')), get_display(arabic_reshaper.reshape('تیوا')), 
                                    get_display(arabic_reshaper.reshape('فام')), get_display(arabic_reshaper.reshape('آیو'))],
                       'visits_operators':df_sar_operator['تعداد بازدید']}
df_sar_pie_operators=pd.DataFrame(data_operators_visits, columns=['operators', 'visits_operators'])

def func(pct, allvalues):    #values and perecentage in pie graph
         absolute = int(pct / 100.*np.sum(allvalues)) 
         return "{:.1f}%\n\n{:d}".format(pct, absolute) 
#         return "{:.1f}%\n({:d} g)".format(pct, absolute)
################################################بازدید اپراتورها به تفکیک#######################################################
lenz_visits=df_sar_pie_operators.iat[0,1]
tva_visits=df_sar_pie_operators.iat[1,1]
fam_visits=df_sar_pie_operators.iat[2,1]
aio_visits=df_sar_pie_operators.iat[3,1]
#print(fam_visits)

 ################################# ده محتوای پربازدید ####################################
df_sar_all_content_visit=df_sar.groupby(['نام برنامه']).sum().reset_index()
df_sar_all_content_visit.sort_values('تعداد بازدید', axis = 0, ascending = False, inplace = True, na_position ='last')
#df_sar_all_content_visit=df_sar_all_content_visit.drop(columns=['تاریخ شروع', 'میانگین','تاریخ پایان', 'مدت بازدید','ساعت','تاریخ','ردیف','جنس','نام برنامه اولیه'])
content_popular_visit=[]
content_popular_visitnumber=[]
content_popular_name=[]
content_popular_name=df_sar_all_content_visit["نام برنامه"].tolist()
content_popular_visit.append(content_popular_name)
content_popular_visitnumber=df_sar_all_content_visit["تعداد بازدید"].tolist()
content_popular_visit.append(content_popular_visitnumber)
content_popular_visit_data={'content_popular_name_data' : [get_display(arabic_reshaper.reshape(content_popular_name[0])), 
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
df_sar_content_popular_visit=pd.DataFrame(content_popular_visit_data, columns=['content_popular_name_data' , 'content_popular_visitnumber_data'])
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
df_sar_content_popular_visit_persection_data=pd.DataFrame(content_popular_visit_persection_data, columns=['content_popular_name_persection_data' , 'content_popular_visitnumber_persection_data']) 
df_sar_content_popular_visit_persection_data.sort_values('content_popular_visitnumber_persection_data', axis = 0, ascending = False, inplace = True, na_position ='last')
 ################################# توزیع ژانر محتواها ####################################
#genre_content_popular=[]



#######################################################################################################
########################################### گزارش رئیس سازمان #########################################
########################################################################################################

with PdfPages(r'C:\Users\PC\Desktop\total statistics\گزارش رئیس سازمان.pdf') as export_pdf:
    #################################### تعداد بازدید و تعداد محتوا و مدت زمان محتواها ######################################     
     firstPage = plt.figure(figsize=(10,12))
     firstPage.clf()
     txt1 = get_display(arabic_reshaper.reshape('به نام خداوند بخشنده مهربان'))
     firstPage.text(0.5,0.2,txt1, transform=firstPage.transFigure, size=24, ha="center")
     export_pdf.savefig()
     plt.close()
     df_sarall_visits=pd.DataFrame()
     df_sarall_visits[get_display(arabic_reshaper.reshape('نام محتوا'))]=[programs_all_contents]
     df_sarall_visits[get_display(arabic_reshaper.reshape('تعداد بازدید کل محتواهای سازمان'))]=[programs_all_visits]
     df_sarall_visits[get_display(arabic_reshaper.reshape('مدت زمان بازدید کل محتواهای \n\n سازمان (به دقیقه)'))]=[programs_all_duration]
     fig = plt.figure(figsize=(10,12))
     plt.subplot(111)
     plt.axis('off')
     plt.title(get_display(arabic_reshaper.reshape('تعداد محتوا، بازدید و مدت زمان بازدید کل شبکه های سازمان\n')),
               fontweight ="bold",
               fontsize=18,
               loc="center") 
     plt.table(cellText=df_sarall_visits.values, 
               colLabels=df_sarall_visits.columns,
               colWidths=[1] * 3,
               bbox=[0,0,1,1], 
               edges='closed',
               rowLoc='center',
#               rowColours=["palegreen"] * 16,
               colColours=["palegreen"] * 12,
               cellLoc='center')     
     plt.subplots_adjust(left=.1, top=.8)
     export_pdf.savefig()
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
     rects1=plt.barh(df_sar_barh_all_channels['channels'], df_sar_barh_all_channels['visits_channels'], 
                     color='blue', 
                     align='center', 
                     alpha=0.5)
     for i, v in enumerate(df_sar_barh_all_channels['visits_channels']):
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
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     export_pdf.savefig()
     plt.show()
     plt.close()
     #################################تعداد بازدید اپراتورها####################################
     colors=('aqua', 'dodgerblue', 'deepskyblue', 'blue')
     plt.figure(figsize=(9, 6))
     plt.pie(df_sar_pie_operators['visits_operators'], labels=df_sar_pie_operators['operators'], shadow=False, colors=colors, explode=(0.1, 0, 0.1, 0), 
             startangle=50, autopct=lambda pct: func(pct, df_sar_pie_operators['visits_operators']))
     plt.title(get_display(arabic_reshaper.reshape('تعداد بازدید اپراتورها')), fontsize=22, fontname='B Nazanin', weight="bold")
     plt.legend(df_sar_pie_operators['operators'], loc="best")
     plt.axis('equal')
#     plot=df_saroperator.plot.pie(y='radius', title=get_display(arabic_reshaper.reshape('بازدید اپراتورها')), legend=False, 
#                   autopct='%1.1f%%', explode=(0.05, 0.05, 0.05), shadow=True, startangle=0, colors=colors, figsize=(6,6))
     export_pdf.savefig()
     plt.show()
     plt.close()
 #################################تعداد کاربران فعال اپراتورها####################################
     plt.figure(figsize=(9, 6))
     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(operators_name, operators_visitors, color='aqua', width=0.75, align='center', alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('کاربران فعال ماهانه اپراتورها')), fontsize=18, fontname='B Nazanin', weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام اپراتور')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد کاربر فعال')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.rc('font', family='B Nazanin', size=16, weight="bold")
     plt.text(-0.25,operators_visitors[0]+150, operators_visitors[0],  **text1_font)
     plt.text(0.90,operators_visitors[1]+150, operators_visitors[1],  **text1_font)
     plt.text(1.90,operators_visitors[2]+150, operators_visitors[2],  **text1_font)
     plt.text(2.90,operators_visitors[3]+150, operators_visitors[3],  **text1_font)
     plt.text(3.90,operators_visitors[4]+150, operators_visitors[4],  **text1_font)
     plt.text(4.90,operators_visitors[5]+150, operators_visitors[5],  **text1_font)
     plt.text(5.90,operators_visitors[6]+150, operators_visitors[6],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     export_pdf.savefig()
     plt.show()
     plt.close()
 ################################# آمار بازدید شبکه های کودک ####################################
     plt.figure(figsize=(8, 9))
     plt.suptitle(get_display(arabic_reshaper.reshape('آمار شبکه های اختصاصی کودک')), fontsize=24, fontname='B Nazanin', weight="bold") 
     plt.subplot(211)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(channels_name_child, channels_visits_child, color='aqua', width=0.75, align='center', alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('تعداد بازدید از شبکه های اختصاصی کودک')), fontsize=18, fontname='B Nazanin', weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام شبکه ها')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.rc('font', family='B Nazanin', size=16, weight="bold")
     plt.text(-0.1,channels_visits_child[0]+10000, channels_visits_child[0],  **text1_font)
     plt.text(0.90,channels_visits_child[1]+10000, channels_visits_child[1],  **text1_font)
     plt.text(1.90,channels_visits_child[2]+10000, channels_visits_child[2],  **text1_font)
     plt.text(2.90,channels_visits_child[3]+10000, channels_visits_child[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     plt.subplot(212)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(channels_name_child, channels_contents_child, color='aqua', width=0.75, align='center', alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('تعداد محتواهای شبکه های اختصاصی کودک')), fontsize=18, fontname='B Nazanin', weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام شبکه')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد محتوا')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.rc('font', family='B Nazanin', size=16, weight="bold")
     plt.text(-0.1,channels_contents_child[0]+10000, channels_contents_child[0],  **text1_font)
     plt.text(0.90,channels_contents_child[1]+10000, channels_contents_child[1],  **text1_font)
     plt.text(1.90,channels_contents_child[2]+10000, channels_contents_child[2],  **text1_font)
     plt.text(2.90,channels_contents_child[3]+10000, channels_contents_child[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     export_pdf.savefig()
     plt.show()
     plt.close() 
 ################################# آمار بازدید شبکه های ورزش ####################################
     plt.figure(figsize=(8, 9))
     plt.suptitle(get_display(arabic_reshaper.reshape('آمار شبکه های اختصاصی ورزش')), fontsize=24, fontname='B Nazanin', weight="bold") 
     plt.subplot(211)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(channels_name_sports, channels_visits_sports, color='aqua', width=0.75, align='center', alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('تعداد بازدید از شبکه های اختصاصی ورزش')), fontsize=18, fontname='B Nazanin', weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام شبکه ها')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.rc('font', family='B Nazanin', size=16, weight="bold")
     plt.text(-0.1,channels_visits_sports[0]+10000, channels_visits_sports[0],  **text1_font)
     plt.text(0.90,channels_visits_sports[1]+10000, channels_visits_sports[1],  **text1_font)
     plt.text(1.90,channels_visits_sports[2]+10000, channels_visits_sports[2],  **text1_font)
     plt.text(2.90,channels_visits_sports[3]+10000, channels_visits_sports[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     plt.subplot(212)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(channels_name_sports, channels_contents_sports, color='aqua', width=0.75, align='center', alpha=1)
     plt.title(get_display(arabic_reshaper.reshape('تعداد محتواهای شبکه های اختصاصی ورزش')), fontsize=18, fontname='B Nazanin', weight="bold")
     plt.xlabel(get_display(arabic_reshaper.reshape('نام شبکه')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد محتوا')), fontsize=14, fontname='B Nazanin', weight="bold")
     plt.rc('font', family='B Nazanin', size=16, weight="bold")
     plt.text(-0.1,channels_contents_sports[0]+10000, channels_contents_sports[0],  **text1_font)
     plt.text(0.90,channels_contents_sports[1]+10000, channels_contents_sports[1],  **text1_font)
     plt.text(1.90,channels_contents_sports[2]+10000, channels_contents_sports[2],  **text1_font)
     plt.text(2.90,channels_contents_sports[3]+10000, channels_contents_sports[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     export_pdf.savefig()
     plt.show()
     plt.close() 
 ################################# ده محتوای پربازدید ####################################
     plt.figure(figsize=(10, 9))
     plt.suptitle(get_display(arabic_reshaper.reshape('محتواهای پربازدید سازمان')), fontsize=24, fontname='B Nazanin', weight="bold") 
     plt.subplot(211, projection='3d')
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(df_sar_content_popular_visit['content_popular_name_data'], df_sar_content_popular_visit['content_popular_visitnumber_data'], 
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
#     plt.text(-0.1,channels_visits_sports[0]+10000, channels_visits_sports[0],  **text1_font)
#     plt.text(0.90,channels_visits_sports[1]+10000, channels_visits_sports[1],  **text1_font)
#     plt.text(1.90,channels_visits_sports[2]+10000, channels_visits_sports[2],  **text1_font)
#     plt.text(2.90,channels_visits_sports[3]+10000, channels_visits_sports[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     plt.subplot(212)
#     text1_font = {'fontname':'B Nazanin', 'size':'14', 'color':'purple', 'weight':'bold', 'verticalalignment':'center'}
     plt.bar(df_sar_content_popular_visit_persection_data['content_popular_name_persection_data'],df_sar_content_popular_visit_persection_data['content_popular_visitnumber_persection_data'], 
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
#     plt.text(-0.1,channels_contents_sports[0]+10000, channels_contents_sports[0],  **text1_font)
#     plt.text(0.90,channels_contents_sports[1]+10000, channels_contents_sports[1],  **text1_font)
#     plt.text(1.90,channels_contents_sports[2]+10000, channels_contents_sports[2],  **text1_font)
#     plt.text(2.90,channels_contents_sports[3]+10000, channels_contents_sports[3],  **text1_font)
#     plt.grid(True)
#     plt.legend('نمودار معین',loc='upper right', numpoints=1)
     export_pdf.savefig()
     plt.show()
     plt.close()
     
 
 
 
#print(content_popular_visitnumber[0]) 
 
#######################################################################################################
################################################ گزارش شبکه یک ########################################
#######################################################################################################
###################################### ده محتوای پربازدید شبکه یک ###################################

#with PdfPages(r'C:UsersPCDesktopشبکه یک.pdf') as export_pdf:
#     plt.figure(figsize=(7, 4))
#     plt.bar(df_sar_ch_one['shabake1'], df_sar_ch_one['shabake11'], color='blue', width=0.25, align='center', alpha=1)
#     plt.title(get_display(arabic_reshaper.reshape('10 محتوای پربازدید')), fontsize=18, fontname='B Nazanin', weight="bold")
#     plt.xlabel(get_display(arabic_reshaper.reshape('نام محتوا')), fontsize=12, fontname='B Nazanin', weight="bold")
#     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), fontsize=12, fontname='B Nazanin', weight="bold")
#     plt.rc('font', family='B Nazanin', size=12, weight="bold")
##     plt.bar(format=comma_fmt)
##     plt.colorbar(format=comma_fmt)
##     plt.rc('font', size=12)          # controls default text sizes
##     plt.rc('axes', titlesize=12)     # fontsize of the axes title
##     plt.rc('axes', labelsize=12)    # fontsize of the x and y labels
##     plt.rc('legend', fontsize=12)    # legend fontsize
##     plt.rc('figure', titlesize=12)  # fontsize of the figure title
#     plt.text(-.1, ch_one2[0]+500, ch_one2[0], **text_font)
#     plt.text(0.9, ch_one2[1]+500, ch_one2[1], **text_font)
#     plt.text(1.9, ch_one2[2]+500, ch_one2[2], **text_font)
##     plt.grid(True)
##     plt.legend('نمودار معین',loc='upper right', numpoints=1)
#     export_pdf.savefig()
#     plt.show()
##     plt.close()####################################### ده محتوای پربازدید شبکه دو ###############################
#with PdfPages(r'C:UsersPCDesktopشبکه دو.pdf') as export_pdf:
#     plt.figure(figsize=(7, 4))
#     plt.bar(df_sar_ch_two['shabake2'], df_sar_ch_two['shabake22'], color='blue', width=0.25, align='center', alpha=1)
#     plt.title(get_display(arabic_reshaper.reshape('10 محتوای پربازدید')), fontsize=18, fontname='B Nazanin', weight="bold")
#     plt.xlabel(get_display(arabic_reshaper.reshape('نام محتوا')), fontsize=12, fontname='B Nazanin', weight="bold")
#     plt.ylabel(get_display(arabic_reshaper.reshape('تعداد بازدید')), fontsize=12, fontname='B Nazanin', weight="bold")
#     plt.text(-.1, ch_two2[0]*1.1, ch_two2[0], **text_font)
#     plt.text(0.9, ch_two2[1]*1.1, ch_two2[1], **text_font)
#     plt.text(1.9, ch_two2[2]*1.1, ch_two2[2], **text_font)
#     export_pdf.savefig()
#     plt.show()
#     plt.close()

#####################################################################
  