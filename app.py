import datetime
import pandas as pd
import requests
import streamlit as st

'''
# TaxiFareModel front
'''

d = st.date_input(
    "When do you want to take a cab?",
    datetime.date(2013, 7, 6))

t = st.time_input('What time?', datetime.time(17, 18))

pickup_datetime = datetime.datetime.combine(d, t)

pickup_longitude = st.number_input('Pickup longtitude?', value=-73.950655)

pickup_latitude = st.number_input('Pickup latitude?', value=40.783282)

dropoff_longitude = st.number_input('Dropoff longtitude?', value=-73.984365)

dropoff_latitude = st.number_input('Dropoff latitude?', value=40.769802)

passenger_count = st.slider('How many passengers?', min_value=1, max_value=8, value=1)


st.write(f"You want a cab on {pickup_datetime} from {pickup_longitude, pickup_latitude} to {dropoff_longitude, dropoff_latitude} for {passenger_count} passangers.")


url = 'https://taxifare-41597316435.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
## Estimated fare
'''

params = dict(
        pickup_datetime=[pickup_datetime],
        pickup_longitude=[pickup_longitude],
        pickup_latitude=[pickup_latitude],
        dropoff_longitude=[dropoff_longitude],
        dropoff_latitude=[dropoff_latitude],
        passenger_count=[passenger_count],
    )

data = requests.get(url, params=params).json()

st.write("$", round(data["fare"], 2))
