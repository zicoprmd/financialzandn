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

df_feb = pd.read_excel(excel_file,
                        sheet_name=sheet_1,
                        header=70,
                        usecols='A:R',
                        nrows=53)

df_mar = pd.read_excel(excel_file,
                        sheet_name=sheet_1,
                        header=146,
                        usecols='A:R',
                        nrows=33)

df_apr = pd.read_excel(excel_file,
                        sheet_name=sheet_1,
                        header=237,
                        usecols='A:R',
                        nrows=48)


### ---- TITLE
st.title('Laporan Keuangan Tahunan zico & novia')



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

    bar_sosial = px.bar(df_jan,
                            x='Sosial',
                            y='Pengeluaran.2',
                            color='Pengeluaran.2')
    
    col1.plotly_chart(bar_sosial)
    
    bar_sedekah = px.bar(df_jan,
                            x='Sedekah',
                            y='Pengeluaran.3',
                            color='Pengeluaran.3')
    
    col2.plotly_chart(bar_sedekah)

    bar_transpot = px.bar(df_jan,
                            x='Transport',
                            y='Pengeluaran.4',
                            color='Pengeluaran.4')
    
    col2.plotly_chart(bar_transpot)

    bar_sekunder = px.bar(df_jan,
                            x='Sekunder',
                            y='Pengeluaran.5',
                            color='Pengeluaran.5')
    
    col2.plotly_chart(bar_sekunder)

    

if option == 'Februari':
    st.subheader(f'Laporan {option}')

    ### BIKIN COLUMNS
    col1, col2 = st.columns(2)

    ### BAR CHART FEBRUARI
    bar_kewajiban = px.bar(df_feb,
                            x='Kewajiban',
                            y='Pengeluaran',
                            color='Pengeluaran')
    
    col1.plotly_chart(bar_kewajiban)

    bar_makan = px.bar(df_feb,
                            x='Makan',
                            y='Pengeluaran.1',
                            color='Pengeluaran.1')
    
    col1.plotly_chart(bar_makan)

    bar_sosial = px.bar(df_feb,
                            x='Sosial',
                            y='Pengeluaran.2',
                            color='Pengeluaran.2')
    
    col1.plotly_chart(bar_sosial)
    
    bar_sedekah = px.bar(df_feb,
                            x='Sedekah',
                            y='Pengeluaran.3',
                            color='Pengeluaran.3')
    
    col2.plotly_chart(bar_sedekah)

    bar_transpot = px.bar(df_feb,
                            x='Transport',
                            y='Pengeluaran.4',
                            color='Pengeluaran.4')
    
    col2.plotly_chart(bar_transpot)

    bar_sekunder = px.bar(df_feb,
                            x='Sekunder',
                            y='Pengeluaran.5',
                            color='Pengeluaran.5')
    
    col2.plotly_chart(bar_sekunder)

if option == 'Maret':
    st.subheader(f'Laporan {option}')

    ### BIKIN COLUMNS
    col1, col2 = st.columns(2)

    ### BAR CHART FEBRUARI
    bar_kewajiban = px.bar(df_mar,
                            x='Kewajiban',
                            y='Pengeluaran',
                            color='Pengeluaran')
    
    col1.plotly_chart(bar_kewajiban)

    bar_makan = px.bar(df_mar,
                            x='Makan',
                            y='Pengeluaran.1',
                            color='Pengeluaran.1')
    
    col1.plotly_chart(bar_makan)

    bar_sosial = px.bar(df_mar,
                            x='Sosial',
                            y='Pengeluaran.2',
                            color='Pengeluaran.2')
    
    col1.plotly_chart(bar_sosial)
    
    bar_sedekah = px.bar(df_mar,
                            x='Sedekah',
                            y='Pengeluaran.3',
                            color='Pengeluaran.3')
    
    col2.plotly_chart(bar_sedekah)

    bar_transpot = px.bar(df_mar,
                            x='Transport',
                            y='Pengeluaran.4',
                            color='Pengeluaran.4')
    
    col2.plotly_chart(bar_transpot)

    bar_sekunder = px.bar(df_mar,
                            x='Sekunder',
                            y='Pengeluaran.5',
                            color='Pengeluaran.5')
    
    col2.plotly_chart(bar_sekunder)

if option == 'April':
    st.subheader(f'Laporan {option}')

    ### BIKIN COLUMNS
    col1, col2 = st.columns(2)

    ### BAR CHART FEBRUARI
    bar_kewajiban = px.bar(df_apr,
                            x='Kewajiban',
                            y='Pengeluaran',
                            color='Pengeluaran')
    
    col1.plotly_chart(bar_kewajiban)

    bar_makan = px.bar(df_apr,
                            x='Makan',
                            y='Pengeluaran.1',
                            color='Pengeluaran.1')
    
    col1.plotly_chart(bar_makan)

    bar_sosial = px.bar(df_apr,
                            x='Sosial',
                            y='Pengeluaran.2',
                            color='Pengeluaran.2')
    
    col1.plotly_chart(bar_sosial)
    
    bar_sedekah = px.bar(df_apr,
                            x='Sedekah',
                            y='Pengeluaran.3',
                            color='Pengeluaran.3')
    
    col2.plotly_chart(bar_sedekah)

    bar_transpot = px.bar(df_apr,
                            x='Transport',
                            y='Pengeluaran.4',
                            color='Pengeluaran.4')
    
    col2.plotly_chart(bar_transpot)

    bar_sekunder = px.bar(df_apr,
                            x='Sekunder',
                            y='Pengeluaran.5',
                            color='Pengeluaran.5')
    
    col2.plotly_chart(bar_sekunder)

