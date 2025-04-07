import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('linea_temp.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
