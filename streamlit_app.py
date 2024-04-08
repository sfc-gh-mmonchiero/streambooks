import streamlit as st

@st.experimental_fragment
def cell(key):
    with st.container(border=True):
        text = st.text_area("Type here", key=f"text_area{key}")
        if text:
            exec(text, None, st.session_state.my_locals)
        st.button("Run cell", key=f"button{key}")

def main():
    if 'my_locals' not in st.session_state:
        st.session_state.my_locals = {}

    st.title("My Streambook")

    with st.sidebar:
        rows = st.number_input("Number of rows", 3)
    for i in range(rows):
        cell(i)

if __name__ == "__main__":
    main();
