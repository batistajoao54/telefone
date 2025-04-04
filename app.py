import streamlit as st
import pandas as pd

#tratando os dados para dentro do codigo
df = pd.read_csv('telefone.csv')

st.title("CONSULTA DE TELEFONE")

filtro = st.text_input("Cliente") #para filtrar os clientes
df_filtro = df.cliente.str.contains(filtro.lower()) #pegando os dados ja filtrados

df_dados = df.loc[df_filtro] #salvando os dados filtrados

nomes = df_dados['cliente'] #pegando apenas os nomes dos dados filtrados

cliente = st.selectbox('',nomes)

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

