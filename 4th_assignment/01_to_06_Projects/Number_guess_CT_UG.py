import streamlit as st # type: ignore
import random

st.title("🎲 Number Guessing Game (1 to 3)")

# Store the random number only once using session_state
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 3)

# User input
user_input = st.number_input("Input Your Number", min_value=1, max_value=3, step=1)

# Check the guess
if st.button("Check the Number"):
    if user_input < st.session_state.random_number:
        st.warning("Too low! Try a little bigger number. 📈")
    elif user_input > st.session_state.random_number:
        st.warning("Too high! Try a little smaller number. 📉")
    else:
        st.success("🎉 Congratulations! You guessed the right number.")
        # Reset for a new game
        st.session_state.random_number = random.randint(1, 3)
       