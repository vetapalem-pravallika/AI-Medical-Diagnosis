import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Disease Prediction", page_icon="$")

# Hide Streamlit default UI elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://i.postimg.cc/W18pjR04/DALL-E-2025-03-15-19-49-05-A-futuristic-AI-powered-healthcare-background-featuring-a-digital-brain.jpg"
st.markdown(f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url({background_image_url});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
        }}
    </style>
""", unsafe_allow_html=True)

# Load trained models
models = {
    'Diabetes': pickle.load(open('models/Diabetics_model.pkl', 'rb')),
    'Heart Disease': pickle.load(open('models/Heart_Disease_model.pkl', 'rb')),
    'Parkinsons': pickle.load(open('models/parkinsons_model.pkl', 'rb')),
    'Lung Cancer': pickle.load(open('models/lung_cancer_model.pkl', 'rb')),
    'Hypo-Thyroid': pickle.load(open('models/thyroid_model.pkl', 'rb'))
}

# Select Disease
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
)

def display_input(label, key, tooltip, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1) if type == "number" else st.text_input(label, key=key, help=tooltip)

# 🚑 **Diabetes Prediction**
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    gender = display_input('Gender (1=Male, 0=Female)', 'gender', 'Enter gender')
    age = display_input('Age', 'age', 'Enter age')
    hypertension = display_input('Hypertension (1=Yes, 0=No)', 'hypertension', 'Hypertension presence')
    heart_disease = display_input('Heart Disease (1=Yes, 0=No)', 'heart_disease', 'Heart disease presence')
    bmi = display_input('BMI', 'bmi', 'Body Mass Index')
    HbA1c_level = display_input('HbA1c Level', 'HbA1c_level', 'HbA1c Level')
    blood_glucose_level = display_input('Blood Glucose Level', 'blood_glucose_level', 'Blood Glucose Level')

    # Smoking history
    smoking_current = display_input('Smoking Current (1=Yes, 0=No)', 'smoking_current', 'Currently Smokes')
    smoking_ever = display_input('Smoking Ever (1=Yes, 0=No)', 'smoking_ever', 'Ever Smoked')
    smoking_former = display_input('Smoking Former (1=Yes, 0=No)', 'smoking_former', 'Former Smoker')
    smoking_never = display_input('Smoking Never (1=Yes, 0=No)', 'smoking_never', 'Never Smoked')
    smoking_not_current = display_input('Smoking Not Current (1=Yes, 0=No)', 'smoking_not_current', 'Not a Current Smoker')

    if st.button('Diabetes Test Result'):
        features = np.array([[gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, smoking_current, smoking_ever, smoking_former, smoking_never, smoking_not_current]])
        prediction = models['Diabetes'].predict(features)
        st.success('Diabetic' if prediction[0] == 1 else 'Not Diabetic')

# ❤️ **Heart Disease Prediction**
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    age = display_input('Age', 'age', 'Enter age')
    sex = display_input('Sex (1=Male, 0=Female)', 'sex', 'Enter sex')
    cp = display_input('Chest Pain Type', 'cp', 'Chest pain type')
    bp = display_input('Blood Pressure', 'bp', 'Blood pressure value')
    chol = display_input('Cholesterol', 'chol', 'Cholesterol level')
    fbs = display_input('FBS Over 120 (1=Yes, 0=No)', 'fbs', 'Fasting blood sugar >120')
    ekg = display_input('EKG Results', 'ekg', 'Electrocardiogram results')
    max_hr = display_input('Max Heart Rate', 'max_hr', 'Maximum heart rate achieved')
    exang = display_input('Exercise Angina (1=Yes, 0=No)', 'exang', 'Exercise-induced angina')
    st_depression = display_input('ST Depression', 'st_depression', 'ST depression induced by exercise')
    slope = display_input('Slope of ST Segment', 'slope', 'Slope of peak exercise ST segment')
    num_vessels = display_input('Number of Vessels', 'num_vessels', 'Fluoroscopy detected vessels')
    thallium = display_input('Thallium Test Result', 'thallium', 'Thallium scan results')

    if st.button('Heart Disease Test Result'):
        features = np.array([[age, sex, cp, bp, chol, fbs, ekg, max_hr, exang, st_depression, slope, num_vessels, thallium]])
        prediction = models['Heart Disease'].predict(features)
        st.success('Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease')

# 🫁 **Lung Cancer Prediction**
elif selected == 'Lung Cancer Prediction':
    st.title('Lung Cancer Prediction')

    features = [display_input(label, key, label) for label, key in [
        ('Gender (1=Male, 0=Female)', 'gender'),
        ('Age', 'age'),
        ('Smoking (1=Yes, 0=No)', 'smoking'),
        ('Yellow Fingers (1=Yes, 0=No)', 'yellow_fingers'),
        ('Anxiety (1=Yes, 0=No)', 'anxiety'),
        ('Peer Pressure (1=Yes, 0=No)', 'peer_pressure'),
        ('Chronic Disease (1=Yes, 0=No)', 'chronic_disease'),
        ('Fatigue (1=Yes, 0=No)', 'fatigue'),
        ('Allergy (1=Yes, 0=No)', 'allergy'),
        ('Wheezing (1=Yes, 0=No)', 'wheezing'),
        ('Alcohol Consumption (1=Yes, 0=No)', 'alcohol_consuming'),
        ('Coughing (1=Yes, 0=No)', 'coughing'),
        ('Shortness of Breath (1=Yes, 0=No)', 'shortness_of_breath'),
        ('Swallowing Difficulty (1=Yes, 0=No)', 'swallowing_difficulty'),
        ('Chest Pain (1=Yes, 0=No)', 'chest_pain')
    ]]

    if st.button('Lung Cancer Test Result'):
        prediction = models['Lung Cancer'].predict([features])
        st.success('Lung Cancer Detected' if prediction[0] == 1 else 'No Lung Cancer')

elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction")

    # ✅ Load Scaler
    scaler = pickle.load(open("C:/Users/prava/models/parkinsons_scaler.pkl", "rb"))

    # ✅ Input Fields (22 Features) with Limited Decimal Support (3 Decimal Places)
    features = [st.number_input(label, format="%.3f") for label in [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", 
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", 
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", 
        "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]]

    # ✅ Convert to NumPy Array & Scale It
    input_data = np.array(features).reshape(1, -1)
    input_data = scaler.transform(input_data)  # Apply same scaler used during training

    if st.button("Predict Parkinson's"):
        prediction = models['Parkinsons'].predict(input_data)
        st.success("Parkinson's Detected!" if prediction[0] == 1 else "No Parkinson's Disease.")

# 🦋 **Hypo-Thyroid Prediction**
elif selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid Prediction")

    features = [display_input(label, key, label) for label, key in [
        ("Age", "age"), ("TSH", "TSH"), ("T3", "T3"), ("TT4", "TT4"), ("T4U", "T4U"), ("FTI", "FTI")
    ]]

    if st.button("Thyroid Test Result"):
        prediction = models['Hypo-Thyroid'].predict([features])
        st.success('Hypo-Thyroid Detected' if prediction[0] == 1 else 'No Hypo-Thyroid')
