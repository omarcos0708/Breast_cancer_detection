import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregue seu modelo treinado (substitua isso pelo seu próprio modelo)
modelo = joblib.load('..\model\model.pkl')

st.write("""
# Aplicativo de Detecção de Câncer de Mama
""")

# Crie caixas de texto para cada recurso
radius_mean = st.number_input('Insira o valor para radius_mean', format="%.5f")
texture_mean = st.number_input('Insira o valor para texture_mean', format="%.5f")
area_mean = st.number_input('Insira o valor para area_mean', format="%.5f")
smoothness_mean = st.number_input('Insira o valor para smoothness_mean', format="%.5f")
compactness_mean = st.number_input('Insira o valor para compactness_mean', format="%.5f")
concavity_mean = st.number_input('Insira o valor para concavity_mean', format="%.5f")
symmetry_mean = st.number_input('Insira o valor para symmetry_mean', format="%.5f")
fractal_dimension_mean = st.number_input('Insira o valor para fractal_dimension_mean', format="%.5f")

# Crie um botão para fazer a previsão
if st.button('Prever'):
    # Crie um dataframe com os valores inseridos
    dados = pd.DataFrame(np.array([[radius_mean, texture_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, symmetry_mean, fractal_dimension_mean]]), columns=['radius_mean', 'texture_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'symmetry_mean', 'fractal_dimension_mean'])

    # Converter os dados para float
    dados = dados.astype('float32')
    
    # Normalizar os dados (se necessário)
    scaler = StandardScaler()
    dados_normalizados = scaler.fit_transform(dados)

    # Faça previsões com o modelo
    previsoes_proba = modelo.predict(dados)

    # Adicione as previsões de classe como uma nova coluna ao DataFrame original (não normalizado)
    dados['previsto'] = previsoes_proba

    # Mostre o dataframe atualizado
    st.write(dados)

    # Exiba uma mensagem com o resultado da previsão
    st.write(previsoes_proba)

# Adicione uma mensagem de aviso no final do aplicativo
st.write("""
## Aviso Importante

Este modelo não é 100% preciso e deve ser usado apenas por profissionais médicos como uma ferramenta auxiliar no diagnóstico precoce do câncer de mama. Sempre consulte um profissional médico para aconselhamento e tratamento médico.
""")




