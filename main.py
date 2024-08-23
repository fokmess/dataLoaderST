import streamlit as st

твой_ответ = st.selectbox('Выбирай мудро',options=['1', '2', '3'])

st.write(f"{твой_ответ = }")