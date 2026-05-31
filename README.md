#  Customer Churn Prediction System

##  Project Overview

The Customer Churn Prediction System is a Machine Learning project developed to predict whether a customer is likely to leave a telecom company. The project uses classification algorithms and business insights to help companies improve customer retention strategies.

This project includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning model training
* SHAP explainability
* Streamlit web application
* GitHub integration

---

#  Features

✅ Data Cleaning & Preprocessing
✅ Exploratory Data Analysis (EDA)
✅ Logistic Regression Model
✅ Random Forest Classifier
✅ XGBoost Classifier
✅ SHAP Explainability
✅ Streamlit Web Application
✅ Business Insights Visualization
✅ Model Comparison
✅ GitHub Ready Structure

---

#  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* SHAP
* Streamlit
* Jupyter Notebook

---

#  Project Structure

```bash
Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── images/
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Exploratory Data Analysis

The project includes:

* Customer churn distribution analysis
* Contract type vs churn analysis
* Monthly charges analysis
* Tenure analysis
* Correlation heatmap

---

#  Machine Learning Models

The following classification models were trained and evaluated:

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~81-82%     |
| Random Forest       | ~79-80%     |
| XGBoost             | ~80-81%  |

---

#  SHAP Explainability

SHAP (SHapley Additive exPlanations) was used to interpret model predictions and identify the most important features affecting customer churn.

Important features include:

* Monthly Charges
* Tenure
* Contract Type
* Internet Service

---

#  Streamlit Web Application

The project includes a Streamlit web application where users can:

* Enter customer information
* Predict churn instantly
* View prediction results interactively

Run the application using:

```bash
streamlit run app/app.py
```

---

#  Project Screenshots

## Main Application

(Add screenshot here)

## Prediction Result

(Add screenshot here)

## SHAP Explainability

(Add screenshot here)

---

#  Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into project folder:

```bash
cd Customer-Churn-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app/app.py
```

---

#  Business Impact

This project helps telecom companies:

* Identify customers likely to churn
* Improve retention strategies
* Reduce revenue loss
* Increase customer satisfaction
* Support data-driven business decisions

---

#  Author

Shubham Mishra

---

#  Conclusion

The Customer Churn Prediction System demonstrates how Machine Learning can be used to solve real-world business problems effectively. The project combines predictive analytics, explainable AI, and interactive deployment to create a complete end-to-end Data Science solution.
