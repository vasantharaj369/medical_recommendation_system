import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))
workout = pickle.load(open('workout.pkl', 'rb'))
pre = pickle.load(open('pre.pkl', 'rb'))
med = pickle.load(open('med.pkl', 'rb'))
diet = pickle.load(open('diet.pkl', 'rb'))
des = pickle.load(open('des.pkl', 'rb'))
sym = pickle.load(open('sym.pkl', 'rb'))
st.header('Medical Recommendation System')


dis_value = {
 15: 'Fungal infection',
 4: 'Allergy',
 16: 'GERD',
 9: 'Chronic cholestasis',
 14: 'Drug Reaction',
 33: 'Peptic ulcer diseae',
 1: 'AIDS',
 12: 'Diabetes ',
 17: 'Gastroenteritis',
 6: 'Bronchial Asthma',
 23: 'Hypertension ',
 30: 'Migraine',
 7: 'Cervical spondylosis',
 32: 'Paralysis (brain hemorrhage)',
 28: 'Jaundice',
 29: 'Malaria',
 8: 'Chicken pox',
 11: 'Dengue',
 37: 'Typhoid',
 40: 'hepatitis A',
 19: 'Hepatitis B',
 20: 'Hepatitis C',
 21: 'Hepatitis D',
 22: 'Hepatitis E',
 3: 'Alcoholic hepatitis',
 36: 'Tuberculosis',
 10: 'Common Cold',
 34: 'Pneumonia',
 13: 'Dimorphic hemmorhoids(piles)',
 18: 'Heart attack',
 39: 'Varicose veins',
 26: 'Hypothyroidism',
 24: 'Hyperthyroidism',
 25: 'Hypoglycemia',
 31: 'Osteoarthristis',
 5: 'Arthritis',
 0: '(vertigo) Paroymsal  Positional Vertigo',
 2: 'Acne',
 38: 'Urinary tract infection',
 35: 'Psoriasis',
 27: 'Impetigo'}

tar_value = {
    'itching': 0,
 'skin_rash': 0,
 'nodal_skin_eruptions': 0,
 'continuous_sneezing': 0,
 'shivering': 0,
 'chills': 0,
 'joint_pain': 0,
 'stomach_pain': 0,
 'acidity': 0,
 'ulcers_on_tongue': 0,
 'muscle_wasting': 0,
 'vomiting': 0,
 'burning_micturition': 0,
 'spotting_ urination': 0,
 'fatigue': 0,
 'weight_gain': 0,
 'anxiety': 0,
 'cold_hands_and_feets': 0,
 'mood_swings': 0,
 'weight_loss': 0,
 'restlessness': 0,
 'lethargy': 0,
 'patches_in_throat': 0,
 'irregular_sugar_level': 0,
 'cough': 0,
 'high_fever': 0,
 'sunken_eyes': 0,
 'breathlessness': 0,
 'sweating': 0,
 'dehydration': 0,
 'indigestion': 0,
 'headache': 0,
 'yellowish_skin': 0,
 'dark_urine': 0,
 'nausea': 0,
 'loss_of_appetite': 0,
 'pain_behind_the_eyes': 0,
 'back_pain': 0,
 'constipation': 0,
 'abdominal_pain': 0,
 'diarrhoea': 0,
 'mild_fever': 0,
 'yellow_urine': 0,
 'yellowing_of_eyes': 0,
 'acute_liver_failure': 0,
 'fluid_overload': 0,
 'swelling_of_stomach': 0,
 'swelled_lymph_nodes': 0,
 'malaise': 0,
 'blurred_and_distorted_vision': 0,
 'phlegm': 0,
 'throat_irritation': 0,
 'redness_of_eyes': 0,
 'sinus_pressure': 0,
 'runny_nose': 0,
 'congestion': 0,
 'chest_pain': 0,
 'weakness_in_limbs': 0,
 'fast_heart_rate': 0,
 'pain_during_bowel_movements': 0,
 'pain_in_anal_region': 0,
 'bloody_stool': 0,
 'irritation_in_anus': 0,
 'neck_pain': 0,
 'dizziness': 0,
 'cramps': 0,
 'bruising': 0,
 'obesity': 0,
 'swollen_legs': 0,
 'swollen_blood_vessels': 0,
 'puffy_face_and_eyes': 0,
 'enlarged_thyroid': 0,
 'brittle_nails': 0,
 'swollen_extremeties': 0,
 'excessive_hunger': 0,
 'extra_marital_contacts': 0,
 'drying_and_tingling_lips': 0,
 'slurred_speech': 0,
 'knee_pain': 0,
 'hip_joint_pain': 0,
 'muscle_weakness': 0,
 'stiff_neck': 0,
 'swelling_joints': 0,
 'movement_stiffness': 0,
 'spinning_movements': 0,
 'loss_of_balance': 0,
 'unsteadiness': 0,
 'weakness_of_one_body_side': 0,
 'loss_of_smell': 0,
 'bladder_discomfort': 0,
 'foul_smell_of urine': 0,
 'continuous_feel_of_urine': 0,
 'passage_of_gases': 0,
 'internal_itching': 0,
 'toxic_look_(typhos)': 0,
 'depression': 0,
 'irritability': 0,
 'muscle_pain': 0,
 'altered_sensorium': 0,
 'red_spots_over_body': 0,
 'belly_pain': 0,
 'abnormal_menstruation': 0,
 'dischromic _patches': 0,
 'watering_from_eyes': 0,
 'increased_appetite': 0,
 'polyuria': 0,
 'family_history': 0,
 'mucoid_sputum': 0,
 'rusty_sputum': 0,
 'lack_of_concentration': 0,
 'visual_disturbances': 0,
 'receiving_blood_transfusion': 0,
 'receiving_unsterile_injections': 0,
 'coma': 0,
 'stomach_bleeding': 0,
 'distention_of_abdomen': 0,
 'history_of_alcohol_consumption': 0,
 'fluid_overload.1': 0,
 'blood_in_sputum': 0,
 'prominent_veins_on_calf': 0,
 'palpitations': 0,
 'painful_walking': 0,
 'pus_filled_pimples': 0,
 'blackheads': 0,
 'scurring': 0,
 'skin_peeling': 0,
 'silver_like_dusting': 0,
 'small_dents_in_nails': 0,
 'inflammatory_nails': 0,
 'blister': 0,
 'red_sore_around_nose': 0,
 'yellow_crust_ooze': 0}

input_value = st.selectbox('Enter the symptoms : ', sym['Symptoms'].unique())

if st.button('Predict'):
    input_value = input_value.split(',')
    new = tar_value.copy()
    for i in input_value:
        new[i.strip()] = 1
    test_value = []
    for i in new.values():
        test_value.append(i)
    predicted = model.predict([test_value])[0]
    disease = dis_value[predicted]
    st.header('Predicted Disease : ')
    st.write(disease)

    description = disease.split()
    val = []
    for i in description:
     val.append(i.strip())
    disease = ' '.join(val)

    description = des[des['Disease'] == disease]['Description'].values[0]
    st.header('Description : ')
    st.write(description)

    diet_value = diet[diet['Disease'] == disease]['Diet']
    diet_value = eval(diet_value.values[0])
    st.header('Diet :')
    count = 1
    for i in diet_value:
     st.write(count, '. ', i)
     count = count + 1

    medicine = med[med['Disease'] == disease]['Medication']
    medicine = eval(medicine.values[0])
    st.header('Medications :')
    count = 1
    for i in medicine:
     st.write(count, '. ', i)
     count = count + 1

    precautions = pre[pre['Disease'] == disease]['precaution'].values[0]
    st.header('Precautions : ')
    count = 1
    for i in precautions:
     st.write(count, '. ', i)
     count = count + 1

    workouts = workout[workout['disease'] == disease]['workout'].tolist()
    count = 1
    st.header('Workouts : ')
    for i in workouts:
     st.write(count, '. ', i)
     count = count + 1
