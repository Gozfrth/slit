import streamlit as st

join_us = """
    ## JOIN THE COMPUTER INTELLIGENCE CLUB
"""

st.markdown(join_us)

st.write("")
st.write("")
st.write("")

with st.form("join_form"):
    col1, col2 = st.columns(2)
    name = col1.text_input(label="FULL NAME*")

    email = col2.text_input(label="EMAIL*")

    usn = col1.text_input(label="USN",  placeholder="Optional")

    department = col2.text_input(label="DEPARTMENT", placeholder="Optional")

    membership_type = st.selectbox("MEMBERSHIP TYPE*", ("Community", "Student", "Alumni", "Faculty/Advisor"))

    description = st.text_input(label="WHY DO YOU WANT TO JOIN THIS CLUB?",  placeholder="Optional")

    st.form_submit_button("JOIN US!", type="primary")