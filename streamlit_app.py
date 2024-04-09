import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

@st.experimental_fragment
def cell(key):
    with st.container(border=True):
        text = st.text_area("Type here", key=f"text_area{key}")
        if text:
            try:
                exec(text, None, st.session_state.my_locals)
            except Exception as e:
                st.exception(e)
        st.button("Run cell", key=f"button{key}")

def main():
    if 'my_locals' not in st.session_state:
        st.session_state.my_locals = {}

    st.title("My Streambook")
    intro_markdown = read_markdown_file("README.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)


    with st.sidebar:
        rows = st.number_input("Number of rows", 5)
    for i in range(rows):
        cell(i)

if __name__ == "__main__":
    main();
