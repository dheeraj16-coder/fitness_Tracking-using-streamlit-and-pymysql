import streamlit as st
from pages.auth import register_user, authenticate_user

def register(username, password, age, height, weight, gender, activity_level):
    user_id = register_user(username, age, height, weight, gender, password, activity_level)
    if user_id!=0:
        st.success(f'Registration successful! Your user ID is: {user_id}')
    else:
        st.error('Registration failed.')

def main():
    st.title("Login and Registration")
    st.subheader("Registration")
    reg_username = st.text_input("Enter Username")
    reg_password = st.text_input("Enter Password", type="password")
    reg_age = st.text_input("Enter age")
    reg_weight = st.text_input("Enter weight in kg")
    reg_height = st.text_input("Enter height in cm")
    reg_activity_level = st.selectbox("Select activity level", ["active", "medium active", "sedentary"])
    reg_gender = st.selectbox("Select Gender", ["Male", "Female"])
    register_button = st.button("Register")

    if register_button:
            if not reg_username or not reg_password or not reg_age or not reg_weight or not reg_height or not reg_activity_level or not reg_gender:
                st.warning("Please provide all registration details.")
            else:
                k=register(reg_username, reg_password, reg_age, reg_height, reg_weight, reg_gender, reg_activity_level)
                st.write("your user_id is",k)
if __name__ == "__main__":
    main()
