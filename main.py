import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="TikTok Data Privacy Dashboard", layout="wide")
st.title("🇺🇸 TikTok Data Privacy Dashboard")
st.markdown("Simulating TikTok's USDS (U.S. Data Security) compliance system 🛡️")

# Fetch data from FastAPI
response = requests.get("http://127.0.0.1:8000/data")
data = response.json()["users"]
df = pd.DataFrame(data)

# Display the data
st.subheader("📁 User Data Overview")
st.dataframe(df)

# Charts
st.subheader("📊 Data by Region")
st.bar_chart(df["region"].value_counts())

st.subheader("🧩 Compliance Status")
st.bar_chart(df["status"].value_counts())

# Alerts
if "Non-Compliant" in df["status"].values:
    st.error("⚠️ Data outside U.S. detected! Immediate review required.")
else:
    st.success("✅ All user data compliant within U.S. boundaries.")
