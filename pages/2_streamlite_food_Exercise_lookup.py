import streamlit as st
from pages.food_exercise_queries import get_food_data,get_exercise_data

def main():
    st.title("Food and Exercise Information")
    # Add a title for the options
    st.header("Select an Option")

    # Select food or exercise using a radio button
    option = st.radio("Choose an option:", ["Food", "Exercise"])

    # Set the default option to "Food"
    if option is None:
        option = "Food"

    st.write("")  # Add some spacing

    if option == "Food":
        st.subheader("Select a Food:")

        # Query food data from the database (replace with your actual function)
        food_data = get_food_data()
        food_data_info = [(row[0], row[1]) for row in food_data]
        selected_food_info = st.selectbox("Choose a food:", [f"{food_id} - {name}" for food_id, name in food_data_info])
        selected_food_id = int(selected_food_info.split(" - ")[0])
        selected_food = None
        for food in food_data:
            if food[0] == selected_food_id:
              selected_food = food
        if selected_food:
            st.subheader("name",selected_food[1])  # Display food name
            st.write("fat",selected_food[2],"grams") 
            st.write("protien",selected_food[3],"grams") 
            st.write("carbs",selected_food[4],"grams") 
            st.write("calories",selected_food[5],"kcal_per_serving")
            st.write("type",selected_food[6])

                 
        else:
            st.warning("Selected food not found")
    else:
        st.subheader("Select an Exercise:")
        ex_data = get_exercise_data()
        ex_data_info = [(row[0], row[1]) for row in ex_data]
        selected_ex_info = st.selectbox("Choose a exercise:", [f"{ex_id} - {name}" for ex_id, name in ex_data_info])
        selected_ex_id = int(selected_ex_info.split(" - ")[0])
        selected_ex = None
        for ex in ex_data:
            if ex[0] == selected_ex_id:
              selected_ex= ex
              

        if selected_ex:
            st.subheader("name",selected_ex[1])  # Display food name
            st.write("met",selected_ex[2]) 
            st.write("caloires_burn",selected_ex[3],"kcal_per_min") 
if __name__ == "__main__":
    main()
