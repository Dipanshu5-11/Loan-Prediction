import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('Model1.pkl', 'rb'))

def run():

    st.title("Bank Loan Prediction using Machine Learning")

    # Add a short description of the app
    st.markdown("Welcome to the Bank Loan Prediction App! Fill in the required information below, and we will predict whether you are eligible for a loan or not.")

    # Input fields for user details
    st.header("User Details")

    account_no = st.text_input('Account number')
    fn = st.text_input('Full Name')

    # Use radio buttons for gender instead of a select box
    st.write("Gender:")
    gen_display = ('Female', 'Male')
    gen = st.radio("", gen_display)

    # Use radio buttons for Marital Status
    st.write("Marital Status:")
    mar_display = ('No', 'Yes')
    mar = st.radio("", mar_display)

    # Use radio buttons for No of dependents
    st.write("Dependents:")
    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep = st.radio("", dep_display)

    # Use radio buttons for education
    st.write("Education:")
    edu_display = ('Not Graduate', 'Graduate')
    edu = st.radio("", edu_display)

    # Use radio buttons for employment status
    st.write("Employment Status:")
    emp_display = ('Job', 'Business')
    emp = st.radio("", emp_display)

    # Use radio buttons for property area
    st.write("Property Area:")
    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop = st.radio("", prop_display)

    # Use radio buttons for credit score
    st.write("Credit Score:")
    cred_display = ('Between 300 to 500', 'Above 500')
    cred = st.radio("", cred_display)

    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)
    loan_amt = st.number_input("Loan Amount", value=0)

    # Use radio buttons for loan duration
    st.write("Loan Duration:")
    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur = st.radio("", dur_display)

    if st.button("Submit"):
        duration = 0
        if dur == '2 Month':
            duration = 60
        elif dur == '6 Month':
            duration = 180
        elif dur == '8 Month':
            duration = 240
        elif dur == '1 Year':
            duration = 360
        elif dur == '16 Month':
            duration = 480

        features = [[gen_display.index(gen), mar_display.index(mar), dep_display.index(dep),
                     edu_display.index(edu), emp_display.index(emp), mon_income, co_mon_income,
                     loan_amt, duration, cred_display.index(cred), prop_display.index(prop)]]

        prediction = model.predict(features)
        if prediction[0] == 0:
            st.error("Sorry, you are not eligible for a loan.")
        else:
            st.success("Congratulations! You are eligible for a loan.")

run()
