import datetime
import streamlit as st
from pages.food_exercise_queries import get_exercise_data,get_food_data
from pages.food_exercise_logging import log_exercise, log_exercise_exercise,log_foods,log_food_food
from pages.calories_burnt_calculation import calculate_total_calories_burned,insert_calories_burnt,calculate_total_calories_consumed,insert_calories_consumed

def log_exercises(user_id):
    st.subheader("Log Exercises")

    workout_type = st.selectbox("Workout Type", ["Intensive", "Moderate", "Simple"])
    time_options = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "13:00 PM", "14:00 PM", "15:00 PM"]
    time = st.selectbox("Select Time", time_options)
    current_date = datetime.date.today()
    date = st.date_input("Date", value=current_date)
    exercise_duration = {}

    st.subheader("Select Exercises")
    exercises = get_exercise_data()  # You should have a function to fetch exercises
    selected_exercises = st.multiselect("Select exercises to log:", [(f"{exercise[0]} - {exercise[1]}") for exercise in exercises])
    for selected_exercise in selected_exercises:
        exercise_id, exercise_name = selected_exercise.split("-")
        duration = st.number_input(f"Duration for {exercise_name} (minutes)", min_value=0)
        exercise_duration[exercise_id] = duration

    workout_data = st.session_state.get('workout_data', {'workout_id': None, 'exercise_duration': {}})
    workout_id = workout_data['workout_id']

    log_exercise_button = st.button("Log Exercise")
    log_exercise_exercise_button = st.button("Log Exercise Exercise")

    if log_exercise_button:
        if workout_type and time and date:
            # Create a new exercise log entry
            print(f"Debug: user_id={user_id}, workout_type={workout_type}, time={time}, date={date}")
            workout_id = log_exercise(user_id,workout_type,time,date)
            st.success("Exercise logged successfully")
            workout_data['workout_id'] = workout_id

    if log_exercise_exercise_button:
        if workout_id is not None and exercise_duration:
            # Log exercise details using log_exercise_exercise
            for exercise_id, duration in exercise_duration.items():
                log_exercise_exercise(workout_id, exercise_id, duration)
            st.success("Exercise details logged successfully")
            k=calculate_total_calories_burned(workout_id)
            insert_calories_burnt(workout_id,k)
        else:
            st.error("Some error: workout_id is missing or exercise_duration is empty")

    workout_data['exercise_duration'] = exercise_duration
    st.session_state.workout_data = workout_data

def log_food(user_id):

    st.subheader("Log Meals")

    meal_type = st.selectbox("meal Type", ["breakfast", "Lunch", "Dinner"])
    time_options = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "13:00 PM", "14:00 PM", "15:00 PM"]
    time = st.selectbox("Select Time", time_options)
    current_date = datetime.date.today()
    date = st.date_input("Date", value=current_date)
    food_servings = {}

    st.subheader("Select food")
    foods = get_food_data()  # You should have a function to fetch foods
    selected_foods = st.multiselect("Select foods to log:", [(f"{food[0]} - {food[1]}") for food in foods])
    for selected_food in selected_foods:
            food_id, food_name = selected_food.split("-")
            serving = st.number_input(f"serving for {food_name} (grams)", min_value=0)
            food_servings[food_id] = serving
            
    meal_data = st.session_state.get('meal_data', {'meal_id': None, 'food_servings': {}})
    meal_id = meal_data['meal_id']

    log_food_button = st.button("Log food")
    log_food_food_button = st.button("Log food food")

    if log_food_button:
        if meal_type and time and date:
            # Create a new food log entry
            print(f"Debug: user_id={user_id}, meal_type={meal_type}, time={time}, date={date}")
            meal_id = log_foods(user_id,meal_type,time,date)
            st.success("food logged successfully")
            meal_data['meal_id'] =meal_id
            print(meal_id)
    print(food_servings)
    
    if log_food_food_button:
        print(meal_id)
        if meal_id is not None and food_servings:
           for food_id, serving in food_servings.items():
                log_food_food(meal_id, food_id, serving)
                st.success("food details logged successfully")
           k=calculate_total_calories_consumed(meal_id)
           insert_calories_consumed(meal_id,k)
        else:
            st.error("Some error: meal_id is missing or food_servings is empty")
    meal_data['food_servings'] = food_servings
    st.session_state.meal_data = meal_data

if __name__ == "__main__":
    log_type=None
    user_id = st.number_input("user_id")
    
    if user_id:
        log_type = st.radio("Select log type", ["Exercise", "Food"])

    if log_type == "Exercise":
        log_exercises(user_id)
    elif log_type == "Food":
        log_food(user_id)
