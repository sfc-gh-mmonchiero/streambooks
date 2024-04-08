import streamlit as st

code_list = []


@st.experimental_fragment
def cell(key):
    with st.container(border=True):
        text = st.text_area("Type here", key=f"text_area{key}")
        if text:
            exec(text, None, st.session_state.my_locals)
        st.button("Run cell", key=f"button{key}")

def cell_list(key):
    text = st.text_area("Type here", key=key)
    if text:
        compiled = compile(text, "", "exec")
        placeholder = st.container(border=True)
        code_list.append((compiled, placeholder))

@st.experimental_fragment
def frag_exec(e):
    with e[1]:
        exec(e[0], None, st.session_state.my_locals)

def cell_co():
    i = 0
    while True:
        text = st.text_area("Type here", key=i)
        if text:
            exec(text)
            i = i + 1
        else:
            yield

def main():
    if 'my_locals' not in st.session_state:
        st.session_state.my_locals = {}

    st.title("My Streambook")

    # this is cute, but not exactly a notebbok... sementic is driven by "clicks"
    # cell_co().__next__()

    with st.sidebar:
        rows = st.number_input("Number of rows", 3)
        if st.button("Rerun"):
            st.rerun()
    for i in range(rows):
        cell(i)
    #for e in code_list:
    #   frag_exec(e)



if __name__ == "__main__":
    main();
