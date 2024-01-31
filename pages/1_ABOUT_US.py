import streamlit as st
from streamlit_extras.streaming_write import write
import time


st.set_page_config(
    page_title="Home",
    page_icon="⌂",
)

header = """# ABOUT US"""
description = """
##### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse est libero, auctor ac purus dignissim, consectetur maximus massa. Cras non massa vel tortor porttitor accumsan. Vivamus eget cursus orci, quis interdum nisi. In et elementum eros. Mauris vel ornare tortor, nec tempor nisl. Etiam iaculis tincidunt ligula, eu rhoncus dui pretium ac. Donec ultrices lobortis erat, et laoreet elit vestibulum porttitor.
##### Nunc viverra justo eu consequat iaculis. Suspendisse malesuada vel mi id convallis. Phasellus euismod, dui id euismod volutpat, est ligula molestie mauris, id congue nisl metus et ante. Morbi finibus ante nec sem scelerisque lobortis. Mauris volutpat dui sapien, sed molestie ipsum ultrices sit amet. Maecenas gravida sapien vitae sapien semper, eu luctus lorem venenatis. Mauris faucibus ex eros, sit amet dictum sem venenatis tristique. Sed sed tristique massa. Aliquam tellus libero, dapibus a ante sit amet, euismod suscipit risus.

"""

team_members = ["John", "Doe", "Bob"]

club_achievements="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""


def stream_header():
    for word in header.split():
        yield word + " "
        time.sleep(0.1)
write(stream_header)

st.markdown("""<hr style="border:3px solid rgb(255,255,255) ">""", unsafe_allow_html=True)

st.write(description)



# ADD MEMBERSHIP INFORMATION. WHAT WOULD MEMBERS GAIN FROM JOINING THE CLUB/COMMUNITY? 



st.write("")
st.write("")
st.write("")

st.markdown(f"""
    ### Team Members
    <div>{' '.join(str + "&nbsp &nbsp" for str in team_members)}</div>
""", unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.write("### Collaborations and Partnerships")

st.write("___")