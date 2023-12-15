#home page

import streamlit as st

# Set the title and subtitle
st.title("Welcome to Your Fitness Journey! 💪🏋️‍♀️")
st.write("Your one and only website to help you get in shape!")

# Custom CSS for styling
custom_css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    h1 {
        color: #4CAF50;
        font-size: 3em;
        margin-bottom: 20px;
    }

    p {
        font-size: 1.5em;
        color: #333;
        text-align: center;
        max-width: 600px;
        margin-bottom: 40px;
    }

    .created-by {
        font-size: 1.2em;
        color: #666;
        text-align: center;
        margin-top: 40px;
    }

    /* Add more styles as needed */
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Welcoming message
st.markdown(
    """
    <h1>Hello Fitness Enthusiast! 🌟</h1>
    <p>
        Whether you're just starting your fitness journey or aiming for new heights,
        this is your go-to destination for achieving your fitness goals.
        Explore workout plans, log your exercises, track your nutrition, and stay motivated
        with a community of like-minded individuals.
    </p>
    """
, unsafe_allow_html=True)

# Additional information
st.markdown(
    """
    <p class="created-by">Created by Dheeraj and Urja</p>
    """
, unsafe_allow_html=True)
