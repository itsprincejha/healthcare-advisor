# Importing the required libaries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # Load the environment variables
import pandas as pd

# Set up the Gemini API key in VS Code
genai.configure(api_key = os.getenv('GOOGLE-API-KEY'))


#Streamlit Page
st.header(" 👨‍⚕️Healthcare :blue[Advisor]⚕️" , divider = "green")
input = st.text_input("Hi1! I am your Medical Expert 💊 .ASK me Anything....?")
submit = st.button("Submit")


# Create a BMI Calculator - Sidebar
st.sidebar.subheader("BMI Calculator✍️")
weight = st.sidebar.text_input("Enter your weight (in kgs):")
height = st.sidebar.text_input("Enter your height (in cms):")
# BMI = Weight /height**2
height_nums = pd.to_numeric(height)
weight_nums = pd.to_numeric(weight)
height_mts = height_nums/100
bmi = weight_nums/(height_mts**2)

# BMI Scale
notes = f'''The BMI Value can be interpreted as:
* Underweight: BMI<18.5
* Normal: BMI 18.5 - 24.9
* Overweight: BMI 25 - 29.9
* Obesity: BMI >= 30'''


if bmi:
    st.sidebar.markdown("The BMI is: ")
    st.sidebar.write(bmi)
    st.sidebar.write(notes)


# Generative AI Application

def get_response(input):
    model = genai.GenerativeModel("gemini-pro")
    if input!="":
        response = model.generate_content(input)
    else:
        st.write("Please enter Prompt!!")
    return (response.text)
    
    
if submit:
    response = get_response(input)
    st.subheader("The :orange[Response]📝 is:")
    st.write(response)

# Disclaimer
st.subheader("Disclaimer:", divider = True)
note = f'''The information provided by the Healthcare Advisor is for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read on this website.'''
st.markdown(note)
    
