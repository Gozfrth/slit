import streamlit as st
from streamlit_card import card
from pages.blogs.example_collection import *

titles = {"Demo-Uber pickups in NYC": uber,
          "Demo-Langchain": langchain,
          "Demo-Chat with Search": chat_with_search}

for title, function in titles.items():
    hasClicked = card(
        styles={
            "card": {
                "width": "auto",
                "margin": "10px",
                "padding": "10px",
                "background-color": "black"
            },
            "text": {}
        },
        on_click=function,
        title=title,
        text="",
    )