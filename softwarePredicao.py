# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:35:16 2022

@author: JPARSA
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title("Software de Predição")

with st.form(key="app"):
    input_tecnology = st.selectbox("Selecione a Tecnologia", ["GSM", "WCDMA", "LTE", "5G"])
    option = st.selectbox("Selecione: 1-Cidade pequena       2-Cidade grande", [1, 2])
    
    input_distance = st.number_input(label="Insira a Distância entre as Antenas: ")
    #input_distance = input_distance/1000
    input_frequency = st.number_input(label="Insira a Frequência: ")
    mb = 10**6
    #input_frequency = input_frequency*mb
    input_h1 = st.number_input(label="Insira a a Altura da Antena 1: ")
    input_h2_mobile = st.number_input(label="Insira a a Altura da Antena 2: ")
    input_button_calculate = st.form_submit_button("Calcular")
    lista = []
    
    if option==1:
        for i in range(1, int(input_distance)):
            a = (((1.1*np.log10(input_frequency))-0.7)*input_h2_mobile)-(1.56*np.log10(input_frequency)-0.8) #small to medium
            pl_urban = 69.55+(26.16*np.log10(input_frequency))-(13.82*np.log10(input_h1))-a+((44.9-(6.55*np.log10(input_h1)))*np.log10(i/1000))
            lista.append(pl_urban)
        lista = pd.DataFrame(lista, columns=['cidade_pequena'])
            
    if option==2 and input_frequency>=300:
        for i in range(1, int(input_distance)):
            a = (3.2*(np.log10(11.75*input_h2_mobile)**2))-4.97 #large city
            #pl_urban =  69.55 + (26.16*np.log10(input_frequency))-(13.82*np.log10(input_h1))- a + ((44.9-(6.55*np.log10(input_h2_mobile)))*np.log10(input_distance))
            pl_urban = 69.55 + (26.16*np.log10(input_frequency))-(13.82*np.log10(input_h1)) - a +((44.9-(6.55*np.log10(input_h1)))*np.log10(i/1000))
            lista.append(pl_urban)
        lista = pd.DataFrame(lista, columns=['cidade_grande'])
            
    if option==2 and input_frequency <=300:
        a = (8.29*(np.log10(1.54*input_h2_mobile)**2))-1.1 #large city
        pl_urban = 69.55 + (26.16*np.log10(input_frequency))-(13.82*np.log10(input_h1)) - a +((44.9-(6.55*np.log10(input_h1)))*np.log10(i/1000))
        lista.append(pl_urban)
        lista = pd.DataFrame(lista, columns=['cidade_grande'])
    
if input_button_calculate:
    st.write(f'Perda: {pl_urban:,.2f}')
    st.write(f'Fator de correção a: {a:,.2f}')
    st.line_chart(lista)
   