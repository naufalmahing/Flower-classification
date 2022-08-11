import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.header('Tes deploy model ke streamlit sebagai dasar buat integrasi model ke aplikasi')
st.text_input("Enter your name: ", key="name")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# load model
filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# show dataframe
if st.checkbox('Show dataframe'):
    df