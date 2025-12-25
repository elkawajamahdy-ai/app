
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout= 'wide', page_title= 'car insurance')

html_title = """<h1 style="color:white;text-align:center;"> sales_eda </h1>"""
st.markdown(html_title, unsafe_allow_html=True)

st.title('sales_eda Project')

df = pd.read_csv('cleaned_data.csv', index_col= 0)

st.dataframe(df)

page = st.sidebar.radio('Pages', ['Univariate Analysis','Bivariate Analysis', 'Multivariate Analysis'])

if page == 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:

        st.plotly_chart(px.histogram(data_frame= df, x= col, title= col))
elif page == 'Bivariate Analysis':

    st.title('Bivariate Analysis')

    occu_freq = df.groupby('origin')['Sales_Volume'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(occu_freq, x= 'origin', y= 'Sales_Volume', title= 'Total Sales Volume by origin Season'))

    car_clm = df.groupby('season')['Sales_Volume'].sum().sort_values(ascending= False).reset_index()
    st.plotly_chart(px.bar(car_clm, x= 'season', y= 'Sales_Volume', title= 'Total Sales Volume by Season'))

    st.plotly_chart(px.box(df,x="price",y="Sales_Volume",title="Driver Sales_Volume Distribution by price"))

    st.plotly_chart(px.histogram(df,x="price",color="season",barmode="group",title="price"))


elif page == 'Multivariate Analysis' :

    st.title('Multivariate Analysis')

    df_1 = df.groupby(['season', 'terms'])["material"].count().sort_values(ascending = False).reset_index()
    st.plotly_chart(px.bar(df_1,x="terms",y="material",color="season",barmode="group",title="season and terms"))

    df_2 = df.groupby(["season", "terms"])["Sales_Volume"].count().sort_values(ascending = False).reset_index()
    st.plotly_chart(px.bar(df_2,x="season",y="Sales_Volume",color="terms",barmode="group",title="Sales Volume by Season and Terms"))
