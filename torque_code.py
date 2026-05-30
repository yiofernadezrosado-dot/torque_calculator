# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:35:06 2026

@author: Yidier
"""
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora de Torque", layout="centered")

st.title("Sistema Analítico de Torque para Brazo Robótico")
st.markdown("---")

# Sección de Entradas
st.subheader("Parámetros de Entrada")

parte_pieza = st.selectbox(
    "Seleccione la articulación o parte a evaluar:",
    ("Base (Rotación Horizontal)", "Hombro (Elevación Principal)", "Codo (Articulación Secundaria)", "Muñeca (Soporte de Teléfono)")
)

col1, col2 = st.columns(2)

with col1:
    masa_g = st.number_input("Masa estimada (gramos):", min_value=1.0, value=300.0, step=10.0)
with col2:
    longitud_cm = st.number_input("Longitud desde el eje (cm):", min_value=1.0, value=25.0, step=1.0)

tipo_carga = st.radio(
    "Distribución de la masa en el sistema:",
    ("Carga puntual en el extremo (Ej. Teléfono móvil)", "Masa distribuida del eslabón (Ej. Pieza estructural)")
)

st.markdown("---")

# Lógica de Cálculo
masa_kg = masa_g / 1000.0

# Ajuste del centro de masa según el tipo de carga
if tipo_carga == "Carga puntual en el extremo (Ej. Teléfono móvil)":
    distancia_efectiva = longitud_cm
else:
    # Para una pieza estructural, se asume el centro de masa a la mitad de su longitud
    distancia_efectiva = longitud_cm / 2.0

torque_teorico = masa_kg * distancia_efectiva
factor_seguridad = 1.5
torque_requerido = torque_teorico * factor_seguridad

# Sección de Resultados
st.subheader("Resultados del Análisis")

st.info(f"Evaluación en curso para: {parte_pieza}")

col3, col4 = st.columns(2)
with col3:
    st.metric(label="Torque Estático Teórico (kg-cm)", value=f"{torque_teorico:.2f}")
with col4:
    st.metric(label="Torque de Diseño (FoS 1.5x)", value=f"{torque_requerido:.2f}")

st.markdown("---")

# Clasificación y Recomendaciones
st.subheader("Recomendación de Componentes")

if torque_requerido <= 2.5:
    st.success("Clasificación: Carga Ligera. Se recomienda la integración de un micro servo (Ej. SG90).")
elif torque_requerido <= 11.0:
    st.success("Clasificación: Carga Media. Se recomienda la integración de un servo estándar con engranajes metálicos (Ej. MG996R).")
elif torque_requerido <= 25.0:
    st.warning("Clasificación: Carga Alta. Se requiere un servo de alto torque (Ej. DS3218).")
else:
    st.error("Clasificación: Carga Crítica. El torque excede los parámetros estándar. Se recomienda implementar un motor paso a paso con reducción o rediseñar la longitud del eslabón.")
