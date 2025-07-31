import streamlit as st
from add_update_ui import add_update
from analytics_category_ui import analytics_by_category
from analytics_month_ui import analytics_by_month


st.title("Expense Tracking System")

tab1,tab2,tab3=st.tabs(["Add/Update","Analytics by Category","Analytics by Month"])

with tab1:
    add_update()
with tab2:
    analytics_by_category()
with tab3:
    analytics_by_month()





