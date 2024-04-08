import streamlit as st
from subprocess import Popen, PIPE
import shlex

@st.experimental_fragment
def box(key):
    text = st.text_area("Type here", key=key)
    if text:
        exec(text)

def main():
    with st.sidebar:
        rows = st.number_input("Number of rows", 1)

    st.title("My Streambook")
    for i in range(rows):
        box(i)

if __name__ == "__main__":
    main();
