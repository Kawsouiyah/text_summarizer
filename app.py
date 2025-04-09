import streamlit as st
import emoji
from summarizer import summarize


st.set_page_config(page_title="Smart Text Summarizer", page_icon=emoji.emojize(":memo:"))
st.title(emoji.emojize(":memo: Smart Text Summarizer"))
st.write(emoji.emojize(":bulb: Entrez un texte long ci-dessous, et l'application générera un résumé court et pertinent."))


text_input = st.text_area(emoji.emojize(":writing_hand: Texte à résumer"), height=300, placeholder="Collez ou écrivez votre texte ici...")

if st.button(emoji.emojize(":writing_hand: Générer le résumé")):
    if text_input.strip():
        summary = summarize(text_input)
        st.subheader(emoji.emojize(":scroll: Résumé généré"))
        for line in summary:
            st.write(emoji.emojize(":blue_heart: " + line))
    else:
        st.warning(emoji.emojize(":warning: Veuillez entrer un texte avant de générer le résumé."))
