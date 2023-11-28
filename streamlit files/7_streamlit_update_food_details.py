import streamlit as st
import pymysql

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "fitness_tracking",
}

# Create a Streamlit app
st.title("Meal Tracker")

# Function to update meal details
def update_meal_foods(meal_id, food_id, new_serving_size, connection,new_food_id):
    update_query = "UPDATE meal_log_food SET food_id=%s,servings_size = %s WHERE meal_id = %s AND food_id = %s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(update_query, (new_food_id,new_serving_size, meal_id, food_id))
            connection.commit()
            return True
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        connection.rollback()
        return False

# Function to get meals for a particular user
def get_user_meals(user_id, connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT meal_id, meal_type, date FROM meals WHERE user_id = %s"
            cursor.execute(select_query, (user_id,))
            user_meals = cursor.fetchall()
            return user_meals
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to get foods for a particular meal
def get_meal_foods(meal_id, connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT f.food_id, f.food_name, mlf.servings_size FROM foods f JOIN meal_log_food mlf ON f.food_id = mlf.food_id WHERE mlf.meal_id = %s"
            cursor.execute(select_query, (meal_id,))
            meal_foods = cursor.fetchall()
            return meal_foods
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

# Function to get all foods for dropdown selection
def get_all_foods(connection):
    try:
        with connection.cursor() as cursor:
            select_query = "SELECT food_id, food_name FROM foods"
            cursor.execute(select_query)
            foods = cursor.fetchall()
            return foods
    except pymysql.Error as err:
        st.error(f"Error: {err}")
        return []

if __name__ == "__main__":
    # Create a database connection
    connection = pymysql.connect(**db_config)

    # User interface
    st.header("Update Meal Foods")

    user_id_options = st.number_input("Enter User ID:")

    user_meals = get_user_meals(user_id_options, connection)

    if user_meals:
        st.write(f"Meals for the Selected User:")
        for meal in user_meals:
            st.write(f"Meal ID: {meal[0]}, Meal Type: {meal[1]}, Date: {meal[2]}")

        st.header("Update or Add Foods for a Meal")

        meal_id_options = [meal[0] for meal in user_meals]
        selected_meal_id = st.selectbox("Select Meal to Update", meal_id_options + ["Add New Meal"], index=0)

        # If the user wants to add a new meal
        
            # If the user wants to update an existing meal
        st.write("Updating Existing Meal")

        meal_foods = get_meal_foods(selected_meal_id, connection)
        print(meal_foods)

        for food in meal_foods:
                st.write(f"Food ID: {food[0]}, Food Name: {food[1]}, Servings Size: {food[2]}")

        st.header("Update Meal")

            # Dropdown to select existing foods
        food_id_options = [food[0] for food in meal_foods]
        selected_food_id = st.selectbox("Select Food to Update", food_id_options, index=0)

            # If the user wants to add a new food
                # If the user wants to update an existing food
        st.write("Updating Existing Food")

        all_foods = get_all_foods(connection)
        food_name_mapping = {name[1]: name[0] for name in all_foods}
        selected_new_food_name = st.selectbox("Select a New Food", list(food_name_mapping.keys()), index=0)
        print("this is meal_foods",meal_foods)
        new_serving_size = st.number_input("Enter New Servings Size", value=meal_foods[0][2])

        update_button = st.button("Update Food")

        if update_button:
                    print(selected_new_food_name)
                    if selected_new_food_name in food_name_mapping:
                        selected_new_food_id = food_name_mapping[selected_new_food_name]
                        print(selected_meal_id,selected_food_id,new_serving_size)
                        success = update_meal_foods(selected_meal_id, selected_food_id, new_serving_size, connection,selected_new_food_id)
                        if success:
                            st.success("Foods for the meal updated successfully.")
                        else:
                            st.warning("Failed to update foods for the meal.")
                    else:
                        st.warning("Please select a valid new food name.")
    else:
        st.warning("No meals found for the selected user ID.")
