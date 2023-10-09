import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Web App title
st.title("Retail Sales Prediction")

# Message
st.write("Please enter the following information to predict sales:")

# Importing X_train object to know required columns:
X_train = pickle.load(open('X_train.pkl', 'rb'))

# Display a select box for the user to choose from
Open = st.selectbox("Select Store Status:", ['Open', 'Closed'])

if Open=='Open':
    Open=1
else:
    Open=0

if Open==1:
    DayOfWeek = st.selectbox('Select Day of the Week:', sorted(X_train['DayOfWeek'].unique()))

    Promo = st.selectbox('Select Promotion Status:', ["Yes", "No"])

    if Promo=="Yes":
        Promo=1
    else:
        Promo=0

    StateHoliday = st.selectbox('Select State Holiday Status:', ["Yes", "No"])

    if StateHoliday=="Yes":
        StateHoliday=1
    else:
        StateHoliday=0

    SchoolHoliday = st.selectbox('Select School Holiday Status:', ["Yes", "No"])

    if SchoolHoliday == "Yes":
        SchoolHoliday = 1
    else:
        SchoolHoliday = 0

    StoreType_b = 0
    StoreType_c = 0
    StoreType_d = 0

    StoreType = st.selectbox("Select Store Type",["A", "B", "C", "D"])

    if StoreType == "B":
        StoreType_b = 1
    elif StoreType == "C":
        StoreType_c = 1
    elif StoreType == "D":
        StoreType_d = 1

    Assortment_b = 0
    Assortment_c = 0

    Assortment = st.selectbox("Select Assortment Type",["A", "B", "C"])

    if Assortment == "B":
        Assortment_b = 1
    elif Assortment == "C":
        Assortment_c = 1

    # Get an integer input from the user
    Customers = st.number_input("Please enter the number of customers", step=1)

    button_style = """
        <style>
        div.stButton > button:first-child {
            background-color: green !important;
            color: black !important;
        }
        </style>
    """

    # Display the button with the custom style
    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("Predict"):

        if Customers == 0:
            st.write("No Sales when Customers are 0")
        else:
            user_dict = {"Open": [Open], "DayOfWeek": [DayOfWeek], "Promo": [Promo], "StateHoliday": [StateHoliday],
                         "SchoolHoliday": [SchoolHoliday], "StoreType_b": [StoreType_b], "StoreType_c": [StoreType_c],
                         "StoreType_d": [StoreType_d], "Assortment_b": [Assortment_b], "Assortment_c": [Assortment_c],
                         "Customers": [Customers]}

            user_df = pd.DataFrame(user_dict)

            # Importing trained XGBoost model object:
            model = pickle.load(open('xggrid.pkl', 'rb'))

            # Making prediction
            result = model.predict(user_df)

            st.write("Predicted Sales:  ", str(np.round(float(result),2)))

else:
    st.write("No sales as Store is Closed")
