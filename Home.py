import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")

st.write("""

At [Company Name], we're dedicated to revolutionizing [industry/niche] through
innovation, integrity, and excellence. As a leading [describe industry/niche]
company, we pride ourselves on delivering high-quality [products/services] that
exceed our customers' expectations.
Our team of skilled professionals is committed to pushing the boundaries of
what's possible in [industry/niche]. Through cutting-edge research, advanced
technology, and a customer-centric approach, we continuously strive to set new
standards of excellence.

""")

st.header("Our Team")

df = pd.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].capitalize() + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].capitalize() + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].capitalize() + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        

