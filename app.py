import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests


# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# # Remember that there are several ways to output content into your web page...

# # Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# # ''')

st.title('NY TAXI: IS THAT A FAIR FARE?')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''


date = st.date_input('Date', datetime.date(2019, 7, 6))
time = st.time_input('Time', datetime.time(8, 45))

pickup_longitude = st.text_input('Pickup Longitude', value=40.7805414)
pickup_latitude = st.text_input('Pickup Latitude', value=-73.968285)


dropoff_longitude = st.text_input('Dropoff Longitude', value=40.7127431)
dropoff_latitude = st.text_input('Dropoff Latitude', value=-74.0895972)


passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, value=1)


def get_map_data():
    return pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [40.7805414, -73.968285],
        columns=['lat', 'lon']
    )

map_data = get_map_data()

st.map(map_data)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''
# 2. Let's build a dictionary containing the parameters for our API...
# '''

X_pred = {
    'pickup_datetime': f'{date} {time}',
    'pickup_longitude': float(pickup_longitude),
    'pickup_latitude': float(pickup_latitude),
    'dropoff_longitude': float(dropoff_longitude),
    'dropoff_latitude': float(dropoff_latitude),
    'passenger_count': int(passenger_count)
}

# '''
# 3. Let's call our API using the `requests` package...
# '''

response = requests.get(url, params=X_pred)

# '''
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# '''

prediction = response.json()

tarif = prediction['fare']
rounded_tarif = round(tarif, 2)

st.title(f'TARIF: {rounded_tarif} $')
