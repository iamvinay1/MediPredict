# -*- coding: utf-8 -*-
"""
Created on Sat May 10 22:45:35 2025

@author: vinay
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

# Load and display the logo
logo = Image.open("D:/MediPredict/logopng.png")

st.image(logo, width=120) 

# Optional: Center it using markdown
st.markdown("<h1 style='text-align: center;'>MediPredict+</h1>", unsafe_allow_html=True)
with st.sidebar:
    st.image(logo, width=120)  # You can adjust width
    st.markdown("<h3 style='text-align: center;'>MediPredict+</h3>", unsafe_allow_html=True)
    

#loading the saved Model

diabetes_model = pickle.load(open("D:/MediPredict/Saved Models/Diabetes_trained_model.sav",'rb'))

heart_disease_model = pickle.load(open("D:/MediPredict/Saved Models/trained_model.sav",'rb'))

breast_cancer_model = pickle.load(open("D:/MediPredict/Saved Models/breast_cancer_model.sav",'rb'))

parkinsons_model = pickle.load(open("D:/MediPredict/Saved Models/Parkinsons_trained_model.sav",'rb'))

lungs_model = pickle.load(open("D:/MediPredict/Saved Models/lung_trained_model.sav",'rb'))

#sidebar for Navigation

with st.sidebar:
    
    selected = option_menu("MediPrdeict+ (Unified ML Based Multi Disease Prediction System)", ['Diabetes Prediction','Heart disease Prediction',
                                                                              'Breast Cancer Classification', 'Parkinsons Diasease Prdeiction',
                                                                              'Lungs Cancer Prediction'],menu_icon='hospital-fill',
                                                                               icons=['activity', 'heart', 'person', 'person', 'lungs'],
                                                                               default_index = 0)
  # Diabetes Prediction Page

if selected == 'Diabetes Prediction':

    # Page Title
    st.title('Diabetes Prediction')

    # Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        glucose = st.text_input('Glucose Level')

    with col3:
        blood_pressure = st.text_input('Blood Pressure value')

    with col1:
        skin_thickness = st.text_input('Skin Thickness value')

    with col2:
        insulin = st.text_input('Insulin Level')

    with col3:
        bmi = st.text_input('BMI value')

    with col1:
        diabetes_pedigree = st.text_input('Diabetes Pedigree Function value')

    with col2:
        age = st.text_input('Age')

    # Code for Prediction
    diabetes_diagnosis = ''

    # Button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [
                pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                bmi, diabetes_pedigree, age
            ]

            user_input = [float(x) for x in user_input]

            diabetes_prediction = diabetes_model.predict([user_input])

            if diabetes_prediction[0] == 1:
                diabetes_diagnosis = 'The person is diabetic'
            else:
                diabetes_diagnosis = 'The person is not diabetic'

        except:
            diabetes_diagnosis = '❗ Please enter valid numeric values in all fields'

    st.success(diabetes_diagnosis)

        
     # Heart Disease Prediction Page
if selected == 'Heart disease Prediction':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
   # Breast Cancer Prediction Page
if selected == 'Breast Cancer Classification':

    st.title('Breast Cancer Prediction')

    # Input Fields – 30 features
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Radius Mean')
    with col2:
        texture_mean = st.text_input('Texture Mean')
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')

    with col1:
        area_mean = st.text_input('Area Mean')
    with col2:
        smoothness_mean = st.text_input('Smoothness Mean')
    with col3:
        compactness_mean = st.text_input('Compactness Mean')

    with col1:
        concavity_mean = st.text_input('Concavity Mean')
    with col2:
        concave_points_mean = st.text_input('Concave Points Mean')
    with col3:
        symmetry_mean = st.text_input('Symmetry Mean')

    with col1:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
    with col2:
        radius_se = st.text_input('Radius SE')
    with col3:
        texture_se = st.text_input('Texture SE')

    with col1:
        perimeter_se = st.text_input('Perimeter SE')
    with col2:
        area_se = st.text_input('Area SE')
    with col3:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
        compactness_se = st.text_input('Compactness SE')
    with col2:
        concavity_se = st.text_input('Concavity SE')
    with col3:
        concave_points_se = st.text_input('Concave Points SE')

    with col1:
        symmetry_se = st.text_input('Symmetry SE')
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
    with col3:
        radius_worst = st.text_input('Radius Worst')

    with col1:
        texture_worst = st.text_input('Texture Worst')
    with col2:
        perimeter_worst = st.text_input('Perimeter Worst')
    with col3:
        area_worst = st.text_input('Area Worst')

    with col1:
        smoothness_worst = st.text_input('Smoothness Worst')
    with col2:
        compactness_worst = st.text_input('Compactness Worst')
    with col3:
        concavity_worst = st.text_input('Concavity Worst')

    with col1:
        concave_points_worst = st.text_input('Concave Points Worst')
    with col2:
        symmetry_worst = st.text_input('Symmetry Worst')
    with col3:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')

    # Prediction Logic
    breast_cancer_diagnosis = ''

    if st.button('Breast Cancer Test Result'):
        try:
            user_input = [
                radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
            ]

            # Convert input to float
            user_input = [float(x) for x in user_input]

            # Predict using the model
            cancer_prediction = breast_cancer_model.predict([user_input])

            if cancer_prediction[0] == 1:
                breast_cancer_diagnosis = 'The person has Breast Cancer (Malignant)'
            else:
                breast_cancer_diagnosis = 'The person does not have Breast Cancer (Benign)'

        except:
            breast_cancer_diagnosis = '❗ Please enter valid numeric values in all fields'

    st.success(breast_cancer_diagnosis)


    # Lungs Cancer Prediction Page

if selected == 'Lungs Cancer Prediction':

    st.title('Lung Cancer Prediction')

    # Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Gender', ['M', 'F'])

    with col2:
        age = st.text_input('Age')

    with col3:
        smoking = st.selectbox('Smoking', [1, 2])

    with col1:
        yellow_fingers = st.selectbox('Yellow Fingers', [1, 2])

    with col2:
        anxiety = st.selectbox('Anxiety', [1, 2])

    with col3:
        peer_pressure = st.selectbox('Peer Pressure', [1, 2])

    with col1:
        chronic_disease = st.selectbox('Chronic Disease', [1, 2])

    with col2:
        fatigue = st.selectbox('Fatigue', [1, 2])

    with col3:
        allergy = st.selectbox('Allergy', [1, 2])

    with col1:
        wheezing = st.selectbox('Wheezing', [1, 2])

    with col2:
        alcohol_consuming = st.selectbox('Alcohol Consuming', [1, 2])

    with col3:
        coughing = st.selectbox('Coughing', [1, 2])

    with col1:
        shortness_of_breath = st.selectbox('Shortness of Breath', [1, 2])

    with col2:
        swallowing_difficulty = st.selectbox('Swallowing Difficulty', [1, 2])

    with col3:
        chest_pain = st.selectbox('Chest Pain', [1, 2])

    # Code for Prediction
    lung_cancer_diagnosis = ''

    if st.button('Lung Cancer Test Result'):
        try:
            gender_val = 1 if gender == 'M' else 0

            user_input = [
                gender_val, float(age), smoking, yellow_fingers, anxiety, peer_pressure,
                chronic_disease, fatigue, allergy, wheezing, alcohol_consuming,
                coughing, shortness_of_breath, swallowing_difficulty, chest_pain
            ]

            lung_prediction = lungs_model.predict([user_input])

            if lung_prediction[0] == 1:
                lung_cancer_diagnosis = 'The person has Lung Cancer'
            else:
                lung_cancer_diagnosis = 'The person does not have Lung Cancer'

        except:
            lung_cancer_diagnosis = '❗ Please enter valid numeric values in all fields'

    st.success(lung_cancer_diagnosis)

    # Parkinson's Disease Prediction Page

if selected == 'Parkinsons Diasease Prdeiction':

    # Page Title
    st.title('Parkinson’s Disease Prediction')

    # Input Fields (Based on common 22 features used in Parkinson's datasets)
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        rap = st.text_input('MDVP:RAP')

    with col1:
        ppq = st.text_input('MDVP:PPQ')

    with col2:
        ddp = st.text_input('Jitter:DDP')

    with col3:
        shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        apq3 = st.text_input('Shimmer:APQ3')

    with col3:
        apq5 = st.text_input('Shimmer:APQ5')

    with col1:
        apq = st.text_input('MDVP:APQ')

    with col2:
        dda = st.text_input('Shimmer:DDA')

    with col3:
        nhr = st.text_input('NHR')

    with col1:
        hnr = st.text_input('HNR')

    with col2:
        rpde = st.text_input('RPDE')

    with col3:
        dfa = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        d2 = st.text_input('D2')

    with col1:
        ppe = st.text_input('PPE')

    # Prediction Code
    parkinsons_diagnosis = ''

    if st.button('Parkinson’s Test Result'):
        try:
            input_data = [
                fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                rpde, dfa, spread1, spread2, d2, ppe
            ]

            input_data = [float(x) for x in input_data]

            parkinsons_prediction = parkinsons_model.predict([input_data])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person has Parkinson’s Disease'
            else:
                parkinsons_diagnosis = 'The person does not have Parkinson’s Disease'

        except:
            parkinsons_diagnosis = '❗ Please enter valid numeric values for all fields'

    st.success(parkinsons_diagnosis)

