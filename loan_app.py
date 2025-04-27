import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('best_rf_model.pkl')
scaler = joblib.load("Scaler.pkl")

st.set_page_config(page_title="LoanVerity", page_icon="🏦", layout="wide")
st.caption("Smart loan insights at your fingertips")
st.title("🏦 Check Your Loan Approval Instantly")
st.markdown("Fill in the information below to check your loan approval status:")

with st.sidebar:
    st.markdown("### 📋 Applicant Information")
    no_of_dependents = st.number_input("👨‍👩‍👧 Number of Dependents", min_value=0, max_value=20, step=1)
    education = st.radio("🎓 Education Level", ["No", "Yes"])
    education_val = 1 if education == "Yes" else 0

    self_employed = st.radio("💼 Self-Employed", ["No", "Yes"])
    self_employed_val = 1 if self_employed == "Yes" else 0

    income_annum = st.number_input("💰 Annual Income (₹)", min_value=10000, step=1000)
    loan_amount = st.number_input("🏦 Requested Loan Amount (₹)", min_value=1000, step=1000)
    loan_term = st.number_input("📆 Loan Term (in years)", min_value=1.0, max_value=30.0, step=1.0, format="%.2f")
    cibil_score = st.number_input("📊 CIBIL Score", min_value=300, max_value=900, step=1)
    Assets_value = st.number_input("🏠 Total Assets Value (₹)", min_value=0, step=1000)

    


if st.button("🔍 Predict"):
    # Eligibility calculations
    max_eligible_loan = (income_annum * 0.4 * loan_term) + (Assets_value * 0.7)
    strong_asset_backup = Assets_value >= loan_amount
    sufficient_income = (income_annum * 0.4 * loan_term) >= loan_amount

    # Interest logic
    base_interest_rate = 0.085
    interest_rate = base_interest_rate
    if income_annum < 50000:
        interest_rate += 0.02
    if loan_amount > 500000:
        interest_rate += 0.02
    if Assets_value < loan_amount * 0.5:
        interest_rate += 0.03
    if cibil_score < 600:
        interest_rate += 0.05

    total_interest = loan_amount * interest_rate * loan_term
    emi = (loan_amount + total_interest) / (loan_term * 12)

    # EMI breakdown
    monthly_interest_rate = interest_rate / 12
    total_payment = loan_amount + total_interest
    principal_payment = loan_amount / (loan_term * 12)
    interest_payment = total_payment / (loan_term * 12) - principal_payment

    # Policy checks
    cibil_violation = cibil_score < 650
    loan_limit_violation = loan_amount > max_eligible_loan
    emi_risk = loan_term < 4 and loan_amount / income_annum > 2

    if (cibil_violation and not (strong_asset_backup and sufficient_income)) or loan_limit_violation or emi_risk:
        st.error("❌ Loan Rejected due to policy violation.")
        st.metric(label="Max Eligible Loan (₹)", value=f"{max_eligible_loan:,.2f}")

        st.markdown("### 🔍 Risk Indicators")
        if cibil_violation and not (strong_asset_backup and sufficient_income):
            st.warning("⚠️ CIBIL score too low (minimum 650 required), and no strong asset/income backup.")
        if loan_limit_violation:
            st.warning(f"⚠️ Requested loan exceeds eligible limit (₹{max_eligible_loan:,.2f}).")
        if emi_risk:
            st.warning("⚠️ Short term + high EMI risk.")

        # Smart Suggestions
        st.markdown("### 💡 Smart Suggestions")
        suggestions = []

        if cibil_score < 650:
            suggestions.append("📈 Improve your CIBIL score by maintaining timely payments and clearing debts.")
        if loan_amount > max_eligible_loan:
            suggestions.append(f"📉 Reduce the loan amount to below ₹{max_eligible_loan:,.2f} or increase your income/assets.")
        if emi_risk:
            suggestions.append("📅 Choose a longer loan term or reduce loan amount to make EMI manageable.")

        if not (strong_asset_backup and sufficient_income):
            suggestions.append("💰 Strengthen your asset base or annual income to support higher loan eligibility.")

        if suggestions:
            for sug in suggestions:
                st.write(sug)
        else:
            st.success("🎯 No major issues detected. Minor improvements might help.")

    else:
        # Prediction if policies passed
        input_df = pd.DataFrame([{
            'no_of_dependents': no_of_dependents,
            'education': education_val,
            'self_employed': self_employed_val,
            'income_annum': income_annum,
            'loan_amount': loan_amount,
            'loan_term': loan_term,
            'cibil_score': cibil_score,
            'Assets_value': Assets_value
        }])
        input_df_scaled = scaler.transform(input_df)

        prediction = model.predict(input_df_scaled)
        prob = model.predict_proba(input_df_scaled)[0][1]

        st.markdown("### 🔍 Results")
        st.metric(label="Prediction Confidence", value=f"{prob:.2f}")

        if prediction[0] == 1:
            st.success("✅ Loan Approved")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Estimated EMI (₹)", value=f"{emi:,.2f}")
            with col2:
                st.metric(label="Interest Rate (%)", value=f"{interest_rate * 100:.2f}%")

            st.metric(label="Max Eligible Loan (₹)", value=f"{max_eligible_loan:,.2f}")

            # EMI Breakdown
            st.markdown("### 💡 EMI Breakdown")
            st.write(f"Total EMI: ₹{emi:,.2f} per month")
            st.write(f"Principal Payment: ₹{principal_payment:,.2f} per month")
            st.write(f"Interest Payment: ₹{interest_payment:,.2f} per month")

            st.markdown("### 💡 Positive Indicators")
            if cibil_score >= 650:
                st.info("✔️ Healthy credit score")
            if loan_amount <= max_eligible_loan:
                st.info("✔️ Loan within eligible range")
            if Assets_value > (0.5 * loan_amount):
                st.info("✔️ Strong asset backup")
            if self_employed_val == 1:
                st.info("✔️ Additional income source")

        else:
            st.error("❌ Loan Rejected")
            st.metric(label="Max Eligible Loan (₹)", value=f"{max_eligible_loan:,.2f}")

            st.markdown("### 🔍 Risk Indicators")
            if cibil_score < 650:
                st.warning("⚠️ CIBIL score is low")
            if loan_amount > max_eligible_loan:
                st.warning(f"⚠️ Requested loan exceeds eligible limit (₹{max_eligible_loan:,.2f})")
            if emi_risk:
                st.warning("⚠️ Short term + high EMI risk")

            st.markdown("### 💡 Smart Suggestions")
            suggestions = []

            if cibil_score < 650:
                suggestions.append("📈 Improve your CIBIL score by maintaining timely payments and clearing debts.")
            if loan_amount > max_eligible_loan:
                suggestions.append(f"📉 Reduce the loan amount to below ₹{max_eligible_loan:,.2f} or increase your income/assets.")
            if emi_risk:
                suggestions.append("📅 Choose a longer loan term or reduce loan amount to make EMI manageable.")

            if not (strong_asset_backup and sufficient_income):
                suggestions.append("💰 Strengthen your asset base or annual income to support higher loan eligibility.")

            if suggestions:
                for sug in suggestions:
                    st.write(sug)
            else:
                st.success("🎯 No major issues detected. Minor improvements might help.")

        # 🎯 SMART Further Advice
        st.markdown("### 💡 Further Advice")
        advice = []

        if cibil_score < 700:
            advice.append("📈 Aim to improve your CIBIL score above 700 for better loan terms.")
        if loan_amount > max_eligible_loan:
            advice.append("📉 Try reducing the loan amount or boosting your income.")
        if emi_risk:
            advice.append("📅 Consider opting for a longer loan term to ease EMI pressure.")

        if advice:
            for tip in advice:
                st.write(tip)
        else:
            st.success("🎉 You have a strong profile! No further improvements needed.")
