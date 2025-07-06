import streamlit as st
import json
from utils.calc import calculate_equity_score

st.title("Valunauts: DeFi Equity Score PoC v0.3")

st.markdown("""
#### Input your protocol data or use the sample data below to test the Equity Score.
""")

uploaded_file = st.file_uploader("Upload sample_wallets.json", type="json")
if uploaded_file:
    data = json.load(uploaded_file)
else:
    with open("data/sample_wallets.json") as f:
        data = json.load(f)
    st.info("Loaded default sample_wallets.json")

score = calculate_equity_score(data)
st.subheader("Equity Score")
st.write(score)
