import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nascimento, tipo):
    if nome and data_nascimento <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
                  file.write(f"{nome},{data_nascimento},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"]  = False

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="📗"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite seu nome:",
                     key="nome_cliente")

data_nascimento = st.date_input("Digite a Data de Nascimento",
                        format="DD/MM/YYYY")

tipo = st.selectbox("Selecione o tipo do Cliente:",
                    ["Pessoa Jurídica", "Pessoa Física"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome, data_nascimento, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente Cadastrado com Sucesso!", icon="✅")
    else:
        st.error("Houve um erro ao Cadastrar!!", icon="❌")
