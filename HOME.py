import streamlit as st
from streamlit_extras.streaming_write import write
import time
from streamlit_card import card


st.set_page_config(
    page_title="Home",
    page_icon="⌂",
)

header = """# THE COMPUTER INTELLIGENCE CLUB"""
description = """
- ##### Discover our [mission](), meet our talented team, and join us in upcoming events.
- ##### Dive into insightful [newsletters and blogs](), connecting with a community passionate about computing intelligence.
- ##### Ready to embark on a journey of knowledge and collaboration? [Join us]() and be part of the Computer Intelligence Club - where intelligence meets community!

"""


def stream_header():
    for word in header.split():
        yield word + " "
        time.sleep(0.1)
write(stream_header)

st.markdown("""<hr style="border:3px solid rgb(255,255,255) ">""", unsafe_allow_html=True)

write(description)

st.text("")
st.text("")
st.text("")

st.markdown("""# Featured Events""")

st.markdown("""<hr style="border:3px solid rgb(255,255,255) ">""", unsafe_allow_html=True)

featured_events = ["Website Design Contest", "Lorem Ipsum"]
descriptions = ["The Computer Intelligence Community is thrilled to announce the \"Website Design Development Contest\". Participants are encouraged to create user-friendly websites, focusing on clear navigation and essential pages such as landing, home, contact us, activities, events, newsletters, and magazines. The winning designer will receive a Certificate of Appreciation, recognizing their outstanding contribution to enhancing the online presence of the Computer Intelligence Community.", 
                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"]
image_links = ["https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "https://images.unsplash.com/photo-1510936111840-65e151ad71bb?q=80&w=2090&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"]
cols = st.columns(len(featured_events))
   
for i in range(len(cols)):
    hasClicked = card(
        styles={
            "card":{
                "width": "auto",
                "margin": "10px",
                "padding":"10px",
                "background-color":"black"
                },
            "text":{

            }},
        title=featured_events[i],
        text=descriptions[i],
        image=image_links[i]
    )

st.markdown("""
    <div align="right" style="padding: 4px">
        <img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" style="width: 30px; height: 30px;">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 30px; height: 30px; filter: invert(1)">
        <img src="https://cdn4.iconfinder.com/data/icons/social-media-black-white-2/600/Instagram_glyph_svg-512.png" style="width: 30px; height: 30px; filter: invert(1);">
    </div>
""", unsafe_allow_html=True)

