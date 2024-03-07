import pickle
import streamlit as st
with open("model.pickle", 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title('Sales Prediction App')

# Input field for TV ads budget
tv = st.text_input("Enter TV advertising budget")

# Prediction button
if st.button("Predict"):
    try:
        # Convert user input to float and make prediction
        tv_budget = float(tv)
        y_pred = model.predict([[tv_budget]])
        # Display the prediction
        st.write(f"Predicted sales: {y_pred[0]:.2f}")
    except ValueError:
        st.error("Please enter a valid numeric value for TV advertising budget")
