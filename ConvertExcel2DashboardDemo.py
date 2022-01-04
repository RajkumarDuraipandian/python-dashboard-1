from re import template
from _plotly_utils.basevalidators import TitleValidator
from sklearn.preprocessing import Normalizer
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config (page_title= "GCS_OnPrem_TCC_InfraMetrics",
                    page_icon=":bar_chart:"
                    )

st.header('TCC Infra Metrics')
st.subheader ('Visualizing Excel TCC Infra metrics using Python - Streamlit')


csv_file = 'https://github.com/RajkumarDuraipandian/python-dashboard-1/blob/89950e0b8912e5ad964f94ee28972fdff4bbf430/TCC_InfraMetrics_DemoOne1.csv?raw=true'
#sheet_name = 'TCC_InfraMetrics_DemoOne'

df = pd.read_csv (csv_file)   

st.dataframe(df)
df1 = pd.read_csv (csv_file)  

bar_chart = px.funnel(df1,x='Resources', y=['5-Oct', '6-Oct','7-Oct','8-Oct'], title='Four days TCC infra Metrics')
st.plotly_chart(bar_chart)