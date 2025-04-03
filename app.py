import streamlit as st
import pandas as pd

#tratando os dados para dentro do codigo
df = pd.read_csv('telefone.csv')
nome = df['cliente']

st.title("CONSULTA DE TELEFONE")

cliente = st.selectbox('',nome)

df_busca = df[df['cliente'] == cliente].copy()
lista_id = list(df_busca['id'])
lista_cliente = list(df_busca['cliente'])
lista_telefone = list(df_busca['telefone'])
lista_cidade = list(df_busca['cidade'])
lista_estado = list(df_busca['estado'])


st.write(f'ID: {lista_id[0]}')
st.header(f'CLIENTE: {lista_cliente[0]}')
st.header(f'TELEFONE: {lista_telefone[0]}')
st.header(f'CIDADE: {lista_cidade[0]}')
st.write(f'ESTADO: {lista_estado[0]}')

cheq = st.checkbox("VER TODA A LISTA")

if cheq == True:
    st.write(df)

