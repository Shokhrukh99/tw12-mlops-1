import streamlit as st
import pickle

@st.cache_data()
def load_model():
    return pickle.load(open('model.pkl', 'rb')) 

model = load_model()

if model:
    st.toast('Model loaded successfully')
else:
    st.toast('Model could not be loaded')

st.title('California House Pricing')
st.write('House price prediction based on input features')

col1, col2 = st.columns(2)

med_inc = st.slider('Median Income (in thousands of $)', value=400, min_value=0, max_value=2000)

with col1:
    house_age = st.number_input('House age (in years)', min_value=0, value=30, max_value=70)
    ave_bedrooms = st.number_input('AveBedrooms', min_value=0, value=30, max_value=40)

with col2:
    ave_rooms = st.number_input('AveRooms', min_value=1, value=30, max_value=140)
    ave_occup = st.number_input('AveOccup', min_value=0, value=3, max_value=1500)

population = st.slider('Population', value=1500, min_value=10, max_value=35000)

latitude = st.slider('Latitude', value=40.0, min_value=30.0, max_value=50.0)
longitude = st.slider('Longitude', value=-120.0, min_value=-130.0, max_value=-100.0)

map = {
    'lat': [latitude],
    'lon': [longitude]
}
st.map(map, zoom=7)

features = [[
    med_inc, house_age, ave_rooms, ave_bedrooms, population, ave_occup, latitude, longitude
]]

if st.button('Predict'):
    st.write(f'Features: {features}')
    prediction = model.predict(features)
    st.success(f'$ {prediction[0] * 100000:.2f}')