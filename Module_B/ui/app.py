import requests
import streamlit as st

st.title("Научная Аннотация Статей")

st.write("Загрузите научную статью, и наша модель создаст её аннотацию.")
article_text = st.text_area("Введите текст статьи ниже:")

if st.button("Создать аннотацию"):
    if article_text:
        response = requests.post("http://localhost:8000/annotate/", json={"text": article_text})
        if response.status_code == 200:
            annotation = response.json()["annotation"]
            st.write("### Аннотация:")
            st.write(annotation)
        else:
            st.write("Произошла ошибка: ", response.status_code)
    else:
        st.write("Пожалуйста, введите текст для аннотирования.")