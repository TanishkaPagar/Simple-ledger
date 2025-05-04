import streamlit as st

# Initialize session state to store the ledger across interactions
if "ledger" not in st.session_state:
    st.session_state.ledger = []

st.title("Simple Transaction Ledger")

# Input for new transaction
transaction = st.number_input("Enter transaction amount:", step=1)

# Button to add transaction
if st.button("Add Transaction"):
    st.session_state.ledger.append(transaction)
    st.success(f"Transaction of {transaction} added to the ledger.")

# Display current ledger
st.subheader("Current Ledger")
st.write(st.session_state.ledger)
