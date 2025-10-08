import streamlit as st
import pandas as pd

st.set_page_config(page_title="Balance Sheet App", page_icon="📊")

st.title("📊 Balance Sheet Automation by SIDHARTH")

st.write("Upload an Excel file with columns **Category** and **Amount**")

uploaded_file = st.file_uploader("Choose your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        data = pd.read_excel(uploaded_file)
        totals = data.groupby("Category")["Amount"].sum()

        assets = totals.get("Asset", 0)
        liabilities = totals.get("Liability", 0)
        equity = totals.get("Equity", 0)
        indirect_exp = totals.get("Indirect Expense", 0)
        direct_exp = totals.get("Direct Expense", 0)

        adjusted_equity = equity + indirect_exp + direct_exp
        difference = assets - (liabilities + adjusted_equity)

        st.subheader("Balance Sheet Summary")
        st.write(f"**Total Assets:** ₹{assets:,.2f}")
        st.write(f"**Liabilities:** ₹{liabilities:,.2f}")
        st.write(f"**Equity:** ₹{equity:,.2f}")
        st.write(f"**Indirect Expense:** ₹{indirect_exp:,.2f}")
        st.write(f"**Direct Expense:** ₹{direct_exp:,.2f}")
        st.write(f"**Adjusted Equity:** ₹{adjusted_equity:,.2f}")
        st.write(f"**Liabilities + Adjusted Equity:** ₹{(liabilities + adjusted_equity):,.2f}")

        if abs(difference) < 0.01:
            st.success("✅ The balance sheet is balanced!")
        else:
            st.error(f"❌ Not balanced! Difference: ₹{difference:,.2f}")

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload an Excel file to continue.")
