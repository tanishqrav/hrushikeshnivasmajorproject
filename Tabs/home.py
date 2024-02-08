"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Chronic Kidney Disease Predictor")
    st.image("images/chronicimage.png")



    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Chronic Kidney Disease is a condition in which the kidneys are damaged and cannot filter blood as well as they should.
        </p>
    """, unsafe_allow_html=True)
