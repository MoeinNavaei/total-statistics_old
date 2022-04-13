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

################################# input data ########################################
sima=pd.read_excel('sarasari_tir99.xlsx')
ekhtesasi=pd.read_excel('ekhtesasi_tir99.xlsx')
radio=pd.read_excel('radio-tir99.xlsx')
ostani=pd.read_excel('ostani_tir99.xlsx')
vod_lenz=pd.read_csv('lenz-vod-tir99.csv')
vod_tva=pd.read_csv('tva-tir99.csv')

#################################  visit ########################################
sima_visit=sima['تعداد بازدید'].sum()
ekhtesasi_visit=ekhtesasi['تعداد بازدید'].sum()
radio_visit=radio['تعداد بازدید'].sum()
ostani_visit=ostani['تعداد بازدید'].sum()
vod_lenz_visit_serial=vod_lenz.query("film != '1'")
vod_lenz_visit_film=vod_lenz.query("film == '1'")
vod_lenz_visit_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_lenz_visit_film=vod_lenz_visit_film['bazdid'].sum()
vod_lenz_visit_serial=vod_lenz_visit_serial['bazdid'].sum()
vod_lenz_visit=vod_lenz_visit_film+vod_lenz_visit_serial
vod_tva_visit_serial=vod_tva.query("film != '1'")
vod_tva_visit_film=vod_tva.query("film == '1'")
vod_tva_visit_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_tva_visit_film=vod_tva_visit_film['bazdid'].sum()
vod_tva_visit_serial=vod_tva_visit_serial['bazdid'].sum()
vod_tva_visit=vod_tva_visit_film+vod_tva_visit_serial
vod_visit=vod_lenz_visit+vod_tva_visit
visit={'type_content': ['سیما', 'اختصاصی', 'رادیو', 'استانی', 'ویدئوی درخواستی'],
       'visit_number': [sima_visit, ekhtesasi_visit, radio_visit, ostani_visit, vod_visit]}
visit=pd.DataFrame(visit, columns=['type_content', 'visit_number'])

################################# duration ########################################
sima_duration=sima['مدت بازدید'].sum()
ekhtesasi_duration=ekhtesasi['مدت بازدید'].sum()
radio_duration=radio['مدت بازدید'].sum()
ostani_duration=ostani['مدت بازدید'].sum()
vod_lenz_duration_serial=vod_lenz.query("film != '1'")
vod_lenz_duration_film=vod_lenz.query("film == '1'")
vod_lenz_duration_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_lenz_duration_film=vod_lenz_duration_film['minute'].sum()
vod_lenz_duration_serial=vod_lenz_duration_serial['minute'].sum()
vod_lenz_duration=vod_lenz_duration_film+vod_lenz_duration_serial
vod_tva_duration_serial=vod_tva.query("film != '1'")
vod_tva_duration_film=vod_tva.query("film == '1'")
vod_tva_duration_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_tva_duration_film=vod_tva_duration_film['minute'].sum()
vod_tva_duration_serial=vod_tva_duration_serial['minute'].sum()
vod_tva_duration=vod_tva_duration_film+vod_tva_duration_serial
vod_duration=vod_lenz_duration+vod_tva_duration
sima_duration=round(sima_duration, 0)
ekhtesasi_duration=round(ekhtesasi_duration, 0)
radio_duration=round(radio_duration, 0)
ostani_duration=round(ostani_duration, 0)
vod_duration=round(vod_duration, 0)
duration={'type_content': ['سیما', 'اختصاصی', 'رادیو', 'استانی', 'ویدئوی درخواستی'],
       'duration_number': [sima_duration*60, ekhtesasi_duration*60, radio_duration*60, ostani_duration*60, vod_duration*60]}
duration=pd.DataFrame(duration, columns=['type_content', 'duration_number'])

################################# content ########################################
sima_content=sima.copy()
sima_content.drop_duplicates(subset =['نام برنامه', 'نام شبکه'], keep = 'first', inplace = True)
sima_content=len(sima_content)
ekhtesasi_content=ekhtesasi.copy()
ekhtesasi_content.drop_duplicates(subset =['نام برنامه', 'نام شبکه'], keep = 'first', inplace = True) 
ekhtesasi_content=len(ekhtesasi_content)
radio_content=radio.copy()
radio_content.drop_duplicates(subset =['نام برنامه', 'نام شبکه'], keep = 'first', inplace = True) 
radio_content=len(radio_content)
ostani_content=ostani.copy()
ostani_content.drop_duplicates(subset =['نام برنامه', 'نام شبکه'], keep = 'first', inplace = True) 
ostani_content=len(ostani_content)
vod_lenz_content_serial=vod_lenz.query("film != '1'")
vod_lenz_content_film=vod_lenz.query("film == '1'")
vod_lenz_content_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_lenz_content_serial=len(vod_lenz_content_serial)
vod_lenz_content_film=len(vod_lenz_content_film)
vod_lenz_content=vod_lenz_content_serial+vod_lenz_content_film
vod_tva_content_serial=vod_tva.query("film != '1'")
vod_tva_content_film=vod_tva.query("film == '1'")
vod_tva_content_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
vod_tva_content_serial=len(vod_tva_content_serial)
vod_tva_content_film=len(vod_tva_content_film)
vod_tva_content=vod_tva_content_serial+vod_tva_content_film
vod_content=vod_lenz_content+vod_tva_content
content={'type_content': ['سیما', 'اختصاصی', 'رادیو', 'استانی', 'ویدئوی درخواستی'],
       'content_number': [sima_content, ekhtesasi_content, radio_content, ostani_content, vod_content]}
content=pd.DataFrame(content, columns=['type_content', 'content_number'])

################################# summary ########################################
sima_tva=sima.query("اپراتور == 'تیوا'")
sima_lenz=sima.query("اپراتور == 'لنز'")
sima_televebion=sima.query("اپراتور == 'تلوبیون'")
sima_anten=sima.query("اپراتور == 'آنتن'")
radio_tva=radio.query("اپراتور == 'تیوا'")
radio_lenz=radio.query("اپراتور == 'لنز'")
radio_televebion=radio.query("اپراتور == 'تلوبیون'")
radio_anten=radio.query("اپراتور == 'آنتن'")
ostani_tva=ostani.query("اپراتور == 'تیوا'")
ostani_lenz=ostani.query("اپراتور == 'لنز'")
ostani_televebion=ostani.query("اپراتور == 'تلوبیون'")
ostani_anten=ostani.query("اپراتور == 'آنتن'")
ekhtesasi_tva=ekhtesasi.query("اپراتور == 'تیوا'")
ekhtesasi_lenz=ekhtesasi.query("اپراتور == 'لنز'")
ekhtesasi_televebion=ekhtesasi.query("اپراتور == 'تلوبیون'")
ekhtesasi_anten=ekhtesasi.query("اپراتور == 'آنتن'")

sima_tva_channel=sima_tva.copy()
sima_tva_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
sima_tva_channel=len(sima_tva_channel)
radio_tva_channel=radio_tva.copy()
radio_tva_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
radio_tva_channel=len(radio_tva_channel)
ostani_tva_channel=ostani_tva.copy()
ostani_tva_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ostani_tva_channel=len(ostani_tva_channel)
ekhtesasi_tva_channel=ekhtesasi_tva.copy()
ekhtesasi_tva_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ekhtesasi_tva_channel=len(ekhtesasi_tva_channel)
sima_tva_visit=sima_tva['تعداد بازدید'].sum()
radio_tva_visit=radio_tva['تعداد بازدید'].sum()
ostani_tva_visit=ostani_tva['تعداد بازدید'].sum()
ekhtesasi_tva_visit=ekhtesasi_tva['تعداد بازدید'].sum()
sima_tva_duration=sima_tva['مدت بازدید'].sum()
radio_tva_duration=radio_tva['مدت بازدید'].sum()
ostani_tva_duration=ostani_tva['مدت بازدید'].sum()
ekhtesasi_tva_duration=ekhtesasi_tva['مدت بازدید'].sum()

sima_lenz_channel=sima_lenz.copy()
sima_lenz_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
sima_lenz_channel=len(sima_lenz_channel)
radio_lenz_channel=radio_lenz.copy()
radio_lenz_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
radio_lenz_channel=len(radio_lenz_channel)
ostani_lenz_channel=ostani_lenz.copy()
ostani_lenz_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ostani_lenz_channel=len(ostani_lenz_channel)
ekhtesasi_lenz_channel=ekhtesasi_lenz.copy()
ekhtesasi_lenz_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ekhtesasi_lenz_channel=len(ekhtesasi_lenz_channel)
sima_lenz_visit=sima_lenz['تعداد بازدید'].sum()
radio_lenz_visit=radio_lenz['تعداد بازدید'].sum()
ostani_lenz_visit=ostani_lenz['تعداد بازدید'].sum()
ekhtesasi_lenz_visit=ekhtesasi_lenz['تعداد بازدید'].sum()
sima_lenz_duration=sima_lenz['مدت بازدید'].sum()
radio_lenz_duration=radio_lenz['مدت بازدید'].sum()
ostani_lenz_duration=ostani_lenz['مدت بازدید'].sum()
ekhtesasi_lenz_duration=ekhtesasi_lenz['مدت بازدید'].sum()

sima_televebion_channel=sima_televebion.copy()
sima_televebion_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
sima_televebion_channel=len(sima_televebion_channel)
radio_televebion_channel=radio_televebion.copy()
radio_televebion_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
radio_televebion_channel=len(radio_televebion_channel)
ostani_televebion_channel=ostani_televebion.copy()
ostani_televebion_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ostani_televebion_channel=len(ostani_televebion_channel)
ekhtesasi_televebion_channel=ekhtesasi_televebion.copy()
ekhtesasi_televebion_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ekhtesasi_televebion_channel=len(ekhtesasi_televebion_channel)
sima_televebion_visit=sima_televebion['تعداد بازدید'].sum()
radio_televebion_visit=radio_televebion['تعداد بازدید'].sum()
ostani_televebion_visit=ostani_televebion['تعداد بازدید'].sum()
ekhtesasi_televebion_visit=ekhtesasi_televebion['تعداد بازدید'].sum()
sima_televebion_duration=sima_televebion['مدت بازدید'].sum()
radio_televebion_duration=radio_televebion['مدت بازدید'].sum()
ostani_televebion_duration=ostani_televebion['مدت بازدید'].sum()
ekhtesasi_televebion_duration=ekhtesasi_televebion['مدت بازدید'].sum()

sima_anten_channel=sima_anten.copy()
sima_anten_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
sima_anten_channel=len(sima_anten_channel)
radio_anten_channel=radio_anten.copy()
radio_anten_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
radio_anten_channel=len(radio_anten_channel)
ostani_anten_channel=ostani_anten.copy()
ostani_anten_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ostani_anten_channel=len(ostani_anten_channel)
ekhtesasi_anten_channel=ekhtesasi_anten.copy()
ekhtesasi_anten_channel.drop_duplicates(subset =['نام شبکه'], keep = 'first', inplace = True)
ekhtesasi_anten_channel=len(ekhtesasi_anten_channel)
sima_anten_visit=sima_anten['تعداد بازدید'].sum()
radio_anten_visit=radio_anten['تعداد بازدید'].sum()
ostani_anten_visit=ostani_anten['تعداد بازدید'].sum()
ekhtesasi_anten_visit=ekhtesasi_anten['تعداد بازدید'].sum()
sima_anten_duration=sima_anten['مدت بازدید'].sum()
radio_anten_duration=radio_anten['مدت بازدید'].sum()
ostani_anten_duration=ostani_anten['مدت بازدید'].sum()
ekhtesasi_anten_duration=ekhtesasi_anten['مدت بازدید'].sum()
################################# output ########################################

all_data=pd.concat([visit, duration, content,], axis=1)
all_data.to_excel('output\summary.xlsx')

################################# append all data ########################################
sima_data=pd.read_excel('output\sima.xlsx')
ekhtesasi_data=pd.read_excel('output\ekhtesasi.xlsx')
radio_data=pd.read_excel('output\RADIO.xlsx')
ostani_data=pd.read_excel('output\ostani.xlsx')
vod_data=pd.read_excel('output\VOD second.xlsx')

output=pd.concat([sima_data, ekhtesasi_data,radio_data, ostani_data, vod_data,], axis=1)
output.to_excel('output\output.xlsx')



