import streamlit as st
import pandas as pd
import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib.use('Agg')

#from sklearn.linear_model import LinearRegression
from PIL import Image
from urllib.request import urlopen



pd.options.mode.chained_assignment = None  # default='warn'





# Récupération du fichier
link = 'https://raw.githubusercontent.com/KoxNoob/Datathon/master/group.cvs'
link2 = 'https://raw.githubusercontent.com/KoxNoob/Datathon/master/toto.csv'
link3 = 'https://raw.githubusercontent.com/KoxNoob/Datathon/master/predict_abst.csv'
link4 = 'https://raw.githubusercontent.com/KoxNoob/Datathon/master/predict_blanc.csv'


group_by_1 = pd.read_csv(link)
toto = pd.read_csv(link2)
pred1 = pd.read_csv(link3)
pred2 = pd.read_csv(link4)

url="https://github.com/marie-31/datathon1-wcs/blob/master/images/logo.png"

img = Image.open(urlopen(url))
img

st.sidebar.image(img, use_column_width=True)

st.markdown("<h1 style='text-align: center; color: grey;'>Save my election</h1>", unsafe_allow_html=True)

group_by_1 = group_by_1.reset_index()

vue = st.sidebar.radio(
     "Détail",
     ('global', 'national', 'par département', 'prédictions'), 0)


if vue == 'par département':
     dept = st.sidebar.selectbox(
          'Choisissez un département',
          group_by_1['Nom département'].unique(), 38)
if vue not in ('global', 'prédictions'):
     tour = st.sidebar.selectbox(
          'Choisissez un tour',
          group_by_1['N° tour'].unique())
     if tour == 1:
          tour_label = '1er Tour'
     else:
          tour_label = '2e tour'

     annee = st.sidebar.selectbox(
          'Choisissez une année',
          group_by_1['Année'].unique(), 3)


if vue == 'par département':
     mask1 = group_by_1['Nom département'] == dept 
     mask2 = group_by_1['N° tour'] == tour
     mask3 = group_by_1['Année'] == annee
     mask = mask1 & mask2 & mask3

     var1 = group_by_1[mask]['Just For Fun'].unique()[0]
     var2 = group_by_1[mask]['Les Gaulois'].unique()[0]
     var3 = group_by_1[mask]['Girl Power'].unique()[0]
     var4 = group_by_1[mask]['Gotheim'].unique()[0]
     var5 = group_by_1[mask]['Boy Power'].unique()[0]

     # Pie chart
     labels = ['Les Gaulois','Girl Power','Gotheim','Boy Power' , 'Just For Fun' ]

     sizes = [var1,var2,var3,var4,var5]
     colors = ['red','lightcoral','darkorange','cornflowerblue','royalblue']

     fig1, ax1 = plt.subplots()
     
     title1 = "<h2 style='text-align: center; color: grey;'>Répartition des votes par groupe politique</h2></br><h3 style='text-align: center; color: grey;'>Département : "+dept+" </br> Année "+str(annee)+" - "+tour_label+"</h3>"
     st.markdown(title1, unsafe_allow_html=True)
     ax1 = plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
     st.pyplot(clear_figure=False)
     # Equal aspect ratio ensures that pie is drawn as a circle

     title2 = "<h2 style='text-align: center; color: grey;'>Abstention</h2></br><h3 style='text-align: center; color: grey;'>Département : "+dept+" </br> Année "+str(annee)+" - "+tour_label+"</h3>"
     st.markdown(title2, unsafe_allow_html=True)
     var1 = toto[mask]['Inscrits'].unique()[0] - toto[mask]['Votants'].unique()[0]
     var2 = toto[mask]['Inscrits'].unique()[0]
     # Pie chart
     labels = ['Abstentionnistes','Votants']
     sizes = [var1,var2]
     colors = ['mediumpurple','cadetblue']
     fig, ax2 = plt.subplots()
     ax2 = plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
     st.pyplot(clear_figure=False)
     # Equal aspect ratio ensures that pie is drawn as a circle


     title3 = "<h2 style='text-align: center; color: grey;'>Votes blancs ou nuls</h2></br><h3 style='text-align: center; color: grey;'>Département : "+dept+" </br> Année "+str(annee)+" - "+tour_label+"</h3>"
     
     st.markdown(title3, unsafe_allow_html=True)
     var1 = toto[mask]['Votants'].unique()[0] - toto[mask]['Exprimés'].unique()[0]
     var2 = toto[mask]['Votants'].unique()[0]
     # Pie chart
     labels = ['Blancs ou nuls', 'Exprimés']
     sizes = [var1,var2]
     colors = ['darkorange', 'steelblue']
     fig, ax3 = plt.subplots()
     ax3 = plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
     st.pyplot(clear_figure=False)
     

elif vue == 'national':
     title = "<h2 style='text-align: center; color: grey;'>Vainqueur départemental</h2></br><h3 style='text-align: center; color: grey;'> </br> Année "+str(annee)+" - "+tour_label+"</h3>"
     st.markdown(title, unsafe_allow_html=True)
     if (annee == 2002 and tour == 1) :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2002_1.jpeg"
          st.image(Image.open(path), caption='2002 / 1er Tour', use_column_width=True)
     elif annee == 2002 and tour == 2  :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2002_2.jpeg"
          st.image(Image.open(path), caption='2002 / 2e Tour', use_column_width=True)
     elif annee == 2007 and tour == 1:
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2007_1.jpeg"
          st.image(Image.open(path), caption='2007 / 1er Tour', use_column_width=True)
     elif annee == 2007 and tour == 2 :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2007_2.jpeg"
          st.image(Image.open(path), caption='2007 / 2e Tour', use_column_width=True)
     elif annee == 2012 and tour == 1 :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2012_1.jpeg"
          st.image(Image.open(path), caption='2012 / 1er Tour', use_column_width=True)
     elif annee == 2012 and tour == 2 :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2012_2.jpeg"
          st.image(Image.open(path), caption='2012 / 2e Tour', use_column_width=True)
     elif annee == 2017 and tour == 1  :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2017_1.jpeg"
          st.image(Image.open(path), caption='2017 / 1er Tour', use_column_width=True)
     elif annee == 2017 and tour == 2 :
          path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\2017_2.jpeg"
          st.image(Image.open(path), caption='2017 / 2e Tour', use_column_width=True)
     #st.sidebar.image(Image.open(path), caption='2017 / 2e Tour', use_column_width=True)
elif vue == 'prédictions':  
     pred1.set_index('Année', inplace=True)
     pred2.set_index('Année', inplace=True)
     pred1.columns = pred2.columns =(['1er Tour', '2e Tour'])
     

     def highlight_pred(value):
          color = "orange" if (value == 20.5 or value == 27.4 or value == 2) else "white"
          return "background-color: %s" % color

     title1 = "<h2 style='text-align: center; color: grey;'>Taux d'abstention national, réels et prédictions (en %)</h2>"
     st.markdown(title1, unsafe_allow_html=True)
     st.table(pred1.style.applymap(highlight_pred))
     title1 = "<h2 style='text-align: center; color: grey;'>Votes blancs ou nuls, réels et prédictions (en %)</h2>"
     st.markdown(title1, unsafe_allow_html=True)
     st.table(pred2.style.applymap(highlight_pred))

else:
     from PIL import Image
     title1 = "<h2 style='text-align: center; color: grey;'>Taux d'abstention national</h2>"
     
     st.markdown(title1, unsafe_allow_html=True)
     path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\abstention.png"
     st.image(Image.open(path), use_column_width=True)
     
     title2 = "<h2 style='text-align: center; color: grey;'></br></br>Votes blancs ou nuls</h2>"
     st.markdown(title2, unsafe_allow_html=True)
     path="C:\\Users\\marie\\OneDrive\\Documents\\GitHub\\hackaton1_WCS_app\\images\\blanc.png"
     st.image(Image.open(path), use_column_width=True)
