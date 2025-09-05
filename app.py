import streamlit as st
import pandas as pd

st.title("💰 Personal Finance Tracker")

# Input fields
income = st.number_input("Enter your income", min_value=0)
expense = st.number_input("Enter your expenses", min_value=0)

if st.button("Calculate Savings"):
    savings = income - expense
    st.success(f"Your Savings: {savings}")

# Show existing transactions if file exists
try:
    df = pd.read_csv("transactions.csv")
    st.subheader("📊 Your Transactions")
    st.dataframe(df)
except FileNotFoundError:
    st.warning("No transactions found yet.")
