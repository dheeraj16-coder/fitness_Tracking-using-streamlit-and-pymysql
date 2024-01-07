import streamlit as st
import pymysql

def delete_record(record_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='VeenaUG@28',
        database='fitness_tracking'
    )

    try:
        with connection.cursor() as cursor:
            # Assuming you have a table named 'your_table' with a column 'id'
            sql = f"DELETE FROM users WHERE user_id = {record_id}"
            cursor.execute(sql)
            connection.commit()
            st.success(f"Record with ID {record_id} deleted successfully.")

            # Clear cached user information
            print("the value of st.session_state.user","and","value of record_id","is",st.session_state.user,"and",record_id,"respectively")
            if st.session_state.user == record_id:
                st.session_state.user = None
                st.success("Record deleted. Cache cleared.")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        connection.close()

def main():
    st.title("Streamlit Delete Program")

    # Get user input for record ID to delete
    record_id = st.number_input("Enter the ID of the record to delete:", min_value=1, step=1)

    # Checkbox for confirmation
    confirmation = st.checkbox("I confirm that I want to delete this record")

    # Button to trigger record deletion
    delete_button = st.button("Delete Record")

    dummy_trigger = st.empty()

    if delete_button and confirmation:
        delete_record(record_id)


if __name__ == "__main__":
    main()
