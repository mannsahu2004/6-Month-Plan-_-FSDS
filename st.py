#1. Import Streamlit
import streamlit as st

#2. Add a title to your app
st.title("My first streamlit app created by mann sahu")

#3. Add some text
st.write("Welcome! this app calculates the square of a number.")

#4. Create an interactive slider
st.header("Select a number")
number = st.slider("Pick a number",0,100,25) # min, max, default

#5. Calculate and display the result
st.subheader("Result")
squared_number = number*number
st.write("The square of **(number)** is **(squared_number)**.")

#py -m streamlit run st.py