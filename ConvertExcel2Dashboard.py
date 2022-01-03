from _plotly_utils.basevalidators import TitleValidator
from sklearn.preprocessing import Normalizer
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


st.set_page_config(page_title='TCC Infra Metrics')
st.header('TCC Infra Metrics')
st.subheader ('Visualizing Excel TCC Infra metrics using Python - Streamlit')

### --- Load Dataframe

#csv_file = 'TCC_InfraMetrics_DemoOne.csv'
csv_file = 'https://github.com/RajkumarDuraipandian/python-dashboard-1/blob/89950e0b8912e5ad964f94ee28972fdff4bbf430/TCC_InfraMetrics_DemoOne1.csv?raw=true'
#sheet_name = 'TCC_InfraMetrics_DemoOne'

df = pd.read_csv (csv_file)                  

st.dataframe(df)

df1 = pd.read_csv (csv_file)
pie_chart = px.strip(df1,
                   title= 'TCC Infra data from CCSI')

st.plotly_chart (pie_chart)

df1 = pd.read_csv (csv_file)
pie_chart = px.bar(df1,
                   title= 'TCC Infra data from CCSI')

st.plotly_chart (pie_chart)

df1 = pd.read_csv (csv_file)
pie_chart = px.scatter_matrix(df1,
                   title= 'TCC Infra data from CCSI')

st.plotly_chart (pie_chart)

df1 = pd.read_csv (csv_file)
pie_chart = px.funnel(df1,
                   title= 'TCC Infra data from CCSI')

st.plotly_chart (pie_chart)

#fig = px.box(df1,
#                   title= 'TCC Infra data from CCSI',)
#fig.show()


#excel_file = 'TCC_InfraMetrics_DemoOne.xlsx'
#sheet_name = 'Sheet1'

#df = pd.read_excel( excel_file,
 #                   sheet_name=sheet_name,
  #                  usecols= 'A:E',
   #                 header = 1)                
#st.dataframe(df)
