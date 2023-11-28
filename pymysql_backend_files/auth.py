import pymysql
import hashlib
import os

# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='', database='fitness_tracking')

def hash_password(password):
    salt = os.urandom(16)


    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


    return salt + hashed_password


def check_user_exists(user_id):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users WHERE user_id = %s", (user_id,))
            user_exists = cur.fetchone()[0]
            print(user_exists)
        return user_exists
    except Exception as e:
        print(f"Error: {e}")
        return None


def authenticate_user(user_id, password):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT password FROM users WHERE user_id = %s", (user_id,))
            stored_password_with_salt = cur.fetchone()[0]

        
        stored_salt = stored_password_with_salt[:16]

        
        hashed_input_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)

        
        if stored_password_with_salt == stored_salt + hashed_input_password:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def register_user(name, age, height, weight, gender, password, activity_level):
    try:
        password = hash_password(password)
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, age, height, weight, gender, password, activity_level) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, age, height, weight, gender, password, activity_level)
            )
            cur.execute("Select user_id from users where name=%s",(name,))
            conn.commit()
            username_id=cur.fetchone()[0]
            return username_id
    except Exception as e:
        print(f"Error: {e}")
        return 0

def update_user_info(user_id, field_name, new_value):
    try:
        with conn.cursor() as cur:
         update_query = f"UPDATE users SET {field_name}=%s WHERE user_id=%s"
         cur.execute(update_query, (new_value, user_id))
        
        conn.commit()
        
        return True
    except Exception as e:
        print(f"Error updating user info: {str(e)}")
        return False
    
def get_user_info(user_id):
    try:
         with conn.cursor() as cur:
             cur.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
             user_info = cur.fetchone()
             if user_info:
              user_data = {
                 "user_id": user_info[0],
                 "age": user_info[1],
                 "height": user_info[2],
                 "weight": user_info[3],
                 "gender": user_info[4],
                 "password": user_info[5],
                 "name": user_info[6],
                 "activity_level": user_info[7]
              }
              return user_data
             else:
              return None
    except Exception as e:
        print(f"Error fetching user info: {str(e)}")
        return None

        
