import xlsxwriter 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import arabic_reshaper
from bidi.algorithm import get_display
import matplotlib as mpl
import matplotlib.ticker as tkr
import numpy as np
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D
import glob
#import xlwt
#from xlwt.Workbook import *

tva_df_vod = pd.read_csv('tva-tir99.csv') 
print("start TVA")
#
#def trim_all_columns(tva_df_vod):
#    """
#    Trim whitespace from ends of each value across all series in dataframe
#    """
#    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
#    return tva_df_vod.applymap(trim_strings)
#
#tva_df_vod = trim_all_columns(tva_df_vod)

tva_df_vod.replace('(^\s+|\s+$)', '', regex=True, inplace=True)

#tva_df_vod['title1'].str.strip()

tva_df_serial=tva_df_vod.query("film != '1'")
tva_df_film=tva_df_vod.query("film == '1'")

##############################################################################################################################
##############################################################################################################################
########################################################## film ###############################################################
##############################################################################################################################
##############################################################################################################################
tva_df_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 

print("statistics of tva film")
tva_film_count_content=tva_df_film['bazdid']
tva_film_count_content=len(tva_film_count_content)
tva_film_sum_bazdid=tva_df_film['bazdid'].sum()
tva_film_sum_karbaran=tva_df_film['karbaran'].sum()
tva_film_sum_minute=tva_df_film['minute'].sum()

print("genre of tva film")
##############################################################################################################################
########################################################## genre ###############################################################
##############################################################################################################################

df_tva_film_genre=tva_df_film['genre']
tva_count_of_all_genre=len(tva_df_film)
tva_visit_of_all_genre=tva_df_film['bazdid'].sum()

tva_film_siasi = df_tva_film_genre.str.count("سیاسی") 
tva_film_siasi=pd.DataFrame(tva_film_siasi) 
tva_film_siasi=tva_film_siasi['genre'].sum()
tva_film_siasi_visit = tva_df_film[tva_df_film['genre'].str.contains('سیاسی')]
tva_film_siasi_visit=tva_film_siasi_visit['bazdid'].sum()

tva_film_tarsnak = df_tva_film_genre.str.count("ترسناک") 
tva_film_tarsnak=pd.DataFrame(tva_film_tarsnak) 
tva_film_tarsnak=tva_film_tarsnak['genre'].sum()
tva_film_vahshat = df_tva_film_genre.str.count("وحشت") 
tva_film_vahshat=pd.DataFrame(tva_film_vahshat) 
tva_film_vahshat=tva_film_vahshat['genre'].sum()
tva_film_tarsnak=tva_film_tarsnak+tva_film_vahshat
tva_film_tarsnak_visit = tva_df_film[tva_df_film['genre'].str.contains('ترسناک')]
tva_film_tarsnak_visit=tva_film_tarsnak_visit['bazdid'].sum()
tva_film_vahshat_visit = tva_df_film[tva_df_film['genre'].str.contains('وحشت')]
tva_film_vahshat_visit=tva_film_vahshat_visit['bazdid'].sum()
tva_film_tarsnak_visit=tva_film_tarsnak_visit+tva_film_vahshat_visit

tva_film_razalod = df_tva_film_genre.str.count("رازآلود") 
tva_film_razalod=pd.DataFrame(tva_film_razalod) 
tva_film_razalod=tva_film_razalod['genre'].sum()
tva_film_razalod1 = df_tva_film_genre.str.count("راز آلود") 
tva_film_razalod1=pd.DataFrame(tva_film_razalod1) 
tva_film_razalod1=tva_film_razalod1['genre'].sum()
tva_film_razalod=tva_film_razalod+tva_film_razalod1
tva_film_razalod_visit = tva_df_film[tva_df_film['genre'].str.contains('رازآلود')]
tva_film_razalod_visit=tva_film_razalod_visit['bazdid'].sum()
tva_film_razalod1_visit = tva_df_film[tva_df_film['genre'].str.contains('رازآلود')]
tva_film_razalod1_visit=tva_film_razalod1_visit['bazdid'].sum()
tva_film_razalod_visit=tva_film_razalod_visit+tva_film_razalod1_visit

tva_film_zendeginame = df_tva_film_genre.str.count("زندگینامه") 
tva_film_zendeginame=pd.DataFrame(tva_film_zendeginame) 
tva_film_zendeginame=tva_film_zendeginame['genre'].sum()
tva_film_zendeginame1 = df_tva_film_genre.str.count("زندگی نامه") 
tva_film_zendeginame1=pd.DataFrame(tva_film_zendeginame1) 
tva_film_zendeginame1=tva_film_zendeginame1['genre'].sum()
tva_film_zendeginame=tva_film_zendeginame+tva_film_zendeginame1
tva_film_zendeginame_visit = tva_df_film[tva_df_film['genre'].str.contains('زندگینامه')]
tva_film_zendeginame_visit=tva_film_zendeginame_visit['bazdid'].sum()
tva_film_zendeginame1_visit = tva_df_film[tva_df_film['genre'].str.contains('زندگینامه')]
tva_film_zendeginame1_visit=tva_film_zendeginame1_visit['bazdid'].sum()
tva_film_zendeginame_visit=tva_film_zendeginame_visit+tva_film_zendeginame1_visit

tva_film_romantic = df_tva_film_genre.str.count("رمانتیک") 
tva_film_romantic=pd.DataFrame(tva_film_romantic) 
tva_film_romantic=tva_film_romantic['genre'].sum()
tva_film_romantic_visit = tva_df_film[tva_df_film['genre'].str.contains('رمانتیک')]
tva_film_romantic_visit=tva_film_romantic_visit['bazdid'].sum()

tva_film_mostanad = df_tva_film_genre.str.count("مستند") 
tva_film_mostanad=pd.DataFrame(tva_film_mostanad) 
tva_film_mostanad=tva_film_mostanad['genre'].sum()
tva_film_mostanad_visit = tva_df_film[tva_df_film['genre'].str.contains('مستند')]
tva_film_mostanad_visit=tva_film_mostanad_visit['bazdid'].sum()

tva_film_jenai = df_tva_film_genre.str.count("جنائی") 
tva_film_jenai=pd.DataFrame(tva_film_jenai) 
tva_film_jenai=tva_film_jenai['genre'].sum()
tva_film_jenai1 = df_tva_film_genre.str.count("جنایی") 
tva_film_jenai1=pd.DataFrame(tva_film_jenai1) 
tva_film_jenai1=tva_film_jenai1['genre'].sum()
tva_film_jenai=tva_film_jenai+tva_film_jenai1
tva_film_jenai_visit = tva_df_film[tva_df_film['genre'].str.contains('جنائی')]
tva_film_jenai_visit=tva_film_jenai_visit['bazdid'].sum()
tva_film_jenai1_visit = tva_df_film[tva_df_film['genre'].str.contains('جنائی')]
tva_film_jenai1_visit=tva_film_jenai1_visit['bazdid'].sum()
tva_film_jenai_visit=tva_film_jenai_visit+tva_film_jenai1_visit

tva_film_tarikhi = df_tva_film_genre.str.count("تاریخی") 
tva_film_tarikhi=pd.DataFrame(tva_film_tarikhi) 
tva_film_tarikhi=tva_film_tarikhi['genre'].sum()
tva_film_tarikhi_visit = tva_df_film[tva_df_film['genre'].str.contains('تاریخی')]
tva_film_tarikhi_visit=tva_film_tarikhi_visit['bazdid'].sum()

tva_film_animeyshen = df_tva_film_genre.str.count("انیمیشن") 
tva_film_animeyshen=pd.DataFrame(tva_film_animeyshen) 
tva_film_animeyshen=tva_film_animeyshen['genre'].sum()
tva_film_animeyshen_visit = tva_df_film[tva_df_film['genre'].str.contains('انیمیشن')]
tva_film_animeyshen_visit=tva_film_animeyshen_visit['bazdid'].sum()

tva_film_kodak = df_tva_film_genre.str.count("کودک") 
tva_film_kodak=pd.DataFrame(tva_film_kodak) 
tva_film_kodak=tva_film_kodak['genre'].sum()
tva_film_kodak1 = df_tva_film_genre.str.count("کودکان") 
tva_film_kodak1=pd.DataFrame(tva_film_kodak1) 
tva_film_kodak1=tva_film_kodak1['genre'].sum()
tva_film_kodak=tva_film_kodak+tva_film_kodak1
tva_film_kodak_visit = tva_df_film[tva_df_film['genre'].str.contains('کودک')]
tva_film_kodak_visit=tva_film_kodak_visit['bazdid'].sum()
tva_film_kodak1_visit = tva_df_film[tva_df_film['genre'].str.contains('کودک')]
tva_film_kodak1_visit=tva_film_kodak1_visit['bazdid'].sum()
tva_film_kodak_visit=tva_film_kodak_visit+tva_film_kodak1_visit

tva_film_hayejanangiz = df_tva_film_genre.str.count("هیجان انگیز") 
tva_film_hayejanangiz=pd.DataFrame(tva_film_hayejanangiz) 
tva_film_hayejanangiz=tva_film_hayejanangiz['genre'].sum()
tva_film_hayejanangiz_visit = tva_df_film[tva_df_film['genre'].str.contains('هیجان انگیز')]
tva_film_hayejanangiz_visit=tva_film_hayejanangiz_visit['bazdid'].sum()

tva_film_khanevadegi = df_tva_film_genre.str.count("خانوادگی") 
tva_film_khanevadegi=pd.DataFrame(tva_film_khanevadegi) 
tva_film_khanevadegi=tva_film_khanevadegi['genre'].sum()
tva_film_khanevadegi_visit = tva_df_film[tva_df_film['genre'].str.contains('خانوادگی')]
tva_film_khanevadegi_visit=tva_film_khanevadegi_visit['bazdid'].sum()

tva_film_majarajoi = df_tva_film_genre.str.count("ماجراجویی") 
tva_film_majarajoi=pd.DataFrame(tva_film_majarajoi) 
tva_film_majarajoi=tva_film_majarajoi['genre'].sum()
tva_film_majarai = df_tva_film_genre.str.count("ماجرایی") 
tva_film_majarai=pd.DataFrame(tva_film_majarai) 
tva_film_majarai=tva_film_majarai['genre'].sum()
tva_film_majarajoi=tva_film_majarajoi+tva_film_majarai
tva_film_majarajoi_visit = tva_df_film[tva_df_film['genre'].str.contains('ماجراجویی')]
tva_film_majarajoi_visit=tva_film_majarajoi_visit['bazdid'].sum()
tva_film_majarajoi1_visit = tva_df_film[tva_df_film['genre'].str.contains('ماجراجویی')]
tva_film_majarajoi1_visit=tva_film_majarajoi1_visit['bazdid'].sum()
tva_film_majarajoi_visit=tva_film_majarajoi_visit+tva_film_majarajoi1_visit

tva_film_deram = df_tva_film_genre.str.count("درام") 
tva_film_deram=pd.DataFrame(tva_film_deram) 
tva_film_deram=tva_film_deram['genre'].sum()
tva_film_deram_visit = tva_df_film[tva_df_film['genre'].str.contains('درام')]
tva_film_deram_visit=tva_film_deram_visit['bazdid'].sum()

tva_film_komedi = df_tva_film_genre.str.count("کمدی") 
tva_film_komedi=pd.DataFrame(tva_film_komedi) 
tva_film_komedi=tva_film_komedi['genre'].sum()
tva_film_komedi_visit = tva_df_film[tva_df_film['genre'].str.contains('کمدی')]
tva_film_komedi_visit=tva_film_komedi_visit['bazdid'].sum()

tva_film_vestern = df_tva_film_genre.str.count("وسترن") 
tva_film_vestern=pd.DataFrame(tva_film_vestern) 
tva_film_vestern=tva_film_vestern['genre'].sum()
tva_film_vestern_visit = tva_df_film[tva_df_film['genre'].str.contains('وسترن')]
tva_film_vestern_visit=tva_film_vestern_visit['bazdid'].sum()

tva_film_fantezi = df_tva_film_genre.str.count("فانتزی") 
tva_film_fantezi=pd.DataFrame(tva_film_fantezi) 
tva_film_fantezi=tva_film_fantezi['genre'].sum()
tva_film_fantezi_visit = tva_df_film[tva_df_film['genre'].str.contains('فانتزی')]
tva_film_fantezi_visit=tva_film_fantezi_visit['bazdid'].sum()

tva_film_varzeshi = df_tva_film_genre.str.count("ورزشی") 
tva_film_varzeshi=pd.DataFrame(tva_film_varzeshi) 
tva_film_varzeshi=tva_film_varzeshi['genre'].sum()
tva_film_varzeshi_visit = tva_df_film[tva_df_film['genre'].str.contains('ورزشی')]
tva_film_varzeshi_visit=tva_film_varzeshi_visit['bazdid'].sum()

tva_film_elmi_takhayoli = df_tva_film_genre.str.count("علمی-تخیلی") 
tva_film_elmi_takhayoli=pd.DataFrame(tva_film_elmi_takhayoli) 
tva_film_elmi_takhayoli=tva_film_elmi_takhayoli['genre'].sum()
tva_film_elmi_takhayoli_visit = tva_df_film[tva_df_film['genre'].str.contains('علمی-تخیلی')]
tva_film_elmi_takhayoli_visit=tva_film_elmi_takhayoli_visit['bazdid'].sum()

tva_film_acshen = df_tva_film_genre.str.count("اکشن") 
tva_film_acshen=pd.DataFrame(tva_film_acshen) 
tva_film_acshen=tva_film_acshen['genre'].sum()
tva_film_acshen_visit = tva_df_film[tva_df_film['genre'].str.contains('اکشن')]
tva_film_acshen_visit=tva_film_acshen_visit['bazdid'].sum()

tva_film_mozical = df_tva_film_genre.str.count("موزیکال") 
tva_film_mozical=pd.DataFrame(tva_film_mozical) 
tva_film_mozical=tva_film_mozical['genre'].sum()
tva_film_mozical_visit = tva_df_film[tva_df_film['genre'].str.contains('موزیکال')]
tva_film_mozical_visit=tva_film_mozical_visit['bazdid'].sum()

tva_film_jangi = df_tva_film_genre.str.count("جنگی") 
tva_film_jangi=pd.DataFrame(tva_film_jangi) 
tva_film_jangi=tva_film_jangi['genre'].sum()
tva_film_jangi_visit = tva_df_film[tva_df_film['genre'].str.contains('جنگی')]
tva_film_jangi_visit=tva_film_jangi_visit['bazdid'].sum()

tva_film_goftego = df_tva_film_genre.str.count("گفتگو") 
tva_film_goftego=pd.DataFrame(tva_film_goftego) 
tva_film_goftego=tva_film_goftego['genre'].sum()
tva_film_goftego_visit = tva_df_film[tva_df_film['genre'].str.contains('گفتگو')]
tva_film_goftego_visit=tva_film_goftego_visit['bazdid'].sum()

tva_film_khiali = df_tva_film_genre.str.count("خیالی") 
tva_film_khiali=pd.DataFrame(tva_film_khiali) 
tva_film_khiali=tva_film_khiali['genre'].sum()
tva_film_khiali1 = df_tva_film_genre.str.count("تخیلی") 
tva_film_khiali1=pd.DataFrame(tva_film_khiali1) 
tva_film_khiali1=tva_film_khiali1['genre'].sum()
tva_film_khiali=tva_film_khiali+tva_film_khiali1
tva_film_khiali_visit = tva_df_film[tva_df_film['genre'].str.contains('خیالی')]
tva_film_khiali_visit=tva_film_khiali_visit['bazdid'].sum()
tva_film_khiali1_visit = tva_df_film[tva_df_film['genre'].str.contains('خیالی')]
tva_film_khiali1_visit=tva_film_khiali1_visit['bazdid'].sum()
tva_film_khiali_visit=tva_film_khiali_visit+tva_film_khiali1_visit

tva_film_count_of_genre={'tva_film_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'tva_film_count_of_genre1': [tva_film_mozical, tva_film_hayejanangiz, tva_film_varzeshi,
                                tva_film_goftego, tva_film_mostanad, tva_film_majarajoi, 
                                tva_film_kodak,tva_film_komedi, tva_film_fantezi,tva_film_elmi_takhayoli, 
                                tva_film_siasi,tva_film_zendeginame, tva_film_romantic, 
                                tva_film_razalod,tva_film_deram, tva_film_khiali, 
                                tva_film_khanevadegi, tva_film_jangi, tva_film_jenai,
                                tva_film_tarsnak, tva_film_tarikhi,
                                tva_film_animeyshen, tva_film_acshen, tva_film_vestern]}
tva_film_count_of_genre=pd.DataFrame(tva_film_count_of_genre, columns=['tva_film_type_of_genre', 'tva_film_count_of_genre1'])
tva_film_count_of_genre=tva_film_count_of_genre.query("tva_film_count_of_genre1 != '0'")
tva_film_count_of_genre.sort_values('tva_film_count_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')

tva_film_visit_of_genre={'tva_film_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'tva_film_visit_of_genre1': [tva_film_mozical, tva_film_hayejanangiz, tva_film_varzeshi,
                                tva_film_goftego, tva_film_mostanad, tva_film_majarajoi, 
                                tva_film_kodak,tva_film_komedi, tva_film_fantezi,tva_film_elmi_takhayoli, 
                                tva_film_siasi,tva_film_zendeginame, tva_film_romantic, 
                                tva_film_razalod,tva_film_deram, tva_film_khiali, 
                                tva_film_khanevadegi, tva_film_jangi, tva_film_jenai,
                                tva_film_tarsnak, tva_film_tarikhi,
                                tva_film_animeyshen, tva_film_acshen, tva_film_vestern]}
tva_film_visit_of_genre=pd.DataFrame(tva_film_visit_of_genre, columns=['tva_film_type_of_genre', 'tva_film_visit_of_genre1'])
tva_film_visit_of_genre=tva_film_visit_of_genre.query("tva_film_visit_of_genre1 != '0'")
tva_film_visit_of_genre.sort_values('tva_film_visit_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')
print("finish genre of tva film")
##############################################################################################################################
########################################################## country ###############################################################
##############################################################################################################################
print("country of tva film")
df_tva_film_country=tva_df_film['country']
tva_film_count_of_all_country=len(tva_df_film)
tva_film_visit_of_all_country=tva_df_film['bazdid'].sum()

tva_film_amrika = df_tva_film_country.str.count("آمریکا") 
tva_film_amrika=pd.DataFrame(tva_film_amrika) 
tva_film_amrika=tva_film_amrika['country'].sum()
tva_film_amrika_visit = tva_df_film[tva_df_film['country'].str.contains('آمریکا')]
tva_film_amrika_visit=tva_film_amrika_visit['bazdid'].sum()

tva_film_iran = df_tva_film_country.str.count("ایران") 
tva_film_iran=pd.DataFrame(tva_film_iran) 
tva_film_iran=tva_film_iran['country'].sum()
tva_film_iran_visit = tva_df_film[tva_df_film['country'].str.contains('ایران')]
tva_film_iran_visit=tva_film_iran_visit['bazdid'].sum()

tva_film_holand = df_tva_film_country.str.count("هلند") 
tva_film_holand=pd.DataFrame(tva_film_holand) 
tva_film_holand=tva_film_holand['country'].sum()
tva_film_holand_visit = tva_df_film[tva_df_film['country'].str.contains('هلند')]
tva_film_holand_visit=tva_film_holand_visit['bazdid'].sum()

tva_film_alman = df_tva_film_country.str.count("آلمان") 
tva_film_alman=pd.DataFrame(tva_film_alman) 
tva_film_alman=tva_film_alman['country'].sum()
tva_film_alman_visit = tva_df_film[tva_df_film['country'].str.contains('آلمان')]
tva_film_alman_visit=tva_film_alman_visit['bazdid'].sum()

tva_film_englis = df_tva_film_country.str.count("انگلیس") 
tva_film_englis=pd.DataFrame(tva_film_englis) 
tva_film_englis=tva_film_englis['country'].sum()
tva_film_englis_visit = tva_df_film[tva_df_film['country'].str.contains('انگلیس')]
tva_film_englis_visit=tva_film_englis_visit['bazdid'].sum()
tva_film_englis1 = df_tva_film_country.str.count("انگلستان") 
tva_film_englis1=pd.DataFrame(tva_film_englis1) 
tva_film_englis1=tva_film_englis1['country'].sum()
tva_film_englis1_visit = tva_df_film[tva_df_film['country'].str.contains('انگلستان')]
tva_film_englis1_visit=tva_film_englis1_visit['bazdid'].sum()
tva_film_englis_visit=tva_film_englis_visit+tva_film_englis1_visit
tva_film_englis=tva_film_englis+tva_film_englis1

tva_film_kore_jonobi = df_tva_film_country.str.count("کره جنوبی") 
tva_film_kore_jonobi=pd.DataFrame(tva_film_kore_jonobi) 
tva_film_kore_jonobi=tva_film_kore_jonobi['country'].sum()
tva_film_kore_jonobi_visit = tva_df_film[tva_df_film['country'].str.contains('کره جنوبی')]
tva_film_kore_jonobi_visit=tva_film_kore_jonobi_visit['bazdid'].sum()

tva_film_faranse = df_tva_film_country.str.count("فرانسه") 
tva_film_faranse=pd.DataFrame(tva_film_faranse) 
tva_film_faranse=tva_film_faranse['country'].sum()
tva_film_faranse_visit = tva_df_film[tva_df_film['country'].str.contains('فرانسه')]
tva_film_faranse_visit=tva_film_faranse_visit['bazdid'].sum()

tva_film_japon = df_tva_film_country.str.count("ژاپن") 
tva_film_japon=pd.DataFrame(tva_film_japon) 
tva_film_japon=tva_film_japon['country'].sum()
tva_film_japon_visit = tva_df_film[tva_df_film['country'].str.contains('ژاپن')]
tva_film_japon_visit=tva_film_japon_visit['bazdid'].sum()

tva_film_kanada = df_tva_film_country.str.count("کانادا") 
tva_film_kanada=pd.DataFrame(tva_film_kanada) 
tva_film_kanada=tva_film_kanada['country'].sum()
tva_film_kanada_visit = tva_df_film[tva_df_film['country'].str.contains('کانادا')]
tva_film_kanada_visit=tva_film_kanada_visit['bazdid'].sum()

tva_film_fanland = df_tva_film_country.str.count("فنلاند") 
tva_film_fanland=pd.DataFrame(tva_film_fanland) 
tva_film_fanland=tva_film_fanland['country'].sum()
tva_film_fanland_visit = tva_df_film[tva_df_film['country'].str.contains('فنلاند')]
tva_film_fanland_visit=tva_film_fanland_visit['bazdid'].sum()

tva_film_korovasi = df_tva_film_country.str.count("کرواسی") 
tva_film_korovasi=pd.DataFrame(tva_film_korovasi) 
tva_film_korovasi=tva_film_korovasi['country'].sum()
tva_film_korovasi_visit = tva_df_film[tva_df_film['country'].str.contains('کرواسی')]
tva_film_korovasi_visit=tva_film_korovasi_visit['bazdid'].sum()

tva_film_majarestan = df_tva_film_country.str.count("مجارستان") 
tva_film_majarestan=pd.DataFrame(tva_film_majarestan) 
tva_film_majarestan=tva_film_majarestan['country'].sum()
tva_film_majarestan_visit = tva_df_film[tva_df_film['country'].str.contains('مجارستان')]
tva_film_majarestan_visit=tva_film_majarestan_visit['bazdid'].sum()

tva_film_lahestan = df_tva_film_country.str.count("لهستان") 
tva_film_lahestan=pd.DataFrame(tva_film_lahestan) 
tva_film_lahestan=tva_film_lahestan['country'].sum()
tva_film_lahestan_visit = tva_df_film[tva_df_film['country'].str.contains('لهستان')]
tva_film_lahestan_visit=tva_film_lahestan_visit['bazdid'].sum()

tva_film_sois = df_tva_film_country.str.count("سوئیس") 
tva_film_sois=pd.DataFrame(tva_film_sois) 
tva_film_sois=tva_film_sois['country'].sum()
tva_film_sois_visit = tva_df_film[tva_df_film['country'].str.contains('سوئیس')]
tva_film_sois_visit=tva_film_sois_visit['bazdid'].sum()

tva_film_belgik = df_tva_film_country.str.count("بلژیک") 
tva_film_belgik=pd.DataFrame(tva_film_belgik) 
tva_film_belgik=tva_film_belgik['country'].sum()
tva_film_belgik_visit = tva_df_film[tva_df_film['country'].str.contains('بلژیک')]
tva_film_belgik_visit=tva_film_belgik_visit['bazdid'].sum()

tva_film_rosie = df_tva_film_country.str.count("روسیه") 
tva_film_rosie=pd.DataFrame(tva_film_rosie) 
tva_film_rosie=tva_film_rosie['country'].sum()
tva_film_rosie_visit = tva_df_film[tva_df_film['country'].str.contains('روسیه')]
tva_film_rosie_visit=tva_film_rosie_visit['bazdid'].sum()

tva_film_italia = df_tva_film_country.str.count("ایتالیا") 
tva_film_italia=pd.DataFrame(tva_film_italia) 
tva_film_italia=tva_film_italia['country'].sum()
tva_film_italia_visit = tva_df_film[tva_df_film['country'].str.contains('ایتالیا')]
tva_film_italia_visit=tva_film_italia_visit['bazdid'].sum()

tva_film_bolgharestan = df_tva_film_country.str.count("بلغارستان") 
tva_film_bolgharestan=pd.DataFrame(tva_film_bolgharestan) 
tva_film_bolgharestan=tva_film_bolgharestan['country'].sum()
tva_film_bolgharestan_visit = tva_df_film[tva_df_film['country'].str.contains('بلغارستان')]
tva_film_bolgharestan_visit=tva_film_bolgharestan_visit['bazdid'].sum()

tva_film_ostralia = df_tva_film_country.str.count("استرالیا") 
tva_film_ostralia=pd.DataFrame(tva_film_ostralia) 
tva_film_ostralia=tva_film_ostralia['country'].sum()
tva_film_ostralia_visit = tva_df_film[tva_df_film['country'].str.contains('استرالیا')]
tva_film_ostralia_visit=tva_film_ostralia_visit['bazdid'].sum()

tva_film_norvej = df_tva_film_country.str.count("نروژ") 
tva_film_norvej=pd.DataFrame(tva_film_norvej) 
tva_film_norvej=tva_film_norvej['country'].sum()
tva_film_norvej_visit = tva_df_film[tva_df_film['country'].str.contains('نروژ')]
tva_film_norvej_visit=tva_film_norvej_visit['bazdid'].sum()

tva_film_chin = df_tva_film_country.str.count("چین") 
tva_film_chin=pd.DataFrame(tva_film_chin) 
tva_film_chin=tva_film_chin['country'].sum()
tva_film_chin_visit = tva_df_film[tva_df_film['country'].str.contains('چین')]
tva_film_chin_visit=tva_film_chin_visit['bazdid'].sum()

tva_film_tayland = df_tva_film_country.str.count("تایلند") 
tva_film_tayland=pd.DataFrame(tva_film_tayland) 
tva_film_tayland=tva_film_tayland['country'].sum()
tva_film_tayland_visit = tva_df_film[tva_df_film['country'].str.contains('تایلند')]
tva_film_tayland_visit=tva_film_tayland_visit['bazdid'].sum()

tva_film_sangapor = df_tva_film_country.str.count("سنگاپور") 
tva_film_sangapor=pd.DataFrame(tva_film_sangapor) 
tva_film_sangapor=tva_film_sangapor['country'].sum()
tva_film_sangapor_visit = tva_df_film[tva_df_film['country'].str.contains('سنگاپور')]
tva_film_sangapor_visit=tva_film_sangapor_visit['bazdid'].sum()

tva_film_otrish = df_tva_film_country.str.count("اتریش") 
tva_film_otrish=pd.DataFrame(tva_film_otrish) 
tva_film_otrish=tva_film_otrish['country'].sum()
tva_film_otrish_visit = tva_df_film[tva_df_film['country'].str.contains('اتریش')]
tva_film_otrish_visit=tva_film_otrish_visit['bazdid'].sum()

tva_film_spania = df_tva_film_country.str.count("اسپانیا") 
tva_film_spania=pd.DataFrame(tva_film_spania) 
tva_film_spania=tva_film_spania['country'].sum()
tva_film_spania_visit = tva_df_film[tva_df_film['country'].str.contains('اسپانیا')]
tva_film_spania_visit=tva_film_spania_visit['bazdid'].sum()

tva_film_okrayn = df_tva_film_country.str.count("اکراین") 
tva_film_okrayn=pd.DataFrame(tva_film_okrayn) 
tva_film_okrayn=tva_film_okrayn['country'].sum()
tva_film_okrayn_visit = tva_df_film[tva_df_film['country'].str.contains('اکراین')]
tva_film_okrayn_visit=tva_film_okrayn_visit['bazdid'].sum()

tva_film_emarat = df_tva_film_country.str.count("امارات") 
tva_film_emarat=pd.DataFrame(tva_film_emarat) 
tva_film_emarat=tva_film_emarat['country'].sum()
tva_film_emarat_visit = tva_df_film[tva_df_film['country'].str.contains('امارات')]
tva_film_emarat_visit=tva_film_emarat_visit['bazdid'].sum()

tva_film_irland = df_tva_film_country.str.count("ایرلند") 
tva_film_irland=pd.DataFrame(tva_film_irland) 
tva_film_irland=tva_film_irland['country'].sum()
tva_film_irland_visit = tva_df_film[tva_df_film['country'].str.contains('ایرلند')]
tva_film_irland_visit=tva_film_irland_visit['bazdid'].sum()

tva_film_argantin = df_tva_film_country.str.count("آرژانتین") 
tva_film_argantin=pd.DataFrame(tva_film_argantin) 
tva_film_argantin=tva_film_argantin['country'].sum()
tva_film_argantin_visit = tva_df_film[tva_df_film['country'].str.contains('آرژانتین')]
tva_film_argantin_visit=tva_film_argantin_visit['bazdid'].sum()

tva_film_afrigha_jonobi = df_tva_film_country.str.count("آفریقای جنوبی") 
tva_film_afrigha_jonobi=pd.DataFrame(tva_film_afrigha_jonobi) 
tva_film_afrigha_jonobi=tva_film_afrigha_jonobi['country'].sum()
tva_film_afrigha_jonobi_visit = tva_df_film[tva_df_film['country'].str.contains('آفریقای جنوبی')]
tva_film_afrigha_jonobi_visit=tva_film_afrigha_jonobi_visit['bazdid'].sum()

tva_film_danmark = df_tva_film_country.str.count("دانمارک") 
tva_film_danmark=pd.DataFrame(tva_film_danmark) 
tva_film_danmark=tva_film_danmark['country'].sum()
tva_film_danmark_visit = tva_df_film[tva_df_film['country'].str.contains('دانمارک')]
tva_film_danmark_visit=tva_film_danmark_visit['bazdid'].sum()

tva_film_shili = df_tva_film_country.str.count("شیلی") 
tva_film_shili=pd.DataFrame(tva_film_shili) 
tva_film_shili=tva_film_shili['country'].sum()
tva_film_shili_visit = tva_df_film[tva_df_film['country'].str.contains('شیلی')]
tva_film_shili_visit=tva_film_shili_visit['bazdid'].sum()

tva_film_malezi = df_tva_film_country.str.count("مالزی") 
tva_film_malezi=pd.DataFrame(tva_film_malezi) 
tva_film_malezi=tva_film_malezi['country'].sum()
tva_film_malezi_visit = tva_df_film[tva_df_film['country'].str.contains('مالزی')]
tva_film_malezi_visit=tva_film_malezi_visit['bazdid'].sum()

tva_film_honkkong = df_tva_film_country.str.count("هنک کنگ") 
tva_film_honkkong=pd.DataFrame(tva_film_honkkong) 
tva_film_honkkong=tva_film_honkkong['country'].sum()
tva_film_honkkong_visit = tva_df_film[tva_df_film['country'].str.contains('هنک کنگ')]
tva_film_honkkong_visit=tva_film_honkkong_visit['bazdid'].sum()

tva_film_soed = df_tva_film_country.str.count("سوئد") 
tva_film_soed=pd.DataFrame(tva_film_soed) 
tva_film_soed=tva_film_soed['country'].sum()
tva_film_soed_visit = tva_df_film[tva_df_film['country'].str.contains('سوئد')]
tva_film_soed_visit=tva_film_soed_visit['bazdid'].sum()

tva_film_sois = df_tva_film_country.str.count("سوئیس") 
tva_film_sois=pd.DataFrame(tva_film_sois) 
tva_film_sois=tva_film_sois['country'].sum()
tva_film_sois_visit = tva_df_film[tva_df_film['country'].str.contains('سوئیس')]
tva_film_sois_visit=tva_film_sois_visit['bazdid'].sum()

tva_film_mekzik = df_tva_film_country.str.count("مکزیک") 
tva_film_mekzik=pd.DataFrame(tva_film_mekzik) 
tva_film_mekzik=tva_film_mekzik['country'].sum()
tva_film_mekzik_visit = tva_df_film[tva_df_film['country'].str.contains('مکزیک')]
tva_film_mekzik_visit=tva_film_mekzik_visit['bazdid'].sum()

tva_film_nioziland = df_tva_film_country.str.count("نیوزیلند") 
tva_film_nioziland=pd.DataFrame(tva_film_nioziland) 
tva_film_nioziland=tva_film_nioziland['country'].sum()
tva_film_nioziland_visit = tva_df_film[tva_df_film['country'].str.contains('نیوزیلند')]
tva_film_nioziland_visit=tva_film_nioziland_visit['bazdid'].sum()

tva_film_hend = df_tva_film_country.str.count("هند") 
tva_film_hend=pd.DataFrame(tva_film_hend) 
tva_film_hend=tva_film_hend['country'].sum()
tva_film_hend_visit = tva_df_film[tva_df_film['country'].str.contains('هند')]
tva_film_hend_visit=tva_film_hend_visit['bazdid'].sum()

tva_film_country_content_count={'tva_film_country_name1': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'tva_film_country_count1': [tva_film_amrika, tva_film_iran,tva_film_holand, tva_film_alman,
                                                         tva_film_englis, tva_film_kore_jonobi,tva_film_faranse, tva_film_japon,
                                                         tva_film_kanada, tva_film_fanland,tva_film_korovasi, tva_film_majarestan,
                                                         tva_film_lahestan, tva_film_sois,tva_film_belgik, tva_film_rosie,
                                                         tva_film_italia, tva_film_bolgharestan,tva_film_ostralia, tva_film_norvej,
                                                         tva_film_chin, tva_film_tayland,tva_film_sangapor, tva_film_otrish,
                                                         tva_film_spania, tva_film_okrayn,tva_film_emarat, tva_film_irland,
                                                         tva_film_argantin, tva_film_afrigha_jonobi,tva_film_danmark, tva_film_shili,
                                                         tva_film_malezi, tva_film_honkkong,tva_film_soed, tva_film_sois,
                                                         tva_film_mekzik, tva_film_nioziland,tva_film_hend]}                                 

tva_film_country_content_count=pd.DataFrame(tva_film_country_content_count, columns=['tva_film_country_name1', 'tva_film_country_count1']) 
tva_film_country_content_count=tva_film_country_content_count.query("tva_film_country_count1 != '0'")
tva_film_country_content_count.sort_values('tva_film_country_count1', axis = 0, ascending = False, inplace = True, na_position ='last')
                                  
tva_film_country_content_visit={'tva_film_country_name2': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'tva_film_country_visit1': [tva_film_amrika_visit, tva_film_iran_visit,tva_film_holand_visit, tva_film_alman_visit,
                                                         tva_film_englis_visit, tva_film_kore_jonobi_visit,tva_film_faranse_visit, tva_film_japon_visit,
                                                         tva_film_kanada_visit, tva_film_fanland_visit,tva_film_korovasi_visit, tva_film_majarestan_visit,
                                                         tva_film_lahestan_visit, tva_film_sois_visit,tva_film_belgik_visit, tva_film_rosie_visit,
                                                         tva_film_italia_visit, tva_film_bolgharestan_visit,tva_film_ostralia_visit, tva_film_norvej_visit,
                                                         tva_film_chin_visit, tva_film_tayland_visit,tva_film_sangapor_visit, tva_film_otrish_visit,
                                                         tva_film_spania_visit, tva_film_okrayn_visit,tva_film_emarat_visit, tva_film_irland_visit,
                                                         tva_film_argantin_visit, tva_film_afrigha_jonobi_visit,tva_film_danmark_visit, tva_film_shili_visit,
                                                         tva_film_malezi_visit, tva_film_honkkong_visit,tva_film_soed_visit, tva_film_sois_visit,
                                                         tva_film_mekzik_visit, tva_film_nioziland_visit,tva_film_hend_visit,]}

tva_film_country_content_visit=pd.DataFrame(tva_film_country_content_visit, columns=['tva_film_country_name2', 'tva_film_country_visit1'])
tva_film_country_content_visit=tva_film_country_content_visit.query("tva_film_country_visit1 != '0'")
tva_film_country_content_visit.sort_values('tva_film_country_visit1', axis = 0, ascending = False, inplace = True, na_position ='last') 
print("finish country of tva film")
##############################################################################################################################
########################################################## year ###############################################################
##############################################################################################################################
print("year of tva film")
df_tva_film_year=tva_df_film['year']
tva_count_of_all_year=len(tva_df_film)
tva_visit_of_all_year=tva_df_film['bazdid'].sum()

tva_film_year_1399=tva_df_film.query("year == '1399'")
tva_film_year_1399_count=len(tva_film_year_1399)
tva_film_year_1399_visit=tva_film_year_1399['bazdid'].sum()

tva_film_year_1398=tva_df_film.query("year == '1398'")
tva_film_year_1398_count=len(tva_film_year_1398)
tva_film_year_1398_visit=tva_film_year_1398['bazdid'].sum()

tva_film_year_1397=tva_df_film.query("year == '1397'")
tva_film_year_1397_count=len(tva_film_year_1397)
tva_film_year_1397_visit=tva_film_year_1397['bazdid'].sum()

tva_film_year_1396=tva_df_film.query("year == '1396'")
tva_film_year_1396_count=len(tva_film_year_1396)
tva_film_year_1396_visit=tva_film_year_1396['bazdid'].sum()

tva_film_year_1395=tva_df_film.query("year == '1395'")
tva_film_year_1395_count=len(tva_film_year_1395)
tva_film_year_1395_visit=tva_film_year_1395['bazdid'].sum()

tva_film_year_1394=tva_df_film.query("year == '1394'")
tva_film_year_1394_count=len(tva_film_year_1394)
tva_film_year_1394_visit=tva_film_year_1394['bazdid'].sum()

tva_film_year_1393=tva_df_film.query("year == '1393'")
tva_film_year_1393_count=len(tva_film_year_1393)
tva_film_year_1393_visit=tva_film_year_1393['bazdid'].sum()

tva_film_year_1392=tva_df_film.query("year == '1392'")
tva_film_year_1392_count=len(tva_film_year_1392)
tva_film_year_1392_visit=tva_film_year_1392['bazdid'].sum()

tva_film_year_1391=tva_df_film.query("year == '1391'")
tva_film_year_1391_count=len(tva_film_year_1391)
tva_film_year_1391_visit=tva_film_year_1391['bazdid'].sum()

tva_film_year_1390=tva_df_film.query("year == '1390'")
tva_film_year_1390_count=len(tva_film_year_1390)
tva_film_year_1390_visit=tva_film_year_1390['bazdid'].sum()

tva_film_year_1389=tva_df_film.query("year == '1389'")
tva_film_year_1389_count=len(tva_film_year_1389)
tva_film_year_1389_visit=tva_film_year_1389['bazdid'].sum()

tva_film_year_1388=tva_df_film.query("year == '1388'")
tva_film_year_1388_count=len(tva_film_year_1388)
tva_film_year_1388_visit=tva_film_year_1388['bazdid'].sum()

tva_film_year_1387=tva_df_film.query("year == '1387'")
tva_film_year_1387_count=len(tva_film_year_1387)
tva_film_year_1387_visit=tva_film_year_1387['bazdid'].sum()

tva_film_year_1386=tva_df_film.query("year == '1386'")
tva_film_year_1386_count=len(tva_film_year_1386)
tva_film_year_1386_visit=tva_film_year_1386['bazdid'].sum()

tva_film_year_1385=tva_df_film.query("year == '1385'")
tva_film_year_1385_count=len(tva_film_year_1385)
tva_film_year_1385_visit=tva_film_year_1385['bazdid'].sum()

tva_film_year_1384=tva_df_film.query("year == '1384'")
tva_film_year_1384_count=len(tva_film_year_1384)
tva_film_year_1384_visit=tva_film_year_1384['bazdid'].sum()

tva_film_year_1383=tva_df_film.query("year == '1383'")
tva_film_year_1383_count=len(tva_film_year_1383)
tva_film_year_1383_visit=tva_film_year_1383['bazdid'].sum()

tva_film_year_1382=tva_df_film.query("year == '1382'")
tva_film_year_1382_count=len(tva_film_year_1382)
tva_film_year_1382_visit=tva_film_year_1382['bazdid'].sum()

tva_film_year_1381=tva_df_film.query("year == '1381'")
tva_film_year_1381_count=len(tva_film_year_1381)
tva_film_year_1381_visit=tva_film_year_1381['bazdid'].sum()

tva_film_year_1380=tva_df_film.query("year == '1380'")
tva_film_year_1380_count=len(tva_film_year_1380)
tva_film_year_1380_visit=tva_film_year_1380['bazdid'].sum()

tva_film_year_1379=tva_df_film.query("year == '1379'")
tva_film_year_1379_count=len(tva_film_year_1379)
tva_film_year_1379_visit=tva_film_year_1379['bazdid'].sum()

tva_film_year_1378=tva_df_film.query("year == '1378'")
tva_film_year_1378_count=len(tva_film_year_1378)
tva_film_year_1378_visit=tva_film_year_1378['bazdid'].sum()

tva_film_year_1377=tva_df_film.query("year == '1377'")
tva_film_year_1377_count=len(tva_film_year_1377)
tva_film_year_1377_visit=tva_film_year_1377['bazdid'].sum()

tva_film_year_1376=tva_df_film.query("year == '1376'")
tva_film_year_1376_count=len(tva_film_year_1376)
tva_film_year_1376_visit=tva_film_year_1376['bazdid'].sum()

tva_film_year_1375=tva_df_film.query("year == '1375'")
tva_film_year_1375_count=len(tva_film_year_1375)
tva_film_year_1375_visit=tva_film_year_1375['bazdid'].sum()

tva_film_year_1374=tva_df_film.query("year == '1374'")
tva_film_year_1374_count=len(tva_film_year_1374)
tva_film_year_1374_visit=tva_film_year_1374['bazdid'].sum()

tva_film_year_1373=tva_df_film.query("year == '1373'")
tva_film_year_1373_count=len(tva_film_year_1373)
tva_film_year_1373_visit=tva_film_year_1373['bazdid'].sum()

tva_film_year_1372=tva_df_film.query("year == '1372'")
tva_film_year_1372_count=len(tva_film_year_1372)
tva_film_year_1372_visit=tva_film_year_1372['bazdid'].sum()

tva_film_year_1371=tva_df_film.query("year == '1371'")
tva_film_year_1371_count=len(tva_film_year_1371)
tva_film_year_1371_visit=tva_film_year_1371['bazdid'].sum()

tva_film_year_1370=tva_df_film.query("year == '1370'")
tva_film_year_1370_count=len(tva_film_year_1370)
tva_film_year_1370_visit=tva_film_year_1370['bazdid'].sum()

tva_film_year_1369=tva_df_film.query("year == '1369'")
tva_film_year_1369_count=len(tva_film_year_1369)
tva_film_year_1369_visit=tva_film_year_1369['bazdid'].sum()

tva_film_year_1368=tva_df_film.query("year == '1368'")
tva_film_year_1368_count=len(tva_film_year_1368)
tva_film_year_1368_visit=tva_film_year_1368['bazdid'].sum()

tva_film_year_1367=tva_df_film.query("year == '1367'")
tva_film_year_1367_count=len(tva_film_year_1367)
tva_film_year_1367_visit=tva_film_year_1367['bazdid'].sum()

tva_film_year_1366=tva_df_film.query("year == '1366'")
tva_film_year_1366_count=len(tva_film_year_1366)
tva_film_year_1366_visit=tva_film_year_1366['bazdid'].sum()

tva_film_year_1365=tva_df_film.query("year == '1365'")
tva_film_year_1365_count=len(tva_film_year_1365)
tva_film_year_1365_visit=tva_film_year_1365['bazdid'].sum()

tva_film_year_1364=tva_df_film.query("year == '1364'")
tva_film_year_1364_count=len(tva_film_year_1364)
tva_film_year_1364_visit=tva_film_year_1364['bazdid'].sum()

tva_film_year_1363=tva_df_film.query("year == '1363'")
tva_film_year_1363_count=len(tva_film_year_1363)
tva_film_year_1363_visit=tva_film_year_1363['bazdid'].sum()

tva_film_year_1362=tva_df_film.query("year == '1362'")
tva_film_year_1362_count=len(tva_film_year_1362)
tva_film_year_1362_visit=tva_film_year_1362['bazdid'].sum()

tva_film_year_1361=tva_df_film.query("year == '1361'")
tva_film_year_1361_count=len(tva_film_year_1361)
tva_film_year_1361_visit=tva_film_year_1361['bazdid'].sum()

tva_film_year_1360=tva_df_film.query("year == '1360'")
tva_film_year_1360_count=len(tva_film_year_1360)
tva_film_year_1360_visit=tva_film_year_1360['bazdid'].sum()

tva_film_year_1359=tva_df_film.query("year == '1359'")
tva_film_year_1359_count=len(tva_film_year_1359)
tva_film_year_1359_visit=tva_film_year_1359['bazdid'].sum()

tva_film_year_1358=tva_df_film.query("year == '1358'")
tva_film_year_1358_count=len(tva_film_year_1358)
tva_film_year_1358_visit=tva_film_year_1358['bazdid'].sum()

tva_film_year_1357=tva_df_film.query('year < 1358')
tva_film_year_1357_count=len(tva_film_year_1357)
tva_film_year_1357_visit=tva_film_year_1357['bazdid'].sum()

tva_film_year_count={'tva_film_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'tva_film_year_count': [tva_film_year_1357_count,tva_film_year_1358_count,tva_film_year_1359_count,tva_film_year_1360_count,
                                           tva_film_year_1361_count,tva_film_year_1362_count,tva_film_year_1363_count,tva_film_year_1364_count,
                                           tva_film_year_1365_count,tva_film_year_1366_count,tva_film_year_1367_count,tva_film_year_1368_count,
                                           tva_film_year_1369_count,tva_film_year_1370_count,tva_film_year_1371_count,tva_film_year_1372_count,
                                           tva_film_year_1373_count,tva_film_year_1374_count,tva_film_year_1375_count,tva_film_year_1376_count,
                                           tva_film_year_1377_count,tva_film_year_1378_count,tva_film_year_1379_count,tva_film_year_1380_count,
                                           tva_film_year_1381_count,tva_film_year_1382_count,tva_film_year_1383_count,tva_film_year_1384_count,
                                           tva_film_year_1385_count,tva_film_year_1386_count,tva_film_year_1387_count,tva_film_year_1388_count,
                                           tva_film_year_1389_count,tva_film_year_1390_count,tva_film_year_1391_count,tva_film_year_1392_count,
                                           tva_film_year_1393_count,tva_film_year_1394_count,tva_film_year_1395_count,tva_film_year_1396_count,
                                           tva_film_year_1397_count,tva_film_year_1398_count,tva_film_year_1399_count,]}
tva_film_year_visit={'tva_film_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'tva_film_year_visit': [tva_film_year_1357_visit,tva_film_year_1358_visit,tva_film_year_1359_visit,tva_film_year_1360_visit,
                                           tva_film_year_1361_visit,tva_film_year_1362_visit,tva_film_year_1363_visit,tva_film_year_1364_visit,
                                           tva_film_year_1365_visit,tva_film_year_1366_visit,tva_film_year_1367_visit,tva_film_year_1368_visit,
                                           tva_film_year_1369_visit,tva_film_year_1370_visit,tva_film_year_1371_visit,tva_film_year_1372_visit,
                                           tva_film_year_1373_visit,tva_film_year_1374_visit,tva_film_year_1375_visit,tva_film_year_1376_visit,
                                           tva_film_year_1377_visit,tva_film_year_1378_visit,tva_film_year_1379_visit,tva_film_year_1380_visit,
                                           tva_film_year_1381_visit,tva_film_year_1382_visit,tva_film_year_1383_visit,tva_film_year_1384_visit,
                                           tva_film_year_1385_visit,tva_film_year_1386_visit,tva_film_year_1387_visit,tva_film_year_1388_visit,
                                           tva_film_year_1389_visit,tva_film_year_1390_visit,tva_film_year_1391_visit,tva_film_year_1392_visit,
                                           tva_film_year_1393_visit,tva_film_year_1394_visit,tva_film_year_1395_visit,tva_film_year_1396_visit,
                                           tva_film_year_1397_visit,tva_film_year_1398_visit,tva_film_year_1399_visit,]}
tva_film_year_count=pd.DataFrame(tva_film_year_count, columns=['tva_film_year','tva_film_year_count'])
tva_film_year_visit=pd.DataFrame(tva_film_year_visit, columns=['tva_film_year','tva_film_year_visit'])
print("finish year of tva film")
##############################################################################################################################
########################################################## IMDB ###############################################################
##############################################################################################################################
print("imdb of tva film")
df_tva_film_imdb=tva_df_film['imdb']
tva_count_of_all_imdb=len(df_tva_film_imdb)
tva_visit_of_all_imdb=tva_df_film['bazdid'].sum()

tva_film_imdb_lower6=tva_df_film.query('imdb < 6')
tva_film_imdb_lower6_count=len(tva_film_imdb_lower6)
tva_film_imdb_lower6_visit=tva_film_imdb_lower6['bazdid'].sum()

tva_film_imdb_between_6_7=tva_df_film.query('imdb > 5.9 and imdb < 7')
tva_film_imdb_between_6_7_count=len(tva_film_imdb_between_6_7)
tva_film_imdb_between_6_7_visit=tva_film_imdb_between_6_7['bazdid'].sum()

tva_film_imdb_between_7_8=tva_df_film.query('imdb > 6.9 and imdb < 8')
tva_film_imdb_between_7_8_count=len(tva_film_imdb_between_7_8)
tva_film_imdb_between_7_8_visit=tva_film_imdb_between_7_8['bazdid'].sum()

tva_film_imdb_between_8_9=tva_df_film.query('imdb > 7.9 and imdb < 9')
tva_film_imdb_between_8_9_count=len(tva_film_imdb_between_8_9)
tva_film_imdb_between_8_9_visit=tva_film_imdb_between_8_9['bazdid'].sum()

tva_film_imdb_upper9=tva_df_film.query('imdb > 8.9')
tva_film_imdb_upper9_count=len(tva_film_imdb_upper9)
tva_film_imdb_upper9_visit=tva_film_imdb_upper9['bazdid'].sum()

tva_film_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'count_of_imdb_film': [tva_film_imdb_lower6_count,
                                        tva_film_imdb_between_6_7_count,
                                        tva_film_imdb_between_7_8_count,
                                        tva_film_imdb_between_8_9_count,
                                        tva_film_imdb_upper9_count]}
                 
tva_film_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'visit_of_imdb_film': [tva_film_imdb_lower6_visit,
                                        tva_film_imdb_between_6_7_visit,
                                        tva_film_imdb_between_7_8_visit,
                                        tva_film_imdb_between_8_9_visit,
                                        tva_film_imdb_upper9_visit]}
tva_film_imdb_count=pd.DataFrame(tva_film_imdb_count, columns=['limitation', 'count_of_imdb_film'])
tva_film_imdb_visit=pd.DataFrame(tva_film_imdb_visit, columns=['limitation', 'visit_of_imdb_film'])
print("finish imdb of tva film")
##############################################################################################################################
########################################################## 10 contents film ###############################################################
##############################################################################################################################
print("popular of tva film")
tva_df_film.sort_values('bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_film_content_popular_bazdid=[]
tva_film_content_popular_visitnumber_bazdid=[]
tva_film_content_popular_name_bazdid=[]
tva_film_content_popular_name_bazdid=tva_df_film["title1"].tolist()
tva_film_content_popular_bazdid.append(tva_film_content_popular_name_bazdid)
tva_film_content_popular_visitnumber_bazdid=tva_df_film["bazdid"].tolist()
tva_film_content_popular_bazdid.append(tva_film_content_popular_visitnumber_bazdid)
tva_film_content_popular_bazdid_with_lenz=tva_film_content_popular_bazdid
tva_film_content_popular_bazdid={'tva_film_content_popular_name_bazdid' : [tva_film_content_popular_name_bazdid[0], 
                                                           tva_film_content_popular_name_bazdid[1], 
                                                           tva_film_content_popular_name_bazdid[2],
                                                           tva_film_content_popular_name_bazdid[3], 
                                                           tva_film_content_popular_name_bazdid[4], 
                                                           tva_film_content_popular_name_bazdid[5],
                                                           tva_film_content_popular_name_bazdid[6], 
                                                           tva_film_content_popular_name_bazdid[7], 
                                                           tva_film_content_popular_name_bazdid[8],
                                                           tva_film_content_popular_name_bazdid[9]],
                            'tva_film_content_popular_visitnumber_bazdid' : [tva_film_content_popular_visitnumber_bazdid[0], tva_film_content_popular_visitnumber_bazdid[1],
                                                                  tva_film_content_popular_visitnumber_bazdid[2], tva_film_content_popular_visitnumber_bazdid[3],
                                                                  tva_film_content_popular_visitnumber_bazdid[4], tva_film_content_popular_visitnumber_bazdid[5],
                                                                  tva_film_content_popular_visitnumber_bazdid[6], tva_film_content_popular_visitnumber_bazdid[7],
                                                                  tva_film_content_popular_visitnumber_bazdid[8], tva_film_content_popular_visitnumber_bazdid[9]]}
tva_film_content_popular_bazdid=pd.DataFrame(tva_film_content_popular_bazdid, columns=['tva_film_content_popular_name_bazdid' , 'tva_film_content_popular_visitnumber_bazdid'])
tva_film_content_popular_bazdid.sort_values('tva_film_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_df_film.sort_values('karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_film_content_popular_karbaran=[]
tva_film_content_popular_visitnumber_karbaran=[]
tva_film_content_popular_name_karbaran=[]
tva_film_content_popular_name_karbaran=tva_df_film["title1"].tolist()
tva_film_content_popular_karbaran.append(tva_film_content_popular_name_karbaran)
tva_film_content_popular_visitnumber_karbaran=tva_df_film["karbaran"].tolist()
tva_film_content_popular_karbaran.append(tva_film_content_popular_visitnumber_karbaran)
tva_film_content_popular_karbaran_with_lenz=tva_film_content_popular_karbaran
tva_film_content_popular_karbaran={'tva_film_content_popular_name_karbaran' : [tva_film_content_popular_name_karbaran[0], 
                                                           tva_film_content_popular_name_karbaran[1], 
                                                           tva_film_content_popular_name_karbaran[2],
                                                           tva_film_content_popular_name_karbaran[3], 
                                                           tva_film_content_popular_name_karbaran[4], 
                                                           tva_film_content_popular_name_karbaran[5],
                                                           tva_film_content_popular_name_karbaran[6], 
                                                           tva_film_content_popular_name_karbaran[7], 
                                                           tva_film_content_popular_name_karbaran[8],
                                                           tva_film_content_popular_name_karbaran[9]],
                            'tva_film_content_popular_visitnumber_karbaran' : [tva_film_content_popular_visitnumber_karbaran[0], tva_film_content_popular_visitnumber_karbaran[1],
                                                                  tva_film_content_popular_visitnumber_karbaran[2], tva_film_content_popular_visitnumber_karbaran[3],
                                                                  tva_film_content_popular_visitnumber_karbaran[4], tva_film_content_popular_visitnumber_karbaran[5],
                                                                  tva_film_content_popular_visitnumber_karbaran[6], tva_film_content_popular_visitnumber_karbaran[7],
                                                                  tva_film_content_popular_visitnumber_karbaran[8], tva_film_content_popular_visitnumber_karbaran[9]]}
tva_film_content_popular_karbaran=pd.DataFrame(tva_film_content_popular_karbaran, columns=['tva_film_content_popular_name_karbaran' , 'tva_film_content_popular_visitnumber_karbaran'])
tva_film_content_popular_karbaran.sort_values('tva_film_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_df_film.sort_values('minute', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_film_content_popular_minute=[]
tva_film_content_popular_visitnumber_minute=[]
tva_film_content_popular_name_minute=[]
tva_film_content_popular_name_minute=tva_df_film["title1"].tolist()
tva_film_content_popular_minute.append(tva_film_content_popular_name_minute)
tva_film_content_popular_visitnumber_minute=tva_df_film["minute"].tolist()
tva_film_content_popular_minute.append(tva_film_content_popular_visitnumber_minute)
tva_film_content_popular_minute_with_lenz=tva_film_content_popular_minute
tva_film_content_popular_minute={'tva_film_content_popular_name_minute' : [tva_film_content_popular_name_minute[0], 
                                                           tva_film_content_popular_name_minute[1], 
                                                           tva_film_content_popular_name_minute[2],
                                                           tva_film_content_popular_name_minute[3], 
                                                           tva_film_content_popular_name_minute[4], 
                                                           tva_film_content_popular_name_minute[5],
                                                           tva_film_content_popular_name_minute[6], 
                                                           tva_film_content_popular_name_minute[7], 
                                                           tva_film_content_popular_name_minute[8],
                                                           tva_film_content_popular_name_minute[9]],
                            'tva_film_content_popular_visitnumber_minute' : [tva_film_content_popular_visitnumber_minute[0], tva_film_content_popular_visitnumber_minute[1],
                                                                  tva_film_content_popular_visitnumber_minute[2], tva_film_content_popular_visitnumber_minute[3],
                                                                  tva_film_content_popular_visitnumber_minute[4], tva_film_content_popular_visitnumber_minute[5],
                                                                  tva_film_content_popular_visitnumber_minute[6], tva_film_content_popular_visitnumber_minute[7],
                                                                  tva_film_content_popular_visitnumber_minute[8], tva_film_content_popular_visitnumber_minute[9]]}
tva_film_content_popular_minute=pd.DataFrame(tva_film_content_popular_minute, columns=['tva_film_content_popular_name_minute' , 'tva_film_content_popular_visitnumber_minute'])
tva_film_content_popular_minute.sort_values('tva_film_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
tva_film_content_popular_minute=round(tva_film_content_popular_minute*60, 0)
print("finish popular of tva film")
##############################################################################################################################
##############################################################################################################################
########################################################## serial ###############################################################
##############################################################################################################################
##############################################################################################################################
#tva_df_serial.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
tva_df_serial=tva_df_serial.groupby(['title1', 'genre', 'country', 'year', 'imdb']).sum().reset_index()

print("statistics of tva serial")
tva_serial_count_content=tva_df_serial['bazdid']
tva_serial_count_content=len(tva_serial_count_content)
tva_serial_sum_bazdid=tva_df_serial['bazdid'].sum()
tva_serial_sum_karbaran=tva_df_serial['karbaran'].sum()
tva_serial_sum_minute=tva_df_serial['minute'].sum()

##############################################################################################################################
########################################################## genre ###############################################################
##############################################################################################################################
print("genre of tva serial")
df_tva_serial_genre=tva_df_serial['genre']
tva_count_of_all_genre=len(tva_df_serial)
tva_visit_of_all_genre=tva_df_serial['bazdid'].sum()

tva_serial_siasi = df_tva_serial_genre.str.count("سیاسی") 
tva_serial_siasi=pd.DataFrame(tva_serial_siasi) 
tva_serial_siasi=tva_serial_siasi['genre'].sum()
tva_serial_siasi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('سیاسی')]
tva_serial_siasi_visit=tva_serial_siasi_visit['bazdid'].sum()

tva_serial_tarsnak = df_tva_serial_genre.str.count("ترسناک") 
tva_serial_tarsnak=pd.DataFrame(tva_serial_tarsnak) 
tva_serial_tarsnak=tva_serial_tarsnak['genre'].sum()
tva_serial_vahshat = df_tva_serial_genre.str.count("وحشت") 
tva_serial_vahshat=pd.DataFrame(tva_serial_vahshat) 
tva_serial_vahshat=tva_serial_vahshat['genre'].sum()
tva_serial_tarsnak=tva_serial_tarsnak+tva_serial_vahshat
tva_serial_tarsnak_visit = tva_df_serial[tva_df_serial['genre'].str.contains('ترسناک')]
tva_serial_tarsnak_visit=tva_serial_tarsnak_visit['bazdid'].sum()
tva_serial_vahshat_visit = tva_df_serial[tva_df_serial['genre'].str.contains('وحشت')]
tva_serial_vahshat_visit=tva_serial_vahshat_visit['bazdid'].sum()
tva_serial_tarsnak_visit=tva_serial_tarsnak_visit+tva_serial_vahshat_visit

tva_serial_razalod = df_tva_serial_genre.str.count("رازآلود") 
tva_serial_razalod=pd.DataFrame(tva_serial_razalod) 
tva_serial_razalod=tva_serial_razalod['genre'].sum()
tva_serial_razalod1 = df_tva_serial_genre.str.count("راز آلود") 
tva_serial_razalod1=pd.DataFrame(tva_serial_razalod1) 
tva_serial_razalod1=tva_serial_razalod1['genre'].sum()
tva_serial_razalod=tva_serial_razalod+tva_serial_razalod1
tva_serial_razalod_visit = tva_df_serial[tva_df_serial['genre'].str.contains('رازآلود')]
tva_serial_razalod_visit=tva_serial_razalod_visit['bazdid'].sum()
tva_serial_razalod1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('رازآلود')]
tva_serial_razalod1_visit=tva_serial_razalod1_visit['bazdid'].sum()
tva_serial_razalod_visit=tva_serial_razalod_visit+tva_serial_razalod1_visit

tva_serial_zendeginame = df_tva_serial_genre.str.count("زندگینامه") 
tva_serial_zendeginame=pd.DataFrame(tva_serial_zendeginame) 
tva_serial_zendeginame=tva_serial_zendeginame['genre'].sum()
tva_serial_zendeginame1 = df_tva_serial_genre.str.count("زندگی نامه") 
tva_serial_zendeginame1=pd.DataFrame(tva_serial_zendeginame1) 
tva_serial_zendeginame1=tva_serial_zendeginame1['genre'].sum()
tva_serial_zendeginame=tva_serial_zendeginame+tva_serial_zendeginame1
tva_serial_zendeginame_visit = tva_df_serial[tva_df_serial['genre'].str.contains('زندگینامه')]
tva_serial_zendeginame_visit=tva_serial_zendeginame_visit['bazdid'].sum()
tva_serial_zendeginame1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('زندگینامه')]
tva_serial_zendeginame1_visit=tva_serial_zendeginame1_visit['bazdid'].sum()
tva_serial_zendeginame_visit=tva_serial_zendeginame_visit+tva_serial_zendeginame1_visit

tva_serial_romantic = df_tva_serial_genre.str.count("رمانتیک") 
tva_serial_romantic=pd.DataFrame(tva_serial_romantic) 
tva_serial_romantic=tva_serial_romantic['genre'].sum()
tva_serial_romantic_visit = tva_df_serial[tva_df_serial['genre'].str.contains('رمانتیک')]
tva_serial_romantic_visit=tva_serial_romantic_visit['bazdid'].sum()

tva_serial_mostanad = df_tva_serial_genre.str.count("مستند") 
tva_serial_mostanad=pd.DataFrame(tva_serial_mostanad) 
tva_serial_mostanad=tva_serial_mostanad['genre'].sum()
tva_serial_mostanad_visit = tva_df_serial[tva_df_serial['genre'].str.contains('مستند')]
tva_serial_mostanad_visit=tva_serial_mostanad_visit['bazdid'].sum()

tva_serial_jenai = df_tva_serial_genre.str.count("جنائی") 
tva_serial_jenai=pd.DataFrame(tva_serial_jenai) 
tva_serial_jenai=tva_serial_jenai['genre'].sum()
tva_serial_jenai1 = df_tva_serial_genre.str.count("جنایی") 
tva_serial_jenai1=pd.DataFrame(tva_serial_jenai1) 
tva_serial_jenai1=tva_serial_jenai1['genre'].sum()
tva_serial_jenai=tva_serial_jenai+tva_serial_jenai1
tva_serial_jenai_visit = tva_df_serial[tva_df_serial['genre'].str.contains('جنائی')]
tva_serial_jenai_visit=tva_serial_jenai_visit['bazdid'].sum()
tva_serial_jenai1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('جنائی')]
tva_serial_jenai1_visit=tva_serial_jenai1_visit['bazdid'].sum()
tva_serial_jenai_visit=tva_serial_jenai_visit+tva_serial_jenai1_visit

tva_serial_tarikhi = df_tva_serial_genre.str.count("تاریخی") 
tva_serial_tarikhi=pd.DataFrame(tva_serial_tarikhi) 
tva_serial_tarikhi=tva_serial_tarikhi['genre'].sum()
tva_serial_tarikhi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('تاریخی')]
tva_serial_tarikhi_visit=tva_serial_tarikhi_visit['bazdid'].sum()

tva_serial_animeyshen = df_tva_serial_genre.str.count("انیمیشن") 
tva_serial_animeyshen=pd.DataFrame(tva_serial_animeyshen) 
tva_serial_animeyshen=tva_serial_animeyshen['genre'].sum()
tva_serial_animeyshen_visit = tva_df_serial[tva_df_serial['genre'].str.contains('انیمیشن')]
tva_serial_animeyshen_visit=tva_serial_animeyshen_visit['bazdid'].sum()

tva_serial_kodak = df_tva_serial_genre.str.count("کودک") 
tva_serial_kodak=pd.DataFrame(tva_serial_kodak) 
tva_serial_kodak=tva_serial_kodak['genre'].sum()
tva_serial_kodak1 = df_tva_serial_genre.str.count("کودکان") 
tva_serial_kodak1=pd.DataFrame(tva_serial_kodak1) 
tva_serial_kodak1=tva_serial_kodak1['genre'].sum()
tva_serial_kodak=tva_serial_kodak+tva_serial_kodak1
tva_serial_kodak_visit = tva_df_serial[tva_df_serial['genre'].str.contains('کودک')]
tva_serial_kodak_visit=tva_serial_kodak_visit['bazdid'].sum()
tva_serial_kodak1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('کودک')]
tva_serial_kodak1_visit=tva_serial_kodak1_visit['bazdid'].sum()
tva_serial_kodak_visit=tva_serial_kodak_visit+tva_serial_kodak1_visit

tva_serial_hayejanangiz = df_tva_serial_genre.str.count("هیجان انگیز") 
tva_serial_hayejanangiz=pd.DataFrame(tva_serial_hayejanangiz) 
tva_serial_hayejanangiz=tva_serial_hayejanangiz['genre'].sum()
tva_serial_hayejanangiz_visit = tva_df_serial[tva_df_serial['genre'].str.contains('هیجان انگیز')]
tva_serial_hayejanangiz_visit=tva_serial_hayejanangiz_visit['bazdid'].sum()

tva_serial_khanevadegi = df_tva_serial_genre.str.count("خانوادگی") 
tva_serial_khanevadegi=pd.DataFrame(tva_serial_khanevadegi) 
tva_serial_khanevadegi=tva_serial_khanevadegi['genre'].sum()
tva_serial_khanevadegi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('خانوادگی')]
tva_serial_khanevadegi_visit=tva_serial_khanevadegi_visit['bazdid'].sum()

tva_serial_majarajoi = df_tva_serial_genre.str.count("ماجراجویی") 
tva_serial_majarajoi=pd.DataFrame(tva_serial_majarajoi) 
tva_serial_majarajoi=tva_serial_majarajoi['genre'].sum()
tva_serial_majarai = df_tva_serial_genre.str.count("ماجرایی") 
tva_serial_majarai=pd.DataFrame(tva_serial_majarai) 
tva_serial_majarai=tva_serial_majarai['genre'].sum()
tva_serial_majarajoi=tva_serial_majarajoi+tva_serial_majarai
tva_serial_majarajoi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('ماجراجویی')]
tva_serial_majarajoi_visit=tva_serial_majarajoi_visit['bazdid'].sum()
tva_serial_majarajoi1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('ماجراجویی')]
tva_serial_majarajoi1_visit=tva_serial_majarajoi1_visit['bazdid'].sum()
tva_serial_majarajoi_visit=tva_serial_majarajoi_visit+tva_serial_majarajoi1_visit

tva_serial_deram = df_tva_serial_genre.str.count("درام") 
tva_serial_deram=pd.DataFrame(tva_serial_deram) 
tva_serial_deram=tva_serial_deram['genre'].sum()
tva_serial_deram_visit = tva_df_serial[tva_df_serial['genre'].str.contains('درام')]
tva_serial_deram_visit=tva_serial_deram_visit['bazdid'].sum()

tva_serial_komedi = df_tva_serial_genre.str.count("کمدی") 
tva_serial_komedi=pd.DataFrame(tva_serial_komedi) 
tva_serial_komedi=tva_serial_komedi['genre'].sum()
tva_serial_komedi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('کمدی')]
tva_serial_komedi_visit=tva_serial_komedi_visit['bazdid'].sum()

tva_serial_vestern = df_tva_serial_genre.str.count("وسترن") 
tva_serial_vestern=pd.DataFrame(tva_serial_vestern) 
tva_serial_vestern=tva_serial_vestern['genre'].sum()
tva_serial_vestern_visit = tva_df_serial[tva_df_serial['genre'].str.contains('وسترن')]
tva_serial_vestern_visit=tva_serial_vestern_visit['bazdid'].sum()

tva_serial_fantezi = df_tva_serial_genre.str.count("فانتزی") 
tva_serial_fantezi=pd.DataFrame(tva_serial_fantezi) 
tva_serial_fantezi=tva_serial_fantezi['genre'].sum()
tva_serial_fantezi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('فانتزی')]
tva_serial_fantezi_visit=tva_serial_fantezi_visit['bazdid'].sum()

tva_serial_varzeshi = df_tva_serial_genre.str.count("ورزشی") 
tva_serial_varzeshi=pd.DataFrame(tva_serial_varzeshi) 
tva_serial_varzeshi=tva_serial_varzeshi['genre'].sum()
tva_serial_varzeshi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('ورزشی')]
tva_serial_varzeshi_visit=tva_serial_varzeshi_visit['bazdid'].sum()

tva_serial_elmi_takhayoli = df_tva_serial_genre.str.count("علمی-تخیلی") 
tva_serial_elmi_takhayoli=pd.DataFrame(tva_serial_elmi_takhayoli) 
tva_serial_elmi_takhayoli=tva_serial_elmi_takhayoli['genre'].sum()
tva_serial_elmi_takhayoli_visit = tva_df_serial[tva_df_serial['genre'].str.contains('علمی-تخیلی')]
tva_serial_elmi_takhayoli_visit=tva_serial_elmi_takhayoli_visit['bazdid'].sum()

tva_serial_acshen = df_tva_serial_genre.str.count("اکشن") 
tva_serial_acshen=pd.DataFrame(tva_serial_acshen) 
tva_serial_acshen=tva_serial_acshen['genre'].sum()
tva_serial_acshen_visit = tva_df_serial[tva_df_serial['genre'].str.contains('اکشن')]
tva_serial_acshen_visit=tva_serial_acshen_visit['bazdid'].sum()

tva_serial_mozical = df_tva_serial_genre.str.count("موزیکال") 
tva_serial_mozical=pd.DataFrame(tva_serial_mozical) 
tva_serial_mozical=tva_serial_mozical['genre'].sum()
tva_serial_mozical_visit = tva_df_serial[tva_df_serial['genre'].str.contains('موزیکال')]
tva_serial_mozical_visit=tva_serial_mozical_visit['bazdid'].sum()

tva_serial_jangi = df_tva_serial_genre.str.count("جنگی") 
tva_serial_jangi=pd.DataFrame(tva_serial_jangi) 
tva_serial_jangi=tva_serial_jangi['genre'].sum()
tva_serial_jangi_visit = tva_df_serial[tva_df_serial['genre'].str.contains('جنگی')]
tva_serial_jangi_visit=tva_serial_jangi_visit['bazdid'].sum()

tva_serial_goftego = df_tva_serial_genre.str.count("گفتگو") 
tva_serial_goftego=pd.DataFrame(tva_serial_goftego) 
tva_serial_goftego=tva_serial_goftego['genre'].sum()
tva_serial_goftego_visit = tva_df_serial[tva_df_serial['genre'].str.contains('گفتگو')]
tva_serial_goftego_visit=tva_serial_goftego_visit['bazdid'].sum()

tva_serial_khiali = df_tva_serial_genre.str.count("خیالی") 
tva_serial_khiali=pd.DataFrame(tva_serial_khiali) 
tva_serial_khiali=tva_serial_khiali['genre'].sum()
tva_serial_khiali1 = df_tva_serial_genre.str.count("تخیلی") 
tva_serial_khiali1=pd.DataFrame(tva_serial_khiali1) 
tva_serial_khiali1=tva_serial_khiali1['genre'].sum()
tva_serial_khiali=tva_serial_khiali+tva_serial_khiali1
tva_serial_khiali_visit = tva_df_serial[tva_df_serial['genre'].str.contains('خیالی')]
tva_serial_khiali_visit=tva_serial_khiali_visit['bazdid'].sum()
tva_serial_khiali1_visit = tva_df_serial[tva_df_serial['genre'].str.contains('خیالی')]
tva_serial_khiali1_visit=tva_serial_khiali1_visit['bazdid'].sum()
tva_serial_khiali_visit=tva_serial_khiali_visit+tva_serial_khiali1_visit

tva_serial_count_of_genre={'tva_serial_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'tva_serial_count_of_genre1': [tva_serial_mozical, tva_serial_hayejanangiz, tva_serial_varzeshi,
                                tva_serial_goftego, tva_serial_mostanad, tva_serial_majarajoi, 
                                tva_serial_kodak,tva_serial_komedi, tva_serial_fantezi,tva_serial_elmi_takhayoli, 
                                tva_serial_siasi,tva_serial_zendeginame, tva_serial_romantic, 
                                tva_serial_razalod,tva_serial_deram, tva_serial_khiali, 
                                tva_serial_khanevadegi, tva_serial_jangi, tva_serial_jenai,
                                tva_serial_tarsnak, tva_serial_tarikhi,
                                tva_serial_animeyshen, tva_serial_acshen, tva_serial_vestern]}
tva_serial_count_of_genre=pd.DataFrame(tva_serial_count_of_genre, columns=['tva_serial_type_of_genre', 'tva_serial_count_of_genre1'])
tva_serial_count_of_genre=tva_serial_count_of_genre.query("tva_serial_count_of_genre1 != '0'")
tva_serial_count_of_genre.sort_values('tva_serial_count_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')

tva_serial_visit_of_genre={'tva_serial_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'tva_serial_visit_of_genre1': [tva_serial_mozical, tva_serial_hayejanangiz, tva_serial_varzeshi,
                                tva_serial_goftego, tva_serial_mostanad, tva_serial_majarajoi, 
                                tva_serial_kodak,tva_serial_komedi, tva_serial_fantezi,tva_serial_elmi_takhayoli, 
                                tva_serial_siasi,tva_serial_zendeginame, tva_serial_romantic, 
                                tva_serial_razalod,tva_serial_deram, tva_serial_khiali, 
                                tva_serial_khanevadegi, tva_serial_jangi, tva_serial_jenai,
                                tva_serial_tarsnak, tva_serial_tarikhi,
                                tva_serial_animeyshen, tva_serial_acshen, tva_serial_vestern]}
tva_serial_visit_of_genre=pd.DataFrame(tva_serial_visit_of_genre, columns=['tva_serial_type_of_genre', 'tva_serial_visit_of_genre1'])
tva_serial_visit_of_genre=tva_serial_visit_of_genre.query("tva_serial_visit_of_genre1 != '0'")
tva_serial_visit_of_genre.sort_values('tva_serial_visit_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')
print("finish genre of tva serial")
##############################################################################################################################
########################################################## country ###############################################################
##############################################################################################################################
print("country of tva serial")
df_tva_serial_country=tva_df_serial['country']
tva_serial_count_of_all_country=len(tva_df_serial)
tva_serial_visit_of_all_country=tva_df_serial['bazdid'].sum()

tva_serial_amrika = df_tva_serial_country.str.count("آمریکا") 
tva_serial_amrika=pd.DataFrame(tva_serial_amrika) 
tva_serial_amrika=tva_serial_amrika['country'].sum()
tva_serial_amrika_visit = tva_df_serial[tva_df_serial['country'].str.contains('آمریکا')]
tva_serial_amrika_visit=tva_serial_amrika_visit['bazdid'].sum()

tva_serial_iran = df_tva_serial_country.str.count("ایران") 
tva_serial_iran=pd.DataFrame(tva_serial_iran) 
tva_serial_iran=tva_serial_iran['country'].sum()
tva_serial_iran_visit = tva_df_serial[tva_df_serial['country'].str.contains('ایران')]
tva_serial_iran_visit=tva_serial_iran_visit['bazdid'].sum()

tva_serial_holand = df_tva_serial_country.str.count("هلند") 
tva_serial_holand=pd.DataFrame(tva_serial_holand) 
tva_serial_holand=tva_serial_holand['country'].sum()
tva_serial_holand_visit = tva_df_serial[tva_df_serial['country'].str.contains('هلند')]
tva_serial_holand_visit=tva_serial_holand_visit['bazdid'].sum()

tva_serial_alman = df_tva_serial_country.str.count("آلمان") 
tva_serial_alman=pd.DataFrame(tva_serial_alman) 
tva_serial_alman=tva_serial_alman['country'].sum()
tva_serial_alman_visit = tva_df_serial[tva_df_serial['country'].str.contains('آلمان')]
tva_serial_alman_visit=tva_serial_alman_visit['bazdid'].sum()

tva_serial_englis = df_tva_serial_country.str.count("انگلیس") 
tva_serial_englis=pd.DataFrame(tva_serial_englis) 
tva_serial_englis=tva_serial_englis['country'].sum()
tva_serial_englis_visit = tva_df_serial[tva_df_serial['country'].str.contains('انگلیس')]
tva_serial_englis_visit=tva_serial_englis_visit['bazdid'].sum()
tva_serial_englis1 = df_tva_serial_country.str.count("انگلستان") 
tva_serial_englis1=pd.DataFrame(tva_serial_englis1) 
tva_serial_englis1=tva_serial_englis1['country'].sum()
tva_serial_englis1_visit = tva_df_serial[tva_df_serial['country'].str.contains('انگلستان')]
tva_serial_englis1_visit=tva_serial_englis1_visit['bazdid'].sum()
tva_serial_englis_visit=tva_serial_englis_visit+tva_serial_englis1_visit
tva_serial_englis=tva_serial_englis+tva_serial_englis1

tva_serial_kore_jonobi = df_tva_serial_country.str.count("کره جنوبی") 
tva_serial_kore_jonobi=pd.DataFrame(tva_serial_kore_jonobi) 
tva_serial_kore_jonobi=tva_serial_kore_jonobi['country'].sum()
tva_serial_kore_jonobi_visit = tva_df_serial[tva_df_serial['country'].str.contains('کره جنوبی')]
tva_serial_kore_jonobi_visit=tva_serial_kore_jonobi_visit['bazdid'].sum()

tva_serial_faranse = df_tva_serial_country.str.count("فرانسه") 
tva_serial_faranse=pd.DataFrame(tva_serial_faranse) 
tva_serial_faranse=tva_serial_faranse['country'].sum()
tva_serial_faranse_visit = tva_df_serial[tva_df_serial['country'].str.contains('فرانسه')]
tva_serial_faranse_visit=tva_serial_faranse_visit['bazdid'].sum()

tva_serial_japon = df_tva_serial_country.str.count("ژاپن") 
tva_serial_japon=pd.DataFrame(tva_serial_japon) 
tva_serial_japon=tva_serial_japon['country'].sum()
tva_serial_japon_visit = tva_df_serial[tva_df_serial['country'].str.contains('ژاپن')]
tva_serial_japon_visit=tva_serial_japon_visit['bazdid'].sum()

tva_serial_kanada = df_tva_serial_country.str.count("کانادا") 
tva_serial_kanada=pd.DataFrame(tva_serial_kanada) 
tva_serial_kanada=tva_serial_kanada['country'].sum()
tva_serial_kanada_visit = tva_df_serial[tva_df_serial['country'].str.contains('کانادا')]
tva_serial_kanada_visit=tva_serial_kanada_visit['bazdid'].sum()

tva_serial_fanland = df_tva_serial_country.str.count("فنلاند") 
tva_serial_fanland=pd.DataFrame(tva_serial_fanland) 
tva_serial_fanland=tva_serial_fanland['country'].sum()
tva_serial_fanland_visit = tva_df_serial[tva_df_serial['country'].str.contains('فنلاند')]
tva_serial_fanland_visit=tva_serial_fanland_visit['bazdid'].sum()

tva_serial_korovasi = df_tva_serial_country.str.count("کرواسی") 
tva_serial_korovasi=pd.DataFrame(tva_serial_korovasi) 
tva_serial_korovasi=tva_serial_korovasi['country'].sum()
tva_serial_korovasi_visit = tva_df_serial[tva_df_serial['country'].str.contains('کرواسی')]
tva_serial_korovasi_visit=tva_serial_korovasi_visit['bazdid'].sum()

tva_serial_majarestan = df_tva_serial_country.str.count("مجارستان") 
tva_serial_majarestan=pd.DataFrame(tva_serial_majarestan) 
tva_serial_majarestan=tva_serial_majarestan['country'].sum()
tva_serial_majarestan_visit = tva_df_serial[tva_df_serial['country'].str.contains('مجارستان')]
tva_serial_majarestan_visit=tva_serial_majarestan_visit['bazdid'].sum()

tva_serial_lahestan = df_tva_serial_country.str.count("لهستان") 
tva_serial_lahestan=pd.DataFrame(tva_serial_lahestan) 
tva_serial_lahestan=tva_serial_lahestan['country'].sum()
tva_serial_lahestan_visit = tva_df_serial[tva_df_serial['country'].str.contains('لهستان')]
tva_serial_lahestan_visit=tva_serial_lahestan_visit['bazdid'].sum()

tva_serial_sois = df_tva_serial_country.str.count("سوئیس") 
tva_serial_sois=pd.DataFrame(tva_serial_sois) 
tva_serial_sois=tva_serial_sois['country'].sum()
tva_serial_sois_visit = tva_df_serial[tva_df_serial['country'].str.contains('سوئیس')]
tva_serial_sois_visit=tva_serial_sois_visit['bazdid'].sum()

tva_serial_belgik = df_tva_serial_country.str.count("بلژیک") 
tva_serial_belgik=pd.DataFrame(tva_serial_belgik) 
tva_serial_belgik=tva_serial_belgik['country'].sum()
tva_serial_belgik_visit = tva_df_serial[tva_df_serial['country'].str.contains('بلژیک')]
tva_serial_belgik_visit=tva_serial_belgik_visit['bazdid'].sum()

tva_serial_rosie = df_tva_serial_country.str.count("روسیه") 
tva_serial_rosie=pd.DataFrame(tva_serial_rosie) 
tva_serial_rosie=tva_serial_rosie['country'].sum()
tva_serial_rosie_visit = tva_df_serial[tva_df_serial['country'].str.contains('روسیه')]
tva_serial_rosie_visit=tva_serial_rosie_visit['bazdid'].sum()

tva_serial_italia = df_tva_serial_country.str.count("ایتالیا") 
tva_serial_italia=pd.DataFrame(tva_serial_italia) 
tva_serial_italia=tva_serial_italia['country'].sum()
tva_serial_italia_visit = tva_df_serial[tva_df_serial['country'].str.contains('ایتالیا')]
tva_serial_italia_visit=tva_serial_italia_visit['bazdid'].sum()

tva_serial_bolgharestan = df_tva_serial_country.str.count("بلغارستان") 
tva_serial_bolgharestan=pd.DataFrame(tva_serial_bolgharestan) 
tva_serial_bolgharestan=tva_serial_bolgharestan['country'].sum()
tva_serial_bolgharestan_visit = tva_df_serial[tva_df_serial['country'].str.contains('بلغارستان')]
tva_serial_bolgharestan_visit=tva_serial_bolgharestan_visit['bazdid'].sum()

tva_serial_ostralia = df_tva_serial_country.str.count("استرالیا") 
tva_serial_ostralia=pd.DataFrame(tva_serial_ostralia) 
tva_serial_ostralia=tva_serial_ostralia['country'].sum()
tva_serial_ostralia_visit = tva_df_serial[tva_df_serial['country'].str.contains('استرالیا')]
tva_serial_ostralia_visit=tva_serial_ostralia_visit['bazdid'].sum()

tva_serial_norvej = df_tva_serial_country.str.count("نروژ") 
tva_serial_norvej=pd.DataFrame(tva_serial_norvej) 
tva_serial_norvej=tva_serial_norvej['country'].sum()
tva_serial_norvej_visit = tva_df_serial[tva_df_serial['country'].str.contains('نروژ')]
tva_serial_norvej_visit=tva_serial_norvej_visit['bazdid'].sum()

tva_serial_chin = df_tva_serial_country.str.count("چین") 
tva_serial_chin=pd.DataFrame(tva_serial_chin) 
tva_serial_chin=tva_serial_chin['country'].sum()
tva_serial_chin_visit = tva_df_serial[tva_df_serial['country'].str.contains('چین')]
tva_serial_chin_visit=tva_serial_chin_visit['bazdid'].sum()

tva_serial_tayland = df_tva_serial_country.str.count("تایلند") 
tva_serial_tayland=pd.DataFrame(tva_serial_tayland) 
tva_serial_tayland=tva_serial_tayland['country'].sum()
tva_serial_tayland_visit = tva_df_serial[tva_df_serial['country'].str.contains('تایلند')]
tva_serial_tayland_visit=tva_serial_tayland_visit['bazdid'].sum()

tva_serial_sangapor = df_tva_serial_country.str.count("سنگاپور") 
tva_serial_sangapor=pd.DataFrame(tva_serial_sangapor) 
tva_serial_sangapor=tva_serial_sangapor['country'].sum()
tva_serial_sangapor_visit = tva_df_serial[tva_df_serial['country'].str.contains('سنگاپور')]
tva_serial_sangapor_visit=tva_serial_sangapor_visit['bazdid'].sum()

tva_serial_otrish = df_tva_serial_country.str.count("اتریش") 
tva_serial_otrish=pd.DataFrame(tva_serial_otrish) 
tva_serial_otrish=tva_serial_otrish['country'].sum()
tva_serial_otrish_visit = tva_df_serial[tva_df_serial['country'].str.contains('اتریش')]
tva_serial_otrish_visit=tva_serial_otrish_visit['bazdid'].sum()

tva_serial_spania = df_tva_serial_country.str.count("اسپانیا") 
tva_serial_spania=pd.DataFrame(tva_serial_spania) 
tva_serial_spania=tva_serial_spania['country'].sum()
tva_serial_spania_visit = tva_df_serial[tva_df_serial['country'].str.contains('اسپانیا')]
tva_serial_spania_visit=tva_serial_spania_visit['bazdid'].sum()

tva_serial_okrayn = df_tva_serial_country.str.count("اکراین") 
tva_serial_okrayn=pd.DataFrame(tva_serial_okrayn) 
tva_serial_okrayn=tva_serial_okrayn['country'].sum()
tva_serial_okrayn_visit = tva_df_serial[tva_df_serial['country'].str.contains('اکراین')]
tva_serial_okrayn_visit=tva_serial_okrayn_visit['bazdid'].sum()

tva_serial_emarat = df_tva_serial_country.str.count("امارات") 
tva_serial_emarat=pd.DataFrame(tva_serial_emarat) 
tva_serial_emarat=tva_serial_emarat['country'].sum()
tva_serial_emarat_visit = tva_df_serial[tva_df_serial['country'].str.contains('امارات')]
tva_serial_emarat_visit=tva_serial_emarat_visit['bazdid'].sum()

tva_serial_irland = df_tva_serial_country.str.count("ایرلند") 
tva_serial_irland=pd.DataFrame(tva_serial_irland) 
tva_serial_irland=tva_serial_irland['country'].sum()
tva_serial_irland_visit = tva_df_serial[tva_df_serial['country'].str.contains('ایرلند')]
tva_serial_irland_visit=tva_serial_irland_visit['bazdid'].sum()

tva_serial_argantin = df_tva_serial_country.str.count("آرژانتین") 
tva_serial_argantin=pd.DataFrame(tva_serial_argantin) 
tva_serial_argantin=tva_serial_argantin['country'].sum()
tva_serial_argantin_visit = tva_df_serial[tva_df_serial['country'].str.contains('آرژانتین')]
tva_serial_argantin_visit=tva_serial_argantin_visit['bazdid'].sum()

tva_serial_afrigha_jonobi = df_tva_serial_country.str.count("آفریقای جنوبی") 
tva_serial_afrigha_jonobi=pd.DataFrame(tva_serial_afrigha_jonobi) 
tva_serial_afrigha_jonobi=tva_serial_afrigha_jonobi['country'].sum()
tva_serial_afrigha_jonobi_visit = tva_df_serial[tva_df_serial['country'].str.contains('آفریقای جنوبی')]
tva_serial_afrigha_jonobi_visit=tva_serial_afrigha_jonobi_visit['bazdid'].sum()

tva_serial_danmark = df_tva_serial_country.str.count("دانمارک") 
tva_serial_danmark=pd.DataFrame(tva_serial_danmark) 
tva_serial_danmark=tva_serial_danmark['country'].sum()
tva_serial_danmark_visit = tva_df_serial[tva_df_serial['country'].str.contains('دانمارک')]
tva_serial_danmark_visit=tva_serial_danmark_visit['bazdid'].sum()

tva_serial_shili = df_tva_serial_country.str.count("شیلی") 
tva_serial_shili=pd.DataFrame(tva_serial_shili) 
tva_serial_shili=tva_serial_shili['country'].sum()
tva_serial_shili_visit = tva_df_serial[tva_df_serial['country'].str.contains('شیلی')]
tva_serial_shili_visit=tva_serial_shili_visit['bazdid'].sum()

tva_serial_malezi = df_tva_serial_country.str.count("مالزی") 
tva_serial_malezi=pd.DataFrame(tva_serial_malezi) 
tva_serial_malezi=tva_serial_malezi['country'].sum()
tva_serial_malezi_visit = tva_df_serial[tva_df_serial['country'].str.contains('مالزی')]
tva_serial_malezi_visit=tva_serial_malezi_visit['bazdid'].sum()

tva_serial_honkkong = df_tva_serial_country.str.count("هنک کنگ") 
tva_serial_honkkong=pd.DataFrame(tva_serial_honkkong) 
tva_serial_honkkong=tva_serial_honkkong['country'].sum()
tva_serial_honkkong_visit = tva_df_serial[tva_df_serial['country'].str.contains('هنک کنگ')]
tva_serial_honkkong_visit=tva_serial_honkkong_visit['bazdid'].sum()

tva_serial_soed = df_tva_serial_country.str.count("سوئد") 
tva_serial_soed=pd.DataFrame(tva_serial_soed) 
tva_serial_soed=tva_serial_soed['country'].sum()
tva_serial_soed_visit = tva_df_serial[tva_df_serial['country'].str.contains('سوئد')]
tva_serial_soed_visit=tva_serial_soed_visit['bazdid'].sum()

tva_serial_sois = df_tva_serial_country.str.count("سوئیس") 
tva_serial_sois=pd.DataFrame(tva_serial_sois) 
tva_serial_sois=tva_serial_sois['country'].sum()
tva_serial_sois_visit = tva_df_serial[tva_df_serial['country'].str.contains('سوئیس')]
tva_serial_sois_visit=tva_serial_sois_visit['bazdid'].sum()

tva_serial_mekzik = df_tva_serial_country.str.count("مکزیک") 
tva_serial_mekzik=pd.DataFrame(tva_serial_mekzik) 
tva_serial_mekzik=tva_serial_mekzik['country'].sum()
tva_serial_mekzik_visit = tva_df_serial[tva_df_serial['country'].str.contains('مکزیک')]
tva_serial_mekzik_visit=tva_serial_mekzik_visit['bazdid'].sum()

tva_serial_nioziland = df_tva_serial_country.str.count("نیوزیلند") 
tva_serial_nioziland=pd.DataFrame(tva_serial_nioziland) 
tva_serial_nioziland=tva_serial_nioziland['country'].sum()
tva_serial_nioziland_visit = tva_df_serial[tva_df_serial['country'].str.contains('نیوزیلند')]
tva_serial_nioziland_visit=tva_serial_nioziland_visit['bazdid'].sum()

tva_serial_hend = df_tva_serial_country.str.count("هند") 
tva_serial_hend=pd.DataFrame(tva_serial_hend) 
tva_serial_hend=tva_serial_hend['country'].sum()
tva_serial_hend_visit = tva_df_serial[tva_df_serial['country'].str.contains('هند')]
tva_serial_hend_visit=tva_serial_hend_visit['bazdid'].sum()

tva_serial_country_content_count={'tva_serial_country_name': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'tva_serial_country_count1': [tva_serial_amrika, tva_serial_iran,tva_serial_holand, tva_serial_alman,
                                                         tva_serial_englis, tva_serial_kore_jonobi,tva_serial_faranse, tva_serial_japon,
                                                         tva_serial_kanada, tva_serial_fanland,tva_serial_korovasi, tva_serial_majarestan,
                                                         tva_serial_lahestan, tva_serial_sois,tva_serial_belgik, tva_serial_rosie,
                                                         tva_serial_italia, tva_serial_bolgharestan,tva_serial_ostralia, tva_serial_norvej,
                                                         tva_serial_chin, tva_serial_tayland,tva_serial_sangapor, tva_serial_otrish,
                                                         tva_serial_spania, tva_serial_okrayn,tva_serial_emarat, tva_serial_irland,
                                                         tva_serial_argantin, tva_serial_afrigha_jonobi,tva_serial_danmark, tva_serial_shili,
                                                         tva_serial_malezi, tva_serial_honkkong,tva_serial_soed, tva_serial_sois,
                                                         tva_serial_mekzik, tva_serial_nioziland,tva_serial_hend]}
 
tva_serial_country_content_count=pd.DataFrame(tva_serial_country_content_count, columns=['tva_serial_country_name', 'tva_serial_country_count1'])
tva_serial_country_content_count=tva_serial_country_content_count.query("tva_serial_country_count1 != '0'") 
tva_serial_country_content_count.sort_values('tva_serial_country_count1', axis = 0, ascending = False, inplace = True, na_position ='last') 
                               
tva_serial_country_content_visit={'tva_serial_country_name': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'tva_serial_country_visit1': [tva_serial_amrika_visit, tva_serial_iran_visit,tva_serial_holand_visit, tva_serial_alman_visit,
                                                         tva_serial_englis_visit, tva_serial_kore_jonobi_visit,tva_serial_faranse_visit, tva_serial_japon_visit,
                                                         tva_serial_kanada_visit, tva_serial_fanland_visit,tva_serial_korovasi_visit, tva_serial_majarestan_visit,
                                                         tva_serial_lahestan_visit, tva_serial_sois_visit,tva_serial_belgik_visit, tva_serial_rosie_visit,
                                                         tva_serial_italia_visit, tva_serial_bolgharestan_visit,tva_serial_ostralia_visit, tva_serial_norvej_visit,
                                                         tva_serial_chin_visit, tva_serial_tayland_visit,tva_serial_sangapor_visit, tva_serial_otrish_visit,
                                                         tva_serial_spania_visit, tva_serial_okrayn_visit,tva_serial_emarat_visit, tva_serial_irland_visit,
                                                         tva_serial_argantin_visit, tva_serial_afrigha_jonobi_visit,tva_serial_danmark_visit, tva_serial_shili_visit,
                                                         tva_serial_malezi_visit, tva_serial_honkkong_visit,tva_serial_soed_visit, tva_serial_sois_visit,
                                                         tva_serial_mekzik_visit, tva_serial_nioziland_visit,tva_serial_hend_visit,]}

tva_serial_country_content_visit=pd.DataFrame(tva_serial_country_content_visit, columns=['tva_serial_country_name', 'tva_serial_country_visit1'])
tva_serial_country_content_visit=tva_serial_country_content_visit.query("tva_serial_country_visit1 != '0'")  
tva_serial_country_content_visit.sort_values('tva_serial_country_visit1', axis = 0, ascending = False, inplace = True, na_position ='last') 
print("finish country of tva serial")
##############################################################################################################################
########################################################## year ###############################################################
##############################################################################################################################
print("year of tva serial")
df_tva_serial_year=tva_df_serial['year']
tva_count_of_all_year=len(tva_df_serial)
tva_visit_of_all_year=tva_df_serial['bazdid'].sum()

tva_serial_year_1399=tva_df_serial.query("year == '1399'")
tva_serial_year_1399_count=len(tva_serial_year_1399)
tva_serial_year_1399_visit=tva_serial_year_1399['bazdid'].sum()

tva_serial_year_1398=tva_df_serial.query("year == '1398'")
tva_serial_year_1398_count=len(tva_serial_year_1398)
tva_serial_year_1398_visit=tva_serial_year_1398['bazdid'].sum()

tva_serial_year_1397=tva_df_serial.query("year == '1397'")
tva_serial_year_1397_count=len(tva_serial_year_1397)
tva_serial_year_1397_visit=tva_serial_year_1397['bazdid'].sum()

tva_serial_year_1396=tva_df_serial.query("year == '1396'")
tva_serial_year_1396_count=len(tva_serial_year_1396)
tva_serial_year_1396_visit=tva_serial_year_1396['bazdid'].sum()

tva_serial_year_1395=tva_df_serial.query("year == '1395'")
tva_serial_year_1395_count=len(tva_serial_year_1395)
tva_serial_year_1395_visit=tva_serial_year_1395['bazdid'].sum()

tva_serial_year_1394=tva_df_serial.query("year == '1394'")
tva_serial_year_1394_count=len(tva_serial_year_1394)
tva_serial_year_1394_visit=tva_serial_year_1394['bazdid'].sum()

tva_serial_year_1393=tva_df_serial.query("year == '1393'")
tva_serial_year_1393_count=len(tva_serial_year_1393)
tva_serial_year_1393_visit=tva_serial_year_1393['bazdid'].sum()

tva_serial_year_1392=tva_df_serial.query("year == '1392'")
tva_serial_year_1392_count=len(tva_serial_year_1392)
tva_serial_year_1392_visit=tva_serial_year_1392['bazdid'].sum()

tva_serial_year_1391=tva_df_serial.query("year == '1391'")
tva_serial_year_1391_count=len(tva_serial_year_1391)
tva_serial_year_1391_visit=tva_serial_year_1391['bazdid'].sum()

tva_serial_year_1390=tva_df_serial.query("year == '1390'")
tva_serial_year_1390_count=len(tva_serial_year_1390)
tva_serial_year_1390_visit=tva_serial_year_1390['bazdid'].sum()

tva_serial_year_1389=tva_df_serial.query("year == '1389'")
tva_serial_year_1389_count=len(tva_serial_year_1389)
tva_serial_year_1389_visit=tva_serial_year_1389['bazdid'].sum()

tva_serial_year_1388=tva_df_serial.query("year == '1388'")
tva_serial_year_1388_count=len(tva_serial_year_1388)
tva_serial_year_1388_visit=tva_serial_year_1388['bazdid'].sum()

tva_serial_year_1387=tva_df_serial.query("year == '1387'")
tva_serial_year_1387_count=len(tva_serial_year_1387)
tva_serial_year_1387_visit=tva_serial_year_1387['bazdid'].sum()

tva_serial_year_1386=tva_df_serial.query("year == '1386'")
tva_serial_year_1386_count=len(tva_serial_year_1386)
tva_serial_year_1386_visit=tva_serial_year_1386['bazdid'].sum()

tva_serial_year_1385=tva_df_serial.query("year == '1385'")
tva_serial_year_1385_count=len(tva_serial_year_1385)
tva_serial_year_1385_visit=tva_serial_year_1385['bazdid'].sum()

tva_serial_year_1384=tva_df_serial.query("year == '1384'")
tva_serial_year_1384_count=len(tva_serial_year_1384)
tva_serial_year_1384_visit=tva_serial_year_1384['bazdid'].sum()

tva_serial_year_1383=tva_df_serial.query("year == '1383'")
tva_serial_year_1383_count=len(tva_serial_year_1383)
tva_serial_year_1383_visit=tva_serial_year_1383['bazdid'].sum()

tva_serial_year_1382=tva_df_serial.query("year == '1382'")
tva_serial_year_1382_count=len(tva_serial_year_1382)
tva_serial_year_1382_visit=tva_serial_year_1382['bazdid'].sum()

tva_serial_year_1381=tva_df_serial.query("year == '1381'")
tva_serial_year_1381_count=len(tva_serial_year_1381)
tva_serial_year_1381_visit=tva_serial_year_1381['bazdid'].sum()

tva_serial_year_1380=tva_df_serial.query("year == '1380'")
tva_serial_year_1380_count=len(tva_serial_year_1380)
tva_serial_year_1380_visit=tva_serial_year_1380['bazdid'].sum()

tva_serial_year_1379=tva_df_serial.query("year == '1379'")
tva_serial_year_1379_count=len(tva_serial_year_1379)
tva_serial_year_1379_visit=tva_serial_year_1379['bazdid'].sum()

tva_serial_year_1378=tva_df_serial.query("year == '1378'")
tva_serial_year_1378_count=len(tva_serial_year_1378)
tva_serial_year_1378_visit=tva_serial_year_1378['bazdid'].sum()

tva_serial_year_1377=tva_df_serial.query("year == '1377'")
tva_serial_year_1377_count=len(tva_serial_year_1377)
tva_serial_year_1377_visit=tva_serial_year_1377['bazdid'].sum()

tva_serial_year_1376=tva_df_serial.query("year == '1376'")
tva_serial_year_1376_count=len(tva_serial_year_1376)
tva_serial_year_1376_visit=tva_serial_year_1376['bazdid'].sum()

tva_serial_year_1375=tva_df_serial.query("year == '1375'")
tva_serial_year_1375_count=len(tva_serial_year_1375)
tva_serial_year_1375_visit=tva_serial_year_1375['bazdid'].sum()

tva_serial_year_1374=tva_df_serial.query("year == '1374'")
tva_serial_year_1374_count=len(tva_serial_year_1374)
tva_serial_year_1374_visit=tva_serial_year_1374['bazdid'].sum()

tva_serial_year_1373=tva_df_serial.query("year == '1373'")
tva_serial_year_1373_count=len(tva_serial_year_1373)
tva_serial_year_1373_visit=tva_serial_year_1373['bazdid'].sum()

tva_serial_year_1372=tva_df_serial.query("year == '1372'")
tva_serial_year_1372_count=len(tva_serial_year_1372)
tva_serial_year_1372_visit=tva_serial_year_1372['bazdid'].sum()

tva_serial_year_1371=tva_df_serial.query("year == '1371'")
tva_serial_year_1371_count=len(tva_serial_year_1371)
tva_serial_year_1371_visit=tva_serial_year_1371['bazdid'].sum()

tva_serial_year_1370=tva_df_serial.query("year == '1370'")
tva_serial_year_1370_count=len(tva_serial_year_1370)
tva_serial_year_1370_visit=tva_serial_year_1370['bazdid'].sum()

tva_serial_year_1369=tva_df_serial.query("year == '1369'")
tva_serial_year_1369_count=len(tva_serial_year_1369)
tva_serial_year_1369_visit=tva_serial_year_1369['bazdid'].sum()

tva_serial_year_1368=tva_df_serial.query("year == '1368'")
tva_serial_year_1368_count=len(tva_serial_year_1368)
tva_serial_year_1368_visit=tva_serial_year_1368['bazdid'].sum()

tva_serial_year_1367=tva_df_serial.query("year == '1367'")
tva_serial_year_1367_count=len(tva_serial_year_1367)
tva_serial_year_1367_visit=tva_serial_year_1367['bazdid'].sum()

tva_serial_year_1366=tva_df_serial.query("year == '1366'")
tva_serial_year_1366_count=len(tva_serial_year_1366)
tva_serial_year_1366_visit=tva_serial_year_1366['bazdid'].sum()

tva_serial_year_1365=tva_df_serial.query("year == '1365'")
tva_serial_year_1365_count=len(tva_serial_year_1365)
tva_serial_year_1365_visit=tva_serial_year_1365['bazdid'].sum()

tva_serial_year_1364=tva_df_serial.query("year == '1364'")
tva_serial_year_1364_count=len(tva_serial_year_1364)
tva_serial_year_1364_visit=tva_serial_year_1364['bazdid'].sum()

tva_serial_year_1363=tva_df_serial.query("year == '1363'")
tva_serial_year_1363_count=len(tva_serial_year_1363)
tva_serial_year_1363_visit=tva_serial_year_1363['bazdid'].sum()

tva_serial_year_1362=tva_df_serial.query("year == '1362'")
tva_serial_year_1362_count=len(tva_serial_year_1362)
tva_serial_year_1362_visit=tva_serial_year_1362['bazdid'].sum()

tva_serial_year_1361=tva_df_serial.query("year == '1361'")
tva_serial_year_1361_count=len(tva_serial_year_1361)
tva_serial_year_1361_visit=tva_serial_year_1361['bazdid'].sum()

tva_serial_year_1360=tva_df_serial.query("year == '1360'")
tva_serial_year_1360_count=len(tva_serial_year_1360)
tva_serial_year_1360_visit=tva_serial_year_1360['bazdid'].sum()

tva_serial_year_1359=tva_df_serial.query("year == '1359'")
tva_serial_year_1359_count=len(tva_serial_year_1359)
tva_serial_year_1359_visit=tva_serial_year_1359['bazdid'].sum()

tva_serial_year_1358=tva_df_serial.query("year == '1358'")
tva_serial_year_1358_count=len(tva_serial_year_1358)
tva_serial_year_1358_visit=tva_serial_year_1358['bazdid'].sum()

tva_serial_year_1357=tva_df_serial.query('year < 1358')
tva_serial_year_1357_count=len(tva_serial_year_1357)
tva_serial_year_1357_visit=tva_serial_year_1357['bazdid'].sum()

tva_serial_year_count={'tva_serial_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'tva_serial_year_count': [tva_serial_year_1357_count,tva_serial_year_1358_count,tva_serial_year_1359_count,tva_serial_year_1360_count,
                                           tva_serial_year_1361_count,tva_serial_year_1362_count,tva_serial_year_1363_count,tva_serial_year_1364_count,
                                           tva_serial_year_1365_count,tva_serial_year_1366_count,tva_serial_year_1367_count,tva_serial_year_1368_count,
                                           tva_serial_year_1369_count,tva_serial_year_1370_count,tva_serial_year_1371_count,tva_serial_year_1372_count,
                                           tva_serial_year_1373_count,tva_serial_year_1374_count,tva_serial_year_1375_count,tva_serial_year_1376_count,
                                           tva_serial_year_1377_count,tva_serial_year_1378_count,tva_serial_year_1379_count,tva_serial_year_1380_count,
                                           tva_serial_year_1381_count,tva_serial_year_1382_count,tva_serial_year_1383_count,tva_serial_year_1384_count,
                                           tva_serial_year_1385_count,tva_serial_year_1386_count,tva_serial_year_1387_count,tva_serial_year_1388_count,
                                           tva_serial_year_1389_count,tva_serial_year_1390_count,tva_serial_year_1391_count,tva_serial_year_1392_count,
                                           tva_serial_year_1393_count,tva_serial_year_1394_count,tva_serial_year_1395_count,tva_serial_year_1396_count,
                                           tva_serial_year_1397_count,tva_serial_year_1398_count,tva_serial_year_1399_count,]}
tva_serial_year_visit={'tva_serial_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'tva_serial_year_visit': [tva_serial_year_1357_visit,tva_serial_year_1358_visit,tva_serial_year_1359_visit,tva_serial_year_1360_visit,
                                           tva_serial_year_1361_visit,tva_serial_year_1362_visit,tva_serial_year_1363_visit,tva_serial_year_1364_visit,
                                           tva_serial_year_1365_visit,tva_serial_year_1366_visit,tva_serial_year_1367_visit,tva_serial_year_1368_visit,
                                           tva_serial_year_1369_visit,tva_serial_year_1370_visit,tva_serial_year_1371_visit,tva_serial_year_1372_visit,
                                           tva_serial_year_1373_visit,tva_serial_year_1374_visit,tva_serial_year_1375_visit,tva_serial_year_1376_visit,
                                           tva_serial_year_1377_visit,tva_serial_year_1378_visit,tva_serial_year_1379_visit,tva_serial_year_1380_visit,
                                           tva_serial_year_1381_visit,tva_serial_year_1382_visit,tva_serial_year_1383_visit,tva_serial_year_1384_visit,
                                           tva_serial_year_1385_visit,tva_serial_year_1386_visit,tva_serial_year_1387_visit,tva_serial_year_1388_visit,
                                           tva_serial_year_1389_visit,tva_serial_year_1390_visit,tva_serial_year_1391_visit,tva_serial_year_1392_visit,
                                           tva_serial_year_1393_visit,tva_serial_year_1394_visit,tva_serial_year_1395_visit,tva_serial_year_1396_visit,
                                           tva_serial_year_1397_visit,tva_serial_year_1398_visit,tva_serial_year_1399_visit,]}
tva_serial_year_count=pd.DataFrame(tva_serial_year_count, columns=['tva_serial_year','tva_serial_year_count'])
tva_serial_year_visit=pd.DataFrame(tva_serial_year_visit, columns=['tva_serial_year','tva_serial_year_visit'])
print("finish year of tva serial")
##############################################################################################################################
########################################################## IMDB ###############################################################
##############################################################################################################################
print("imdb of tva serial")
df_tva_serial_imdb=tva_df_serial['imdb']
tva_count_of_all_imdb=len(df_tva_serial_imdb)
tva_visit_of_all_imdb=tva_df_serial['bazdid'].sum()

tva_serial_imdb_lower6=tva_df_serial.query('imdb < 6')
tva_serial_imdb_lower6_count=len(tva_serial_imdb_lower6)
tva_serial_imdb_lower6_visit=tva_serial_imdb_lower6['bazdid'].sum()

tva_serial_imdb_between_6_7=tva_df_serial.query('imdb > 5.9 and imdb < 7')
tva_serial_imdb_between_6_7_count=len(tva_serial_imdb_between_6_7)
tva_serial_imdb_between_6_7_visit=tva_serial_imdb_between_6_7['bazdid'].sum()

tva_serial_imdb_between_7_8=tva_df_serial.query('imdb > 6.9 and imdb < 8')
tva_serial_imdb_between_7_8_count=len(tva_serial_imdb_between_7_8)
tva_serial_imdb_between_7_8_visit=tva_serial_imdb_between_7_8['bazdid'].sum()

tva_serial_imdb_between_8_9=tva_df_serial.query('imdb > 7.9 and imdb < 9')
tva_serial_imdb_between_8_9_count=len(tva_serial_imdb_between_8_9)
tva_serial_imdb_between_8_9_visit=tva_serial_imdb_between_8_9['bazdid'].sum()

tva_serial_imdb_upper9=tva_df_serial.query('imdb > 8.9')
tva_serial_imdb_upper9_count=len(tva_serial_imdb_upper9)
tva_serial_imdb_upper9_visit=tva_serial_imdb_upper9['bazdid'].sum()

tva_serial_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'count_of_imdb_serial': [tva_serial_imdb_lower6_count,
                                        tva_serial_imdb_between_6_7_count,
                                        tva_serial_imdb_between_7_8_count,
                                        tva_serial_imdb_between_8_9_count,
                                        tva_serial_imdb_upper9_count]}
                                          
tva_serial_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'visit_of_imdb_serial': [tva_serial_imdb_lower6_visit,
                                        tva_serial_imdb_between_6_7_visit,
                                        tva_serial_imdb_between_7_8_visit,
                                        tva_serial_imdb_between_8_9_visit,
                                        tva_serial_imdb_upper9_visit]}
tva_serial_imdb_count=pd.DataFrame(tva_serial_imdb_count, columns=['limitation', 'count_of_imdb_serial'])
tva_serial_imdb_visit=pd.DataFrame(tva_serial_imdb_visit, columns=['limitation', 'visit_of_imdb_serial'])
print("finish imdb of tva serial")
##############################################################################################################################
########################################################## 10 contents film ###############################################################
##############################################################################################################################
print("popular of tva serial")
tva_df_serial.sort_values('bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_serial_content_popular_bazdid=[]
tva_serial_content_popular_visitnumber_bazdid=[]
tva_serial_content_popular_name_bazdid=[]
tva_serial_content_popular_name_bazdid=tva_df_serial["title1"].tolist()
tva_serial_content_popular_bazdid.append(tva_serial_content_popular_name_bazdid)
tva_serial_content_popular_visitnumber_bazdid=tva_df_serial["bazdid"].tolist()
tva_serial_content_popular_bazdid.append(tva_serial_content_popular_visitnumber_bazdid)
tva_serial_content_popular_bazdid={'tva_serial_content_popular_name_bazdid' : [tva_serial_content_popular_name_bazdid[0], 
                                                           tva_serial_content_popular_name_bazdid[1], 
                                                           tva_serial_content_popular_name_bazdid[2],
                                                           tva_serial_content_popular_name_bazdid[3], 
                                                           tva_serial_content_popular_name_bazdid[4], 
                                                           tva_serial_content_popular_name_bazdid[5],
                                                           tva_serial_content_popular_name_bazdid[6], 
                                                           tva_serial_content_popular_name_bazdid[7], 
                                                           tva_serial_content_popular_name_bazdid[8],
                                                           tva_serial_content_popular_name_bazdid[9]],
                            'tva_serial_content_popular_visitnumber_bazdid' : [tva_serial_content_popular_visitnumber_bazdid[0], tva_serial_content_popular_visitnumber_bazdid[1],
                                                                  tva_serial_content_popular_visitnumber_bazdid[2], tva_serial_content_popular_visitnumber_bazdid[3],
                                                                  tva_serial_content_popular_visitnumber_bazdid[4], tva_serial_content_popular_visitnumber_bazdid[5],
                                                                  tva_serial_content_popular_visitnumber_bazdid[6], tva_serial_content_popular_visitnumber_bazdid[7],
                                                                  tva_serial_content_popular_visitnumber_bazdid[8], tva_serial_content_popular_visitnumber_bazdid[9]]}
tva_serial_content_popular_bazdid=pd.DataFrame(tva_serial_content_popular_bazdid, columns=['tva_serial_content_popular_name_bazdid' , 'tva_serial_content_popular_visitnumber_bazdid'])
tva_serial_content_popular_bazdid.sort_values('tva_serial_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_df_serial.sort_values('karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_serial_content_popular_karbaran=[]
tva_serial_content_popular_visitnumber_karbaran=[]
tva_serial_content_popular_name_karbaran=[]
tva_serial_content_popular_name_karbaran=tva_df_serial["title1"].tolist()
tva_serial_content_popular_karbaran.append(tva_serial_content_popular_name_karbaran)
tva_serial_content_popular_visitnumber_karbaran=tva_df_serial["karbaran"].tolist()
tva_serial_content_popular_karbaran.append(tva_serial_content_popular_visitnumber_karbaran)
tva_serial_content_popular_karbaran={'tva_serial_content_popular_name_karbaran' : [tva_serial_content_popular_name_karbaran[0], 
                                                           tva_serial_content_popular_name_karbaran[1], 
                                                           tva_serial_content_popular_name_karbaran[2],
                                                           tva_serial_content_popular_name_karbaran[3], 
                                                           tva_serial_content_popular_name_karbaran[4], 
                                                           tva_serial_content_popular_name_karbaran[5],
                                                           tva_serial_content_popular_name_karbaran[6], 
                                                           tva_serial_content_popular_name_karbaran[7], 
                                                           tva_serial_content_popular_name_karbaran[8],
                                                           tva_serial_content_popular_name_karbaran[9]],
                            'tva_serial_content_popular_visitnumber_karbaran' : [tva_serial_content_popular_visitnumber_karbaran[0], tva_serial_content_popular_visitnumber_karbaran[1],
                                                                  tva_serial_content_popular_visitnumber_karbaran[2], tva_serial_content_popular_visitnumber_karbaran[3],
                                                                  tva_serial_content_popular_visitnumber_karbaran[4], tva_serial_content_popular_visitnumber_karbaran[5],
                                                                  tva_serial_content_popular_visitnumber_karbaran[6], tva_serial_content_popular_visitnumber_karbaran[7],
                                                                  tva_serial_content_popular_visitnumber_karbaran[8], tva_serial_content_popular_visitnumber_karbaran[9]]}
tva_serial_content_popular_karbaran=pd.DataFrame(tva_serial_content_popular_karbaran, columns=['tva_serial_content_popular_name_karbaran' , 'tva_serial_content_popular_visitnumber_karbaran'])
tva_serial_content_popular_karbaran.sort_values('tva_serial_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_df_serial.sort_values('minute', axis = 0, ascending = False, inplace = True, na_position ='last')

tva_serial_content_popular_minute=[]
tva_serial_content_popular_visitnumber_minute=[]
tva_serial_content_popular_name_minute=[]
tva_serial_content_popular_name_minute=tva_df_serial["title1"].tolist()
tva_serial_content_popular_minute.append(tva_serial_content_popular_name_minute)
tva_serial_content_popular_visitnumber_minute=tva_df_serial["minute"].tolist()
tva_serial_content_popular_minute.append(tva_serial_content_popular_visitnumber_minute)
tva_serial_content_popular_minute={'tva_serial_content_popular_name_minute' : [tva_serial_content_popular_name_minute[0], 
                                                           tva_serial_content_popular_name_minute[1], 
                                                           tva_serial_content_popular_name_minute[2],
                                                           tva_serial_content_popular_name_minute[3], 
                                                           tva_serial_content_popular_name_minute[4], 
                                                           tva_serial_content_popular_name_minute[5],
                                                           tva_serial_content_popular_name_minute[6], 
                                                           tva_serial_content_popular_name_minute[7], 
                                                           tva_serial_content_popular_name_minute[8],
                                                           tva_serial_content_popular_name_minute[9]],
                            'tva_serial_content_popular_visitnumber_minute' : [tva_serial_content_popular_visitnumber_minute[0], tva_serial_content_popular_visitnumber_minute[1],
                                                                  tva_serial_content_popular_visitnumber_minute[2], tva_serial_content_popular_visitnumber_minute[3],
                                                                  tva_serial_content_popular_visitnumber_minute[4], tva_serial_content_popular_visitnumber_minute[5],
                                                                  tva_serial_content_popular_visitnumber_minute[6], tva_serial_content_popular_visitnumber_minute[7],
                                                                  tva_serial_content_popular_visitnumber_minute[8], tva_serial_content_popular_visitnumber_minute[9]]}
tva_serial_content_popular_minute=pd.DataFrame(tva_serial_content_popular_minute, columns=['tva_serial_content_popular_name_minute' , 'tva_serial_content_popular_visitnumber_minute'])
tva_serial_content_popular_minute.sort_values('tva_serial_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
tva_serial_content_popular_minute=round(tva_serial_content_popular_minute*60, 0)
print("finish popular of tva serial")
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################# LENZ #########################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
print("start LENZ")
lenz_df_vod = pd.read_csv('lenz-vod-tir99.csv') 
#
#def trim_all_columns(lenz_df_vod):
#    """
#    Trim whitespace from ends of each value across all series in dataframe
#    """
#    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
#    return lenz_df_vod.applymap(trim_strings)
#
#lenz_df_vod = trim_all_columns(lenz_df_vod)

lenz_df_vod.replace('(^\s+|\s+$)', '', regex=True, inplace=True)

#lenz_df_vod['title1'].str.strip()

lenz_df_serial=lenz_df_vod.query("film != '1'")
lenz_df_film=lenz_df_vod.query("film == '1'")
##############################################################################################################################
##############################################################################################################################
########################################################## film ###############################################################
##############################################################################################################################
##############################################################################################################################
lenz_df_film.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 

print("statistics of lenz film")
lenz_film_count_content=lenz_df_film['bazdid']
lenz_film_count_content=len(lenz_film_count_content)
lenz_film_sum_bazdid=lenz_df_film['bazdid'].sum()
lenz_film_sum_karbaran=lenz_df_film['karbaran'].sum()
lenz_film_sum_minute=lenz_df_film['minute'].sum()

##############################################################################################################################
########################################################## genre ###############################################################
##############################################################################################################################
print("genre of lenz film")
df_lenz_film_genre=lenz_df_film['genre']
lenz_count_of_all_genre=len(lenz_df_film)
lenz_visit_of_all_genre=lenz_df_film['bazdid'].sum()

lenz_film_siasi = df_lenz_film_genre.str.count("سیاسی") 
lenz_film_siasi=pd.DataFrame(lenz_film_siasi) 
lenz_film_siasi=lenz_film_siasi['genre'].sum()
lenz_film_siasi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('سیاسی')]
lenz_film_siasi_visit=lenz_film_siasi_visit['bazdid'].sum()

lenz_film_tarsnak = df_lenz_film_genre.str.count("ترسناک") 
lenz_film_tarsnak=pd.DataFrame(lenz_film_tarsnak) 
lenz_film_tarsnak=lenz_film_tarsnak['genre'].sum()
lenz_film_vahshat = df_lenz_film_genre.str.count("وحشت") 
lenz_film_vahshat=pd.DataFrame(lenz_film_vahshat) 
lenz_film_vahshat=lenz_film_vahshat['genre'].sum()
lenz_film_tarsnak=lenz_film_tarsnak+lenz_film_vahshat
lenz_film_tarsnak_visit = lenz_df_film[lenz_df_film['genre'].str.contains('ترسناک')]
lenz_film_tarsnak_visit=lenz_film_tarsnak_visit['bazdid'].sum()
lenz_film_vahshat_visit = lenz_df_film[lenz_df_film['genre'].str.contains('وحشت')]
lenz_film_vahshat_visit=lenz_film_vahshat_visit['bazdid'].sum()
lenz_film_tarsnak_visit=lenz_film_tarsnak_visit+lenz_film_vahshat_visit

lenz_film_razalod = df_lenz_film_genre.str.count("رازآلود") 
lenz_film_razalod=pd.DataFrame(lenz_film_razalod) 
lenz_film_razalod=lenz_film_razalod['genre'].sum()
lenz_film_razalod1 = df_lenz_film_genre.str.count("راز آلود") 
lenz_film_razalod1=pd.DataFrame(lenz_film_razalod1) 
lenz_film_razalod1=lenz_film_razalod1['genre'].sum()
lenz_film_razalod=lenz_film_razalod+lenz_film_razalod1
lenz_film_razalod_visit = lenz_df_film[lenz_df_film['genre'].str.contains('رازآلود')]
lenz_film_razalod_visit=lenz_film_razalod_visit['bazdid'].sum()
lenz_film_razalod1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('رازآلود')]
lenz_film_razalod1_visit=lenz_film_razalod1_visit['bazdid'].sum()
lenz_film_razalod_visit=lenz_film_razalod_visit+lenz_film_razalod1_visit

lenz_film_zendeginame = df_lenz_film_genre.str.count("زندگینامه") 
lenz_film_zendeginame=pd.DataFrame(lenz_film_zendeginame) 
lenz_film_zendeginame=lenz_film_zendeginame['genre'].sum()
lenz_film_zendeginame1 = df_lenz_film_genre.str.count("زندگی نامه") 
lenz_film_zendeginame1=pd.DataFrame(lenz_film_zendeginame1) 
lenz_film_zendeginame1=lenz_film_zendeginame1['genre'].sum()
lenz_film_zendeginame=lenz_film_zendeginame+lenz_film_zendeginame1
lenz_film_zendeginame_visit = lenz_df_film[lenz_df_film['genre'].str.contains('زندگینامه')]
lenz_film_zendeginame_visit=lenz_film_zendeginame_visit['bazdid'].sum()
lenz_film_zendeginame1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('زندگینامه')]
lenz_film_zendeginame1_visit=lenz_film_zendeginame1_visit['bazdid'].sum()
lenz_film_zendeginame_visit=lenz_film_zendeginame_visit+lenz_film_zendeginame1_visit

lenz_film_romantic = df_lenz_film_genre.str.count("رمانتیک") 
lenz_film_romantic=pd.DataFrame(lenz_film_romantic) 
lenz_film_romantic=lenz_film_romantic['genre'].sum()
lenz_film_romantic_visit = lenz_df_film[lenz_df_film['genre'].str.contains('رمانتیک')]
lenz_film_romantic_visit=lenz_film_romantic_visit['bazdid'].sum()

lenz_film_mostanad = df_lenz_film_genre.str.count("مستند") 
lenz_film_mostanad=pd.DataFrame(lenz_film_mostanad) 
lenz_film_mostanad=lenz_film_mostanad['genre'].sum()
lenz_film_mostanad_visit = lenz_df_film[lenz_df_film['genre'].str.contains('مستند')]
lenz_film_mostanad_visit=lenz_film_mostanad_visit['bazdid'].sum()

lenz_film_jenai = df_lenz_film_genre.str.count("جنائی") 
lenz_film_jenai=pd.DataFrame(lenz_film_jenai) 
lenz_film_jenai=lenz_film_jenai['genre'].sum()
lenz_film_jenai1 = df_lenz_film_genre.str.count("جنایی") 
lenz_film_jenai1=pd.DataFrame(lenz_film_jenai1) 
lenz_film_jenai1=lenz_film_jenai1['genre'].sum()
lenz_film_jenai=lenz_film_jenai+lenz_film_jenai1
lenz_film_jenai_visit = lenz_df_film[lenz_df_film['genre'].str.contains('جنائی')]
lenz_film_jenai_visit=lenz_film_jenai_visit['bazdid'].sum()
lenz_film_jenai1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('جنائی')]
lenz_film_jenai1_visit=lenz_film_jenai1_visit['bazdid'].sum()
lenz_film_jenai_visit=lenz_film_jenai_visit+lenz_film_jenai1_visit

lenz_film_tarikhi = df_lenz_film_genre.str.count("تاریخی") 
lenz_film_tarikhi=pd.DataFrame(lenz_film_tarikhi) 
lenz_film_tarikhi=lenz_film_tarikhi['genre'].sum()
lenz_film_tarikhi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('تاریخی')]
lenz_film_tarikhi_visit=lenz_film_tarikhi_visit['bazdid'].sum()

lenz_film_animeyshen = df_lenz_film_genre.str.count("انیمیشن") 
lenz_film_animeyshen=pd.DataFrame(lenz_film_animeyshen) 
lenz_film_animeyshen=lenz_film_animeyshen['genre'].sum()
lenz_film_animeyshen_visit = lenz_df_film[lenz_df_film['genre'].str.contains('انیمیشن')]
lenz_film_animeyshen_visit=lenz_film_animeyshen_visit['bazdid'].sum()

lenz_film_kodak = df_lenz_film_genre.str.count("کودک") 
lenz_film_kodak=pd.DataFrame(lenz_film_kodak) 
lenz_film_kodak=lenz_film_kodak['genre'].sum()
lenz_film_kodak1 = df_lenz_film_genre.str.count("کودکان") 
lenz_film_kodak1=pd.DataFrame(lenz_film_kodak1) 
lenz_film_kodak1=lenz_film_kodak1['genre'].sum()
lenz_film_kodak=lenz_film_kodak+lenz_film_kodak1
lenz_film_kodak_visit = lenz_df_film[lenz_df_film['genre'].str.contains('کودک')]
lenz_film_kodak_visit=lenz_film_kodak_visit['bazdid'].sum()
lenz_film_kodak1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('کودک')]
lenz_film_kodak1_visit=lenz_film_kodak1_visit['bazdid'].sum()
lenz_film_kodak_visit=lenz_film_kodak_visit+lenz_film_kodak1_visit

lenz_film_hayejanangiz = df_lenz_film_genre.str.count("هیجان انگیز") 
lenz_film_hayejanangiz=pd.DataFrame(lenz_film_hayejanangiz) 
lenz_film_hayejanangiz=lenz_film_hayejanangiz['genre'].sum()
lenz_film_hayejanangiz_visit = lenz_df_film[lenz_df_film['genre'].str.contains('هیجان انگیز')]
lenz_film_hayejanangiz_visit=lenz_film_hayejanangiz_visit['bazdid'].sum()

lenz_film_khanevadegi = df_lenz_film_genre.str.count("خانوادگی") 
lenz_film_khanevadegi=pd.DataFrame(lenz_film_khanevadegi) 
lenz_film_khanevadegi=lenz_film_khanevadegi['genre'].sum()
lenz_film_khanevadegi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('خانوادگی')]
lenz_film_khanevadegi_visit=lenz_film_khanevadegi_visit['bazdid'].sum()

lenz_film_majarajoi = df_lenz_film_genre.str.count("ماجراجویی") 
lenz_film_majarajoi=pd.DataFrame(lenz_film_majarajoi) 
lenz_film_majarajoi=lenz_film_majarajoi['genre'].sum()
lenz_film_majarai = df_lenz_film_genre.str.count("ماجرایی") 
lenz_film_majarai=pd.DataFrame(lenz_film_majarai) 
lenz_film_majarai=lenz_film_majarai['genre'].sum()
lenz_film_majarajoi=lenz_film_majarajoi+lenz_film_majarai
lenz_film_majarajoi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('ماجراجویی')]
lenz_film_majarajoi_visit=lenz_film_majarajoi_visit['bazdid'].sum()
lenz_film_majarajoi1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('ماجراجویی')]
lenz_film_majarajoi1_visit=lenz_film_majarajoi1_visit['bazdid'].sum()
lenz_film_majarajoi_visit=lenz_film_majarajoi_visit+lenz_film_majarajoi1_visit

lenz_film_deram = df_lenz_film_genre.str.count("درام") 
lenz_film_deram=pd.DataFrame(lenz_film_deram) 
lenz_film_deram=lenz_film_deram['genre'].sum()
lenz_film_deram_visit = lenz_df_film[lenz_df_film['genre'].str.contains('درام')]
lenz_film_deram_visit=lenz_film_deram_visit['bazdid'].sum()

lenz_film_komedi = df_lenz_film_genre.str.count("کمدی") 
lenz_film_komedi=pd.DataFrame(lenz_film_komedi) 
lenz_film_komedi=lenz_film_komedi['genre'].sum()
lenz_film_komedi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('کمدی')]
lenz_film_komedi_visit=lenz_film_komedi_visit['bazdid'].sum()

lenz_film_vestern = df_lenz_film_genre.str.count("وسترن") 
lenz_film_vestern=pd.DataFrame(lenz_film_vestern) 
lenz_film_vestern=lenz_film_vestern['genre'].sum()
lenz_film_vestern_visit = lenz_df_film[lenz_df_film['genre'].str.contains('وسترن')]
lenz_film_vestern_visit=lenz_film_vestern_visit['bazdid'].sum()

lenz_film_fantezi = df_lenz_film_genre.str.count("فانتزی") 
lenz_film_fantezi=pd.DataFrame(lenz_film_fantezi) 
lenz_film_fantezi=lenz_film_fantezi['genre'].sum()
lenz_film_fantezi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('فانتزی')]
lenz_film_fantezi_visit=lenz_film_fantezi_visit['bazdid'].sum()

lenz_film_varzeshi = df_lenz_film_genre.str.count("ورزشی") 
lenz_film_varzeshi=pd.DataFrame(lenz_film_varzeshi) 
lenz_film_varzeshi=lenz_film_varzeshi['genre'].sum()
lenz_film_varzeshi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('ورزشی')]
lenz_film_varzeshi_visit=lenz_film_varzeshi_visit['bazdid'].sum()

lenz_film_elmi_takhayoli = df_lenz_film_genre.str.count("علمی-تخیلی") 
lenz_film_elmi_takhayoli=pd.DataFrame(lenz_film_elmi_takhayoli) 
lenz_film_elmi_takhayoli=lenz_film_elmi_takhayoli['genre'].sum()
lenz_film_elmi_takhayoli_visit = lenz_df_film[lenz_df_film['genre'].str.contains('علمی-تخیلی')]
lenz_film_elmi_takhayoli_visit=lenz_film_elmi_takhayoli_visit['bazdid'].sum()

lenz_film_acshen = df_lenz_film_genre.str.count("اکشن") 
lenz_film_acshen=pd.DataFrame(lenz_film_acshen) 
lenz_film_acshen=lenz_film_acshen['genre'].sum()
lenz_film_acshen_visit = lenz_df_film[lenz_df_film['genre'].str.contains('اکشن')]
lenz_film_acshen_visit=lenz_film_acshen_visit['bazdid'].sum()

lenz_film_mozical = df_lenz_film_genre.str.count("موزیکال") 
lenz_film_mozical=pd.DataFrame(lenz_film_mozical) 
lenz_film_mozical=lenz_film_mozical['genre'].sum()
lenz_film_mozical_visit = lenz_df_film[lenz_df_film['genre'].str.contains('موزیکال')]
lenz_film_mozical_visit=lenz_film_mozical_visit['bazdid'].sum()

lenz_film_jangi = df_lenz_film_genre.str.count("جنگی") 
lenz_film_jangi=pd.DataFrame(lenz_film_jangi) 
lenz_film_jangi=lenz_film_jangi['genre'].sum()
lenz_film_jangi_visit = lenz_df_film[lenz_df_film['genre'].str.contains('جنگی')]
lenz_film_jangi_visit=lenz_film_jangi_visit['bazdid'].sum()

lenz_film_goftego = df_lenz_film_genre.str.count("گفتگو") 
lenz_film_goftego=pd.DataFrame(lenz_film_goftego) 
lenz_film_goftego=lenz_film_goftego['genre'].sum()
lenz_film_goftego_visit = lenz_df_film[lenz_df_film['genre'].str.contains('گفتگو')]
lenz_film_goftego_visit=lenz_film_goftego_visit['bazdid'].sum()

lenz_film_khiali = df_lenz_film_genre.str.count("خیالی") 
lenz_film_khiali=pd.DataFrame(lenz_film_khiali) 
lenz_film_khiali=lenz_film_khiali['genre'].sum()
lenz_film_khiali1 = df_lenz_film_genre.str.count("تخیلی") 
lenz_film_khiali1=pd.DataFrame(lenz_film_khiali1) 
lenz_film_khiali1=lenz_film_khiali1['genre'].sum()
lenz_film_khiali=lenz_film_khiali+lenz_film_khiali1
lenz_film_khiali_visit = lenz_df_film[lenz_df_film['genre'].str.contains('خیالی')]
lenz_film_khiali_visit=lenz_film_khiali_visit['bazdid'].sum()
lenz_film_khiali1_visit = lenz_df_film[lenz_df_film['genre'].str.contains('خیالی')]
lenz_film_khiali1_visit=lenz_film_khiali1_visit['bazdid'].sum()
lenz_film_khiali_visit=lenz_film_khiali_visit+lenz_film_khiali1_visit

lenz_film_count_of_genre={'lenz_film_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'lenz_film_count_of_genre1': [lenz_film_mozical, lenz_film_hayejanangiz, lenz_film_varzeshi,
                                lenz_film_goftego, lenz_film_mostanad, lenz_film_majarajoi, 
                                lenz_film_kodak,lenz_film_komedi, lenz_film_fantezi,lenz_film_elmi_takhayoli, 
                                lenz_film_siasi,lenz_film_zendeginame, lenz_film_romantic, 
                                lenz_film_razalod,lenz_film_deram, lenz_film_khiali, 
                                lenz_film_khanevadegi, lenz_film_jangi, lenz_film_jenai,
                                lenz_film_tarsnak, lenz_film_tarikhi,
                                lenz_film_animeyshen, lenz_film_acshen, lenz_film_vestern]}
lenz_film_count_of_genre=pd.DataFrame(lenz_film_count_of_genre, columns=['lenz_film_type_of_genre', 'lenz_film_count_of_genre1'])
lenz_film_count_of_genre=lenz_film_count_of_genre.query("lenz_film_count_of_genre1 != '0'")
lenz_film_count_of_genre.sort_values('lenz_film_count_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')

lenz_film_visit_of_genre={'lenz_film_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'lenz_film_visit_of_genre1': [lenz_film_mozical, lenz_film_hayejanangiz, lenz_film_varzeshi,
                                lenz_film_goftego, lenz_film_mostanad, lenz_film_majarajoi, 
                                lenz_film_kodak,lenz_film_komedi, lenz_film_fantezi,lenz_film_elmi_takhayoli, 
                                lenz_film_siasi,lenz_film_zendeginame, lenz_film_romantic, 
                                lenz_film_razalod,lenz_film_deram, lenz_film_khiali, 
                                lenz_film_khanevadegi, lenz_film_jangi, lenz_film_jenai,
                                lenz_film_tarsnak, lenz_film_tarikhi,
                                lenz_film_animeyshen, lenz_film_acshen, lenz_film_vestern]}
lenz_film_visit_of_genre=pd.DataFrame(lenz_film_visit_of_genre, columns=['lenz_film_type_of_genre', 'lenz_film_visit_of_genre1'])
lenz_film_visit_of_genre=lenz_film_visit_of_genre.query("lenz_film_visit_of_genre1 != '0'")
lenz_film_visit_of_genre.sort_values('lenz_film_visit_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')
print("finish genre of lenz film")
##############################################################################################################################
########################################################## country ###############################################################
##############################################################################################################################
print("country of lenz film")
df_lenz_film_country=lenz_df_film['country']
lenz_film_count_of_all_country=len(lenz_df_film)
lenz_film_visit_of_all_country=lenz_df_film['bazdid'].sum()

lenz_film_amrika = df_lenz_film_country.str.count("آمریکا") 
lenz_film_amrika=pd.DataFrame(lenz_film_amrika) 
lenz_film_amrika=lenz_film_amrika['country'].sum()
lenz_film_amrika_visit = lenz_df_film[lenz_df_film['country'].str.contains('آمریکا')]
lenz_film_amrika_visit=lenz_film_amrika_visit['bazdid'].sum()

lenz_film_iran = df_lenz_film_country.str.count("ایران") 
lenz_film_iran=pd.DataFrame(lenz_film_iran) 
lenz_film_iran=lenz_film_iran['country'].sum()
lenz_film_iran_visit = lenz_df_film[lenz_df_film['country'].str.contains('ایران')]
lenz_film_iran_visit=lenz_film_iran_visit['bazdid'].sum()

lenz_film_holand = df_lenz_film_country.str.count("هلند") 
lenz_film_holand=pd.DataFrame(lenz_film_holand) 
lenz_film_holand=lenz_film_holand['country'].sum()
lenz_film_holand_visit = lenz_df_film[lenz_df_film['country'].str.contains('هلند')]
lenz_film_holand_visit=lenz_film_holand_visit['bazdid'].sum()

lenz_film_alman = df_lenz_film_country.str.count("آلمان") 
lenz_film_alman=pd.DataFrame(lenz_film_alman) 
lenz_film_alman=lenz_film_alman['country'].sum()
lenz_film_alman_visit = lenz_df_film[lenz_df_film['country'].str.contains('آلمان')]
lenz_film_alman_visit=lenz_film_alman_visit['bazdid'].sum()

lenz_film_englis = df_lenz_film_country.str.count("انگلیس") 
lenz_film_englis=pd.DataFrame(lenz_film_englis) 
lenz_film_englis=lenz_film_englis['country'].sum()
lenz_film_englis_visit = lenz_df_film[lenz_df_film['country'].str.contains('انگلیس')]
lenz_film_englis_visit=lenz_film_englis_visit['bazdid'].sum()
lenz_film_englis1 = df_lenz_film_country.str.count("انگلستان") 
lenz_film_englis1=pd.DataFrame(lenz_film_englis1) 
lenz_film_englis1=lenz_film_englis1['country'].sum()
lenz_film_englis1_visit = lenz_df_film[lenz_df_film['country'].str.contains('انگلستان')]
lenz_film_englis1_visit=lenz_film_englis1_visit['bazdid'].sum()
lenz_film_englis_visit=lenz_film_englis_visit+lenz_film_englis1_visit
lenz_film_englis=lenz_film_englis+lenz_film_englis1

lenz_film_kore_jonobi = df_lenz_film_country.str.count("کره جنوبی") 
lenz_film_kore_jonobi=pd.DataFrame(lenz_film_kore_jonobi) 
lenz_film_kore_jonobi=lenz_film_kore_jonobi['country'].sum()
lenz_film_kore_jonobi_visit = lenz_df_film[lenz_df_film['country'].str.contains('کره جنوبی')]
lenz_film_kore_jonobi_visit=lenz_film_kore_jonobi_visit['bazdid'].sum()

lenz_film_faranse = df_lenz_film_country.str.count("فرانسه") 
lenz_film_faranse=pd.DataFrame(lenz_film_faranse) 
lenz_film_faranse=lenz_film_faranse['country'].sum()
lenz_film_faranse_visit = lenz_df_film[lenz_df_film['country'].str.contains('فرانسه')]
lenz_film_faranse_visit=lenz_film_faranse_visit['bazdid'].sum()

lenz_film_japon = df_lenz_film_country.str.count("ژاپن") 
lenz_film_japon=pd.DataFrame(lenz_film_japon) 
lenz_film_japon=lenz_film_japon['country'].sum()
lenz_film_japon_visit = lenz_df_film[lenz_df_film['country'].str.contains('ژاپن')]
lenz_film_japon_visit=lenz_film_japon_visit['bazdid'].sum()

lenz_film_kanada = df_lenz_film_country.str.count("کانادا") 
lenz_film_kanada=pd.DataFrame(lenz_film_kanada) 
lenz_film_kanada=lenz_film_kanada['country'].sum()
lenz_film_kanada_visit = lenz_df_film[lenz_df_film['country'].str.contains('کانادا')]
lenz_film_kanada_visit=lenz_film_kanada_visit['bazdid'].sum()

lenz_film_fanland = df_lenz_film_country.str.count("فنلاند") 
lenz_film_fanland=pd.DataFrame(lenz_film_fanland) 
lenz_film_fanland=lenz_film_fanland['country'].sum()
lenz_film_fanland_visit = lenz_df_film[lenz_df_film['country'].str.contains('فنلاند')]
lenz_film_fanland_visit=lenz_film_fanland_visit['bazdid'].sum()

lenz_film_korovasi = df_lenz_film_country.str.count("کرواسی") 
lenz_film_korovasi=pd.DataFrame(lenz_film_korovasi) 
lenz_film_korovasi=lenz_film_korovasi['country'].sum()
lenz_film_korovasi_visit = lenz_df_film[lenz_df_film['country'].str.contains('کرواسی')]
lenz_film_korovasi_visit=lenz_film_korovasi_visit['bazdid'].sum()

lenz_film_majarestan = df_lenz_film_country.str.count("مجارستان") 
lenz_film_majarestan=pd.DataFrame(lenz_film_majarestan) 
lenz_film_majarestan=lenz_film_majarestan['country'].sum()
lenz_film_majarestan_visit = lenz_df_film[lenz_df_film['country'].str.contains('مجارستان')]
lenz_film_majarestan_visit=lenz_film_majarestan_visit['bazdid'].sum()

lenz_film_lahestan = df_lenz_film_country.str.count("لهستان") 
lenz_film_lahestan=pd.DataFrame(lenz_film_lahestan) 
lenz_film_lahestan=lenz_film_lahestan['country'].sum()
lenz_film_lahestan_visit = lenz_df_film[lenz_df_film['country'].str.contains('لهستان')]
lenz_film_lahestan_visit=lenz_film_lahestan_visit['bazdid'].sum()

lenz_film_sois = df_lenz_film_country.str.count("سوئیس") 
lenz_film_sois=pd.DataFrame(lenz_film_sois) 
lenz_film_sois=lenz_film_sois['country'].sum()
lenz_film_sois_visit = lenz_df_film[lenz_df_film['country'].str.contains('سوئیس')]
lenz_film_sois_visit=lenz_film_sois_visit['bazdid'].sum()

lenz_film_belgik = df_lenz_film_country.str.count("بلژیک") 
lenz_film_belgik=pd.DataFrame(lenz_film_belgik) 
lenz_film_belgik=lenz_film_belgik['country'].sum()
lenz_film_belgik_visit = lenz_df_film[lenz_df_film['country'].str.contains('بلژیک')]
lenz_film_belgik_visit=lenz_film_belgik_visit['bazdid'].sum()

lenz_film_rosie = df_lenz_film_country.str.count("روسیه") 
lenz_film_rosie=pd.DataFrame(lenz_film_rosie) 
lenz_film_rosie=lenz_film_rosie['country'].sum()
lenz_film_rosie_visit = lenz_df_film[lenz_df_film['country'].str.contains('روسیه')]
lenz_film_rosie_visit=lenz_film_rosie_visit['bazdid'].sum()

lenz_film_italia = df_lenz_film_country.str.count("ایتالیا") 
lenz_film_italia=pd.DataFrame(lenz_film_italia) 
lenz_film_italia=lenz_film_italia['country'].sum()
lenz_film_italia_visit = lenz_df_film[lenz_df_film['country'].str.contains('ایتالیا')]
lenz_film_italia_visit=lenz_film_italia_visit['bazdid'].sum()

lenz_film_bolgharestan = df_lenz_film_country.str.count("بلغارستان") 
lenz_film_bolgharestan=pd.DataFrame(lenz_film_bolgharestan) 
lenz_film_bolgharestan=lenz_film_bolgharestan['country'].sum()
lenz_film_bolgharestan_visit = lenz_df_film[lenz_df_film['country'].str.contains('بلغارستان')]
lenz_film_bolgharestan_visit=lenz_film_bolgharestan_visit['bazdid'].sum()

lenz_film_ostralia = df_lenz_film_country.str.count("استرالیا") 
lenz_film_ostralia=pd.DataFrame(lenz_film_ostralia) 
lenz_film_ostralia=lenz_film_ostralia['country'].sum()
lenz_film_ostralia_visit = lenz_df_film[lenz_df_film['country'].str.contains('استرالیا')]
lenz_film_ostralia_visit=lenz_film_ostralia_visit['bazdid'].sum()

lenz_film_norvej = df_lenz_film_country.str.count("نروژ") 
lenz_film_norvej=pd.DataFrame(lenz_film_norvej) 
lenz_film_norvej=lenz_film_norvej['country'].sum()
lenz_film_norvej_visit = lenz_df_film[lenz_df_film['country'].str.contains('نروژ')]
lenz_film_norvej_visit=lenz_film_norvej_visit['bazdid'].sum()

lenz_film_chin = df_lenz_film_country.str.count("چین") 
lenz_film_chin=pd.DataFrame(lenz_film_chin) 
lenz_film_chin=lenz_film_chin['country'].sum()
lenz_film_chin_visit = lenz_df_film[lenz_df_film['country'].str.contains('چین')]
lenz_film_chin_visit=lenz_film_chin_visit['bazdid'].sum()

lenz_film_tayland = df_lenz_film_country.str.count("تایلند") 
lenz_film_tayland=pd.DataFrame(lenz_film_tayland) 
lenz_film_tayland=lenz_film_tayland['country'].sum()
lenz_film_tayland_visit = lenz_df_film[lenz_df_film['country'].str.contains('تایلند')]
lenz_film_tayland_visit=lenz_film_tayland_visit['bazdid'].sum()

lenz_film_sangapor = df_lenz_film_country.str.count("سنگاپور") 
lenz_film_sangapor=pd.DataFrame(lenz_film_sangapor) 
lenz_film_sangapor=lenz_film_sangapor['country'].sum()
lenz_film_sangapor_visit = lenz_df_film[lenz_df_film['country'].str.contains('سنگاپور')]
lenz_film_sangapor_visit=lenz_film_sangapor_visit['bazdid'].sum()

lenz_film_otrish = df_lenz_film_country.str.count("اتریش") 
lenz_film_otrish=pd.DataFrame(lenz_film_otrish) 
lenz_film_otrish=lenz_film_otrish['country'].sum()
lenz_film_otrish_visit = lenz_df_film[lenz_df_film['country'].str.contains('اتریش')]
lenz_film_otrish_visit=lenz_film_otrish_visit['bazdid'].sum()

lenz_film_spania = df_lenz_film_country.str.count("اسپانیا") 
lenz_film_spania=pd.DataFrame(lenz_film_spania) 
lenz_film_spania=lenz_film_spania['country'].sum()
lenz_film_spania_visit = lenz_df_film[lenz_df_film['country'].str.contains('اسپانیا')]
lenz_film_spania_visit=lenz_film_spania_visit['bazdid'].sum()

lenz_film_okrayn = df_lenz_film_country.str.count("اکراین") 
lenz_film_okrayn=pd.DataFrame(lenz_film_okrayn) 
lenz_film_okrayn=lenz_film_okrayn['country'].sum()
lenz_film_okrayn_visit = lenz_df_film[lenz_df_film['country'].str.contains('اکراین')]
lenz_film_okrayn_visit=lenz_film_okrayn_visit['bazdid'].sum()

lenz_film_emarat = df_lenz_film_country.str.count("امارات") 
lenz_film_emarat=pd.DataFrame(lenz_film_emarat) 
lenz_film_emarat=lenz_film_emarat['country'].sum()
lenz_film_emarat_visit = lenz_df_film[lenz_df_film['country'].str.contains('امارات')]
lenz_film_emarat_visit=lenz_film_emarat_visit['bazdid'].sum()

lenz_film_irland = df_lenz_film_country.str.count("ایرلند") 
lenz_film_irland=pd.DataFrame(lenz_film_irland) 
lenz_film_irland=lenz_film_irland['country'].sum()
lenz_film_irland_visit = lenz_df_film[lenz_df_film['country'].str.contains('ایرلند')]
lenz_film_irland_visit=lenz_film_irland_visit['bazdid'].sum()

lenz_film_argantin = df_lenz_film_country.str.count("آرژانتین") 
lenz_film_argantin=pd.DataFrame(lenz_film_argantin) 
lenz_film_argantin=lenz_film_argantin['country'].sum()
lenz_film_argantin_visit = lenz_df_film[lenz_df_film['country'].str.contains('آرژانتین')]
lenz_film_argantin_visit=lenz_film_argantin_visit['bazdid'].sum()

lenz_film_afrigha_jonobi = df_lenz_film_country.str.count("آفریقای جنوبی") 
lenz_film_afrigha_jonobi=pd.DataFrame(lenz_film_afrigha_jonobi) 
lenz_film_afrigha_jonobi=lenz_film_afrigha_jonobi['country'].sum()
lenz_film_afrigha_jonobi_visit = lenz_df_film[lenz_df_film['country'].str.contains('آفریقای جنوبی')]
lenz_film_afrigha_jonobi_visit=lenz_film_afrigha_jonobi_visit['bazdid'].sum()

lenz_film_danmark = df_lenz_film_country.str.count("دانمارک") 
lenz_film_danmark=pd.DataFrame(lenz_film_danmark) 
lenz_film_danmark=lenz_film_danmark['country'].sum()
lenz_film_danmark_visit = lenz_df_film[lenz_df_film['country'].str.contains('دانمارک')]
lenz_film_danmark_visit=lenz_film_danmark_visit['bazdid'].sum()

lenz_film_shili = df_lenz_film_country.str.count("شیلی") 
lenz_film_shili=pd.DataFrame(lenz_film_shili) 
lenz_film_shili=lenz_film_shili['country'].sum()
lenz_film_shili_visit = lenz_df_film[lenz_df_film['country'].str.contains('شیلی')]
lenz_film_shili_visit=lenz_film_shili_visit['bazdid'].sum()

lenz_film_malezi = df_lenz_film_country.str.count("مالزی") 
lenz_film_malezi=pd.DataFrame(lenz_film_malezi) 
lenz_film_malezi=lenz_film_malezi['country'].sum()
lenz_film_malezi_visit = lenz_df_film[lenz_df_film['country'].str.contains('مالزی')]
lenz_film_malezi_visit=lenz_film_malezi_visit['bazdid'].sum()

lenz_film_honkkong = df_lenz_film_country.str.count("هنک کنگ") 
lenz_film_honkkong=pd.DataFrame(lenz_film_honkkong) 
lenz_film_honkkong=lenz_film_honkkong['country'].sum()
lenz_film_honkkong_visit = lenz_df_film[lenz_df_film['country'].str.contains('هنک کنگ')]
lenz_film_honkkong_visit=lenz_film_honkkong_visit['bazdid'].sum()

lenz_film_soed = df_lenz_film_country.str.count("سوئد") 
lenz_film_soed=pd.DataFrame(lenz_film_soed) 
lenz_film_soed=lenz_film_soed['country'].sum()
lenz_film_soed_visit = lenz_df_film[lenz_df_film['country'].str.contains('سوئد')]
lenz_film_soed_visit=lenz_film_soed_visit['bazdid'].sum()

lenz_film_sois = df_lenz_film_country.str.count("سوئیس") 
lenz_film_sois=pd.DataFrame(lenz_film_sois) 
lenz_film_sois=lenz_film_sois['country'].sum()
lenz_film_sois_visit = lenz_df_film[lenz_df_film['country'].str.contains('سوئیس')]
lenz_film_sois_visit=lenz_film_sois_visit['bazdid'].sum()

lenz_film_mekzik = df_lenz_film_country.str.count("مکزیک") 
lenz_film_mekzik=pd.DataFrame(lenz_film_mekzik) 
lenz_film_mekzik=lenz_film_mekzik['country'].sum()
lenz_film_mekzik_visit = lenz_df_film[lenz_df_film['country'].str.contains('مکزیک')]
lenz_film_mekzik_visit=lenz_film_mekzik_visit['bazdid'].sum()

lenz_film_nioziland = df_lenz_film_country.str.count("نیوزیلند") 
lenz_film_nioziland=pd.DataFrame(lenz_film_nioziland) 
lenz_film_nioziland=lenz_film_nioziland['country'].sum()
lenz_film_nioziland_visit = lenz_df_film[lenz_df_film['country'].str.contains('نیوزیلند')]
lenz_film_nioziland_visit=lenz_film_nioziland_visit['bazdid'].sum()

lenz_film_hend = df_lenz_film_country.str.count("هند") 
lenz_film_hend=pd.DataFrame(lenz_film_hend) 
lenz_film_hend=lenz_film_hend['country'].sum()
lenz_film_hend_visit = lenz_df_film[lenz_df_film['country'].str.contains('هند')]
lenz_film_hend_visit=lenz_film_hend_visit['bazdid'].sum()

lenz_film_country_content_count={'lenz_film_country_name1': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'lenz_film_country_count1': [lenz_film_amrika, lenz_film_iran,lenz_film_holand, lenz_film_alman,
                                                         lenz_film_englis, lenz_film_kore_jonobi,lenz_film_faranse, lenz_film_japon,
                                                         lenz_film_kanada, lenz_film_fanland,lenz_film_korovasi, lenz_film_majarestan,
                                                         lenz_film_lahestan, lenz_film_sois,lenz_film_belgik, lenz_film_rosie,
                                                         lenz_film_italia, lenz_film_bolgharestan,lenz_film_ostralia, lenz_film_norvej,
                                                         lenz_film_chin, lenz_film_tayland,lenz_film_sangapor, lenz_film_otrish,
                                                         lenz_film_spania, lenz_film_okrayn,lenz_film_emarat, lenz_film_irland,
                                                         lenz_film_argantin, lenz_film_afrigha_jonobi,lenz_film_danmark, lenz_film_shili,
                                                         lenz_film_malezi, lenz_film_honkkong,lenz_film_soed, lenz_film_sois,
                                                         lenz_film_mekzik, lenz_film_nioziland,lenz_film_hend]}                                 

lenz_film_country_content_count=pd.DataFrame(lenz_film_country_content_count, columns=['lenz_film_country_name1', 'lenz_film_country_count1'])
lenz_film_country_content_count=lenz_film_country_content_count.query("lenz_film_country_count1 != '0'")
lenz_film_country_content_count.sort_values('lenz_film_country_count1', axis = 0, ascending = False, inplace = True, na_position ='last') 
                                 
lenz_film_country_content_visit={'lenz_film_country_name': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'lenz_film_country_visit1': [lenz_film_amrika_visit, lenz_film_iran_visit,lenz_film_holand_visit, lenz_film_alman_visit,
                                                         lenz_film_englis_visit, lenz_film_kore_jonobi_visit,lenz_film_faranse_visit, lenz_film_japon_visit,
                                                         lenz_film_kanada_visit, lenz_film_fanland_visit,lenz_film_korovasi_visit, lenz_film_majarestan_visit,
                                                         lenz_film_lahestan_visit, lenz_film_sois_visit,lenz_film_belgik_visit, lenz_film_rosie_visit,
                                                         lenz_film_italia_visit, lenz_film_bolgharestan_visit,lenz_film_ostralia_visit, lenz_film_norvej_visit,
                                                         lenz_film_chin_visit, lenz_film_tayland_visit,lenz_film_sangapor_visit, lenz_film_otrish_visit,
                                                         lenz_film_spania_visit, lenz_film_okrayn_visit,lenz_film_emarat_visit, lenz_film_irland_visit,
                                                         lenz_film_argantin_visit, lenz_film_afrigha_jonobi_visit,lenz_film_danmark_visit, lenz_film_shili_visit,
                                                         lenz_film_malezi_visit, lenz_film_honkkong_visit,lenz_film_soed_visit, lenz_film_sois_visit,
                                                         lenz_film_mekzik_visit, lenz_film_nioziland_visit,lenz_film_hend_visit,]}

lenz_film_country_content_visit=pd.DataFrame(lenz_film_country_content_visit, columns=['lenz_film_country_name', 'lenz_film_country_visit1']) 
lenz_film_country_content_visit=lenz_film_country_content_visit.query("lenz_film_country_visit1 != '0'")
lenz_film_country_content_visit.sort_values('lenz_film_country_visit1', axis = 0, ascending = False, inplace = True, na_position ='last') 
print("finish country of lenz film")
##############################################################################################################################
########################################################## year ###############################################################
##############################################################################################################################
print("year of lenz film")
df_lenz_film_year=lenz_df_film['year']
lenz_count_of_all_year=len(lenz_df_film)
lenz_visit_of_all_year=lenz_df_film['bazdid'].sum()

lenz_film_year_1399=lenz_df_film.query("year == '1399'")
lenz_film_year_1399_count=len(lenz_film_year_1399)
lenz_film_year_1399_visit=lenz_film_year_1399['bazdid'].sum()

lenz_film_year_1398=lenz_df_film.query("year == '1398'")
lenz_film_year_1398_count=len(lenz_film_year_1398)
lenz_film_year_1398_visit=lenz_film_year_1398['bazdid'].sum()

lenz_film_year_1397=lenz_df_film.query("year == '1397'")
lenz_film_year_1397_count=len(lenz_film_year_1397)
lenz_film_year_1397_visit=lenz_film_year_1397['bazdid'].sum()

lenz_film_year_1396=lenz_df_film.query("year == '1396'")
lenz_film_year_1396_count=len(lenz_film_year_1396)
lenz_film_year_1396_visit=lenz_film_year_1396['bazdid'].sum()

lenz_film_year_1395=lenz_df_film.query("year == '1395'")
lenz_film_year_1395_count=len(lenz_film_year_1395)
lenz_film_year_1395_visit=lenz_film_year_1395['bazdid'].sum()

lenz_film_year_1394=lenz_df_film.query("year == '1394'")
lenz_film_year_1394_count=len(lenz_film_year_1394)
lenz_film_year_1394_visit=lenz_film_year_1394['bazdid'].sum()

lenz_film_year_1393=lenz_df_film.query("year == '1393'")
lenz_film_year_1393_count=len(lenz_film_year_1393)
lenz_film_year_1393_visit=lenz_film_year_1393['bazdid'].sum()

lenz_film_year_1392=lenz_df_film.query("year == '1392'")
lenz_film_year_1392_count=len(lenz_film_year_1392)
lenz_film_year_1392_visit=lenz_film_year_1392['bazdid'].sum()

lenz_film_year_1391=lenz_df_film.query("year == '1391'")
lenz_film_year_1391_count=len(lenz_film_year_1391)
lenz_film_year_1391_visit=lenz_film_year_1391['bazdid'].sum()

lenz_film_year_1390=lenz_df_film.query("year == '1390'")
lenz_film_year_1390_count=len(lenz_film_year_1390)
lenz_film_year_1390_visit=lenz_film_year_1390['bazdid'].sum()

lenz_film_year_1389=lenz_df_film.query("year == '1389'")
lenz_film_year_1389_count=len(lenz_film_year_1389)
lenz_film_year_1389_visit=lenz_film_year_1389['bazdid'].sum()

lenz_film_year_1388=lenz_df_film.query("year == '1388'")
lenz_film_year_1388_count=len(lenz_film_year_1388)
lenz_film_year_1388_visit=lenz_film_year_1388['bazdid'].sum()

lenz_film_year_1387=lenz_df_film.query("year == '1387'")
lenz_film_year_1387_count=len(lenz_film_year_1387)
lenz_film_year_1387_visit=lenz_film_year_1387['bazdid'].sum()

lenz_film_year_1386=lenz_df_film.query("year == '1386'")
lenz_film_year_1386_count=len(lenz_film_year_1386)
lenz_film_year_1386_visit=lenz_film_year_1386['bazdid'].sum()

lenz_film_year_1385=lenz_df_film.query("year == '1385'")
lenz_film_year_1385_count=len(lenz_film_year_1385)
lenz_film_year_1385_visit=lenz_film_year_1385['bazdid'].sum()

lenz_film_year_1384=lenz_df_film.query("year == '1384'")
lenz_film_year_1384_count=len(lenz_film_year_1384)
lenz_film_year_1384_visit=lenz_film_year_1384['bazdid'].sum()

lenz_film_year_1383=lenz_df_film.query("year == '1383'")
lenz_film_year_1383_count=len(lenz_film_year_1383)
lenz_film_year_1383_visit=lenz_film_year_1383['bazdid'].sum()

lenz_film_year_1382=lenz_df_film.query("year == '1382'")
lenz_film_year_1382_count=len(lenz_film_year_1382)
lenz_film_year_1382_visit=lenz_film_year_1382['bazdid'].sum()

lenz_film_year_1381=lenz_df_film.query("year == '1381'")
lenz_film_year_1381_count=len(lenz_film_year_1381)
lenz_film_year_1381_visit=lenz_film_year_1381['bazdid'].sum()

lenz_film_year_1380=lenz_df_film.query("year == '1380'")
lenz_film_year_1380_count=len(lenz_film_year_1380)
lenz_film_year_1380_visit=lenz_film_year_1380['bazdid'].sum()

lenz_film_year_1379=lenz_df_film.query("year == '1379'")
lenz_film_year_1379_count=len(lenz_film_year_1379)
lenz_film_year_1379_visit=lenz_film_year_1379['bazdid'].sum()

lenz_film_year_1378=lenz_df_film.query("year == '1378'")
lenz_film_year_1378_count=len(lenz_film_year_1378)
lenz_film_year_1378_visit=lenz_film_year_1378['bazdid'].sum()

lenz_film_year_1377=lenz_df_film.query("year == '1377'")
lenz_film_year_1377_count=len(lenz_film_year_1377)
lenz_film_year_1377_visit=lenz_film_year_1377['bazdid'].sum()

lenz_film_year_1376=lenz_df_film.query("year == '1376'")
lenz_film_year_1376_count=len(lenz_film_year_1376)
lenz_film_year_1376_visit=lenz_film_year_1376['bazdid'].sum()

lenz_film_year_1375=lenz_df_film.query("year == '1375'")
lenz_film_year_1375_count=len(lenz_film_year_1375)
lenz_film_year_1375_visit=lenz_film_year_1375['bazdid'].sum()

lenz_film_year_1374=lenz_df_film.query("year == '1374'")
lenz_film_year_1374_count=len(lenz_film_year_1374)
lenz_film_year_1374_visit=lenz_film_year_1374['bazdid'].sum()

lenz_film_year_1373=lenz_df_film.query("year == '1373'")
lenz_film_year_1373_count=len(lenz_film_year_1373)
lenz_film_year_1373_visit=lenz_film_year_1373['bazdid'].sum()

lenz_film_year_1372=lenz_df_film.query("year == '1372'")
lenz_film_year_1372_count=len(lenz_film_year_1372)
lenz_film_year_1372_visit=lenz_film_year_1372['bazdid'].sum()

lenz_film_year_1371=lenz_df_film.query("year == '1371'")
lenz_film_year_1371_count=len(lenz_film_year_1371)
lenz_film_year_1371_visit=lenz_film_year_1371['bazdid'].sum()

lenz_film_year_1370=lenz_df_film.query("year == '1370'")
lenz_film_year_1370_count=len(lenz_film_year_1370)
lenz_film_year_1370_visit=lenz_film_year_1370['bazdid'].sum()

lenz_film_year_1369=lenz_df_film.query("year == '1369'")
lenz_film_year_1369_count=len(lenz_film_year_1369)
lenz_film_year_1369_visit=lenz_film_year_1369['bazdid'].sum()

lenz_film_year_1368=lenz_df_film.query("year == '1368'")
lenz_film_year_1368_count=len(lenz_film_year_1368)
lenz_film_year_1368_visit=lenz_film_year_1368['bazdid'].sum()

lenz_film_year_1367=lenz_df_film.query("year == '1367'")
lenz_film_year_1367_count=len(lenz_film_year_1367)
lenz_film_year_1367_visit=lenz_film_year_1367['bazdid'].sum()

lenz_film_year_1366=lenz_df_film.query("year == '1366'")
lenz_film_year_1366_count=len(lenz_film_year_1366)
lenz_film_year_1366_visit=lenz_film_year_1366['bazdid'].sum()

lenz_film_year_1365=lenz_df_film.query("year == '1365'")
lenz_film_year_1365_count=len(lenz_film_year_1365)
lenz_film_year_1365_visit=lenz_film_year_1365['bazdid'].sum()

lenz_film_year_1364=lenz_df_film.query("year == '1364'")
lenz_film_year_1364_count=len(lenz_film_year_1364)
lenz_film_year_1364_visit=lenz_film_year_1364['bazdid'].sum()

lenz_film_year_1363=lenz_df_film.query("year == '1363'")
lenz_film_year_1363_count=len(lenz_film_year_1363)
lenz_film_year_1363_visit=lenz_film_year_1363['bazdid'].sum()

lenz_film_year_1362=lenz_df_film.query("year == '1362'")
lenz_film_year_1362_count=len(lenz_film_year_1362)
lenz_film_year_1362_visit=lenz_film_year_1362['bazdid'].sum()

lenz_film_year_1361=lenz_df_film.query("year == '1361'")
lenz_film_year_1361_count=len(lenz_film_year_1361)
lenz_film_year_1361_visit=lenz_film_year_1361['bazdid'].sum()

lenz_film_year_1360=lenz_df_film.query("year == '1360'")
lenz_film_year_1360_count=len(lenz_film_year_1360)
lenz_film_year_1360_visit=lenz_film_year_1360['bazdid'].sum()

lenz_film_year_1359=lenz_df_film.query("year == '1359'")
lenz_film_year_1359_count=len(lenz_film_year_1359)
lenz_film_year_1359_visit=lenz_film_year_1359['bazdid'].sum()

lenz_film_year_1358=lenz_df_film.query("year == '1358'")
lenz_film_year_1358_count=len(lenz_film_year_1358)
lenz_film_year_1358_visit=lenz_film_year_1358['bazdid'].sum()

lenz_film_year_1357=lenz_df_film.query('year < 1358')
lenz_film_year_1357_count=len(lenz_film_year_1357)
lenz_film_year_1357_visit=lenz_film_year_1357['bazdid'].sum()

lenz_film_year_count={'lenz_film_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'lenz_film_year_count': [lenz_film_year_1357_count,lenz_film_year_1358_count,lenz_film_year_1359_count,lenz_film_year_1360_count,
                                           lenz_film_year_1361_count,lenz_film_year_1362_count,lenz_film_year_1363_count,lenz_film_year_1364_count,
                                           lenz_film_year_1365_count,lenz_film_year_1366_count,lenz_film_year_1367_count,lenz_film_year_1368_count,
                                           lenz_film_year_1369_count,lenz_film_year_1370_count,lenz_film_year_1371_count,lenz_film_year_1372_count,
                                           lenz_film_year_1373_count,lenz_film_year_1374_count,lenz_film_year_1375_count,lenz_film_year_1376_count,
                                           lenz_film_year_1377_count,lenz_film_year_1378_count,lenz_film_year_1379_count,lenz_film_year_1380_count,
                                           lenz_film_year_1381_count,lenz_film_year_1382_count,lenz_film_year_1383_count,lenz_film_year_1384_count,
                                           lenz_film_year_1385_count,lenz_film_year_1386_count,lenz_film_year_1387_count,lenz_film_year_1388_count,
                                           lenz_film_year_1389_count,lenz_film_year_1390_count,lenz_film_year_1391_count,lenz_film_year_1392_count,
                                           lenz_film_year_1393_count,lenz_film_year_1394_count,lenz_film_year_1395_count,lenz_film_year_1396_count,
                                           lenz_film_year_1397_count,lenz_film_year_1398_count,lenz_film_year_1399_count,]}
lenz_film_year_visit={'lenz_film_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'lenz_film_year_visit': [lenz_film_year_1357_visit,lenz_film_year_1358_visit,lenz_film_year_1359_visit,lenz_film_year_1360_visit,
                                           lenz_film_year_1361_visit,lenz_film_year_1362_visit,lenz_film_year_1363_visit,lenz_film_year_1364_visit,
                                           lenz_film_year_1365_visit,lenz_film_year_1366_visit,lenz_film_year_1367_visit,lenz_film_year_1368_visit,
                                           lenz_film_year_1369_visit,lenz_film_year_1370_visit,lenz_film_year_1371_visit,lenz_film_year_1372_visit,
                                           lenz_film_year_1373_visit,lenz_film_year_1374_visit,lenz_film_year_1375_visit,lenz_film_year_1376_visit,
                                           lenz_film_year_1377_visit,lenz_film_year_1378_visit,lenz_film_year_1379_visit,lenz_film_year_1380_visit,
                                           lenz_film_year_1381_visit,lenz_film_year_1382_visit,lenz_film_year_1383_visit,lenz_film_year_1384_visit,
                                           lenz_film_year_1385_visit,lenz_film_year_1386_visit,lenz_film_year_1387_visit,lenz_film_year_1388_visit,
                                           lenz_film_year_1389_visit,lenz_film_year_1390_visit,lenz_film_year_1391_visit,lenz_film_year_1392_visit,
                                           lenz_film_year_1393_visit,lenz_film_year_1394_visit,lenz_film_year_1395_visit,lenz_film_year_1396_visit,
                                           lenz_film_year_1397_visit,lenz_film_year_1398_visit,lenz_film_year_1399_visit,]}
lenz_film_year_count=pd.DataFrame(lenz_film_year_count, columns=['lenz_film_year','lenz_film_year_count'])
lenz_film_year_visit=pd.DataFrame(lenz_film_year_visit, columns=['lenz_film_year','lenz_film_year_visit'])
print("finish year of lenz film")
##############################################################################################################################
########################################################## IMDB ###############################################################
##############################################################################################################################
print("imdb of lenz film")
df_lenz_film_imdb=lenz_df_film['imdb']
lenz_count_of_all_imdb=len(df_lenz_film_imdb)
lenz_visit_of_all_imdb=lenz_df_film['bazdid'].sum()

lenz_film_imdb_lower6=lenz_df_film.query('imdb < 6')
lenz_film_imdb_lower6_count=len(lenz_film_imdb_lower6)
lenz_film_imdb_lower6_visit=lenz_film_imdb_lower6['bazdid'].sum()

lenz_film_imdb_between_6_7=lenz_df_film.query('imdb > 5.9 and imdb < 7')
lenz_film_imdb_between_6_7_count=len(lenz_film_imdb_between_6_7)
lenz_film_imdb_between_6_7_visit=lenz_film_imdb_between_6_7['bazdid'].sum()

lenz_film_imdb_between_7_8=lenz_df_film.query('imdb > 6.9 and imdb < 8')
lenz_film_imdb_between_7_8_count=len(lenz_film_imdb_between_7_8)
lenz_film_imdb_between_7_8_visit=lenz_film_imdb_between_7_8['bazdid'].sum()

lenz_film_imdb_between_8_9=lenz_df_film.query('imdb > 7.9 and imdb < 9')
lenz_film_imdb_between_8_9_count=len(lenz_film_imdb_between_8_9)
lenz_film_imdb_between_8_9_visit=lenz_film_imdb_between_8_9['bazdid'].sum()

lenz_film_imdb_upper9=lenz_df_film.query('imdb > 8.9')
lenz_film_imdb_upper9_count=len(lenz_film_imdb_upper9)
lenz_film_imdb_upper9_visit=lenz_film_imdb_upper9['bazdid'].sum()

lenz_film_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'count_of_imdb_film': [lenz_film_imdb_lower6_count,
                                        lenz_film_imdb_between_6_7_count,
                                        lenz_film_imdb_between_7_8_count,
                                        lenz_film_imdb_between_8_9_count,
                                        lenz_film_imdb_upper9_count]}
                 
lenz_film_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'visit_of_imdb_film': [lenz_film_imdb_lower6_visit,
                                        lenz_film_imdb_between_6_7_visit,
                                        lenz_film_imdb_between_7_8_visit,
                                        lenz_film_imdb_between_8_9_visit,
                                        lenz_film_imdb_upper9_visit]}
lenz_film_imdb_count=pd.DataFrame(lenz_film_imdb_count, columns=['limitation', 'count_of_imdb_film'])
lenz_film_imdb_visit=pd.DataFrame(lenz_film_imdb_visit, columns=['limitation', 'visit_of_imdb_film'])
print("finish imdb of lenz film")
##############################################################################################################################
########################################################## 10 contents film ###############################################################
##############################################################################################################################
print("popular of lenz film")
lenz_df_film.sort_values('bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_film_content_popular_bazdid=[]
lenz_film_content_popular_visitnumber_bazdid=[]
lenz_film_content_popular_name_bazdid=[]
lenz_film_content_popular_name_bazdid=lenz_df_film["title1"].tolist()
lenz_film_content_popular_bazdid.append(lenz_film_content_popular_name_bazdid)
lenz_film_content_popular_visitnumber_bazdid=lenz_df_film["bazdid"].tolist()
lenz_film_content_popular_bazdid.append(lenz_film_content_popular_visitnumber_bazdid)
lenz_film_content_popular_bazdid_with_tva=lenz_film_content_popular_bazdid
lenz_film_content_popular_bazdid={'lenz_film_content_popular_name_bazdid' : [lenz_film_content_popular_name_bazdid[0], 
                                                           lenz_film_content_popular_name_bazdid[1], 
                                                           lenz_film_content_popular_name_bazdid[2],
                                                           lenz_film_content_popular_name_bazdid[3], 
                                                           lenz_film_content_popular_name_bazdid[4], 
                                                           lenz_film_content_popular_name_bazdid[5],
                                                           lenz_film_content_popular_name_bazdid[6], 
                                                           lenz_film_content_popular_name_bazdid[7], 
                                                           lenz_film_content_popular_name_bazdid[8],
                                                           lenz_film_content_popular_name_bazdid[9]],
                            'lenz_film_content_popular_visitnumber_bazdid' : [lenz_film_content_popular_visitnumber_bazdid[0], lenz_film_content_popular_visitnumber_bazdid[1],
                                                                  lenz_film_content_popular_visitnumber_bazdid[2], lenz_film_content_popular_visitnumber_bazdid[3],
                                                                  lenz_film_content_popular_visitnumber_bazdid[4], lenz_film_content_popular_visitnumber_bazdid[5],
                                                                  lenz_film_content_popular_visitnumber_bazdid[6], lenz_film_content_popular_visitnumber_bazdid[7],
                                                                  lenz_film_content_popular_visitnumber_bazdid[8], lenz_film_content_popular_visitnumber_bazdid[9]]}
lenz_film_content_popular_bazdid=pd.DataFrame(lenz_film_content_popular_bazdid, columns=['lenz_film_content_popular_name_bazdid' , 'lenz_film_content_popular_visitnumber_bazdid'])
lenz_film_content_popular_bazdid.sort_values('lenz_film_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_df_film.sort_values('karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_film_content_popular_karbaran=[]
lenz_film_content_popular_visitnumber_karbaran=[]
lenz_film_content_popular_name_karbaran=[]
lenz_film_content_popular_name_karbaran=lenz_df_film["title1"].tolist()
lenz_film_content_popular_karbaran.append(lenz_film_content_popular_name_karbaran)
lenz_film_content_popular_visitnumber_karbaran=lenz_df_film["karbaran"].tolist()
lenz_film_content_popular_karbaran.append(lenz_film_content_popular_visitnumber_karbaran)
lenz_film_content_popular_karbaran_with_tva=lenz_film_content_popular_karbaran
lenz_film_content_popular_karbaran={'lenz_film_content_popular_name_karbaran' : [lenz_film_content_popular_name_karbaran[0], 
                                                           lenz_film_content_popular_name_karbaran[1], 
                                                           lenz_film_content_popular_name_karbaran[2],
                                                           lenz_film_content_popular_name_karbaran[3], 
                                                           lenz_film_content_popular_name_karbaran[4], 
                                                           lenz_film_content_popular_name_karbaran[5],
                                                           lenz_film_content_popular_name_karbaran[6], 
                                                           lenz_film_content_popular_name_karbaran[7], 
                                                           lenz_film_content_popular_name_karbaran[8],
                                                           lenz_film_content_popular_name_karbaran[9]],
                            'lenz_film_content_popular_visitnumber_karbaran' : [lenz_film_content_popular_visitnumber_karbaran[0], lenz_film_content_popular_visitnumber_karbaran[1],
                                                                  lenz_film_content_popular_visitnumber_karbaran[2], lenz_film_content_popular_visitnumber_karbaran[3],
                                                                  lenz_film_content_popular_visitnumber_karbaran[4], lenz_film_content_popular_visitnumber_karbaran[5],
                                                                  lenz_film_content_popular_visitnumber_karbaran[6], lenz_film_content_popular_visitnumber_karbaran[7],
                                                                  lenz_film_content_popular_visitnumber_karbaran[8], lenz_film_content_popular_visitnumber_karbaran[9]]}
lenz_film_content_popular_karbaran=pd.DataFrame(lenz_film_content_popular_karbaran, columns=['lenz_film_content_popular_name_karbaran' , 'lenz_film_content_popular_visitnumber_karbaran'])
lenz_film_content_popular_karbaran.sort_values('lenz_film_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_df_film.sort_values('minute', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_film_content_popular_minute=[]
lenz_film_content_popular_visitnumber_minute=[]
lenz_film_content_popular_name_minute=[]
lenz_film_content_popular_name_minute=lenz_df_film["title1"].tolist()
lenz_film_content_popular_minute.append(lenz_film_content_popular_name_minute)
lenz_film_content_popular_visitnumber_minute=lenz_df_film["minute"].tolist()
lenz_film_content_popular_minute.append(lenz_film_content_popular_visitnumber_minute)
lenz_film_content_popular_minute_with_tva=lenz_film_content_popular_minute
lenz_film_content_popular_minute={'lenz_film_content_popular_name_minute' : [lenz_film_content_popular_name_minute[0], 
                                                           lenz_film_content_popular_name_minute[1], 
                                                           lenz_film_content_popular_name_minute[2],
                                                           lenz_film_content_popular_name_minute[3], 
                                                           lenz_film_content_popular_name_minute[4], 
                                                           lenz_film_content_popular_name_minute[5],
                                                           lenz_film_content_popular_name_minute[6], 
                                                           lenz_film_content_popular_name_minute[7], 
                                                           lenz_film_content_popular_name_minute[8],
                                                           lenz_film_content_popular_name_minute[9]],
                            'lenz_film_content_popular_visitnumber_minute' : [lenz_film_content_popular_visitnumber_minute[0], lenz_film_content_popular_visitnumber_minute[1],
                                                                  lenz_film_content_popular_visitnumber_minute[2], lenz_film_content_popular_visitnumber_minute[3],
                                                                  lenz_film_content_popular_visitnumber_minute[4], lenz_film_content_popular_visitnumber_minute[5],
                                                                  lenz_film_content_popular_visitnumber_minute[6], lenz_film_content_popular_visitnumber_minute[7],
                                                                  lenz_film_content_popular_visitnumber_minute[8], lenz_film_content_popular_visitnumber_minute[9]]}
lenz_film_content_popular_minute=pd.DataFrame(lenz_film_content_popular_minute, columns=['lenz_film_content_popular_name_minute' , 'lenz_film_content_popular_visitnumber_minute'])
lenz_film_content_popular_minute.sort_values('lenz_film_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
lenz_film_content_popular_minute=round(lenz_film_content_popular_minute*60, 0)
print("finish popular of lenz film")
##############################################################################################################################
##############################################################################################################################
########################################################## serial ###############################################################
##############################################################################################################################
##############################################################################################################################
#lenz_df_serial.drop_duplicates(subset =['title1', 'bazdid', 'karbaran'], keep = 'first', inplace = True) 
lenz_df_serial=lenz_df_serial.groupby(['title1', 'genre', 'country', 'year', 'imdb']).sum().reset_index()

print("statistics of lenz serial")
lenz_serial_count_content=lenz_df_serial['bazdid']
lenz_serial_count_content=len(lenz_serial_count_content)
lenz_serial_sum_bazdid=lenz_df_serial['bazdid'].sum()
lenz_serial_sum_karbaran=lenz_df_serial['karbaran'].sum()
lenz_serial_sum_minute=lenz_df_serial['minute'].sum()

##############################################################################################################################
########################################################## genre ###############################################################
##############################################################################################################################
print("genre of lenz serial")
df_lenz_serial_genre=lenz_df_serial['genre']
lenz_count_of_all_genre=len(lenz_df_serial)
lenz_visit_of_all_genre=lenz_df_serial['bazdid'].sum()

lenz_serial_siasi = df_lenz_serial_genre.str.count("سیاسی") 
lenz_serial_siasi=pd.DataFrame(lenz_serial_siasi) 
lenz_serial_siasi=lenz_serial_siasi['genre'].sum()
lenz_serial_siasi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('سیاسی')]
lenz_serial_siasi_visit=lenz_serial_siasi_visit['bazdid'].sum()

lenz_serial_tarsnak = df_lenz_serial_genre.str.count("ترسناک") 
lenz_serial_tarsnak=pd.DataFrame(lenz_serial_tarsnak) 
lenz_serial_tarsnak=lenz_serial_tarsnak['genre'].sum()
lenz_serial_vahshat = df_lenz_serial_genre.str.count("وحشت") 
lenz_serial_vahshat=pd.DataFrame(lenz_serial_vahshat) 
lenz_serial_vahshat=lenz_serial_vahshat['genre'].sum()
lenz_serial_tarsnak=lenz_serial_tarsnak+lenz_serial_vahshat
lenz_serial_tarsnak_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('ترسناک')]
lenz_serial_tarsnak_visit=lenz_serial_tarsnak_visit['bazdid'].sum()
lenz_serial_vahshat_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('وحشت')]
lenz_serial_vahshat_visit=lenz_serial_vahshat_visit['bazdid'].sum()
lenz_serial_tarsnak_visit=lenz_serial_tarsnak_visit+lenz_serial_vahshat_visit

lenz_serial_razalod = df_lenz_serial_genre.str.count("رازآلود") 
lenz_serial_razalod=pd.DataFrame(lenz_serial_razalod) 
lenz_serial_razalod=lenz_serial_razalod['genre'].sum()
lenz_serial_razalod1 = df_lenz_serial_genre.str.count("راز آلود") 
lenz_serial_razalod1=pd.DataFrame(lenz_serial_razalod1) 
lenz_serial_razalod1=lenz_serial_razalod1['genre'].sum()
lenz_serial_razalod=lenz_serial_razalod+lenz_serial_razalod1
lenz_serial_razalod_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('رازآلود')]
lenz_serial_razalod_visit=lenz_serial_razalod_visit['bazdid'].sum()
lenz_serial_razalod1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('رازآلود')]
lenz_serial_razalod1_visit=lenz_serial_razalod1_visit['bazdid'].sum()
lenz_serial_razalod_visit=lenz_serial_razalod_visit+lenz_serial_razalod1_visit

lenz_serial_zendeginame = df_lenz_serial_genre.str.count("زندگینامه") 
lenz_serial_zendeginame=pd.DataFrame(lenz_serial_zendeginame) 
lenz_serial_zendeginame=lenz_serial_zendeginame['genre'].sum()
lenz_serial_zendeginame1 = df_lenz_serial_genre.str.count("زندگی نامه") 
lenz_serial_zendeginame1=pd.DataFrame(lenz_serial_zendeginame1) 
lenz_serial_zendeginame1=lenz_serial_zendeginame1['genre'].sum()
lenz_serial_zendeginame=lenz_serial_zendeginame+lenz_serial_zendeginame1
lenz_serial_zendeginame_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('زندگینامه')]
lenz_serial_zendeginame_visit=lenz_serial_zendeginame_visit['bazdid'].sum()
lenz_serial_zendeginame1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('زندگینامه')]
lenz_serial_zendeginame1_visit=lenz_serial_zendeginame1_visit['bazdid'].sum()
lenz_serial_zendeginame_visit=lenz_serial_zendeginame_visit+lenz_serial_zendeginame1_visit

lenz_serial_romantic = df_lenz_serial_genre.str.count("رمانتیک") 
lenz_serial_romantic=pd.DataFrame(lenz_serial_romantic) 
lenz_serial_romantic=lenz_serial_romantic['genre'].sum()
lenz_serial_romantic_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('رمانتیک')]
lenz_serial_romantic_visit=lenz_serial_romantic_visit['bazdid'].sum()

lenz_serial_mostanad = df_lenz_serial_genre.str.count("مستند") 
lenz_serial_mostanad=pd.DataFrame(lenz_serial_mostanad) 
lenz_serial_mostanad=lenz_serial_mostanad['genre'].sum()
lenz_serial_mostanad_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('مستند')]
lenz_serial_mostanad_visit=lenz_serial_mostanad_visit['bazdid'].sum()

lenz_serial_jenai = df_lenz_serial_genre.str.count("جنائی") 
lenz_serial_jenai=pd.DataFrame(lenz_serial_jenai) 
lenz_serial_jenai=lenz_serial_jenai['genre'].sum()
lenz_serial_jenai1 = df_lenz_serial_genre.str.count("جنایی") 
lenz_serial_jenai1=pd.DataFrame(lenz_serial_jenai1) 
lenz_serial_jenai1=lenz_serial_jenai1['genre'].sum()
lenz_serial_jenai=lenz_serial_jenai+lenz_serial_jenai1
lenz_serial_jenai_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('جنائی')]
lenz_serial_jenai_visit=lenz_serial_jenai_visit['bazdid'].sum()
lenz_serial_jenai1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('جنائی')]
lenz_serial_jenai1_visit=lenz_serial_jenai1_visit['bazdid'].sum()
lenz_serial_jenai_visit=lenz_serial_jenai_visit+lenz_serial_jenai1_visit

lenz_serial_tarikhi = df_lenz_serial_genre.str.count("تاریخی") 
lenz_serial_tarikhi=pd.DataFrame(lenz_serial_tarikhi) 
lenz_serial_tarikhi=lenz_serial_tarikhi['genre'].sum()
lenz_serial_tarikhi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('تاریخی')]
lenz_serial_tarikhi_visit=lenz_serial_tarikhi_visit['bazdid'].sum()

lenz_serial_animeyshen = df_lenz_serial_genre.str.count("انیمیشن") 
lenz_serial_animeyshen=pd.DataFrame(lenz_serial_animeyshen) 
lenz_serial_animeyshen=lenz_serial_animeyshen['genre'].sum()
lenz_serial_animeyshen_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('انیمیشن')]
lenz_serial_animeyshen_visit=lenz_serial_animeyshen_visit['bazdid'].sum()

lenz_serial_kodak = df_lenz_serial_genre.str.count("کودک") 
lenz_serial_kodak=pd.DataFrame(lenz_serial_kodak) 
lenz_serial_kodak=lenz_serial_kodak['genre'].sum()
lenz_serial_kodak1 = df_lenz_serial_genre.str.count("کودکان") 
lenz_serial_kodak1=pd.DataFrame(lenz_serial_kodak1) 
lenz_serial_kodak1=lenz_serial_kodak1['genre'].sum()
lenz_serial_kodak=lenz_serial_kodak+lenz_serial_kodak1
lenz_serial_kodak_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('کودک')]
lenz_serial_kodak_visit=lenz_serial_kodak_visit['bazdid'].sum()
lenz_serial_kodak1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('کودک')]
lenz_serial_kodak1_visit=lenz_serial_kodak1_visit['bazdid'].sum()
lenz_serial_kodak_visit=lenz_serial_kodak_visit+lenz_serial_kodak1_visit

lenz_serial_hayejanangiz = df_lenz_serial_genre.str.count("هیجان انگیز") 
lenz_serial_hayejanangiz=pd.DataFrame(lenz_serial_hayejanangiz) 
lenz_serial_hayejanangiz=lenz_serial_hayejanangiz['genre'].sum()
lenz_serial_hayejanangiz_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('هیجان انگیز')]
lenz_serial_hayejanangiz_visit=lenz_serial_hayejanangiz_visit['bazdid'].sum()

lenz_serial_khanevadegi = df_lenz_serial_genre.str.count("خانوادگی") 
lenz_serial_khanevadegi=pd.DataFrame(lenz_serial_khanevadegi) 
lenz_serial_khanevadegi=lenz_serial_khanevadegi['genre'].sum()
lenz_serial_khanevadegi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('خانوادگی')]
lenz_serial_khanevadegi_visit=lenz_serial_khanevadegi_visit['bazdid'].sum()

lenz_serial_majarajoi = df_lenz_serial_genre.str.count("ماجراجویی") 
lenz_serial_majarajoi=pd.DataFrame(lenz_serial_majarajoi) 
lenz_serial_majarajoi=lenz_serial_majarajoi['genre'].sum()
lenz_serial_majarai = df_lenz_serial_genre.str.count("ماجرایی") 
lenz_serial_majarai=pd.DataFrame(lenz_serial_majarai) 
lenz_serial_majarai=lenz_serial_majarai['genre'].sum()
lenz_serial_majarajoi=lenz_serial_majarajoi+lenz_serial_majarai
lenz_serial_majarajoi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('ماجراجویی')]
lenz_serial_majarajoi_visit=lenz_serial_majarajoi_visit['bazdid'].sum()
lenz_serial_majarajoi1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('ماجراجویی')]
lenz_serial_majarajoi1_visit=lenz_serial_majarajoi1_visit['bazdid'].sum()
lenz_serial_majarajoi_visit=lenz_serial_majarajoi_visit+lenz_serial_majarajoi1_visit

lenz_serial_deram = df_lenz_serial_genre.str.count("درام") 
lenz_serial_deram=pd.DataFrame(lenz_serial_deram) 
lenz_serial_deram=lenz_serial_deram['genre'].sum()
lenz_serial_deram_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('درام')]
lenz_serial_deram_visit=lenz_serial_deram_visit['bazdid'].sum()

lenz_serial_komedi = df_lenz_serial_genre.str.count("کمدی") 
lenz_serial_komedi=pd.DataFrame(lenz_serial_komedi) 
lenz_serial_komedi=lenz_serial_komedi['genre'].sum()
lenz_serial_komedi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('کمدی')]
lenz_serial_komedi_visit=lenz_serial_komedi_visit['bazdid'].sum()

lenz_serial_vestern = df_lenz_serial_genre.str.count("وسترن") 
lenz_serial_vestern=pd.DataFrame(lenz_serial_vestern) 
lenz_serial_vestern=lenz_serial_vestern['genre'].sum()
lenz_serial_vestern_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('وسترن')]
lenz_serial_vestern_visit=lenz_serial_vestern_visit['bazdid'].sum()

lenz_serial_fantezi = df_lenz_serial_genre.str.count("فانتزی") 
lenz_serial_fantezi=pd.DataFrame(lenz_serial_fantezi) 
lenz_serial_fantezi=lenz_serial_fantezi['genre'].sum()
lenz_serial_fantezi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('فانتزی')]
lenz_serial_fantezi_visit=lenz_serial_fantezi_visit['bazdid'].sum()

lenz_serial_varzeshi = df_lenz_serial_genre.str.count("ورزشی") 
lenz_serial_varzeshi=pd.DataFrame(lenz_serial_varzeshi) 
lenz_serial_varzeshi=lenz_serial_varzeshi['genre'].sum()
lenz_serial_varzeshi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('ورزشی')]
lenz_serial_varzeshi_visit=lenz_serial_varzeshi_visit['bazdid'].sum()

lenz_serial_elmi_takhayoli = df_lenz_serial_genre.str.count("علمی-تخیلی") 
lenz_serial_elmi_takhayoli=pd.DataFrame(lenz_serial_elmi_takhayoli) 
lenz_serial_elmi_takhayoli=lenz_serial_elmi_takhayoli['genre'].sum()
lenz_serial_elmi_takhayoli_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('علمی-تخیلی')]
lenz_serial_elmi_takhayoli_visit=lenz_serial_elmi_takhayoli_visit['bazdid'].sum()

lenz_serial_acshen = df_lenz_serial_genre.str.count("اکشن") 
lenz_serial_acshen=pd.DataFrame(lenz_serial_acshen) 
lenz_serial_acshen=lenz_serial_acshen['genre'].sum()
lenz_serial_acshen_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('اکشن')]
lenz_serial_acshen_visit=lenz_serial_acshen_visit['bazdid'].sum()

lenz_serial_mozical = df_lenz_serial_genre.str.count("موزیکال") 
lenz_serial_mozical=pd.DataFrame(lenz_serial_mozical) 
lenz_serial_mozical=lenz_serial_mozical['genre'].sum()
lenz_serial_mozical_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('موزیکال')]
lenz_serial_mozical_visit=lenz_serial_mozical_visit['bazdid'].sum()

lenz_serial_jangi = df_lenz_serial_genre.str.count("جنگی") 
lenz_serial_jangi=pd.DataFrame(lenz_serial_jangi) 
lenz_serial_jangi=lenz_serial_jangi['genre'].sum()
lenz_serial_jangi_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('جنگی')]
lenz_serial_jangi_visit=lenz_serial_jangi_visit['bazdid'].sum()

lenz_serial_goftego = df_lenz_serial_genre.str.count("گفتگو") 
lenz_serial_goftego=pd.DataFrame(lenz_serial_goftego) 
lenz_serial_goftego=lenz_serial_goftego['genre'].sum()
lenz_serial_goftego_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('گفتگو')]
lenz_serial_goftego_visit=lenz_serial_goftego_visit['bazdid'].sum()

lenz_serial_khiali = df_lenz_serial_genre.str.count("خیالی") 
lenz_serial_khiali=pd.DataFrame(lenz_serial_khiali) 
lenz_serial_khiali=lenz_serial_khiali['genre'].sum()
lenz_serial_khiali1 = df_lenz_serial_genre.str.count("تخیلی") 
lenz_serial_khiali1=pd.DataFrame(lenz_serial_khiali1) 
lenz_serial_khiali1=lenz_serial_khiali1['genre'].sum()
lenz_serial_khiali=lenz_serial_khiali+lenz_serial_khiali1
lenz_serial_khiali_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('خیالی')]
lenz_serial_khiali_visit=lenz_serial_khiali_visit['bazdid'].sum()
lenz_serial_khiali1_visit = lenz_df_serial[lenz_df_serial['genre'].str.contains('خیالی')]
lenz_serial_khiali1_visit=lenz_serial_khiali1_visit['bazdid'].sum()
lenz_serial_khiali_visit=lenz_serial_khiali_visit+lenz_serial_khiali1_visit

lenz_serial_count_of_genre={'lenz_serial_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'lenz_serial_count_of_genre1': [lenz_serial_mozical, lenz_serial_hayejanangiz, lenz_serial_varzeshi,
                                lenz_serial_goftego, lenz_serial_mostanad, lenz_serial_majarajoi, 
                                lenz_serial_kodak,lenz_serial_komedi, lenz_serial_fantezi,lenz_serial_elmi_takhayoli, 
                                lenz_serial_siasi,lenz_serial_zendeginame, lenz_serial_romantic, 
                                lenz_serial_razalod,lenz_serial_deram, lenz_serial_khiali, 
                                lenz_serial_khanevadegi, lenz_serial_jangi, lenz_serial_jenai,
                                lenz_serial_tarsnak, lenz_serial_tarikhi,
                                lenz_serial_animeyshen, lenz_serial_acshen, lenz_serial_vestern]}
lenz_serial_count_of_genre=pd.DataFrame(lenz_serial_count_of_genre, columns=['lenz_serial_type_of_genre', 'lenz_serial_count_of_genre1'])
lenz_serial_count_of_genre=lenz_serial_count_of_genre.query("lenz_serial_count_of_genre1 != '0'")
lenz_serial_count_of_genre.sort_values('lenz_serial_count_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')

lenz_serial_visit_of_genre={'lenz_serial_type_of_genre': ['موزیکال', 'هیجان انگیز', 'ورزشی', 
                                'گفتگو', 'مستند',
                            'ماجراجویی', 'کودک',
                               'کمدی', 'فانتزی',
                               'علمی-تخیلی', 'سیاسی',
                               'زندگینامه', 'رمانتیک', 'رازآلود',
                               'درام', 'خیالی', 'خانوادگی',
                                'جنگی', 'جنائی',
                               'وحشت', 'تاریخی',
                               'انیمیشن', 'اکشن',
 'وسترن',],
                'lenz_serial_visit_of_genre1': [lenz_serial_mozical, lenz_serial_hayejanangiz, lenz_serial_varzeshi,
                                lenz_serial_goftego, lenz_serial_mostanad, lenz_serial_majarajoi, 
                                lenz_serial_kodak,lenz_serial_komedi, lenz_serial_fantezi,lenz_serial_elmi_takhayoli, 
                                lenz_serial_siasi,lenz_serial_zendeginame, lenz_serial_romantic, 
                                lenz_serial_razalod,lenz_serial_deram, lenz_serial_khiali, 
                                lenz_serial_khanevadegi, lenz_serial_jangi, lenz_serial_jenai,
                                lenz_serial_tarsnak, lenz_serial_tarikhi,
                                lenz_serial_animeyshen, lenz_serial_acshen, lenz_serial_vestern]}
lenz_serial_visit_of_genre=pd.DataFrame(lenz_serial_visit_of_genre, columns=['lenz_serial_type_of_genre', 'lenz_serial_visit_of_genre1'])
lenz_serial_visit_of_genre=lenz_serial_visit_of_genre.query("lenz_serial_visit_of_genre1 != '0'")
lenz_serial_visit_of_genre.sort_values('lenz_serial_visit_of_genre1', axis = 0, ascending = True, inplace = True, na_position ='last')
print("finish genre of lenz serial")
##############################################################################################################################
########################################################## country ###############################################################
##############################################################################################################################
print("country of lenz serial")
df_lenz_serial_country=lenz_df_serial['country']
lenz_serial_count_of_all_country=len(lenz_df_serial)
lenz_serial_visit_of_all_country=lenz_df_serial['bazdid'].sum()

lenz_serial_amrika = df_lenz_serial_country.str.count("آمریکا") 
lenz_serial_amrika=pd.DataFrame(lenz_serial_amrika) 
lenz_serial_amrika=lenz_serial_amrika['country'].sum()
lenz_serial_amrika_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('آمریکا')]
lenz_serial_amrika_visit=lenz_serial_amrika_visit['bazdid'].sum()

lenz_serial_iran = df_lenz_serial_country.str.count("ایران") 
lenz_serial_iran=pd.DataFrame(lenz_serial_iran) 
lenz_serial_iran=lenz_serial_iran['country'].sum()
lenz_serial_iran_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('ایران')]
lenz_serial_iran_visit=lenz_serial_iran_visit['bazdid'].sum()

lenz_serial_holand = df_lenz_serial_country.str.count("هلند") 
lenz_serial_holand=pd.DataFrame(lenz_serial_holand) 
lenz_serial_holand=lenz_serial_holand['country'].sum()
lenz_serial_holand_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('هلند')]
lenz_serial_holand_visit=lenz_serial_holand_visit['bazdid'].sum()

lenz_serial_alman = df_lenz_serial_country.str.count("آلمان") 
lenz_serial_alman=pd.DataFrame(lenz_serial_alman) 
lenz_serial_alman=lenz_serial_alman['country'].sum()
lenz_serial_alman_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('آلمان')]
lenz_serial_alman_visit=lenz_serial_alman_visit['bazdid'].sum()

lenz_serial_englis = df_lenz_serial_country.str.count("انگلیس") 
lenz_serial_englis=pd.DataFrame(lenz_serial_englis) 
lenz_serial_englis=lenz_serial_englis['country'].sum()
lenz_serial_englis_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('انگلیس')]
lenz_serial_englis_visit=lenz_serial_englis_visit['bazdid'].sum()
lenz_serial_englis1 = df_lenz_serial_country.str.count("انگلستان") 
lenz_serial_englis1=pd.DataFrame(lenz_serial_englis1) 
lenz_serial_englis1=lenz_serial_englis1['country'].sum()
lenz_serial_englis1_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('انگلستان')]
lenz_serial_englis1_visit=lenz_serial_englis1_visit['bazdid'].sum()
lenz_serial_englis_visit=lenz_serial_englis_visit+lenz_serial_englis1_visit
lenz_serial_englis=lenz_serial_englis+lenz_serial_englis1

lenz_serial_kore_jonobi = df_lenz_serial_country.str.count("کره جنوبی") 
lenz_serial_kore_jonobi=pd.DataFrame(lenz_serial_kore_jonobi) 
lenz_serial_kore_jonobi=lenz_serial_kore_jonobi['country'].sum()
lenz_serial_kore_jonobi_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('کره جنوبی')]
lenz_serial_kore_jonobi_visit=lenz_serial_kore_jonobi_visit['bazdid'].sum()

lenz_serial_faranse = df_lenz_serial_country.str.count("فرانسه") 
lenz_serial_faranse=pd.DataFrame(lenz_serial_faranse) 
lenz_serial_faranse=lenz_serial_faranse['country'].sum()
lenz_serial_faranse_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('فرانسه')]
lenz_serial_faranse_visit=lenz_serial_faranse_visit['bazdid'].sum()

lenz_serial_japon = df_lenz_serial_country.str.count("ژاپن") 
lenz_serial_japon=pd.DataFrame(lenz_serial_japon) 
lenz_serial_japon=lenz_serial_japon['country'].sum()
lenz_serial_japon_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('ژاپن')]
lenz_serial_japon_visit=lenz_serial_japon_visit['bazdid'].sum()

lenz_serial_kanada = df_lenz_serial_country.str.count("کانادا") 
lenz_serial_kanada=pd.DataFrame(lenz_serial_kanada) 
lenz_serial_kanada=lenz_serial_kanada['country'].sum()
lenz_serial_kanada_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('کانادا')]
lenz_serial_kanada_visit=lenz_serial_kanada_visit['bazdid'].sum()

lenz_serial_fanland = df_lenz_serial_country.str.count("فنلاند") 
lenz_serial_fanland=pd.DataFrame(lenz_serial_fanland) 
lenz_serial_fanland=lenz_serial_fanland['country'].sum()
lenz_serial_fanland_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('فنلاند')]
lenz_serial_fanland_visit=lenz_serial_fanland_visit['bazdid'].sum()

lenz_serial_korovasi = df_lenz_serial_country.str.count("کرواسی") 
lenz_serial_korovasi=pd.DataFrame(lenz_serial_korovasi) 
lenz_serial_korovasi=lenz_serial_korovasi['country'].sum()
lenz_serial_korovasi_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('کرواسی')]
lenz_serial_korovasi_visit=lenz_serial_korovasi_visit['bazdid'].sum()

lenz_serial_majarestan = df_lenz_serial_country.str.count("مجارستان") 
lenz_serial_majarestan=pd.DataFrame(lenz_serial_majarestan) 
lenz_serial_majarestan=lenz_serial_majarestan['country'].sum()
lenz_serial_majarestan_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('مجارستان')]
lenz_serial_majarestan_visit=lenz_serial_majarestan_visit['bazdid'].sum()

lenz_serial_lahestan = df_lenz_serial_country.str.count("لهستان") 
lenz_serial_lahestan=pd.DataFrame(lenz_serial_lahestan) 
lenz_serial_lahestan=lenz_serial_lahestan['country'].sum()
lenz_serial_lahestan_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('لهستان')]
lenz_serial_lahestan_visit=lenz_serial_lahestan_visit['bazdid'].sum()

lenz_serial_sois = df_lenz_serial_country.str.count("سوئیس") 
lenz_serial_sois=pd.DataFrame(lenz_serial_sois) 
lenz_serial_sois=lenz_serial_sois['country'].sum()
lenz_serial_sois_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('سوئیس')]
lenz_serial_sois_visit=lenz_serial_sois_visit['bazdid'].sum()

lenz_serial_belgik = df_lenz_serial_country.str.count("بلژیک") 
lenz_serial_belgik=pd.DataFrame(lenz_serial_belgik) 
lenz_serial_belgik=lenz_serial_belgik['country'].sum()
lenz_serial_belgik_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('بلژیک')]
lenz_serial_belgik_visit=lenz_serial_belgik_visit['bazdid'].sum()

lenz_serial_rosie = df_lenz_serial_country.str.count("روسیه") 
lenz_serial_rosie=pd.DataFrame(lenz_serial_rosie) 
lenz_serial_rosie=lenz_serial_rosie['country'].sum()
lenz_serial_rosie_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('روسیه')]
lenz_serial_rosie_visit=lenz_serial_rosie_visit['bazdid'].sum()

lenz_serial_italia = df_lenz_serial_country.str.count("ایتالیا") 
lenz_serial_italia=pd.DataFrame(lenz_serial_italia) 
lenz_serial_italia=lenz_serial_italia['country'].sum()
lenz_serial_italia_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('ایتالیا')]
lenz_serial_italia_visit=lenz_serial_italia_visit['bazdid'].sum()

lenz_serial_bolgharestan = df_lenz_serial_country.str.count("بلغارستان") 
lenz_serial_bolgharestan=pd.DataFrame(lenz_serial_bolgharestan) 
lenz_serial_bolgharestan=lenz_serial_bolgharestan['country'].sum()
lenz_serial_bolgharestan_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('بلغارستان')]
lenz_serial_bolgharestan_visit=lenz_serial_bolgharestan_visit['bazdid'].sum()

lenz_serial_ostralia = df_lenz_serial_country.str.count("استرالیا") 
lenz_serial_ostralia=pd.DataFrame(lenz_serial_ostralia) 
lenz_serial_ostralia=lenz_serial_ostralia['country'].sum()
lenz_serial_ostralia_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('استرالیا')]
lenz_serial_ostralia_visit=lenz_serial_ostralia_visit['bazdid'].sum()

lenz_serial_norvej = df_lenz_serial_country.str.count("نروژ") 
lenz_serial_norvej=pd.DataFrame(lenz_serial_norvej) 
lenz_serial_norvej=lenz_serial_norvej['country'].sum()
lenz_serial_norvej_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('نروژ')]
lenz_serial_norvej_visit=lenz_serial_norvej_visit['bazdid'].sum()

lenz_serial_chin = df_lenz_serial_country.str.count("چین") 
lenz_serial_chin=pd.DataFrame(lenz_serial_chin) 
lenz_serial_chin=lenz_serial_chin['country'].sum()
lenz_serial_chin_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('چین')]
lenz_serial_chin_visit=lenz_serial_chin_visit['bazdid'].sum()

lenz_serial_tayland = df_lenz_serial_country.str.count("تایلند") 
lenz_serial_tayland=pd.DataFrame(lenz_serial_tayland) 
lenz_serial_tayland=lenz_serial_tayland['country'].sum()
lenz_serial_tayland_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('تایلند')]
lenz_serial_tayland_visit=lenz_serial_tayland_visit['bazdid'].sum()

lenz_serial_sangapor = df_lenz_serial_country.str.count("سنگاپور") 
lenz_serial_sangapor=pd.DataFrame(lenz_serial_sangapor) 
lenz_serial_sangapor=lenz_serial_sangapor['country'].sum()
lenz_serial_sangapor_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('سنگاپور')]
lenz_serial_sangapor_visit=lenz_serial_sangapor_visit['bazdid'].sum()

lenz_serial_otrish = df_lenz_serial_country.str.count("اتریش") 
lenz_serial_otrish=pd.DataFrame(lenz_serial_otrish) 
lenz_serial_otrish=lenz_serial_otrish['country'].sum()
lenz_serial_otrish_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('اتریش')]
lenz_serial_otrish_visit=lenz_serial_otrish_visit['bazdid'].sum()

lenz_serial_spania = df_lenz_serial_country.str.count("اسپانیا") 
lenz_serial_spania=pd.DataFrame(lenz_serial_spania) 
lenz_serial_spania=lenz_serial_spania['country'].sum()
lenz_serial_spania_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('اسپانیا')]
lenz_serial_spania_visit=lenz_serial_spania_visit['bazdid'].sum()

lenz_serial_okrayn = df_lenz_serial_country.str.count("اکراین") 
lenz_serial_okrayn=pd.DataFrame(lenz_serial_okrayn) 
lenz_serial_okrayn=lenz_serial_okrayn['country'].sum()
lenz_serial_okrayn_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('اکراین')]
lenz_serial_okrayn_visit=lenz_serial_okrayn_visit['bazdid'].sum()

lenz_serial_emarat = df_lenz_serial_country.str.count("امارات") 
lenz_serial_emarat=pd.DataFrame(lenz_serial_emarat) 
lenz_serial_emarat=lenz_serial_emarat['country'].sum()
lenz_serial_emarat_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('امارات')]
lenz_serial_emarat_visit=lenz_serial_emarat_visit['bazdid'].sum()

lenz_serial_irland = df_lenz_serial_country.str.count("ایرلند") 
lenz_serial_irland=pd.DataFrame(lenz_serial_irland) 
lenz_serial_irland=lenz_serial_irland['country'].sum()
lenz_serial_irland_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('ایرلند')]
lenz_serial_irland_visit=lenz_serial_irland_visit['bazdid'].sum()

lenz_serial_argantin = df_lenz_serial_country.str.count("آرژانتین") 
lenz_serial_argantin=pd.DataFrame(lenz_serial_argantin) 
lenz_serial_argantin=lenz_serial_argantin['country'].sum()
lenz_serial_argantin_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('آرژانتین')]
lenz_serial_argantin_visit=lenz_serial_argantin_visit['bazdid'].sum()

lenz_serial_afrigha_jonobi = df_lenz_serial_country.str.count("آفریقای جنوبی") 
lenz_serial_afrigha_jonobi=pd.DataFrame(lenz_serial_afrigha_jonobi) 
lenz_serial_afrigha_jonobi=lenz_serial_afrigha_jonobi['country'].sum()
lenz_serial_afrigha_jonobi_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('آفریقای جنوبی')]
lenz_serial_afrigha_jonobi_visit=lenz_serial_afrigha_jonobi_visit['bazdid'].sum()

lenz_serial_danmark = df_lenz_serial_country.str.count("دانمارک") 
lenz_serial_danmark=pd.DataFrame(lenz_serial_danmark) 
lenz_serial_danmark=lenz_serial_danmark['country'].sum()
lenz_serial_danmark_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('دانمارک')]
lenz_serial_danmark_visit=lenz_serial_danmark_visit['bazdid'].sum()

lenz_serial_shili = df_lenz_serial_country.str.count("شیلی") 
lenz_serial_shili=pd.DataFrame(lenz_serial_shili) 
lenz_serial_shili=lenz_serial_shili['country'].sum()
lenz_serial_shili_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('شیلی')]
lenz_serial_shili_visit=lenz_serial_shili_visit['bazdid'].sum()

lenz_serial_malezi = df_lenz_serial_country.str.count("مالزی") 
lenz_serial_malezi=pd.DataFrame(lenz_serial_malezi) 
lenz_serial_malezi=lenz_serial_malezi['country'].sum()
lenz_serial_malezi_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('مالزی')]
lenz_serial_malezi_visit=lenz_serial_malezi_visit['bazdid'].sum()

lenz_serial_honkkong = df_lenz_serial_country.str.count("هنک کنگ") 
lenz_serial_honkkong=pd.DataFrame(lenz_serial_honkkong) 
lenz_serial_honkkong=lenz_serial_honkkong['country'].sum()
lenz_serial_honkkong_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('هنک کنگ')]
lenz_serial_honkkong_visit=lenz_serial_honkkong_visit['bazdid'].sum()

lenz_serial_soed = df_lenz_serial_country.str.count("سوئد") 
lenz_serial_soed=pd.DataFrame(lenz_serial_soed) 
lenz_serial_soed=lenz_serial_soed['country'].sum()
lenz_serial_soed_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('سوئد')]
lenz_serial_soed_visit=lenz_serial_soed_visit['bazdid'].sum()

lenz_serial_sois = df_lenz_serial_country.str.count("سوئیس") 
lenz_serial_sois=pd.DataFrame(lenz_serial_sois) 
lenz_serial_sois=lenz_serial_sois['country'].sum()
lenz_serial_sois_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('سوئیس')]
lenz_serial_sois_visit=lenz_serial_sois_visit['bazdid'].sum()

lenz_serial_mekzik = df_lenz_serial_country.str.count("مکزیک") 
lenz_serial_mekzik=pd.DataFrame(lenz_serial_mekzik) 
lenz_serial_mekzik=lenz_serial_mekzik['country'].sum()
lenz_serial_mekzik_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('مکزیک')]
lenz_serial_mekzik_visit=lenz_serial_mekzik_visit['bazdid'].sum()

lenz_serial_nioziland = df_lenz_serial_country.str.count("نیوزیلند") 
lenz_serial_nioziland=pd.DataFrame(lenz_serial_nioziland) 
lenz_serial_nioziland=lenz_serial_nioziland['country'].sum()
lenz_serial_nioziland_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('نیوزیلند')]
lenz_serial_nioziland_visit=lenz_serial_nioziland_visit['bazdid'].sum()

lenz_serial_hend = df_lenz_serial_country.str.count("هند") 
lenz_serial_hend=pd.DataFrame(lenz_serial_hend) 
lenz_serial_hend=lenz_serial_hend['country'].sum()
lenz_serial_hend_visit = lenz_df_serial[lenz_df_serial['country'].str.contains('هند')]
lenz_serial_hend_visit=lenz_serial_hend_visit['bazdid'].sum()

lenz_serial_country_content_count={'lenz_serial_country_name': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'lenz_serial_country_count1': [lenz_serial_amrika, lenz_serial_iran,lenz_serial_holand, lenz_serial_alman,
                                                         lenz_serial_englis, lenz_serial_kore_jonobi,lenz_serial_faranse, lenz_serial_japon,
                                                         lenz_serial_kanada, lenz_serial_fanland,lenz_serial_korovasi, lenz_serial_majarestan,
                                                         lenz_serial_lahestan, lenz_serial_sois,lenz_serial_belgik, lenz_serial_rosie,
                                                         lenz_serial_italia, lenz_serial_bolgharestan,lenz_serial_ostralia, lenz_serial_norvej,
                                                         lenz_serial_chin, lenz_serial_tayland,lenz_serial_sangapor, lenz_serial_otrish,
                                                         lenz_serial_spania, lenz_serial_okrayn,lenz_serial_emarat, lenz_serial_irland,
                                                         lenz_serial_argantin, lenz_serial_afrigha_jonobi,lenz_serial_danmark, lenz_serial_shili,
                                                         lenz_serial_malezi, lenz_serial_honkkong,lenz_serial_soed, lenz_serial_sois,
                                                         lenz_serial_mekzik, lenz_serial_nioziland,lenz_serial_hend]}
                                  
lenz_serial_country_content_count=pd.DataFrame(lenz_serial_country_content_count, columns=['lenz_serial_country_name', 'lenz_serial_country_count1'])
lenz_serial_country_content_count=lenz_serial_country_content_count.query("lenz_serial_country_count1 != '0'") 
lenz_serial_country_content_count.sort_values('lenz_serial_country_count1', axis = 0, ascending = False, inplace = True, na_position ='last')                                   
                                  
lenz_serial_country_content_visit={'lenz_serial_country_name': ['آمریکا', 'ایران','هلند', 'آلمان',
                                                        'انگلیس', 'کره جنوبی','فرانسه', 'ژاپن',
                                                        'کانادا', 'فنلاند','کرواسی', 'مجارستان',
                                                        'لهستان', 'سوئیس','بلژیک', 'روسیه',
                                                        'ایتالیا', 'بلغارستان','استرالیا', 'نروژ',
                                                        'چین', 'تایلند','سنگاپور', 'اتریش',
                                                        'اسپانیا', 'اکراین','امارات', 'ایرلند',
                                                        'آرژانتین', 'آفریقای جنوبی','دانمارک', 'شیلی',
                                                        'مالزی', 'هنک کنگ','سوئد', 'سوئیس',
                                                        'مکزیک', 'نیوزیلند','هند',],
                                  'lenz_serial_country_visit1': [lenz_serial_amrika_visit, lenz_serial_iran_visit,lenz_serial_holand_visit, lenz_serial_alman_visit,
                                                         lenz_serial_englis_visit, lenz_serial_kore_jonobi_visit,lenz_serial_faranse_visit, lenz_serial_japon_visit,
                                                         lenz_serial_kanada_visit, lenz_serial_fanland_visit,lenz_serial_korovasi_visit, lenz_serial_majarestan_visit,
                                                         lenz_serial_lahestan_visit, lenz_serial_sois_visit,lenz_serial_belgik_visit, lenz_serial_rosie_visit,
                                                         lenz_serial_italia_visit, lenz_serial_bolgharestan_visit,lenz_serial_ostralia_visit, lenz_serial_norvej_visit,
                                                         lenz_serial_chin_visit, lenz_serial_tayland_visit,lenz_serial_sangapor_visit, lenz_serial_otrish_visit,
                                                         lenz_serial_spania_visit, lenz_serial_okrayn_visit,lenz_serial_emarat_visit, lenz_serial_irland_visit,
                                                         lenz_serial_argantin_visit, lenz_serial_afrigha_jonobi_visit,lenz_serial_danmark_visit, lenz_serial_shili_visit,
                                                         lenz_serial_malezi_visit, lenz_serial_honkkong_visit,lenz_serial_soed_visit, lenz_serial_sois_visit,
                                                         lenz_serial_mekzik_visit, lenz_serial_nioziland_visit,lenz_serial_hend_visit,]}

lenz_serial_country_content_visit=pd.DataFrame(lenz_serial_country_content_visit, columns=['lenz_serial_country_name', 'lenz_serial_country_visit1'])
lenz_serial_country_content_visit=lenz_serial_country_content_visit.query("lenz_serial_country_visit1 != '0'")
lenz_serial_country_content_visit.sort_values('lenz_serial_country_visit1', axis = 0, ascending = False, inplace = True, na_position ='last')  
print("finish country of lenz serial")
##############################################################################################################################
########################################################## year ###############################################################
##############################################################################################################################
print("year of lenz serial")
df_lenz_serial_year=lenz_df_serial['year']
lenz_count_of_all_year=len(lenz_df_serial)
lenz_visit_of_all_year=lenz_df_serial['bazdid'].sum()

lenz_serial_year_1399=lenz_df_serial.query("year == '1399'")
lenz_serial_year_1399_count=len(lenz_serial_year_1399)
lenz_serial_year_1399_visit=lenz_serial_year_1399['bazdid'].sum()

lenz_serial_year_1398=lenz_df_serial.query("year == '1398'")
lenz_serial_year_1398_count=len(lenz_serial_year_1398)
lenz_serial_year_1398_visit=lenz_serial_year_1398['bazdid'].sum()

lenz_serial_year_1397=lenz_df_serial.query("year == '1397'")
lenz_serial_year_1397_count=len(lenz_serial_year_1397)
lenz_serial_year_1397_visit=lenz_serial_year_1397['bazdid'].sum()

lenz_serial_year_1396=lenz_df_serial.query("year == '1396'")
lenz_serial_year_1396_count=len(lenz_serial_year_1396)
lenz_serial_year_1396_visit=lenz_serial_year_1396['bazdid'].sum()

lenz_serial_year_1395=lenz_df_serial.query("year == '1395'")
lenz_serial_year_1395_count=len(lenz_serial_year_1395)
lenz_serial_year_1395_visit=lenz_serial_year_1395['bazdid'].sum()

lenz_serial_year_1394=lenz_df_serial.query("year == '1394'")
lenz_serial_year_1394_count=len(lenz_serial_year_1394)
lenz_serial_year_1394_visit=lenz_serial_year_1394['bazdid'].sum()

lenz_serial_year_1393=lenz_df_serial.query("year == '1393'")
lenz_serial_year_1393_count=len(lenz_serial_year_1393)
lenz_serial_year_1393_visit=lenz_serial_year_1393['bazdid'].sum()

lenz_serial_year_1392=lenz_df_serial.query("year == '1392'")
lenz_serial_year_1392_count=len(lenz_serial_year_1392)
lenz_serial_year_1392_visit=lenz_serial_year_1392['bazdid'].sum()

lenz_serial_year_1391=lenz_df_serial.query("year == '1391'")
lenz_serial_year_1391_count=len(lenz_serial_year_1391)
lenz_serial_year_1391_visit=lenz_serial_year_1391['bazdid'].sum()

lenz_serial_year_1390=lenz_df_serial.query("year == '1390'")
lenz_serial_year_1390_count=len(lenz_serial_year_1390)
lenz_serial_year_1390_visit=lenz_serial_year_1390['bazdid'].sum()

lenz_serial_year_1389=lenz_df_serial.query("year == '1389'")
lenz_serial_year_1389_count=len(lenz_serial_year_1389)
lenz_serial_year_1389_visit=lenz_serial_year_1389['bazdid'].sum()

lenz_serial_year_1388=lenz_df_serial.query("year == '1388'")
lenz_serial_year_1388_count=len(lenz_serial_year_1388)
lenz_serial_year_1388_visit=lenz_serial_year_1388['bazdid'].sum()

lenz_serial_year_1387=lenz_df_serial.query("year == '1387'")
lenz_serial_year_1387_count=len(lenz_serial_year_1387)
lenz_serial_year_1387_visit=lenz_serial_year_1387['bazdid'].sum()

lenz_serial_year_1386=lenz_df_serial.query("year == '1386'")
lenz_serial_year_1386_count=len(lenz_serial_year_1386)
lenz_serial_year_1386_visit=lenz_serial_year_1386['bazdid'].sum()

lenz_serial_year_1385=lenz_df_serial.query("year == '1385'")
lenz_serial_year_1385_count=len(lenz_serial_year_1385)
lenz_serial_year_1385_visit=lenz_serial_year_1385['bazdid'].sum()

lenz_serial_year_1384=lenz_df_serial.query("year == '1384'")
lenz_serial_year_1384_count=len(lenz_serial_year_1384)
lenz_serial_year_1384_visit=lenz_serial_year_1384['bazdid'].sum()

lenz_serial_year_1383=lenz_df_serial.query("year == '1383'")
lenz_serial_year_1383_count=len(lenz_serial_year_1383)
lenz_serial_year_1383_visit=lenz_serial_year_1383['bazdid'].sum()

lenz_serial_year_1382=lenz_df_serial.query("year == '1382'")
lenz_serial_year_1382_count=len(lenz_serial_year_1382)
lenz_serial_year_1382_visit=lenz_serial_year_1382['bazdid'].sum()

lenz_serial_year_1381=lenz_df_serial.query("year == '1381'")
lenz_serial_year_1381_count=len(lenz_serial_year_1381)
lenz_serial_year_1381_visit=lenz_serial_year_1381['bazdid'].sum()

lenz_serial_year_1380=lenz_df_serial.query("year == '1380'")
lenz_serial_year_1380_count=len(lenz_serial_year_1380)
lenz_serial_year_1380_visit=lenz_serial_year_1380['bazdid'].sum()

lenz_serial_year_1379=lenz_df_serial.query("year == '1379'")
lenz_serial_year_1379_count=len(lenz_serial_year_1379)
lenz_serial_year_1379_visit=lenz_serial_year_1379['bazdid'].sum()

lenz_serial_year_1378=lenz_df_serial.query("year == '1378'")
lenz_serial_year_1378_count=len(lenz_serial_year_1378)
lenz_serial_year_1378_visit=lenz_serial_year_1378['bazdid'].sum()

lenz_serial_year_1377=lenz_df_serial.query("year == '1377'")
lenz_serial_year_1377_count=len(lenz_serial_year_1377)
lenz_serial_year_1377_visit=lenz_serial_year_1377['bazdid'].sum()

lenz_serial_year_1376=lenz_df_serial.query("year == '1376'")
lenz_serial_year_1376_count=len(lenz_serial_year_1376)
lenz_serial_year_1376_visit=lenz_serial_year_1376['bazdid'].sum()

lenz_serial_year_1375=lenz_df_serial.query("year == '1375'")
lenz_serial_year_1375_count=len(lenz_serial_year_1375)
lenz_serial_year_1375_visit=lenz_serial_year_1375['bazdid'].sum()

lenz_serial_year_1374=lenz_df_serial.query("year == '1374'")
lenz_serial_year_1374_count=len(lenz_serial_year_1374)
lenz_serial_year_1374_visit=lenz_serial_year_1374['bazdid'].sum()

lenz_serial_year_1373=lenz_df_serial.query("year == '1373'")
lenz_serial_year_1373_count=len(lenz_serial_year_1373)
lenz_serial_year_1373_visit=lenz_serial_year_1373['bazdid'].sum()

lenz_serial_year_1372=lenz_df_serial.query("year == '1372'")
lenz_serial_year_1372_count=len(lenz_serial_year_1372)
lenz_serial_year_1372_visit=lenz_serial_year_1372['bazdid'].sum()

lenz_serial_year_1371=lenz_df_serial.query("year == '1371'")
lenz_serial_year_1371_count=len(lenz_serial_year_1371)
lenz_serial_year_1371_visit=lenz_serial_year_1371['bazdid'].sum()

lenz_serial_year_1370=lenz_df_serial.query("year == '1370'")
lenz_serial_year_1370_count=len(lenz_serial_year_1370)
lenz_serial_year_1370_visit=lenz_serial_year_1370['bazdid'].sum()

lenz_serial_year_1369=lenz_df_serial.query("year == '1369'")
lenz_serial_year_1369_count=len(lenz_serial_year_1369)
lenz_serial_year_1369_visit=lenz_serial_year_1369['bazdid'].sum()

lenz_serial_year_1368=lenz_df_serial.query("year == '1368'")
lenz_serial_year_1368_count=len(lenz_serial_year_1368)
lenz_serial_year_1368_visit=lenz_serial_year_1368['bazdid'].sum()

lenz_serial_year_1367=lenz_df_serial.query("year == '1367'")
lenz_serial_year_1367_count=len(lenz_serial_year_1367)
lenz_serial_year_1367_visit=lenz_serial_year_1367['bazdid'].sum()

lenz_serial_year_1366=lenz_df_serial.query("year == '1366'")
lenz_serial_year_1366_count=len(lenz_serial_year_1366)
lenz_serial_year_1366_visit=lenz_serial_year_1366['bazdid'].sum()

lenz_serial_year_1365=lenz_df_serial.query("year == '1365'")
lenz_serial_year_1365_count=len(lenz_serial_year_1365)
lenz_serial_year_1365_visit=lenz_serial_year_1365['bazdid'].sum()

lenz_serial_year_1364=lenz_df_serial.query("year == '1364'")
lenz_serial_year_1364_count=len(lenz_serial_year_1364)
lenz_serial_year_1364_visit=lenz_serial_year_1364['bazdid'].sum()

lenz_serial_year_1363=lenz_df_serial.query("year == '1363'")
lenz_serial_year_1363_count=len(lenz_serial_year_1363)
lenz_serial_year_1363_visit=lenz_serial_year_1363['bazdid'].sum()

lenz_serial_year_1362=lenz_df_serial.query("year == '1362'")
lenz_serial_year_1362_count=len(lenz_serial_year_1362)
lenz_serial_year_1362_visit=lenz_serial_year_1362['bazdid'].sum()

lenz_serial_year_1361=lenz_df_serial.query("year == '1361'")
lenz_serial_year_1361_count=len(lenz_serial_year_1361)
lenz_serial_year_1361_visit=lenz_serial_year_1361['bazdid'].sum()

lenz_serial_year_1360=lenz_df_serial.query("year == '1360'")
lenz_serial_year_1360_count=len(lenz_serial_year_1360)
lenz_serial_year_1360_visit=lenz_serial_year_1360['bazdid'].sum()

lenz_serial_year_1359=lenz_df_serial.query("year == '1359'")
lenz_serial_year_1359_count=len(lenz_serial_year_1359)
lenz_serial_year_1359_visit=lenz_serial_year_1359['bazdid'].sum()

lenz_serial_year_1358=lenz_df_serial.query("year == '1358'")
lenz_serial_year_1358_count=len(lenz_serial_year_1358)
lenz_serial_year_1358_visit=lenz_serial_year_1358['bazdid'].sum()

lenz_serial_year_1357=lenz_df_serial.query('year < 1358')
lenz_serial_year_1357_count=len(lenz_serial_year_1357)
lenz_serial_year_1357_visit=lenz_serial_year_1357['bazdid'].sum()

lenz_serial_year_count={'lenz_serial_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'lenz_serial_year_count': [lenz_serial_year_1357_count,lenz_serial_year_1358_count,lenz_serial_year_1359_count,lenz_serial_year_1360_count,
                                           lenz_serial_year_1361_count,lenz_serial_year_1362_count,lenz_serial_year_1363_count,lenz_serial_year_1364_count,
                                           lenz_serial_year_1365_count,lenz_serial_year_1366_count,lenz_serial_year_1367_count,lenz_serial_year_1368_count,
                                           lenz_serial_year_1369_count,lenz_serial_year_1370_count,lenz_serial_year_1371_count,lenz_serial_year_1372_count,
                                           lenz_serial_year_1373_count,lenz_serial_year_1374_count,lenz_serial_year_1375_count,lenz_serial_year_1376_count,
                                           lenz_serial_year_1377_count,lenz_serial_year_1378_count,lenz_serial_year_1379_count,lenz_serial_year_1380_count,
                                           lenz_serial_year_1381_count,lenz_serial_year_1382_count,lenz_serial_year_1383_count,lenz_serial_year_1384_count,
                                           lenz_serial_year_1385_count,lenz_serial_year_1386_count,lenz_serial_year_1387_count,lenz_serial_year_1388_count,
                                           lenz_serial_year_1389_count,lenz_serial_year_1390_count,lenz_serial_year_1391_count,lenz_serial_year_1392_count,
                                           lenz_serial_year_1393_count,lenz_serial_year_1394_count,lenz_serial_year_1395_count,lenz_serial_year_1396_count,
                                           lenz_serial_year_1397_count,lenz_serial_year_1398_count,lenz_serial_year_1399_count,]}
                     
lenz_serial_year_visit={'lenz_serial_year': ['قبل از سال 1358', 'سال 1358', 'سال 1359', 'سال 1360',
                                     'سال 1361', 'سال 1362', 'سال 1363', 'سال 1364',
                                     'سال 1365', 'سال 1366', 'سال 1367', 'سال 1368',
                                     'سال 1369', 'سال 1370', 'سال 1371', 'سال 1372',
                                     'سال 1373', 'سال 1374', 'سال 1375', 'سال 1376',
                                     'سال 1377', 'سال 1378', 'سال 1379', 'سال 1380',
                                     'سال 1381', 'سال 1382', 'سال 1383', 'سال 1384',
                                     'سال 1385', 'سال 1386', 'سال 1387', 'سال 1388',
                                     'سال 1389', 'سال 1390', 'سال 1391', 'سال 1392',
                                     'سال 1393', 'سال 1394', 'سال 1395', 'سال 1396',
                                     'سال 1397', 'سال 1398', 'سال 1399',],
                       'lenz_serial_year_visit': [lenz_serial_year_1357_visit,lenz_serial_year_1358_visit,lenz_serial_year_1359_visit,lenz_serial_year_1360_visit,
                                           lenz_serial_year_1361_visit,lenz_serial_year_1362_visit,lenz_serial_year_1363_visit,lenz_serial_year_1364_visit,
                                           lenz_serial_year_1365_visit,lenz_serial_year_1366_visit,lenz_serial_year_1367_visit,lenz_serial_year_1368_visit,
                                           lenz_serial_year_1369_visit,lenz_serial_year_1370_visit,lenz_serial_year_1371_visit,lenz_serial_year_1372_visit,
                                           lenz_serial_year_1373_visit,lenz_serial_year_1374_visit,lenz_serial_year_1375_visit,lenz_serial_year_1376_visit,
                                           lenz_serial_year_1377_visit,lenz_serial_year_1378_visit,lenz_serial_year_1379_visit,lenz_serial_year_1380_visit,
                                           lenz_serial_year_1381_visit,lenz_serial_year_1382_visit,lenz_serial_year_1383_visit,lenz_serial_year_1384_visit,
                                           lenz_serial_year_1385_visit,lenz_serial_year_1386_visit,lenz_serial_year_1387_visit,lenz_serial_year_1388_visit,
                                           lenz_serial_year_1389_visit,lenz_serial_year_1390_visit,lenz_serial_year_1391_visit,lenz_serial_year_1392_visit,
                                           lenz_serial_year_1393_visit,lenz_serial_year_1394_visit,lenz_serial_year_1395_visit,lenz_serial_year_1396_visit,
                                           lenz_serial_year_1397_visit,lenz_serial_year_1398_visit,lenz_serial_year_1399_visit,]}
lenz_serial_year_count=pd.DataFrame(lenz_serial_year_count, columns=['lenz_serial_year','lenz_serial_year_count'])
lenz_serial_year_visit=pd.DataFrame(lenz_serial_year_visit, columns=['lenz_serial_year','lenz_serial_year_visit'])
print("finish year of lenz serial")
##############################################################################################################################
########################################################## IMDB ###############################################################
##############################################################################################################################
print("imdb of lenz serial")
df_lenz_serial_imdb=lenz_df_serial['imdb']
lenz_count_of_all_imdb=len(df_lenz_serial_imdb)
lenz_visit_of_all_imdb=lenz_df_serial['bazdid'].sum()

lenz_serial_imdb_lower6=lenz_df_serial.query('imdb < 6')
lenz_serial_imdb_lower6_count=len(lenz_serial_imdb_lower6)
lenz_serial_imdb_lower6_visit=lenz_serial_imdb_lower6['bazdid'].sum()

lenz_serial_imdb_between_6_7=lenz_df_serial.query('imdb > 5.9 and imdb < 7')
lenz_serial_imdb_between_6_7_count=len(lenz_serial_imdb_between_6_7)
lenz_serial_imdb_between_6_7_visit=lenz_serial_imdb_between_6_7['bazdid'].sum()

lenz_serial_imdb_between_7_8=lenz_df_serial.query('imdb > 6.9 and imdb < 8')
lenz_serial_imdb_between_7_8_count=len(lenz_serial_imdb_between_7_8)
lenz_serial_imdb_between_7_8_visit=lenz_serial_imdb_between_7_8['bazdid'].sum()

lenz_serial_imdb_between_8_9=lenz_df_serial.query('imdb > 7.9 and imdb < 9')
lenz_serial_imdb_between_8_9_count=len(lenz_serial_imdb_between_8_9)
lenz_serial_imdb_between_8_9_visit=lenz_serial_imdb_between_8_9['bazdid'].sum()

lenz_serial_imdb_upper9=lenz_df_serial.query('imdb > 8.9')
lenz_serial_imdb_upper9_count=len(lenz_serial_imdb_upper9)
lenz_serial_imdb_upper9_visit=lenz_serial_imdb_upper9['bazdid'].sum()

lenz_serial_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                 'count_of_imdb_serial': [lenz_serial_imdb_lower6_count,
                                        lenz_serial_imdb_between_6_7_count,
                                        lenz_serial_imdb_between_7_8_count,
                                        lenz_serial_imdb_between_8_9_count,
                                        lenz_serial_imdb_upper9_count]}
                                          
lenz_serial_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'visit_of_imdb_serial': [lenz_serial_imdb_lower6_visit,
                                        lenz_serial_imdb_between_6_7_visit,
                                        lenz_serial_imdb_between_7_8_visit,
                                        lenz_serial_imdb_between_8_9_visit,
                                        lenz_serial_imdb_upper9_visit]}
lenz_serial_imdb_count=pd.DataFrame(lenz_serial_imdb_count, columns=['limitation', 'count_of_imdb_serial'])
lenz_serial_imdb_visit=pd.DataFrame(lenz_serial_imdb_visit, columns=['limitation', 'visit_of_imdb_serial'])
print("finish imdb of lenz serial")
##############################################################################################################################
########################################################## 10 contents film ###############################################################
##############################################################################################################################
print("popular of lenz serial")
lenz_df_serial.sort_values('bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_serial_content_popular_bazdid=[]
lenz_serial_content_popular_visitnumber_bazdid=[]
lenz_serial_content_popular_name_bazdid=[]
lenz_serial_content_popular_name_bazdid=lenz_df_serial["title1"].tolist()
lenz_serial_content_popular_bazdid.append(lenz_serial_content_popular_name_bazdid)
lenz_serial_content_popular_visitnumber_bazdid=lenz_df_serial["bazdid"].tolist()
lenz_serial_content_popular_bazdid.append(lenz_serial_content_popular_visitnumber_bazdid)
lenz_serial_content_popular_bazdid={'lenz_serial_content_popular_name_bazdid' : [lenz_serial_content_popular_name_bazdid[0], 
                                                           lenz_serial_content_popular_name_bazdid[1], 
                                                           lenz_serial_content_popular_name_bazdid[2],
                                                           lenz_serial_content_popular_name_bazdid[3], 
                                                           lenz_serial_content_popular_name_bazdid[4], 
                                                           lenz_serial_content_popular_name_bazdid[5],
                                                           lenz_serial_content_popular_name_bazdid[6], 
                                                           lenz_serial_content_popular_name_bazdid[7], 
                                                           lenz_serial_content_popular_name_bazdid[8],
                                                           lenz_serial_content_popular_name_bazdid[9]],
                            'lenz_serial_content_popular_visitnumber_bazdid' : [lenz_serial_content_popular_visitnumber_bazdid[0], lenz_serial_content_popular_visitnumber_bazdid[1],
                                                                  lenz_serial_content_popular_visitnumber_bazdid[2], lenz_serial_content_popular_visitnumber_bazdid[3],
                                                                  lenz_serial_content_popular_visitnumber_bazdid[4], lenz_serial_content_popular_visitnumber_bazdid[5],
                                                                  lenz_serial_content_popular_visitnumber_bazdid[6], lenz_serial_content_popular_visitnumber_bazdid[7],
                                                                  lenz_serial_content_popular_visitnumber_bazdid[8], lenz_serial_content_popular_visitnumber_bazdid[9]]}
lenz_serial_content_popular_bazdid=pd.DataFrame(lenz_serial_content_popular_bazdid, columns=['lenz_serial_content_popular_name_bazdid' , 'lenz_serial_content_popular_visitnumber_bazdid'])
lenz_serial_content_popular_bazdid.sort_values('lenz_serial_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_df_serial.sort_values('karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_serial_content_popular_karbaran=[]
lenz_serial_content_popular_visitnumber_karbaran=[]
lenz_serial_content_popular_name_karbaran=[]
lenz_serial_content_popular_name_karbaran=lenz_df_serial["title1"].tolist()
lenz_serial_content_popular_karbaran.append(lenz_serial_content_popular_name_karbaran)
lenz_serial_content_popular_visitnumber_karbaran=lenz_df_serial["karbaran"].tolist()
lenz_serial_content_popular_karbaran.append(lenz_serial_content_popular_visitnumber_karbaran)
lenz_serial_content_popular_karbaran={'lenz_serial_content_popular_name_karbaran' : [lenz_serial_content_popular_name_karbaran[0], 
                                                           lenz_serial_content_popular_name_karbaran[1], 
                                                           lenz_serial_content_popular_name_karbaran[2],
                                                           lenz_serial_content_popular_name_karbaran[3], 
                                                           lenz_serial_content_popular_name_karbaran[4], 
                                                           lenz_serial_content_popular_name_karbaran[5],
                                                           lenz_serial_content_popular_name_karbaran[6], 
                                                           lenz_serial_content_popular_name_karbaran[7], 
                                                           lenz_serial_content_popular_name_karbaran[8],
                                                           lenz_serial_content_popular_name_karbaran[9]],
                            'lenz_serial_content_popular_visitnumber_karbaran' : [lenz_serial_content_popular_visitnumber_karbaran[0], lenz_serial_content_popular_visitnumber_karbaran[1],
                                                                  lenz_serial_content_popular_visitnumber_karbaran[2], lenz_serial_content_popular_visitnumber_karbaran[3],
                                                                  lenz_serial_content_popular_visitnumber_karbaran[4], lenz_serial_content_popular_visitnumber_karbaran[5],
                                                                  lenz_serial_content_popular_visitnumber_karbaran[6], lenz_serial_content_popular_visitnumber_karbaran[7],
                                                                  lenz_serial_content_popular_visitnumber_karbaran[8], lenz_serial_content_popular_visitnumber_karbaran[9]]}
lenz_serial_content_popular_karbaran=pd.DataFrame(lenz_serial_content_popular_karbaran, columns=['lenz_serial_content_popular_name_karbaran' , 'lenz_serial_content_popular_visitnumber_karbaran'])
lenz_serial_content_popular_karbaran.sort_values('lenz_serial_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_df_serial.sort_values('minute', axis = 0, ascending = False, inplace = True, na_position ='last')

lenz_serial_content_popular_minute=[]
lenz_serial_content_popular_visitnumber_minute=[]
lenz_serial_content_popular_name_minute=[]
lenz_serial_content_popular_name_minute=lenz_df_serial["title1"].tolist()
lenz_serial_content_popular_minute.append(lenz_serial_content_popular_name_minute)
lenz_serial_content_popular_visitnumber_minute=lenz_df_serial["minute"].tolist()
lenz_serial_content_popular_minute.append(lenz_serial_content_popular_visitnumber_minute)
lenz_serial_content_popular_minute={'lenz_serial_content_popular_name_minute' : [lenz_serial_content_popular_name_minute[0], 
                                                           lenz_serial_content_popular_name_minute[1], 
                                                           lenz_serial_content_popular_name_minute[2],
                                                           lenz_serial_content_popular_name_minute[3], 
                                                           lenz_serial_content_popular_name_minute[4], 
                                                           lenz_serial_content_popular_name_minute[5],
                                                           lenz_serial_content_popular_name_minute[6], 
                                                           lenz_serial_content_popular_name_minute[7], 
                                                           lenz_serial_content_popular_name_minute[8],
                                                           lenz_serial_content_popular_name_minute[9]],
                            'lenz_serial_content_popular_visitnumber_minute' : [lenz_serial_content_popular_visitnumber_minute[0], lenz_serial_content_popular_visitnumber_minute[1],
                                                                  lenz_serial_content_popular_visitnumber_minute[2], lenz_serial_content_popular_visitnumber_minute[3],
                                                                  lenz_serial_content_popular_visitnumber_minute[4], lenz_serial_content_popular_visitnumber_minute[5],
                                                                  lenz_serial_content_popular_visitnumber_minute[6], lenz_serial_content_popular_visitnumber_minute[7],
                                                                  lenz_serial_content_popular_visitnumber_minute[8], lenz_serial_content_popular_visitnumber_minute[9]]}
lenz_serial_content_popular_minute=pd.DataFrame(lenz_serial_content_popular_minute, columns=['lenz_serial_content_popular_name_minute' , 'lenz_serial_content_popular_visitnumber_minute'])
lenz_serial_content_popular_minute=round(lenz_serial_content_popular_minute*60, 0)
lenz_serial_content_popular_minute.sort_values('lenz_serial_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
print("finish popular of lenz serial")

############################################################################################################
############################################################################################################
##################################################### STATISTICS #######################################################
############################################################################################################
############################################################################################################
print("statistics")
tva_content=tva_film_count_content+tva_serial_count_content        # تعداد محتوای تیوا
lenz_content=lenz_film_count_content+lenz_serial_count_content     # تعداد محتوای لنز
film_content=tva_film_count_content+lenz_film_count_content        # تعداد فیلم
film_bazdid=tva_film_sum_bazdid+lenz_film_sum_bazdid               # کل بازدید
film_karbaran=tva_film_sum_karbaran+lenz_film_sum_karbaran         # کل کاربران
film_minute=tva_film_sum_minute+lenz_film_sum_minute               # زمان بازدید
serial_content=tva_serial_count_content+lenz_serial_count_content  # تعداد سریال
serial_bazdid=tva_serial_sum_bazdid+lenz_serial_sum_bazdid         # تعداد بازدید سریال
serial_karbaran=tva_serial_sum_karbaran+lenz_serial_sum_karbaran   # تعداد کاربران سریال
serial_minute=tva_serial_sum_minute+lenz_serial_sum_minute         # زمان بازدید سریال
tva_bazdid=tva_film_sum_bazdid+tva_serial_sum_bazdid               # تعداد بازدید تیوا
tva_karbaran=tva_film_sum_karbaran+tva_serial_sum_karbaran         # تعداد کاربران تیوا
tva_minute=tva_film_sum_minute+tva_serial_sum_minute               # زمان بازدید تیوا
lenz_bazdid=lenz_film_sum_bazdid+lenz_serial_sum_bazdid            # تعداد بازدید لنز
lenz_karbaran=lenz_film_sum_karbaran+lenz_serial_sum_karbaran      # تعداد کاربران لنز
lenz_minute=lenz_film_sum_minute+lenz_serial_sum_minute            # زمان بازدید لنز

summary_data1={'name_operators': ['لنز', 'تیوا'],
              'content_operators': [lenz_content, tva_content],
              'name_operators': ['لنز', 'تیوا'],
              'bazdid_operators': [lenz_bazdid, tva_bazdid],
              'name_operators': ['لنز', 'تیوا'],
              'karbaran_operators': [lenz_karbaran, tva_karbaran],
              'name_operators': ['لنز', 'تیوا'],
              'minute_operators': [lenz_minute, tva_minute]}
summary_data1=pd.DataFrame(summary_data1, columns=['name_operators', 'content_operators', 'name_operators', 'bazdid_operators',
                                                 'name_operators', 'karbaran_operators', 'name_operators', 'minute_operators'])
                            
summary_data2={'tva_name_statistics': ['تعداد محتوا', 'تعداد بازدید', 'تعداد کاربران', 'زمان بازدید'],
              'tva_statistics': [tva_content, tva_bazdid, tva_karbaran, tva_minute],
              'lenz_name_statistics': ['تعداد محتوا', 'تعداد بازدید', 'تعداد کاربران', 'زمان بازدید'],
              'lenz_statistics': [lenz_content, lenz_bazdid, lenz_karbaran, lenz_minute]}
summary_data2=pd.DataFrame(summary_data2, columns=['lenz_name_statistics', 'lenz_statistics', 'tva_name_statistics', 'tva_statistics'])                            
print("end statistics")
############################################################################################################
############################################################################################################
################################################ OUTPUT ####################################################
############################################################################################################
############################################################################################################
print("convert to excel")
tva_film_count_of_genre.to_excel('tva_film_count_of_genre.xlsx')
tva_film_visit_of_genre.to_excel('tva_film_visit_of_genre.xlsx')
tva_film_country_content_count.to_excel('tva_film_country_content_count.xlsx')
tva_film_country_content_visit.to_excel('tva_film_country_content_visit.xlsx')
tva_film_year_count.to_excel('tva_film_year_count.xlsx')
tva_film_year_visit.to_excel('tva_film_year_visit.xlsx')
tva_film_imdb_count.to_excel('tva_film_imdb_count.xlsx')
tva_film_imdb_visit.to_excel('tva_film_imdb_visit.xlsx')
tva_film_content_popular_bazdid.to_excel('tva_film_content_popular_bazdid.xlsx')
tva_film_content_popular_karbaran.to_excel('tva_film_content_popular_karbaran.xlsx')
tva_film_content_popular_minute.to_excel('tva_film_content_popular_minute.xlsx')
tva_serial_count_of_genre.to_excel('tva_serial_count_of_genre.xlsx')
tva_serial_visit_of_genre.to_excel('tva_serial_visit_of_genre.xlsx')
tva_serial_country_content_count.to_excel('tva_serial_country_content_count.xlsx')
tva_serial_country_content_visit.to_excel('tva_serial_country_content_visit.xlsx')
tva_serial_year_count.to_excel('tva_serial_year_count.xlsx')
tva_serial_year_visit.to_excel('tva_serial_year_visit.xlsx')
tva_serial_imdb_count.to_excel('tva_serial_imdb_count.xlsx')
tva_serial_imdb_visit.to_excel('tva_serial_imdb_visit.xlsx')
tva_serial_content_popular_bazdid.to_excel('tva_serial_content_popular_bazdid.xlsx')
tva_serial_content_popular_karbaran.to_excel('tva_serial_content_popular_karbaran.xlsx')
tva_serial_content_popular_minute.to_excel('tva_serial_content_popular_minute.xlsx')

lenz_film_count_of_genre.to_excel('lenz_film_count_of_genre.xlsx')
lenz_film_visit_of_genre.to_excel('lenz_film_visit_of_genre.xlsx')
lenz_film_country_content_count.to_excel('lenz_film_country_content_count.xlsx')
lenz_film_country_content_visit.to_excel('lenz_film_country_content_visit.xlsx')
lenz_film_year_count.to_excel('lenz_film_year_count.xlsx')
lenz_film_year_visit.to_excel('lenz_film_year_visit.xlsx')
lenz_film_imdb_count.to_excel('lenz_film_imdb_count.xlsx')
lenz_film_imdb_visit.to_excel('lenz_film_imdb_visit.xlsx')
lenz_film_content_popular_bazdid.to_excel('lenz_film_content_popular_bazdid.xlsx')
lenz_film_content_popular_karbaran.to_excel('lenz_film_content_popular_karbaran.xlsx')
lenz_film_content_popular_minute.to_excel('lenz_film_content_popular_minute.xlsx')
lenz_serial_count_of_genre.to_excel('lenz_serial_count_of_genre.xlsx')
lenz_serial_visit_of_genre.to_excel('lenz_serial_visit_of_genre.xlsx')
lenz_serial_country_content_count.to_excel('lenz_serial_country_content_count.xlsx')
lenz_serial_country_content_visit.to_excel('lenz_serial_country_content_visit.xlsx')
lenz_serial_year_count.to_excel('lenz_serial_year_count.xlsx')
lenz_serial_year_visit.to_excel('lenz_serial_year_visit.xlsx')
lenz_serial_imdb_count.to_excel('lenz_serial_imdb_count.xlsx')
lenz_serial_imdb_visit.to_excel('lenz_serial_imdb_visit.xlsx')
lenz_serial_content_popular_bazdid.to_excel('lenz_serial_content_popular_bazdid.xlsx')
lenz_serial_content_popular_karbaran.to_excel('lenz_serial_content_popular_karbaran.xlsx')
lenz_serial_content_popular_minute.to_excel('lenz_serial_content_popular_minute.xlsx')

tva_film_count_of_genre = pd.read_excel ('tva_film_count_of_genre.xlsx')
tva_film_visit_of_genre = pd.read_excel ('tva_film_visit_of_genre.xlsx')
tva_film_country_content_count = pd.read_excel ('tva_film_country_content_count.xlsx')
tva_film_country_content_visit = pd.read_excel ('tva_film_country_content_visit.xlsx')
tva_film_year_count = pd.read_excel ('tva_film_year_count.xlsx')
tva_film_year_visit = pd.read_excel ('tva_film_year_visit.xlsx')
tva_film_imdb_count = pd.read_excel ('tva_film_imdb_count.xlsx')
tva_film_imdb_visit = pd.read_excel ('tva_film_imdb_visit.xlsx')
tva_film_content_popular_bazdid = pd.read_excel ('tva_film_content_popular_bazdid.xlsx')
tva_film_content_popular_karbaran = pd.read_excel ('tva_film_content_popular_karbaran.xlsx')
tva_film_content_popular_minute = pd.read_excel ('tva_film_content_popular_minute.xlsx')
tva_serial_count_of_genre = pd.read_excel ('tva_serial_count_of_genre.xlsx')
tva_serial_visit_of_genre = pd.read_excel ('tva_serial_visit_of_genre.xlsx')
tva_serial_country_content_count = pd.read_excel ('tva_serial_country_content_count.xlsx')
tva_serial_country_content_visit = pd.read_excel ('tva_serial_country_content_visit.xlsx')
tva_serial_year_count = pd.read_excel ('tva_serial_year_count.xlsx')
tva_serial_year_visit = pd.read_excel ('tva_serial_year_visit.xlsx')
tva_serial_imdb_count = pd.read_excel ('tva_serial_imdb_count.xlsx')
tva_serial_imdb_visit = pd.read_excel ('tva_serial_imdb_visit.xlsx')
tva_serial_content_popular_bazdid = pd.read_excel ('tva_serial_content_popular_bazdid.xlsx')
tva_serial_content_popular_karbaran = pd.read_excel ('tva_serial_content_popular_karbaran.xlsx')
tva_serial_content_popular_minute = pd.read_excel ('tva_serial_content_popular_minute.xlsx')

lenz_film_count_of_genre = pd.read_excel ('lenz_film_count_of_genre.xlsx')
lenz_film_visit_of_genre = pd.read_excel ('lenz_film_visit_of_genre.xlsx')
lenz_film_country_content_count = pd.read_excel ('lenz_film_country_content_count.xlsx')
lenz_film_country_content_visit = pd.read_excel ('lenz_film_country_content_visit.xlsx')
lenz_film_year_count = pd.read_excel ('lenz_film_year_count.xlsx')
lenz_film_year_visit = pd.read_excel ('lenz_film_year_visit.xlsx')
lenz_film_imdb_count = pd.read_excel ('lenz_film_imdb_count.xlsx')
lenz_film_imdb_visit = pd.read_excel ('lenz_film_imdb_visit.xlsx')
lenz_film_content_popular_bazdid = pd.read_excel ('lenz_film_content_popular_bazdid.xlsx')
lenz_film_content_popular_karbaran = pd.read_excel ('lenz_film_content_popular_karbaran.xlsx')
lenz_film_content_popular_minute = pd.read_excel ('lenz_film_content_popular_minute.xlsx')
lenz_serial_count_of_genre = pd.read_excel ('lenz_serial_count_of_genre.xlsx')
lenz_serial_visit_of_genre = pd.read_excel ('lenz_serial_visit_of_genre.xlsx')
lenz_serial_country_content_count = pd.read_excel ('lenz_serial_country_content_count.xlsx')
lenz_serial_country_content_visit = pd.read_excel ('lenz_serial_country_content_visit.xlsx')
lenz_serial_year_count = pd.read_excel ('lenz_serial_year_count.xlsx')
lenz_serial_year_visit = pd.read_excel ('lenz_serial_year_visit.xlsx')
lenz_serial_imdb_count = pd.read_excel ('lenz_serial_imdb_count.xlsx')
lenz_serial_imdb_visit = pd.read_excel ('lenz_serial_imdb_visit.xlsx')
lenz_serial_content_popular_bazdid = pd.read_excel ('lenz_serial_content_popular_bazdid.xlsx')
lenz_serial_content_popular_karbaran = pd.read_excel ('lenz_serial_content_popular_karbaran.xlsx')
lenz_serial_content_popular_minute = pd.read_excel ('lenz_serial_content_popular_minute.xlsx')
print("end convert to excel")
print("emit of extra columns")
del tva_film_count_of_genre['Unnamed: 0']
del tva_film_visit_of_genre['Unnamed: 0']
del tva_film_country_content_count['Unnamed: 0']
del tva_film_country_content_visit['Unnamed: 0']
del tva_film_year_count['Unnamed: 0']
del tva_film_year_visit['Unnamed: 0']
del tva_film_imdb_count['Unnamed: 0']
del tva_film_imdb_visit['Unnamed: 0']
del tva_film_content_popular_bazdid['Unnamed: 0']
del tva_film_content_popular_karbaran['Unnamed: 0']
del tva_film_content_popular_minute['Unnamed: 0']
del tva_serial_count_of_genre['Unnamed: 0']
del tva_serial_visit_of_genre['Unnamed: 0']
del tva_serial_country_content_count['Unnamed: 0']
del tva_serial_country_content_visit['Unnamed: 0']
del tva_serial_year_count['Unnamed: 0']
del tva_serial_year_visit['Unnamed: 0']
del tva_serial_imdb_count['Unnamed: 0']
del tva_serial_imdb_visit['Unnamed: 0']
del tva_serial_content_popular_bazdid['Unnamed: 0']
del tva_serial_content_popular_karbaran['Unnamed: 0']
del tva_serial_content_popular_minute['Unnamed: 0']

del lenz_film_count_of_genre['Unnamed: 0']
del lenz_film_visit_of_genre['Unnamed: 0']
del lenz_film_country_content_count['Unnamed: 0']
del lenz_film_country_content_visit['Unnamed: 0']
del lenz_film_year_count['Unnamed: 0']
del lenz_film_year_visit['Unnamed: 0']
del lenz_film_imdb_count['Unnamed: 0']
del lenz_film_imdb_visit['Unnamed: 0']
del lenz_film_content_popular_bazdid['Unnamed: 0']
del lenz_film_content_popular_karbaran['Unnamed: 0']
del lenz_film_content_popular_minute['Unnamed: 0']
del lenz_serial_count_of_genre['Unnamed: 0']
del lenz_serial_visit_of_genre['Unnamed: 0']
del lenz_serial_country_content_count['Unnamed: 0']
del lenz_serial_country_content_visit['Unnamed: 0']
del lenz_serial_year_count['Unnamed: 0']
del lenz_serial_year_visit['Unnamed: 0']
del lenz_serial_imdb_count['Unnamed: 0']
del lenz_serial_imdb_visit['Unnamed: 0']
del lenz_serial_content_popular_bazdid['Unnamed: 0']
del lenz_serial_content_popular_karbaran['Unnamed: 0']
del lenz_serial_content_popular_minute['Unnamed: 0']
print("finish emit of extra columns")
print("integration of all data")
all_data=pd.concat([tva_film_count_of_genre, 
                    tva_film_visit_of_genre,
                    tva_film_country_content_count,
                    tva_film_country_content_visit,
                    tva_film_year_count,
                    tva_film_year_visit,
                    tva_film_imdb_count,
                    tva_film_imdb_visit,
                    tva_film_content_popular_bazdid,
                    tva_film_content_popular_karbaran,
                    tva_film_content_popular_minute,
                    tva_serial_count_of_genre, 
                    tva_serial_visit_of_genre,
                    tva_serial_country_content_count,
                    tva_serial_country_content_visit,
                    tva_serial_year_count,
                    tva_serial_year_visit,
                    tva_serial_imdb_count,
                    tva_serial_imdb_visit,
                    tva_serial_content_popular_bazdid,
                    tva_serial_content_popular_karbaran,
                    tva_serial_content_popular_minute,
                    lenz_film_count_of_genre, 
                    lenz_film_visit_of_genre,
                    lenz_film_country_content_count,
                    lenz_film_country_content_visit,
                    lenz_film_year_count,
                    lenz_film_year_visit,
                    lenz_film_imdb_count,
                    lenz_film_imdb_visit,
                    lenz_film_content_popular_bazdid,
                    lenz_film_content_popular_karbaran,
                    lenz_film_content_popular_minute,
                    lenz_serial_count_of_genre, 
                    lenz_serial_visit_of_genre,
                    lenz_serial_country_content_count,
                    lenz_serial_country_content_visit,
                    lenz_serial_year_count,
                    lenz_serial_year_visit,
                    lenz_serial_imdb_count,
                    lenz_serial_imdb_visit,
                    lenz_serial_content_popular_bazdid,
                    lenz_serial_content_popular_karbaran,
                    lenz_serial_content_popular_minute,], axis=1) 

all_data.to_excel('output\VOD first.xlsx')
print("END excel")

############################################################################################################
############################################################################################################
################################################ Lenz & Tva ####################################################
############################################################################################################
############################################################################################################
print("combination of lenz and tva film")
film_count_of_genre_tva=tva_film_count_of_genre.rename(columns={'tva_film_type_of_genre': 'genre', 'tva_film_count_of_genre1' : 'count'})
film_count_of_genre_lenz=lenz_film_count_of_genre.rename(columns={'lenz_film_type_of_genre': 'genre', 'lenz_film_count_of_genre1' : 'count'})
film_count_of_genre=film_count_of_genre_tva.append(film_count_of_genre_lenz)
film_count_of_genre=film_count_of_genre.groupby(['genre']).sum().reset_index()
film_count_of_genre.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

film_visit_of_genre_tva=tva_film_visit_of_genre.rename(columns={'tva_film_type_of_genre': 'genre', 'tva_film_visit_of_genre1' : 'visit'})
film_visit_of_genre_lenz=lenz_film_visit_of_genre.rename(columns={'lenz_film_type_of_genre': 'genre', 'lenz_film_visit_of_genre1' : 'visit'})
film_visit_of_genre=film_visit_of_genre_tva.append(film_visit_of_genre_lenz)
film_visit_of_genre=film_visit_of_genre.groupby(['genre']).sum().reset_index()
film_visit_of_genre.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

film_country_content_count_tva=tva_film_country_content_count.rename(columns={'tva_film_country_name1': 'country', 'tva_film_country_count1' : 'count'})
film_country_content_count_lenz=lenz_film_country_content_count.rename(columns={'lenz_film_country_name1': 'country', 'lenz_film_country_count1' : 'count'})
film_country_content_count=film_country_content_count_tva.append(film_country_content_count_lenz)
film_country_content_count=film_country_content_count.groupby(['country']).sum().reset_index()
film_country_content_count.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

film_visit_of_country_tva=tva_film_country_content_visit.rename(columns={'tva_film_country_name2': 'country', 'tva_film_country_visit1' : 'visit'})
film_visit_of_country_lenz=lenz_film_country_content_visit.rename(columns={'lenz_film_country_name2': 'country', 'lenz_film_country_visit1' : 'visit'})
film_visit_of_country=film_visit_of_country_tva.append(film_visit_of_country_lenz)
film_visit_of_country=film_visit_of_country.groupby(['country']).sum().reset_index()
film_visit_of_country.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

film_year_content_count_tva=tva_film_year_count.rename(columns={'tva_film_year': 'year', 'tva_film_year_count' : 'count'})
film_year_content_count_lenz=lenz_film_year_count.rename(columns={'lenz_film_year': 'year', 'lenz_film_year_count' : 'count'})
film_year_content_count=film_year_content_count_tva.append(film_year_content_count_lenz)
film_year_content_count=film_year_content_count.groupby(['year']).sum().reset_index()
#film_year_content_count.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

film_year_content_visit_tva=tva_film_year_visit.rename(columns={'tva_film_year': 'year', 'tva_film_year_visit' : 'visit'})
film_year_content_visit_lenz=lenz_film_year_visit.rename(columns={'lenz_film_year': 'year', 'lenz_film_year_visit' : 'visit'})
film_year_content_visit=film_year_content_visit_tva.append(film_year_content_visit_lenz)
film_year_content_visit=film_year_content_visit.groupby(['year']).sum().reset_index()
#film_year_content_visit.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

film_imdb_count=tva_film_imdb_count.append(lenz_film_imdb_count)
film_imdb_count=film_imdb_count.groupby(['limitation']).sum().reset_index()
film_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'count_of_imdb_film': [film_imdb_count.iloc[3,1],
                                        film_imdb_count.iloc[0,1],
                                        film_imdb_count.iloc[1,1],
                                        film_imdb_count.iloc[2,1],
                                        film_imdb_count.iloc[4,1]]}
film_imdb_count=pd.DataFrame(film_imdb_count, columns=['limitation', 'count_of_imdb_film'])

film_imdb_visit=tva_film_imdb_visit.append(lenz_film_imdb_visit)
film_imdb_visit=film_imdb_visit.groupby(['limitation']).sum().reset_index()
film_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'visit_of_imdb_film': [film_imdb_visit.iloc[3,1],
                                        film_imdb_visit.iloc[0,1],
                                        film_imdb_visit.iloc[1,1],
                                        film_imdb_visit.iloc[2,1],
                                        film_imdb_visit.iloc[4,1]]}
film_imdb_visit=pd.DataFrame(film_imdb_visit, columns=['limitation', 'visit_of_imdb_film'])


film_content_popular=tva_df_film.append(lenz_df_film)

film_content_popular_bazdid=[]
film_content_popular_visitnumber_bazdid=[]
film_content_popular_name_bazdid=[]
film_content_popular_name_bazdid=film_content_popular["title1"].tolist()
film_content_popular_bazdid.append(film_content_popular_name_bazdid)
film_content_popular_visitnumber_bazdid=film_content_popular["bazdid"].tolist()
film_content_popular_bazdid.append(film_content_popular_visitnumber_bazdid)
film_content_popular_bazdid_with_tva=film_content_popular_bazdid
film_content_popular_bazdid={'film_content_popular_name_bazdid' : [film_content_popular_name_bazdid[0], 
                                                           film_content_popular_name_bazdid[1], 
                                                           film_content_popular_name_bazdid[2],
                                                           film_content_popular_name_bazdid[3], 
                                                           film_content_popular_name_bazdid[4], 
                                                           film_content_popular_name_bazdid[5],
                                                           film_content_popular_name_bazdid[6], 
                                                           film_content_popular_name_bazdid[7], 
                                                           film_content_popular_name_bazdid[8],
                                                           film_content_popular_name_bazdid[9]],
                            'film_content_popular_visitnumber_bazdid' : [film_content_popular_visitnumber_bazdid[0], film_content_popular_visitnumber_bazdid[1],
                                                                  film_content_popular_visitnumber_bazdid[2], film_content_popular_visitnumber_bazdid[3],
                                                                  film_content_popular_visitnumber_bazdid[4], film_content_popular_visitnumber_bazdid[5],
                                                                  film_content_popular_visitnumber_bazdid[6], film_content_popular_visitnumber_bazdid[7],
                                                                  film_content_popular_visitnumber_bazdid[8], film_content_popular_visitnumber_bazdid[9]]}
film_content_popular_bazdid=pd.DataFrame(film_content_popular_bazdid, columns=['film_content_popular_name_bazdid' , 'film_content_popular_visitnumber_bazdid'])
film_content_popular_bazdid.sort_values('film_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

film_content_popular_karbaran=[]
film_content_popular_visitnumber_karbaran=[]
film_content_popular_name_karbaran=[]
film_content_popular_name_karbaran=film_content_popular["title1"].tolist()
film_content_popular_karbaran.append(film_content_popular_name_karbaran)
film_content_popular_visitnumber_karbaran=film_content_popular["karbaran"].tolist()
film_content_popular_karbaran.append(film_content_popular_visitnumber_karbaran)
film_content_popular_karbaran_with_tva=film_content_popular_karbaran
film_content_popular_karbaran={'film_content_popular_name_karbaran' : [film_content_popular_name_karbaran[0], 
                                                           film_content_popular_name_karbaran[1], 
                                                           film_content_popular_name_karbaran[2],
                                                           film_content_popular_name_karbaran[3], 
                                                           film_content_popular_name_karbaran[4], 
                                                           film_content_popular_name_karbaran[5],
                                                           film_content_popular_name_karbaran[6], 
                                                           film_content_popular_name_karbaran[7], 
                                                           film_content_popular_name_karbaran[8],
                                                           film_content_popular_name_karbaran[9]],
                            'film_content_popular_visitnumber_karbaran' : [film_content_popular_visitnumber_karbaran[0], film_content_popular_visitnumber_karbaran[1],
                                                                  film_content_popular_visitnumber_karbaran[2], film_content_popular_visitnumber_karbaran[3],
                                                                  film_content_popular_visitnumber_karbaran[4], film_content_popular_visitnumber_karbaran[5],
                                                                  film_content_popular_visitnumber_karbaran[6], film_content_popular_visitnumber_karbaran[7],
                                                                  film_content_popular_visitnumber_karbaran[8], film_content_popular_visitnumber_karbaran[9]]}
film_content_popular_karbaran=pd.DataFrame(film_content_popular_karbaran, columns=['film_content_popular_name_karbaran' , 'film_content_popular_visitnumber_karbaran'])
film_content_popular_karbaran.sort_values('film_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

film_content_popular_minute=[]
film_content_popular_visitnumber_minute=[]
film_content_popular_name_minute=[]
film_content_popular_name_minute=film_content_popular["title1"].tolist()
film_content_popular_minute.append(film_content_popular_name_minute)
film_content_popular_visitnumber_minute=film_content_popular["minute"].tolist()
film_content_popular_minute.append(film_content_popular_visitnumber_minute)
film_content_popular_minute_with_tva=film_content_popular_minute
film_content_popular_minute={'film_content_popular_name_minute' : [film_content_popular_name_minute[0], 
                                                           film_content_popular_name_minute[1], 
                                                           film_content_popular_name_minute[2],
                                                           film_content_popular_name_minute[3], 
                                                           film_content_popular_name_minute[4], 
                                                           film_content_popular_name_minute[5],
                                                           film_content_popular_name_minute[6], 
                                                           film_content_popular_name_minute[7], 
                                                           film_content_popular_name_minute[8],
                                                           film_content_popular_name_minute[9]],
                            'film_content_popular_visitnumber_minute' : [film_content_popular_visitnumber_minute[0], film_content_popular_visitnumber_minute[1],
                                                                  film_content_popular_visitnumber_minute[2], film_content_popular_visitnumber_minute[3],
                                                                  film_content_popular_visitnumber_minute[4], film_content_popular_visitnumber_minute[5],
                                                                  film_content_popular_visitnumber_minute[6], film_content_popular_visitnumber_minute[7],
                                                                  film_content_popular_visitnumber_minute[8], film_content_popular_visitnumber_minute[9]]}
film_content_popular_minute=pd.DataFrame(film_content_popular_minute, columns=['film_content_popular_name_minute' , 'film_content_popular_visitnumber_minute'])
film_content_popular_minute.sort_values('film_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
print("finish combination of lenz and tva film")

print("combination of lenz and tva serial")
serial_count_of_genre_tva=tva_serial_count_of_genre.rename(columns={'tva_serial_type_of_genre': 'genre', 'tva_serial_count_of_genre1' : 'count'})
serial_count_of_genre_lenz=lenz_serial_count_of_genre.rename(columns={'lenz_serial_type_of_genre': 'genre', 'lenz_serial_count_of_genre1' : 'count'})
serial_count_of_genre=serial_count_of_genre_tva.append(serial_count_of_genre_lenz)
serial_count_of_genre=serial_count_of_genre.groupby(['genre']).sum().reset_index()
serial_count_of_genre.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_visit_of_genre_tva=tva_serial_visit_of_genre.rename(columns={'tva_serial_type_of_genre': 'genre', 'tva_serial_visit_of_genre1' : 'visit'})
serial_visit_of_genre_lenz=lenz_serial_visit_of_genre.rename(columns={'lenz_serial_type_of_genre': 'genre', 'lenz_serial_visit_of_genre1' : 'visit'})
serial_visit_of_genre=serial_visit_of_genre_tva.append(serial_visit_of_genre_lenz)
serial_visit_of_genre=serial_visit_of_genre.groupby(['genre']).sum().reset_index()
serial_visit_of_genre.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_country_content_count_tva=tva_serial_country_content_count.rename(columns={'tva_serial_country_name': 'country', 'tva_serial_country_count1' : 'count'})
serial_country_content_count_lenz=lenz_serial_country_content_count.rename(columns={'lenz_serial_country_name': 'country', 'lenz_serial_country_count1' : 'count'})
serial_country_content_count=serial_country_content_count_tva.append(serial_country_content_count_lenz)
serial_country_content_count=serial_country_content_count.groupby(['country']).sum().reset_index()
serial_country_content_count.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_visit_of_country_tva=tva_serial_country_content_visit.rename(columns={'tva_serial_country_name': 'country', 'tva_serial_country_visit1' : 'visit'})
serial_visit_of_country_lenz=lenz_serial_country_content_visit.rename(columns={'lenz_serial_country_name': 'country', 'lenz_serial_country_visit1' : 'visit'})
serial_visit_of_country=serial_visit_of_country_tva.append(serial_visit_of_country_lenz)
serial_visit_of_country=serial_visit_of_country.groupby(['country']).sum().reset_index()
serial_visit_of_country.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_year_content_count_tva=tva_serial_year_count.rename(columns={'tva_serial_year': 'year', 'tva_serial_year_count' : 'count'})
serial_year_content_count_lenz=lenz_serial_year_count.rename(columns={'lenz_serial_year': 'year', 'lenz_serial_year_count' : 'count'})
serial_year_content_count=serial_year_content_count_tva.append(serial_year_content_count_lenz)
serial_year_content_count=serial_year_content_count.groupby(['year']).sum().reset_index()
#serial_year_content_count.sort_values('count', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_year_content_visit_tva=tva_serial_year_visit.rename(columns={'tva_serial_year': 'year', 'tva_serial_year_visit' : 'visit'})
serial_year_content_visit_lenz=lenz_serial_year_visit.rename(columns={'lenz_serial_year': 'year', 'lenz_serial_year_visit' : 'visit'})
serial_year_content_visit=serial_year_content_visit_tva.append(serial_year_content_visit_lenz)
serial_year_content_visit=serial_year_content_visit.groupby(['year']).sum().reset_index()
#serial_year_content_visit.sort_values('visit', axis = 0, ascending = True, inplace = True, na_position ='last')

serial_imdb_count=tva_serial_imdb_count.append(lenz_serial_imdb_count)
serial_imdb_count=serial_imdb_count.groupby(['limitation']).sum().reset_index()
serial_imdb_count={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'count_of_imdb_serial': [serial_imdb_count.iloc[3,1],
                                        serial_imdb_count.iloc[0,1],
                                        serial_imdb_count.iloc[1,1],
                                        serial_imdb_count.iloc[2,1],
                                        serial_imdb_count.iloc[4,1]]}
serial_imdb_count=pd.DataFrame(serial_imdb_count, columns=['limitation', 'count_of_imdb_serial'])

serial_imdb_visit=tva_serial_imdb_visit.append(lenz_serial_imdb_visit)
serial_imdb_visit=serial_imdb_visit.groupby(['limitation']).sum().reset_index()
serial_imdb_visit={'limitation': ['imdb<6', '6<imdb<7', '7<imdb<8', '8<imdb<9', 'imdb>9'],
                   'visit_of_imdb_serial': [serial_imdb_visit.iloc[3,1],
                                        serial_imdb_visit.iloc[0,1],
                                        serial_imdb_visit.iloc[1,1],
                                        serial_imdb_visit.iloc[2,1],
                                        serial_imdb_visit.iloc[4,1]]}
serial_imdb_visit=pd.DataFrame(serial_imdb_visit, columns=['limitation', 'visit_of_imdb_serial'])

serial_content_popular=tva_df_serial.append(lenz_df_serial)

serial_content_popular_bazdid=[]
serial_content_popular_visitnumber_bazdid=[]
serial_content_popular_name_bazdid=[]
serial_content_popular_name_bazdid=serial_content_popular["title1"].tolist()
serial_content_popular_bazdid.append(serial_content_popular_name_bazdid)
serial_content_popular_visitnumber_bazdid=serial_content_popular["bazdid"].tolist()
serial_content_popular_bazdid.append(serial_content_popular_visitnumber_bazdid)
serial_content_popular_bazdid_with_tva=serial_content_popular_bazdid
serial_content_popular_bazdid={'serial_content_popular_name_bazdid' : [serial_content_popular_name_bazdid[0], 
                                                           serial_content_popular_name_bazdid[1], 
                                                           serial_content_popular_name_bazdid[2],
                                                           serial_content_popular_name_bazdid[3], 
                                                           serial_content_popular_name_bazdid[4], 
                                                           serial_content_popular_name_bazdid[5],
                                                           serial_content_popular_name_bazdid[6], 
                                                           serial_content_popular_name_bazdid[7], 
                                                           serial_content_popular_name_bazdid[8],
                                                           serial_content_popular_name_bazdid[9]],
                            'serial_content_popular_visitnumber_bazdid' : [serial_content_popular_visitnumber_bazdid[0], serial_content_popular_visitnumber_bazdid[1],
                                                                  serial_content_popular_visitnumber_bazdid[2], serial_content_popular_visitnumber_bazdid[3],
                                                                  serial_content_popular_visitnumber_bazdid[4], serial_content_popular_visitnumber_bazdid[5],
                                                                  serial_content_popular_visitnumber_bazdid[6], serial_content_popular_visitnumber_bazdid[7],
                                                                  serial_content_popular_visitnumber_bazdid[8], serial_content_popular_visitnumber_bazdid[9]]}
serial_content_popular_bazdid=pd.DataFrame(serial_content_popular_bazdid, columns=['serial_content_popular_name_bazdid' , 'serial_content_popular_visitnumber_bazdid'])
serial_content_popular_bazdid.sort_values('serial_content_popular_visitnumber_bazdid', axis = 0, ascending = False, inplace = True, na_position ='last')

serial_content_popular_karbaran=[]
serial_content_popular_visitnumber_karbaran=[]
serial_content_popular_name_karbaran=[]
serial_content_popular_name_karbaran=serial_content_popular["title1"].tolist()
serial_content_popular_karbaran.append(serial_content_popular_name_karbaran)
serial_content_popular_visitnumber_karbaran=serial_content_popular["karbaran"].tolist()
serial_content_popular_karbaran.append(serial_content_popular_visitnumber_karbaran)
serial_content_popular_karbaran_with_tva=serial_content_popular_karbaran
serial_content_popular_karbaran={'serial_content_popular_name_karbaran' : [serial_content_popular_name_karbaran[0], 
                                                           serial_content_popular_name_karbaran[1], 
                                                           serial_content_popular_name_karbaran[2],
                                                           serial_content_popular_name_karbaran[3], 
                                                           serial_content_popular_name_karbaran[4], 
                                                           serial_content_popular_name_karbaran[5],
                                                           serial_content_popular_name_karbaran[6], 
                                                           serial_content_popular_name_karbaran[7], 
                                                           serial_content_popular_name_karbaran[8],
                                                           serial_content_popular_name_karbaran[9]],
                            'serial_content_popular_visitnumber_karbaran' : [serial_content_popular_visitnumber_karbaran[0], serial_content_popular_visitnumber_karbaran[1],
                                                                  serial_content_popular_visitnumber_karbaran[2], serial_content_popular_visitnumber_karbaran[3],
                                                                  serial_content_popular_visitnumber_karbaran[4], serial_content_popular_visitnumber_karbaran[5],
                                                                  serial_content_popular_visitnumber_karbaran[6], serial_content_popular_visitnumber_karbaran[7],
                                                                  serial_content_popular_visitnumber_karbaran[8], serial_content_popular_visitnumber_karbaran[9]]}
serial_content_popular_karbaran=pd.DataFrame(serial_content_popular_karbaran, columns=['serial_content_popular_name_karbaran' , 'serial_content_popular_visitnumber_karbaran'])
serial_content_popular_karbaran.sort_values('serial_content_popular_visitnumber_karbaran', axis = 0, ascending = False, inplace = True, na_position ='last')

serial_content_popular_minute=[]
serial_content_popular_visitnumber_minute=[]
serial_content_popular_name_minute=[]
serial_content_popular_name_minute=serial_content_popular["title1"].tolist()
serial_content_popular_minute.append(serial_content_popular_name_minute)
serial_content_popular_visitnumber_minute=serial_content_popular["minute"].tolist()
serial_content_popular_minute.append(serial_content_popular_visitnumber_minute)
serial_content_popular_minute_with_tva=serial_content_popular_minute
serial_content_popular_minute={'serial_content_popular_name_minute' : [serial_content_popular_name_minute[0], 
                                                           serial_content_popular_name_minute[1], 
                                                           serial_content_popular_name_minute[2],
                                                           serial_content_popular_name_minute[3], 
                                                           serial_content_popular_name_minute[4], 
                                                           serial_content_popular_name_minute[5],
                                                           serial_content_popular_name_minute[6], 
                                                           serial_content_popular_name_minute[7], 
                                                           serial_content_popular_name_minute[8],
                                                           serial_content_popular_name_minute[9]],
                            'serial_content_popular_visitnumber_minute' : [serial_content_popular_visitnumber_minute[0], serial_content_popular_visitnumber_minute[1],
                                                                  serial_content_popular_visitnumber_minute[2], serial_content_popular_visitnumber_minute[3],
                                                                  serial_content_popular_visitnumber_minute[4], serial_content_popular_visitnumber_minute[5],
                                                                  serial_content_popular_visitnumber_minute[6], serial_content_popular_visitnumber_minute[7],
                                                                  serial_content_popular_visitnumber_minute[8], serial_content_popular_visitnumber_minute[9]]}
serial_content_popular_minute=pd.DataFrame(serial_content_popular_minute, columns=['serial_content_popular_name_minute' , 'serial_content_popular_visitnumber_minute'])
serial_content_popular_minute.sort_values('serial_content_popular_visitnumber_minute', axis = 0, ascending = False, inplace = True, na_position ='last')
print("finish combination of lenz and tva serial")

print("convert to excel second")
summary_data1.to_excel('summary_data1.xlsx')
summary_data2.to_excel('summary_data2.xlsx')

film_count_of_genre.to_excel('film_count_of_genre.xlsx')
film_visit_of_genre.to_excel('film_visit_of_genre.xlsx')
film_country_content_count.to_excel('film_country_content_count.xlsx')
film_visit_of_country.to_excel('film_visit_of_country.xlsx')
film_year_content_count.to_excel('film_year_content_count.xlsx')
film_year_content_visit.to_excel('film_year_content_visit.xlsx')
film_imdb_count.to_excel('film_imdb_count.xlsx')
film_imdb_visit.to_excel('film_imdb_visit.xlsx')
film_content_popular_bazdid.to_excel('film_content_popular_bazdid.xlsx')
film_content_popular_karbaran.to_excel('film_content_popular_karbaran.xlsx')
film_content_popular_minute.to_excel('film_content_popular_minute.xlsx')

serial_count_of_genre.to_excel('serial_count_of_genre.xlsx')
serial_visit_of_genre.to_excel('serial_visit_of_genre.xlsx')
serial_country_content_count.to_excel('serial_country_content_count.xlsx')
serial_visit_of_country.to_excel('serial_visit_of_country.xlsx')
serial_year_content_count.to_excel('serial_year_content_count.xlsx')
serial_year_content_visit.to_excel('serial_year_content_visit.xlsx')
serial_imdb_count.to_excel('serial_imdb_count.xlsx')
serial_imdb_visit.to_excel('serial_imdb_visit.xlsx')
serial_content_popular_bazdid.to_excel('serial_content_popular_bazdid.xlsx')
serial_content_popular_karbaran.to_excel('serial_content_popular_karbaran.xlsx')
serial_content_popular_minute.to_excel('serial_content_popular_minute.xlsx')

summary_data1=pd.read_excel('summary_data1.xlsx')
summary_data2=pd.read_excel('summary_data2.xlsx')

film_count_of_genre=pd.read_excel('film_count_of_genre.xlsx')
film_visit_of_genre=pd.read_excel('film_visit_of_genre.xlsx')
film_country_content_count=pd.read_excel('film_country_content_count.xlsx')
film_visit_of_country=pd.read_excel('film_visit_of_country.xlsx')
film_year_content_count=pd.read_excel('film_year_content_count.xlsx')
film_year_content_visit=pd.read_excel('film_year_content_visit.xlsx')
film_imdb_count=pd.read_excel('film_imdb_count.xlsx')
film_imdb_visit=pd.read_excel('film_imdb_visit.xlsx')
film_content_popular_bazdid=pd.read_excel('film_content_popular_bazdid.xlsx')
film_content_popular_karbaran=pd.read_excel('film_content_popular_karbaran.xlsx')
film_content_popular_minute=pd.read_excel('film_content_popular_minute.xlsx')

serial_count_of_genre=pd.read_excel('serial_count_of_genre.xlsx')
serial_visit_of_genre=pd.read_excel('serial_visit_of_genre.xlsx')
serial_country_content_count=pd.read_excel('serial_country_content_count.xlsx')
serial_visit_of_country=pd.read_excel('serial_visit_of_country.xlsx')
serial_year_content_count=pd.read_excel('serial_year_content_count.xlsx')
serial_year_content_visit=pd.read_excel('serial_year_content_visit.xlsx')
serial_imdb_count=pd.read_excel('serial_imdb_count.xlsx')
serial_imdb_visit=pd.read_excel('serial_imdb_visit.xlsx')
serial_content_popular_bazdid=pd.read_excel('serial_content_popular_bazdid.xlsx')
serial_content_popular_karbaran=pd.read_excel('serial_content_popular_karbaran.xlsx')
serial_content_popular_minute=pd.read_excel('serial_content_popular_minute.xlsx')

print("end convert to excel second")
print("emit of extra columns second")
del summary_data1['Unnamed: 0']
del summary_data2['Unnamed: 0']

del film_count_of_genre['Unnamed: 0']
del film_visit_of_genre['Unnamed: 0']
del film_country_content_count['Unnamed: 0']
del film_visit_of_country['Unnamed: 0']
del film_year_content_count['Unnamed: 0']
del film_year_content_visit['Unnamed: 0']
del film_imdb_count['Unnamed: 0']
del film_imdb_visit['Unnamed: 0']
del film_content_popular_bazdid['Unnamed: 0']
del film_content_popular_karbaran['Unnamed: 0']
del film_content_popular_minute['Unnamed: 0']

del serial_count_of_genre['Unnamed: 0']
del serial_visit_of_genre['Unnamed: 0']
del serial_country_content_count['Unnamed: 0']
del serial_visit_of_country['Unnamed: 0']
del serial_year_content_count['Unnamed: 0']
del serial_year_content_visit['Unnamed: 0']
del serial_imdb_count['Unnamed: 0']
del serial_imdb_visit['Unnamed: 0']
del serial_content_popular_bazdid['Unnamed: 0']
del serial_content_popular_karbaran['Unnamed: 0']
del serial_content_popular_minute['Unnamed: 0']

print("finish emit of extra columns second")
print("integration of all data second")
all_data_second=pd.concat([summary_data1,
                           summary_data2,
                           film_count_of_genre, 
                    film_visit_of_genre,
                    film_country_content_count,
                    film_visit_of_country,
                    film_year_content_count,
                    film_year_content_visit,
                    film_imdb_count,
                    film_imdb_visit,
                    film_content_popular_bazdid,
                    film_content_popular_karbaran,
                    film_content_popular_minute,
                    serial_count_of_genre, 
                    serial_visit_of_genre,
                    serial_country_content_count,
                    serial_visit_of_country,
                    serial_year_content_count,
                    serial_year_content_visit,
                    serial_imdb_count,
                    serial_imdb_visit,
                    serial_content_popular_bazdid,
                    serial_content_popular_karbaran,
                    serial_content_popular_minute,], axis=1)
                        
all_data_second.to_excel('output\VOD second.xlsx')
print("END excel second")                    



#writer = pd.ExcelWriter('vodtva.xlsx', engine='xlsxwriter')
#lenz_all_of_data.to_excel(writer, sheet_name='لنز')
##all_sheets_data = all_data.append(lenz_film_visit_of_genre,ignore_index=True)
#tva_all_of_data.to_excel(writer, sheet_name='تیوا')
###all_of_data1.to_excel(writer, sheet_name='آیو')
#writer.save()









