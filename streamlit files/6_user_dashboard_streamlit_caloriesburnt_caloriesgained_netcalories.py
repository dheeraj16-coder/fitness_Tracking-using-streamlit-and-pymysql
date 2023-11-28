import streamlit as st
import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pages.streamlit_login import login

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "fitness_tracking",
}

# Create a Streamlit app
st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="💪",
    layout="wide",  # To make the layout wider
)
# ... (your previous code)
def get_user_data(user_id, connection):
    query = "SELECT name, age, height, weight FROM users WHERE user_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
    return user_data

# Function to get exercise data for a user
def get_exercise_data(user_id, connection):
    query = "SELECT date, calories_burnt FROM exercise_log WHERE user_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        exercise_data = cursor.fetchall()
    return exercise_data

def get_food_data(user_id, connection):
    query = "SELECT date, calories_consumed FROM meals WHERE user_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (user_id,))
        food_data = cursor.fetchall()
    return food_data

connection = pymysql.connect(**db_config)

if 'user' not in st.session_state:
    st.session_state.user = None
st.subheader("User Login")
user_id = st.number_input("User ID:")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
            user_id = login(user_id, password)
            if user_id is not None:
                st.success("Logged in successfully")
                st.session_state.user = user_id  # Initialize user_id here
            else:
                st.error("User not found in the database. Please check your credentials")

if st.session_state.user:
    user_id = st.session_state.user
    user_data = get_user_data(user_id, connection)

    if user_data:
        st.subheader(f"User Information for User ID {user_id}")
        st.write(f"Name: {user_data[0]}")
        st.write(f"Age: {user_data[1]} years")
        st.write(f"Height: {user_data[2]} cm")
        st.write(f"Weight: {user_data[3]} kg")

        # Retrieve exercise data
        exercise_data = get_exercise_data(user_id, connection)
        food_data=get_food_data(user_id, connection)

        if exercise_data and food_data:
            # ... (your previous code)
            #st.subheader("Exercise Data")
            exercise_df = pd.DataFrame(exercise_data,columns=["Date", "Calories Burnt"]).groupby("Date").sum().reset_index()
            food_df = pd.DataFrame(food_data,columns=["Date", "Calories consumed"]).groupby("Date").sum().reset_index()
            #st.write(exercise_df)

            # Calculate net calories
            merged_df = pd.merge(exercise_df, food_df, on="Date", how="outer", suffixes=('_exercise', '_food'))
            merged_df["Date"] = pd.to_datetime(merged_df["Date"])

# Fill NaN values with 0 for "Calories Burnt" and "Calories consumed"
            merged_df["Calories Burnt"].fillna(0, inplace=True) 
            merged_df["Calories consumed"].fillna(0, inplace=True)

# Calculate net calories
            merged_df["Net Calories"] = merged_df["Calories consumed"] - merged_df["Calories Burnt"]
            merged_df= merged_df.groupby("Date").sum().reset_index()

            # Visualize Calories Burnt vs Date using Seaborn
            st.write(exercise_df)
            st.subheader("Calories Burnt vs Date")
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=exercise_df, x="Date", y="Calories Burnt", marker="o")
            plt.xticks(rotation=45)
            plt.xlabel("Date")
            plt.ylabel("Calories Burnt")
            st.pyplot(plt)

            # Visualize Calories Consumed vs Date using Seaborn
            st.write(food_df)
            st.subheader("Calories Consumed vs Date")
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=food_df, x="Date", y="Calories consumed", marker="o")
            plt.xticks(rotation=45)
            plt.xlabel("Date")
            plt.ylabel("Calories Consumed")
            st.pyplot(plt)

            # Visualize Net Calories vs Date using Seaborn
            st.write(merged_df)
            st.subheader("Net Calories vs Date")
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=merged_df, x="Date", y="Net Calories", marker="o")
            plt.xticks(rotation=45)
            plt.xlabel("Date")
            plt.ylabel("Net Calories")
            st.pyplot(plt)

            # Calendar Heatmap using Seaborn
            st.subheader("Calendar Heatmap")
            calendar_heatmap_df = merged_df[["Date", "Net Calories"]].copy()
            calendar_heatmap_df["Date"] = pd.to_datetime(calendar_heatmap_df["Date"])
            calendar_heatmap_df.set_index("Date", inplace=True)
            calendar_heatmap = sns.heatmap(calendar_heatmap_df.resample("D").sum().fillna(0),
                                           cmap="YlGnBu", annot=True, fmt="g")
            st.pyplot(calendar_heatmap.get_figure())

        else:
            st.warning("No exercise data found or food data found for the user.")
    else:
        st.warning("User not found. Please enter a valid User ID.")
else:
    st.warning("Please enter a User ID.")

# Close the database connection
connection.close()
