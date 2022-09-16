from csv import excel
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Data Penduduk',
                    layout='centered')

### --- LOAD DATAFRAME
excel_file = 'excel/Jumlah_Penduduk.xlsx'
sheet_name = 'Sheet1'
sheet_penduduk = 'penduduk'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    header=2,
                    usecols='A:K',
                    nrows=13)

df_pend = pd.read_excel(excel_file,
                    sheet_name=sheet_penduduk,
                    usecols='A:C',
                    nrows=58)

st.title('Jumlah Penduduk Kota Tangerang')



bar_laki = px.bar(df,
                    x='Kecamatan',
                    y=['2018L', '2019L', '2021L'],
                    barmode='group',
                    )

st.plotly_chart(bar_laki)

line_perempuan = px.line(df_pend,
                        x='tahun',
                        y='total penduduk',
                        symbol='Kecamatan',
                        color='Kecamatan'
                        )

st.plotly_chart(line_perempuan)

line_kota = px.line(df,
                    x='Kecamatan',
                    y=['2021L', '2021P', '2021T'],
                    labels={'variable': 'Jenis Kelamin', '2021P': 'Perempuan', 'value': 'Total penduduk'},
                    
                    )

st.plotly_chart(line_kota)
