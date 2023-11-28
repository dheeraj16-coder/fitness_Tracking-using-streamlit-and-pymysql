import pymysql


# Connect to the MySQL database
def connect_to_database():
    try:
        # Replace the following with your MySQL server credentials
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="fitness_tracking"
        )
        return connection
    except pymysql.Error as error:
        print("Error: {}".format(error))
        return None

# Function to get food data from the database
def get_food_data():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM foods")
                food_data = cursor.fetchall()
                return food_data
        except pymysql.Error as error:
            print("Error: {}".format(error))
        finally:
            connection.close()
    return []

# Function to get detailed food information based on food_id
def get_food_info(food_id):
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM foods WHERE food_id = %s", (food_id,))
                food_info = cursor.fetchone()
                return food_info
        except pymysql.Error as error:
            print("Error: {}".format(error))
        finally:
            connection.close()
    return None

# Function to get exercise data from the database
def get_exercise_data():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM exercises")
                exercise_data = cursor.fetchall()
                return exercise_data
        except pymysql.Error as error:
            print("Error: {}".format(error))
        finally:
            connection.close()
    return []
def get_exercise_info(exercise_id):
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM exercises WHERE exercise_id  = %s", (exercise_id,))
                food_info = cursor.fetchone()
                return food_info
        except pymysql.Error as error:
            print("Error: {}".format(error))
        finally:
            connection.close()
    return None

