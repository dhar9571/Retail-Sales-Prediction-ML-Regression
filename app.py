import pandas as pd
import numpy as np
import streamlit as st
import joblib
from datetime import date, datetime

# Importing X_train object to know required columns:
xgs = joblib.load(open('xggrid_s.joblib', 'rb'))
xgc = joblib.load(open('xggrid_c.joblib', 'rb'))

# Web App title
st.title("Retail Sales Prediction")

# Message
st.write("Please enter the following information to predict sales:")

# Display a select box for the user to choose from
Open = st.selectbox("Select Store Status:", ['Open', 'Closed'])

if Open=='Open':
    Open=1
else:
    Open=0

if Open==1:

    # Set the minimum and maximum selectable dates
    min_date = date(2013, 1, 1)
    max_date = date.today()

    # Add a date selection widget
    selected_date = str(st.date_input("Select a date:", min_value=min_date, max_value=max_date, value=min_date))

    # Convert the input string to a datetime object
    date_obj = datetime.strptime(selected_date, '%Y-%m-%d')

    # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
    DayOfWeek = date_obj.weekday()+1

    if DayOfWeek==8:
        DayOfWeek=1

    date1 = selected_date.split("-")
    Day = int(date1[2])
    Month = int(date1[1])
    Year = int(date1[0])

    selected_date = pd.to_datetime(selected_date)
    selected_date = selected_date.timestamp()

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
    CompetitionDistance = st.number_input("Please enter the distance of nearest Competitor Store", step=1)
    CompetitionDistance = round(CompetitionDistance)

    customers = int(xgc.predict([[selected_date,Day,Month,Year,Open,DayOfWeek,Promo,
                              StateHoliday,SchoolHoliday, StoreType_b,StoreType_c,
                              StoreType_d,Assortment_b,Assortment_c,CompetitionDistance]]))

    sales = np.around(xgs.predict([[selected_date,Day,Month,Year,Open,DayOfWeek,Promo,
                              StateHoliday,SchoolHoliday, StoreType_b,StoreType_c,
                              StoreType_d,Assortment_b,Assortment_c,customers,CompetitionDistance]]),
                      decimals=2)


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

        st.write(f'Expected Customers: {str(customers)}')
        st.write(f'Expected Sales: {str(int(sales))}')



else:
    st.write("No Sales and Customers as store status is Closed")
