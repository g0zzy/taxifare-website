import datetime
import pandas as pd
import requests
import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

d = st.date_input(
    "When do you want to take a cab?",
    datetime.date(2013, 7, 6))
st.write('You want it on:', d)

t = st.time_input('What time?', datetime.time(17, 18))

st.write('You want it at', t)

pickup_datetime = datetime.datetime.combine(d, t)

st.write(pickup_datetime)

pickup_longitude = st.number_input('Pickup longtitude?', value=-73.950655)

st.write('Pickup longtitude:  ', pickup_longitude)

pickup_latitude = st.number_input('Pickup latitude?', value=40.783282)

st.write('Pickup latitude:  ', pickup_latitude)

dropoff_longitude = st.number_input('Dropoff longtitude?', value=-73.984365)

st.write('Dropoff longtitude:  ', dropoff_longitude)

dropoff_latitude = st.number_input('Dropoff latitude?', value=40.769802)

st.write('Dropoff latitude:  ', dropoff_latitude)

passenger_count = st.slider('How many passengers?', min_value=1, max_value=8, value=1)

st.write('Number of passengers:  ', passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-41597316435.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
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

st.write(data)
