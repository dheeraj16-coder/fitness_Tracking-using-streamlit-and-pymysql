import pymysql

def connect_to_database():
    try:
        # Replace the following with your MySQL server credentials
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="VeenaUG@28",
            database="fitness_tracking"
        )
        #print("hi")
        return connection
    except pymysql.Error as error:
        print("Error: {}".format(error))
        return None
    
    
def log_exercise(user_id, workout_type, time, date):
    connection = connect_to_database()  
    if connection:
        #print("hi")
        try:
            with connection.cursor() as cursor:
                # Insert a new exercise log entry, omitting workout_id and calories_burnt
                #print("hi")
                insert_query = "INSERT INTO exercise_log (user_id, workout_type, time, date) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_query, (user_id, workout_type, time, date))
                connection.commit()

                # Retrieve the last inserted ID (workout_id)
                cursor.execute("SELECT LAST_INSERT_ID()")
                connection.commit()
                last_inserted_id = cursor.fetchone()[0]

                print(last_inserted_id)
                return last_inserted_id
        except Exception as e:
            print(f"Error logging exercise: {e}")
            return None
        
  


def log_exercise_exercise(workout_id, exercise_id, duration):
    connection = connect_to_database()
    if connection:
       try:
          with connection.cursor() as cursor:
             # Insert a new record in the exercise_log_exercise table
              print("hi")
              insert_query = "INSERT INTO exercise_log_exercise (workout_id,exercise_id, duration) VALUES (%s,%s, %s)"
              cursor.execute(insert_query, (workout_id,exercise_id, duration))
              
              connection.commit()
       except Exception as e:
          print(f"Error logging exercise details: {e}")
       

def log_foods(user_id, meal_type, time, date):
    connection = connect_to_database()  # Assuming you have a function to establish a database connection

    if connection:
        try:
            with connection.cursor() as cursor:
                # Insert a new exercise log entry, omitting workout_id and calories_burnt
                insert_query = "INSERT INTO meals (user_id, meal_type, time, date) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_query, (user_id, meal_type, time, date))
                connection.commit()

                # Retrieve the last inserted ID (workout_id)
                cursor.execute("SELECT LAST_INSERT_ID()")
                connection.commit()
                last_inserted_id = cursor.fetchone()[0]

                print(last_inserted_id)
                return last_inserted_id
        except Exception as e:
            print(f"Error logging exercise: {e}")
            return None
       
       



def log_food_food(meal_id, food_id, servings):
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                # Insert a new record in the exercise_log_exercise table
                insert_query = "INSERT INTO meal_log_food (meal_id,food_id, servings_size) VALUES (%s,%s, %s)"
                cursor.execute(insert_query, (meal_id,food_id, servings))
              
                connection.commit()
        except Exception as e:
          print(f"Error logging exercise details: {e}")
          return None
       




