import streamlit as st


#All demos from https://github.com/streamlit


def uber():
    import pandas as pd
    import numpy as np
    
    st.title('Uber pickups in NYC')
    
    DATE_COLUMN = 'date/time'
    DATA_URL =  ('https://s3-us-west-2.amazonaws.com/'
             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    
    @st.cache_data
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        incre = lambda x: int(x) + 1
        data.rename(lowercase, axis='columns', inplace=True)
        data.rename(incre, axis=0, inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    
    data_load_state = st.text('Loading Data...')
    
    data = load_data(10000)
    
    data_load_state.text("Done! (using st.cache_data)")
    
    if st.checkbox("Show raw data"):
        st.subheader('Raw Data')
        st.write(data)
    
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,25))[0]
    
    st.bar_chart(hist_values)
    
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)
    
    #ADD MAP

def langchain():
    from langchain.llms import OpenAI

    st.title("🦜🔗 Langchain Quickstart App")

    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


    def generate_response(input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))


    with st.form("my_form"):
        text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
        submitted = st.form_submit_button("Submit")
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
        elif submitted:
            generate_response(text)

def chat_with_search():

    from langchain.agents import initialize_agent, AgentType
    from langchain.callbacks import StreamlitCallbackHandler
    from langchain.chat_models import ChatOpenAI
    from langchain.tools import DuckDuckGoSearchRun

    with st.sidebar:
        openai_api_key = st.text_input(
            "OpenAI API Key", key="langchain_search_api_key_openai", type="password"
        )
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

    st.title("🔎 LangChain - Chat with search")

    """
    In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
    Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
    """

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
        search = DuckDuckGoSearchRun(name="Search")
        search_agent = initialize_agent(
            [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
        )
        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
