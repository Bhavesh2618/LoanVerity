

# 🎯 LoanVerity: Smart Loan Approval Prediction

## 💡 Overview

**LoanVerity** is an intelligent web application that predicts the likelihood of loan approval based on the applicant's information. It leverages a **Random Forest model** to analyze various factors and provide instant loan approval predictions. 

With **Streamlit** for the frontend and **Scikit-learn** for the model, **LoanVerity** is designed to assist users in understanding their loan eligibility, offering real-time insights, suggestions, and EMI breakdowns.

---

## 🚀 Features

### 🏦 **Instant Loan Approval Prediction**
- Predict whether your loan will be approved based on your financial information.

### ⚠️ **Risk Indicators**
- Get alerted about potential risks (low CIBIL score, high loan amount, EMI risk).

### 💡 **Smart Suggestions**
- Receive tips to improve your chances of approval such as boosting your income or improving your CIBIL score.

### 📊 **EMI Breakdown**
- See a detailed breakdown of your loan's EMI, principal, and interest payments.

### 📈 **Interest Calculation**
- Automatically calculates an interest rate based on income, loan amount, assets, and CIBIL score.

---

## 📝 Requirements

To run the application locally, make sure you have the following Python packages installed:

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Numpy

To install the required dependencies, simply run:

```bash
pip install streamlit pandas scikit-learn joblib numpy
```

---

## 🚀 Setup & Usage

### 1. **Clone this Repository**

Start by cloning the repository:

```bash
git clone https://github.com/your-username/LoanVerity.git
cd LoanVerity
```

### 2. **Download Model and Scaler Files**
Ensure you have the following files in the root directory of your project:

- `best_rf_model.pkl`: The trained Random Forest model.
- `Scaler.pkl`: The scaler used to scale input features.

You can download them from the repository or place them manually in the project directory.

### 3. **Run the Application**

Start the application with:

```bash
streamlit run app.py
```

The app will be available at the link provided in your terminal. Open the URL in your browser to use the app.

---

## 🧑‍💻 Application Flow

1. **Fill in Applicant Information:**
   - Provide details such as income, loan amount, CIBIL score, education, and more.
   
2. **Click "Predict":**
   - The model will instantly predict whether your loan will be approved.

3. **Results:**
   - **If Approved**: See your **EMI breakdown**, the **interest rate**, and the **maximum eligible loan**.
   - **If Rejected**: View the **risk indicators** and suggestions to help improve your loan chances.

4. **Smart Suggestions & Advice:**
   - The app offers practical suggestions to improve your eligibility and loan terms.

---

## ⚡ Smart Suggestions & Risk Indicators

### **CIBIL Score**
- **Low CIBIL Score (< 650):** You’ll be advised to work on improving your credit score by maintaining timely payments and clearing outstanding debts.

### **Loan Amount**
- **Exceeds Eligible Limit:** If your requested loan exceeds the maximum eligible amount, you may need to **reduce the loan** or **increase your income/assets**.

### **EMI Risk**
- **Short Term + High EMI Risk:** The app might suggest opting for a **longer loan term** or **reducing the loan amount** to make the EMI more manageable.

---

## 💻 Contributing

We welcome contributions! If you have ideas, bug fixes, or enhancements, feel free to fork the repository and submit pull requests. 

- **Open Issues:** If you encounter any bugs or need new features, feel free to [open an issue](https://github.com/your-username/LoanVerity/issues).
- **Contribute:** Create a branch, implement your changes, and send us a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgments

- **Streamlit**: For making web development easy with interactive UIs.
- **Scikit-learn**: For providing powerful tools to build machine learning models.
- **Joblib**: For saving and loading models efficiently.
- **Numpy & Pandas**: For data manipulation and numerical operations.

---

## 💬 Stay Connected

Feel free to reach out for any questions or discussions related to the project!

- **Email:** your-email@example.com
- **Twitter:** [@yourhandle](https://twitter.com/yourhandle)

---

<p align="center">
  <img src="https://img.shields.io/badge/Powered%20by-Streamlit-orange" alt="Powered by Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT">
</p>

# Loanverity - Smart Loan 

## Overview

Welcome to the **Loan Approval Prediction and EMI Management App**! This application leverages machine learning to predict loan approval eligibility and calculate the **Equated Monthly Installment (EMI)** for a loan request. By analyzing key factors such as the applicant's education, income, CIBIL score, loan amount, term, and assets value, the app determines the likelihood of loan approval and helps users calculate their monthly payments.

---

## Features

### 1. **Loan Approval Prediction**
- Predicts whether a loan will be approved based on various input features like income, education, and loan term.

### 2. **EMI Calculation**
- Calculates the EMI based on the loan amount, rate of interest, and loan term, helping applicants plan their finances.

### 3. **Loan Eligibility Suggestions**
- Provides tips to improve eligibility, such as improving the CIBIL score or reducing the loan amount.

### 4. **Visualization**
- Displays graphical representations for an easy understanding of the EMI breakdown.

### 5. **Interactive UI**
- Built with **Streamlit**, the app provides a user-friendly interface that allows users to input data and receive instant predictions.

---

## Installation and Setup

### Requirements

To run this app, you'll need Python 3.x along with the following libraries:

- `streamlit`
- `pandas`
- `numpy`
- `joblib`
- `matplotlib`
- `scikit-learn`

Install them via pip:

```bash
pip install streamlit pandas numpy joblib matplotlib scikit-learn
```

---

### Setting Up the Model

- **Model**: The app uses a trained RandomForest model saved as `best_rf_model.pkl` (or any name you choose, as long as it matches the file name).
- **Scaler**: A `StandardScaler` is used for scaling the input features and should be saved as `Scaler.pkl`.

Save the models and scaler using `joblib`:

```python
import joblib

# Saving the model
joblib.dump(model, 'best_rf_model.pkl')
joblib.dump(scaler, 'Scaler.pkl')
```

---

### Running the App

1. Clone the repository or place the `loan_app.py` file in your working directory.
2. Ensure the model (`best_rf_model.pkl`) and scaler (`Scaler.pkl`) files are in the same directory.
3. Run the app using **Streamlit**:

   ```bash
   streamlit run loan_app.py
   ```

   The app will start on a local server, typically at `http://localhost:8501`.

---

## Model Explanation

The **RandomForestClassifier** model has been trained on a dataset that includes the following features:

- **Number of Dependents**: Number of dependents the applicant has.
- **Education**: Whether the applicant is a graduate or not.
- **Self Employed**: Whether the applicant is self-employed.
- **Annual Income**: The total income of the applicant in a year.
- **Loan Amount**: The requested loan amount.
- **Loan Term**: The duration of the loan in years.
- **CIBIL Score**: The applicant's credit score.
- **Assets Value**: The total value of assets owned by the applicant.

The model predicts the likelihood of loan approval or rejection based on these factors.

---

## How to Use the App

### 1. **Input Applicant Details**:
   - Enter the applicant's **number of dependents**, **education**, **self-employment status**, **annual income**, **loan amount**, **loan term**, **CIBIL score**, and **assets value** in the sidebar.

### 2. **Predict Loan Approval**:
   - After entering the details, click on the "Predict Loan Approval" button to get the loan approval status and the model's prediction confidence.

### 3. **EMI Calculation**:
   - Once the loan is approved, the app will also calculate the EMI based on the provided loan amount, rate of interest, and loan term.

### 4. **Eligibility Suggestions**:
   - The app will provide suggestions on improving eligibility for the loan based on the input details (e.g., improving CIBIL score, reducing loan amount).

### 5. **Visualization**:
   - The app displays a graphical representation of the EMI breakdown, showing the principal and interest components.

---

## Example Use Case

**Input**:

- Number of Dependents: 2
- Education: Graduate
- Self Employed: No
- Annual Income: ₹500,000
- Loan Amount: ₹300,000
- Loan Term: 10 years
- CIBIL Score: 750
- Assets Value: ₹2,000,000

**Output**:

- Loan Approval: Approved
- Loan Approval Probability: 85%
- EMI: ₹3,400 per month
- Suggestions: "📈 Reduce loan amount for better approval chances."

---

## Suggestions for Improvement

- If the applicant’s CIBIL score is below 650, the app will suggest improving their score by clearing debts and making timely payments.
- If the loan amount requested is too high compared to annual income, the app will recommend reducing the amount for better eligibility.

---

## Conclusion

This app provides a simple and effective tool for predicting loan approval, calculating EMI, and offering suggestions for improving loan eligibility. It integrates machine learning with a user-friendly interface to assist individuals in better understanding their financial situations and loan requests.
