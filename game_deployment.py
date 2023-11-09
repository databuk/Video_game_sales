import pandas as pd
import numpy as np
import streamlit as st
import joblib
from data_clean import clean_data

pipeline = joblib.load('game_pipeline.joblib')
st.title('Video Game Sales Prediction')
def take_user_input():
       console = st.selectbox('Console', options=['Nintendo DS', 'Nintendo Wii', 'PlayStation 1', 'PlayStation 2',
              'PlayStation 3', 'PlayStation Portable', 'XB', 'Xbox 360',
              'PlayStation Vita', 'Game Boy Advance', 'GameCube', 'ps',
              'Nintendo Wii U', 'Xbox One', 'PlayStation 4', 'Nintendo 3DS',
              'Dreamcast'])
       category = st.selectbox('Category', options=['role-playing', 'simulation', 'shooter', 'sports', 'action',
              'platform', 'strategy', 'racing', 'misc', 'fighting', 'adventure',
              'puzzle'])
       rating = st.selectbox('Rating', ['Everyone', 'Everyone 10 and Older', 'Mature 17+', 'Teen',
              'Rating Pending'])
       critic_points = st.number_input('Critic Points', min_value=0, max_value=50)
       user_points = st.slider('User Points', min_value=0.0, max_value=3.0, value=0.5)
       return pd.DataFrame(data=[[console, category, rating, critic_points, user_points]],
                    columns=['console', 'category', 'rating', 'critics_points','user_points'])
input_data = take_user_input()
if st.button('Predict'):
       with st.spinner('Calculating prediction...'):
              prediction = pipeline.predict(input_data)
              st.success(f'The total video game sales revenue is ${np.round(prediction[0], 2)} million.')