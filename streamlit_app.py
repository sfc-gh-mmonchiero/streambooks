import streamlit as st

code_list = []

@st.experimental_fragment
def box(key):
    # restore state
    text = st.text_area("Type here", key=key)
    if text:
        exec(text)
    # save state

def box_co(key):
    text = st.text_area("Type here", key=key)
    if text:
        compiled = compile(text, "", "exec")
        code_list.append(compiled)


def main():

    with st.sidebar:
        rows = st.number_input("Number of rows", 3)

    st.title("My Streambook")
    for i in range(rows):
        box_co(i)
    for e in code_list:
        exec(e)
    cose_list = []



if __name__ == "__main__":
    main();
