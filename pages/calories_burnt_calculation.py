import pymysql

# Function to calculate total calories burned for a workout
def calculate_total_calories_burned(workout_id):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='VeenaUG@28',
            database='fitness_tracking',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor
        )

        with connection.cursor() as cursor:
            # Get all exercises and their durations for the given workout
            cursor.execute("SELECT ele.exercise_id, ele.duration, e.met_value, e.calories_burnt_per_minute "
                           "FROM exercise_log_exercise ele "
                           "JOIN exercises e ON ele.exercise_id = e.exercise_id "
                           "WHERE ele.workout_id = %s", (workout_id,))
            exercises_data = cursor.fetchall()

        # Calculate total calories burned based on exercise durations, MET values, and calories burned per minute
        total_calories_burned = 0
        for exercise in exercises_data:
            met_value = exercise['met_value']
            duration = exercise['duration']
            calories_burnt_per_minute = exercise['calories_burnt_per_minute']
            total_calories_burned += (calories_burnt_per_minute * duration)  # Calories burned per minute
            total_calories_burned += (met_value * duration)  # Calories burned based on MET
        return total_calories_burned

    except Exception as e:
        print(f"Error calculating total calories burned: {str(e)}")
        return None

    finally:
        connection.close()

def insert_calories_burnt(workout_id, calories):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='fitness_tracking',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor
        )

        with connection.cursor() as cursor:
            # Assuming you want to update an existing record with a specific workout_id
            update_query = "UPDATE EXERCISE_LOG SET calories_burnt = %s WHERE workout_id = %s"
            cursor.execute(update_query, (calories, workout_id))
            connection.commit()
    except Exception as e:
        print(f"Error updating calories burned: {str(e)}")
        return None
    finally:
        connection.close()
# Function to calculate total calories consumed for a meal
def calculate_total_calories_consumed(meal_id):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='fitness_tracking',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor
        )

        with connection.cursor() as cursor:
            # Get all foods and their servings for the given meal
            cursor.execute("SELECT mlf.food_id, mlf.servings_size, f.fat, f.protein, f.carbohydrates, f.calories_per_Serving "
                           "FROM meal_log_food mlf "
                           "JOIN foods f ON mlf.food_id = f.food_id "
                           "WHERE mlf.meal_id = %s", (meal_id,))
            foods_data = cursor.fetchall()

        # Calculate total calories consumed based on food servings and nutritional information
        total_calories_consumed = 0
        for food in foods_data:
            servings_size = food['servings_size']
            fat = food['fat']
            protein = food['protein']
            carbohydrates = food['carbohydrates']
            calories_per_serving = food['calories_per_Serving']

            # Calculate total calories consumed for each food
            total_calories_consumed += (calories_per_serving * servings_size)
            total_calories_consumed += (fat * 9 * servings_size)  # 9 calories per gram of fat
            total_calories_consumed += (protein * 4 * servings_size)  # 4 calories per gram of protein
            total_calories_consumed += (carbohydrates * 4 * servings_size)  # 4 calories per gram of carbohydrates

        return total_calories_consumed

    except Exception as e:
        print(f"Error calculating total calories consumed: {str(e)}")
        return None

    finally:
        connection.close()

# Function to log foods for a meal
def insert_calories_consumed(meal_id,k):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='fitness_tracking',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor
        )
        # Calculate total calories consumed for the meal
        # Update the calories_consumed column in the meals table
        with connection.cursor() as cursor:
            cursor.execute("UPDATE meals SET calories_consumed = %s WHERE meal_id = %s",
                           (k, meal_id))
            connection.commit()
    except Exception as e:
        print(f"Error logging food: {str(e)}")

    finally:
        connection.close()


# Example usage
