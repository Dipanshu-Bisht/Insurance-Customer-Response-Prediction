<p align="center">
  <img src="Assets/ui 1.png" width="45%" />
  <img src="Assets/ui 2.png" width="45%" />
</p>

# 🚗 Insurance Customer Response Prediction

## 📌 Project Summary
This project analyzes insurance customer data to identify patterns influencing customer response to vehicle insurance policy offers.  
Using data exploration, statistical insights, and predictive modeling, the project helps businesses target the right customers and improve marketing efficiency.

---

## 🎯 Business Objective
Insurance companies often waste resources contacting customers who are unlikely to respond.

**Objective:**
- ✔ Identify high-probability customers  
- ✔ Improve campaign effectiveness  
- ✔ Reduce operational costs  

---

## 📊 Dataset Overview
- **Records:** 381,109 customers  
- **Features:** 12  
- **Target Variable:** `Response` (Interested / Not Interested)  
- **Class Distribution:**  
  - 88% Not Interested  
  - 12% Interested  

### Key Attributes
- Customer demographics (Age, Gender, Region)  
- Vehicle details (Vehicle Age, Vehicle Damage)  
- Policy & engagement metrics (Annual Premium, Previously Insured, Vintage)  

---

## 🔍 Exploratory Data Analysis (EDA)
### Major Insights:
- Customers **not previously insured** show significantly higher interest  
- Vehicles with **past damage** strongly correlate with positive response  
- **Older vehicles (> 2 years)** have higher conversion rates  
- Gender and Driving License have minimal influence  
- Annual Premium and customer tenure show weak predictive power  

These insights directly support **marketing optimization and customer segmentation** strategies.

---

## 🧹 Data Cleaning & Preparation
- Removed non-informative identifier columns  
- Encoded categorical variables  
- Standardized numeric features for consistent analysis  
- Performed stratified train-test split to preserve class distribution  

---

## 📈 Predictive Modeling (Analytical Perspective)
- Logistic Regression used as a **baseline model**  
- Random Forest applied to capture **non-linear patterns**  
- Model performance evaluated using:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  

✔ Priority given to **Recall** to ensure maximum customer reach.

---

## 📌 Key Results
| Metric | Value |
|------|------|
| Accuracy | 76% |
| Recall | 96% |
| Precision | 26% |

---

## 💡 Business Impact
- Improved targeting of insurance offers  
- Reduced marketing waste  
- Data-driven customer segmentation  
- Actionable insights for decision-makers  

---

## 📄 Documentation
📘 [Project Report (PDF)](Docs/Insurance-Customer-Response-Prediction.pdf)

---

## 👤 Author
**Dipanshu Bisht**  
Data Analyst | Data Scientist | ML engineer  B.Tech CSE  

🔗 GitHub: https://github.com/Dipanshu-Bisht  
🔗 LinkedIn: https://linkedin.com/in/dipanshubisht23 
