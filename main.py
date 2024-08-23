import streamlit as st

res = st.selectbox('Выбирай мудро',options=['.Банк', 'Y', 'ITPR'])

match res:
    case '.Банк':
        st.image("img/H.png")
    case 'Y':
        st.image("img/Y.jpeg")
    case 'ITPR':
        st.image("img/True.jpg")
