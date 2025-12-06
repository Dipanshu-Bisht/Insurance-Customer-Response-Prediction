import streamlit as st
import pickle
import pandas as pd

st.title(" Insurance Customer Response Prediction")
st.write("Predict whether a customer is likely to be interested in an insurance policy offer.")

# loading model, scaler, threshold

try:
    with open("tuned_random_forest.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("best_threshold.pkl", "rb") as f:
        best_threshold = pickle.load(f)
except Exception as e:
    st.error("Error loading model / scaler / threshold. Please check that all .pkl files are present")
    st.code(str(e))
    st.stop()

# Mappings 

GENDER_MAP = {'Male': 0, 'Female': 1}
VEHICLE_AGE_MAP = {'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2}
VEHICLE_DAMAGE_MAP = {'No': 0, 'Yes': 1}

FEATURE_COLUMNS = [
    'Gender',
    'Age',
    'Driving_License',
    'Region_Code',
    'Previously_Insured',
    'Vehicle_Age',
    'Vehicle_Damage',
    'Annual_Premium',
    'Policy_Sales_Channel',
    'Vintage'
]

NUM_COLS = ['Age', 'Annual_Premium', 'Vintage']

# Input form

st.markdown("### Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    driving_license = st.selectbox("Driving License (1 = Yes, 0 = No)", [1, 0])
    region_code = st.number_input("Region Code", min_value=0, max_value=50, value=28, step=1)
    previously_insured = st.selectbox("Previously Insured (1 = Yes, 0 = No)", [0, 1])

with col2:
    vehicle_age = st.selectbox("Vehicle Age", ["< 1 Year", "1-2 Year", "> 2 Years"])
    vehicle_damage = st.selectbox("Vehicle Damage Before", ["No", "Yes"])
    annual_premium = st.number_input("Annual Premium", min_value=1000, max_value=1000000, value=30000, step=100)
    policy_sales_channel = st.number_input("Policy Sales Channel", min_value=1, max_value=200, value=26, step=1)
    vintage = st.number_input("Customer Vintage (days with company)", min_value=0, max_value=300, value=150, step=1)

# Predict button

if st.button("Predict Response"):
    # 1. Map categorical values to numbers
    gender_val = GENDER_MAP[gender]
    vehicle_age_val = VEHICLE_AGE_MAP[vehicle_age]
    vehicle_damage_val = VEHICLE_DAMAGE_MAP[vehicle_damage]

    # 2. Create DataFrame
    row = [[
        gender_val,
        age,
        driving_license,
        region_code,
        previously_insured,
        vehicle_age_val,
        vehicle_damage_val,
        annual_premium,
        policy_sales_channel,
        vintage
    ]]
    df = pd.DataFrame(row, columns=FEATURE_COLUMNS)

    # 3. Scale numeric columns
    try:
        df[NUM_COLS] = scaler.transform(df[NUM_COLS])
    except Exception as e:
        st.error("Error while scaling numeric features. Check that scaler.pkl was fitted on ['Age', 'Annual_Premium', 'Vintage'].")
        st.code(str(e))
        st.stop()

    # 4. Predict probability
    try:
        proba = model.predict_proba(df)[:, 1][0]
    except Exception as e:
        st.error("Error while predicting with the model.")
        st.code(str(e))
        st.stop()

    # 5. Apply threshold
    predicted_class = int(proba >= best_threshold)

    # ---------------------------
    # Show results
    # ---------------------------
    st.markdown("### Prediction Result")

    if predicted_class == 1:
        st.success("The model predicts that the customer is **LIKELY TO RESPOND**.")
    else:
        st.warning("The model predicts that the customer is **NOT LIKELY TO RESPOND**.")

    
