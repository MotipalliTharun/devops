from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
st.title('Fashion Recommender System')
st.subheader('explore different ways to progress')
st.sidebar.title("MENU")
def about():
    st.header('aboutPage')
    st.text_input('Please tell about you')

def home():
    st.subheader("Home Page")
    data=st.file_uploader("path to file")
    st.dataframe(data)
def author():
    st.header('Authors')
    st.title('DESIGN PROJECT-3')
    st.text('NAME : M THARUN ')
    st.text('Rollno:19113092')
    st.text('mail:19113092@student.hindustanuniv.ac.in')
with st.sidebar:
    selected_page=st.selectbox(
        "Select Pages",
        ("Home","About","Author"),
    )

if selected_page =='Home':
    home()
if selected_page =='About':
    about()
if selected_page =='Author':
     author()