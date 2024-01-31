import streamlit as st
import time

description = """
<style> h1{color: red;}</style> <h1>Discover</h1> our <strong>mission</strong>, meet our talented team, and join us in upcoming <em>events</em>.
Dive into insightful <a href="#">newsletters</a> and <a href="#">blogs</a>, connecting with a community passionate about computing intelligence.

Ready to embark on a journey of knowledge and collaboration? Join us and be part of the <strong>Computing Intelligence Club</strong> - where intelligence meets community!
"""

st.markdown(description, unsafe_allow_html=True)