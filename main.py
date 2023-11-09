import pickle
import streamlit as st
from read import MAIN

# IMPORTING THE TRAINED MODEL 

# Open the pickle file in binary read mode.
with open("my_pickle_file.pkl", "rb") as f:
    # Load the pickled object from the file.
    # model = pickle.load(f)
    sometext = 'Done'

# Close the pickle file.
f.close()

# Use the pickled object in your application.
# print(my_object)

# THE APP INTERFACE
st.title("Music Genre Prediction")

# gender = st.selectbox("Select Gender", ['Male', 'Female'])
# # age = st.text_input("Age")
# age = st.slider("Select Age", min_value=18, max_value=70)

# submit = st.button("Predict")
# clear = st.button("Clear")
# pred_box = st.write()

# gender_bool = 1 if gender=='Male' else 0

# if submit:
    
#     prediction = model.predict([[gender_bool, age]])
#     st.write(prediction)
#     st.toast("completed 1 prediction")
    
# if clear:
#     pred_box = ''