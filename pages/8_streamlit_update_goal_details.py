import streamlit as st
import pymysql

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "fitness_tracking",  # Change to your database name
}

# Create a Streamlit app
st.set_page_config(
    page_title="Calories Target Calculator",
    page_icon="🎯",
    layout="wide",
)

# Function to calculate calories target using stored procedure
def calculate_calories_target(user_id, goal_type, end_date):
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            # Call the stored procedure
            cursor.callproc('CalculateCaloriesTarget', (user_id, goal_type, end_date))
            connection.commit()
            st.success("Calories target calculated and updated successfully!")
    except pymysql.Error as err:
        st.error(f"Error: {err}")
    finally:
        connection.close()

# Streamlit app
st.title("Calories Target Calculator")

# Input user details
user_id = st.number_input("Enter User ID:", min_value=1)
goal_type = st.selectbox("Select Goal Type:", ["Weight Loss", "Maintenance", "Muscle Gain"])
end_date = st.date_input("Select End Date:")

# Button to calculate calories target
calculate_button = st.button("Calculate Calories Target")

# When the button is clicked, call the procedure
if calculate_button:
    calculate_calories_target(user_id, goal_type, end_date)
