import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='financial zico & novia',
                    page_icon='💸',
                    layout='wide')

option = st.sidebar.selectbox(label='Bulan',
                                options=['Januari', 'Februari', 'Maret', 'April', 'Mei'],
                                index=0)
### ----- LOAD DATAFRAME
excel_file = 'excel/Financial2022.xlsx'
sheet_1 = 'Novia'

df_jan = pd.read_excel(excel_file,
                        sheet_name=sheet_1,
                        header=2,
                        usecols='A:R',
                        nrows=43)

### ---- TITLE
st.title('Laporan Keuangan Tahunan zico & novia')

st.dataframe(df_jan,)

if option == 'Januari':
    st.subheader(f'Laporan {option}')
    ### BIKIN COLUMNS
    col1, col2 = st.columns(2)

    ### BAR CHART
    bar_kewajiban = px.bar(df_jan,
                            x='Kewajiban',
                            y='Pengeluaran',
                            color='Pengeluaran')
    
    col1.plotly_chart(bar_kewajiban)

    bar_makan = px.bar(df_jan,
                            x='Makan',
                            y='Pengeluaran.1',
                            color='Pengeluaran.1')
    
    col1.plotly_chart(bar_makan)