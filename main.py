import pandas as pd
import numpy as np
import streamlit as st
import pickle
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.pipeline import Pipeline

st.header('Tes deploy model ke streamlit sebagai dasar buat integrasi model ke aplikasi')
st.text_input("Enter your name: ", key="name")
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# load model
filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# show dataframe
if st.checkbox('Show dataframe'):
    df

# input 
st.write('Petal and sepal measurement')
sepal_length = st.slider('Sepal length', 0.0, max(df['sepal length']))
sepal_width = st.slider('Sepal width', 0.0, max(df['sepal width']))
petal_length = st.slider('Petal length', 0.0, max(df['petal length']))
petal_width = st.slider('Petal width', 0.0, max(df['petal width']))

# predict button
if st.button('Make prediction'):
    inputs = np.expand_dims([sepal_length, sepal_width, petal_length, petal_width], 0)
    result = loaded_model.predict(inputs)
    print(result)
    st.write('It\'s ' + np.squeeze(result, -1))