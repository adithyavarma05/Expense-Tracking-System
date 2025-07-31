import streamlit as st
import requests
import pandas as pd


API_URL="http://127.0.0.1:8000"

def analytics_by_month():
    st.title("Expense Breakdown By Month")
    response=requests.get(f"{API_URL}/analytics_month/")
    if response.status_code==200:
        data=response.json()
    else:
        st.error("Failed to retrieve data")
        data=[]

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    months_data={
        "Months":[row["month_name"] for row in data],
        "Total":[row["total"] for row in data]
    }
    df=pd.DataFrame(months_data)
    df["Months"] = pd.Categorical(df["Months"], categories=month_order, ordered=True)
    df=df.set_index("Months")
    st.bar_chart(data=df)
    st.table(df)

