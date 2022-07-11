import streamlit as st

from module.input_page import input_function

if 'elem' not in st.session_state:
    st.session_state['elem'] = []
if 'count' not in st.session_state:
    st.session_state['count'] = 1
if 'name_list' not in st.session_state:
    st.session_state['name_list'] = []
else:
    st.session_state['name_list'] = []


def run():
    st.set_page_config(page_title="Shared Expense Calculator", page_icon=":airplane:", layout='wide')
    st.title("💰 Shared Expenses Calculator")
    
    input_function()

if __name__ == "__main__":
    run()
