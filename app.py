import pandas as pd
import streamlit as st

st.title("My FTest Dashboard")
df = pd.DataFrame({"month": ["Jan","Feb","Mar"],"sales":[500,150,120]})
st.bar_chart(df,x="month",y="sales")
st.dataframe(df)