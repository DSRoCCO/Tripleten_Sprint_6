import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Sprint 6: Prueba de Deploy desde Github y Render')

st.write('Esta aplicacion es un proyecto prueba para ver el uso de aplicacion web para mostrar algunos procesos de los cientificos de datos.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma, para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion') # crear un botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion, para el conjunto de datos de anuncios de venta de coches')
    
    # crear un grafico de dispersion  
    fig_disp = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)
    
agree = st.checkbox("Se completo el Sprint 6")

if agree:
    st.write("Great!")
