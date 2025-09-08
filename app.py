import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

# Validar que los datos existen y tienen las columnas necesarias
if 'car_data' in locals() and not car_data.empty and {'odometer', 'price', 'model'}.issubset(car_data.columns):

    # Casilla para mostrar histograma de odómetro
    show_histogram = st.checkbox('Mostrar histograma de odómetro')

    if show_histogram:
        st.subheader('Distribución del Odómetro')
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        fig_odometer = go.Figure()
        fig_odometer.add_trace(go.Histogram(
            x=car_data['odometer'],
            nbinsx=30,
            marker_color='teal',
            opacity=0.75
        ))
        fig_odometer.update_layout(
            title='Distribución del Odómetro',
            xaxis_title='Kilometraje',
            yaxis_title='Frecuencia',
            bargap=0.1,
            template='plotly_white'
        )
        st.plotly_chart(fig_odometer, use_container_width=True)

    # Casilla para mostrar gráfico de dispersión de precios por modelo
    show_scatter = st.checkbox('Mostrar gráfico de dispersión de precios por modelo')

    if show_scatter:
        st.subheader('Relación entre Precio y Modelo')
        st.write('Visualización de cómo varía el precio según el modelo de coche')

        fig_scatter = px.scatter(
            car_data,
            x='model',
            y='price',
            color='model',
            title='Precio vs. Modelo de Coche',
            labels={'model': 'Modelo', 'price': 'Precio'},
            hover_data=['odometer'],
            opacity=0.7
        )
        fig_scatter.update_layout(
            xaxis_title='Modelo',
            yaxis_title='Precio',
            template='plotly_white'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

else:
    st.warning("Los datos necesarios no están disponibles o están incompletos.")sponibles o están incompletos.")
