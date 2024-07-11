# app.py

import streamlit as st
from fashion import recommend  
st.markdown("""
    <style>
        .stApp {
        background-image: url("https://www.shutterstock.com/image-illustration/clothes-on-grunge-background-shelf-600nw-1867100056.jpg");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)
# Page title
st.title('Smart Shopping: AI-Based Fashion Recommendation Engine for Modern Retail')

# Sidebar with user input
query = st.text_input('What exactly are you looking for:', " ")

# Button to trigger recommendation
if st.button('Recommend'):
    # Call recommend function
    result = recommend(query)
    
    # Display recommendation result
    st.subheader('Recommendation:')
    st.write(result)
