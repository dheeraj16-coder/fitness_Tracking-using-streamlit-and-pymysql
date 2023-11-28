import streamlit as st
from pages.auth import get_user_info, update_user_info
from pages.streamlit_login import login

# Initialize session state
if 'user' not in st.session_state:
    print("hi")
    st.session_state.user = None
def main():
    st.title("User Profile")

    if st.session_state.user is None:
        # User Login
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        login_button = st.button("user Login")

        if login_button:
            user_id = login(username, password)
            print("user_id from login",user_id)
            if user_id is not None:
                st.success("Logged in successfully")
                st.session_state.user = user_id  # Initialize user_id here
            else:
                st.error("User not found in the database. Please check your credentials")

    if st.session_state.user:
        user_id = st.session_state.user

        # You can fetch user information using user_id
        user_info = get_user_info(user_id)

        if user_info is not None:
            # Display the user's information
            st.subheader("Current User Information:")
            st.write("Username:", user_info.get("name", "N/A"),)
            st.write("Age:", user_info.get("age", "N/A"))
            st.write("Weight:", user_info.get("weight", "N/A"),"kg")
            st.write("Height:", user_info.get("height", "N/A"),"cm")
            st.write("Gender:", user_info.get("gender", "N/A"))
            st.write("Activity Level:", user_info.get("activity_level", "N/A"))

            st.subheader("Update User Information:")
            # Allow the user to update their information, and save changes to the database
            field_to_update = st.selectbox("Select a field to update", ["Age", "Weight", "Height", "Gender", "activity_level"])
            if field_to_update=="activity_level":
                activity_level_options = ["active","sedentary","medium active"]
                new_value = st.selectbox(f"New {field_to_update}",activity_level_options)
            else:
                new_value = st.text_input(f"New {field_to_update}", user_info.get(field_to_update.lower(), ""))
            update_button = st.button("Update Information")

            if update_button:
                if field_to_update and new_value:
                    # Update the selected user information field
                    update_user_info(user_id, field_to_update.lower(), new_value)
                    st.success(f"{field_to_update} updated successfully")
                else:
                    st.warning("Please provide both a field and a new value to update")
        else:
            st.error("User information not found. Please check your credentials.")

if __name__ == "__main__":
    main()