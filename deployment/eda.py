# import library
import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image

def run():
    # Set Title
    st.title('BRAIN MRI VISUALIZATION')

    # memasukkan gambar
    st.image ('https://cdn.systematic.com/media/g0sj1tbg/hospital-building-001-global.jpg?mode=crop&width=1200&height=630&center=')

    # menampilkan EDA
    st.markdown('## Exploratory Data Analysis (EDA)')
    st.markdown ('---')
 
 
    # EDA 1
    st.markdown("<h3 style='text-align: center;'>Gambar MRI</h3>", unsafe_allow_html=True)

    image = Image.open('EDA3.png')
    st.image(image)
    
    st.write('---')


    # EDA 2
    st.markdown("<h3 style='text-align: center;'>Distribusi Data Train</h3>", unsafe_allow_html=True)

    image = Image.open('EDA1.png')
    st.image(image)

    st.write('---')

    # EDA 3
    st.markdown("<h3 style='text-align: center;'>Distribusi Data Val</h3>", unsafe_allow_html=True)

    image = Image.open('EDA2.png')
    st.image(image)

    st.write('---')

if __name__ == "__main__":
    run()
    