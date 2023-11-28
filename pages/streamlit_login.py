import streamlit as st
from pages.auth import authenticate_user,check_user_exists ,get_user_info
def login(username, password):
    user_exists = check_user_exists(username)
    print("this is user_id after count(*)",user_exists)
    is_authenticated = authenticate_user(username, password)
    if user_exists and is_authenticated:
        # Get the user_id from your authentication mechanism
        st.success("logged in successful")
        return username
    else:
        st.error("cannot login plz register")
        return None
