import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Sprint 6: Prueba de Deploy desde Github y Render')

st.write('Esta aplicacion es un proyecto prueba para ver el uso de aplicacion web para mostrar algunos procesos de los cientificos de datos.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button_hist = st.button('Construir histograma') # crear un botón

if hist_button_hist: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma, para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_disp = st.button('Construir grafico de dispersion') # crear un botón

if hist_button_disp: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma, para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
    
    
