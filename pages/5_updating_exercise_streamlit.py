import streamlit as st
import pymysql

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "VeenaUG@28",
    "database": "fitness_tracking",
}

# Create a Streamlit app
st.title("Workout Tracker")

# Function to get a list of exercises for a workout with additional details using nested query
def get_exercises_with_details_nested(workout_id, connection):
    try:
        with connection.cursor() as cursor:
            select_query = """
                SELECT
                    ele.exercise_id,
                    e.exercise_name,
                    ele.duration,
                    (
                        SELECT ex.met_value
                        FROM exercises ex
                        WHERE ex.exercise_id = ele.exercise_id
                        LIMIT 1
                    ) AS met_value
                FROM
                    exercise_log_exercise ele
                JOIN
                    exercises e ON ele.exercise_id = e.exercise_id
                WHERE
                    ele.workout_id = %s
            """
            cursor.execute(select_query, (workout_id,))
            exercises = cursor.fetchall()
            return exercises
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to update exercise details
def update_exercise_details(workout_id, exercise_id, selected_new_exercise_id, new_duration, connection):
    update_query = "UPDATE exercise_log_exercise SET exercise_id = %s, duration = %s WHERE workout_id = %s AND exercise_id = %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(update_query, (selected_new_exercise_id, new_duration, workout_id, exercise_id))
            connection.commit()
            return True
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        connection.rollback()
        return False

# Function to get a list of workout dates for a user
def get_workout_dates(user_id, connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT DISTINCT date FROM exercise_log WHERE user_id = %s"
            cursor.execute(select_query, (user_id,))
            workout_dates = cursor.fetchall()
            return workout_dates
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to get a list of workouts for a user on a particular date
def get_workouts_for_date(user_id, selected_date, connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT workout_id FROM exercise_log WHERE user_id = %s AND date = %s"
            cursor.execute(select_query, (user_id, selected_date))
            workouts = cursor.fetchall()
            return workouts
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to get a list of exercises for a workout
def get_exercises(workout_id, connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT ele.exercise_id, e.exercise_name, ele.duration FROM exercise_log_exercise ele JOIN exercises e ON ele.exercise_id = e.exercise_id WHERE workout_id = %s"
            cursor.execute(select_query, (workout_id,))
            exercises = cursor.fetchall()
            return exercises
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to get a list of exercise names
def get_exercise_names(connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT exercise_id, exercise_name FROM exercises"
            cursor.execute(select_query)
            exercise_names = cursor.fetchall()
            return exercise_names
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

if __name__ == "__main__":
    # Create a database connection
    connection = pymysql.connect(**db_config)

    # User interface
    st.header("Select a User")

    user_id = st.number_input("Enter User ID:")

    workout_dates = get_workout_dates(user_id, connection)

    if workout_dates:
        workout_dates = [workout_date[0] for workout_date in workout_dates]
        selected_date = st.selectbox("Select a Workout Date", workout_dates, index=0)

        workouts = get_workouts_for_date(user_id, selected_date, connection)

        if workouts:
            workout_ids = [workout[0] for workout in workouts]
            selected_workout_id = st.selectbox("Select a Workout", workout_ids, index=0)

            st.header("Exercises for the Selected Workout")
            exercises = get_exercises_with_details_nested(selected_workout_id, connection)

            for exercise in exercises:
                st.write(f"Exercise ID: {exercise[0]}, Exercise: {exercise[1]}, Duration: {exercise[2]} minutes, MET Value: {exercise[3]}")

            st.header("Update Exercise")

            exercise_names = get_exercise_names(connection)
            exercise_name_mapping = {name[0]: name[1] for name in exercise_names}
            selected_new_exercise_name = st.selectbox("Select a New Exercise Name", list(exercise_name_mapping.values()), index=0)

            if len(exercises) > 0:
                selected_existing_exercise_id = st.selectbox("Select an Exercise to Update", [exercise[0] for exercise in exercises], index=0)

            new_duration = st.number_input("Enter New Duration (minutes)", value=exercises[0][2])

            update_button = st.button("Update Exercise")

            if update_button:
                if selected_new_exercise_name in exercise_name_mapping.values():
                    matching_key = [key for key, value in exercise_name_mapping.items() if value == selected_new_exercise_name]
                    selected_new_exercise_id = matching_key[0]
                    success = update_exercise_details(selected_workout_id, selected_existing_exercise_id, selected_new_exercise_id, new_duration, connection)
                    if success:
                        st.success("Exercise updated successfully.")
                    else:
                        st.warning("Failed to update exercise.")
                else:
                    st.warning("Please select a valid new exercise")

    
            connection.close()
