import streamlit as st
from streamlit_card import card
from blogs import example_collection

titles = ["Demo-Uber pickups in NYC", "Demo-Langchain", "Demo-Chat with Search"]
keys = ["uber", "langchain", "chat_with_search"]

for i in range(len(titles)):
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
        on_click=getattr(example_collection, keys[i]),
        title=titles[i],
        text="",
    )
