

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

- Python 3.11.4
- streamlit==1.44.1
- joblib==1.4.2
- pandas==2.2.3
- numpy==1.26.3
- scikit-learn==1.6.1

To install the required dependencies, simply run:

```bash
pip install streamlit pandas scikit-learn joblib numpy
```

---

## 🚀 Setup & Usage

### 1. **Clone this Repository**

Start by cloning the repository:

```bash
git clone https://github.com/Bhavesh2618/LoanVerity.git
cd LoanVerity
```

### 2. **Download Model and Scaler Files**
Ensure you have the following files in the root directory of your project:

- `best_rf_model.pkl`: The trained Random Forest model.
- `Scaler.pkl`: The scaler used to scale input features.


You can download them from the repository or place them manually in the project directory.

### 3. **Running the App**

1. Clone the repository or place the `loan_app.py` file in your working directory.
2. Ensure the model (`best_rf_model.pkl`) and scaler (`Scaler.pkl`) files are in the same directory.
3. Run the app using **Streamlit**:

   ```bash
   streamlit run loan_app.py
   ```

   The app will start on a local server, typically at `http://localhost:8501`.

---
## 4. **Model Explanation**

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

- **Open Issues:** If you encounter any bugs or need new features, feel free to [open an issue](https://github.com/Bhavesh2618/LoanVerity/issues).
- **Contribute:** Create a branch, implement your changes, and send us a pull request.

---

## 🙏 Acknowledgments

- **Streamlit**: For making web development easy with interactive UIs.
- **Scikit-learn**: For providing powerful tools to build machine learning models.
- **Joblib**: For saving and loading models efficiently.
- **Numpy & Pandas**: For data manipulation and numerical operations.

---
## Conclusion

This app provides a simple and effective tool for predicting loan approval, calculating EMI, and offering suggestions for improving loan eligibility. It integrates machine learning with a user-friendly interface to assist individuals in better understanding their financial situations and loan requests.

## 💬 Stay Connected

Feel free to reach out for any questions or discussions related to the project!

- **Email:** pidugubhaveshkumar@gmail.com

---
