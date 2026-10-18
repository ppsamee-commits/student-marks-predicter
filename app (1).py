
import streamlit as st
import joblib

st.set_page_config(page_title="Student Marks Predictor")

st.title("🎓 Student Marks Predictor")
st.write("Predict your marks using Machine Learning!")

model = joblib.load("student_marks_model.pkl")

hours = st.number_input(
    "Enter hours studied",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

if st.button("Predict Marks"):
    prediction = model.predict([[hours]])
    st.success(f"Predicted Marks: {prediction[0]:.2f}")
