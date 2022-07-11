import streamlit as st
import pandas as pd

from .sidebar import sidebar
from .results import transform_result
from .summary import summary_res

def input_function():
    input_name = sidebar()
    name_list = ['-Select name-', 'Select All']
    for name in input_name:
        if name not in name_list and name != "":
            name_list.append(name)
            
    input_col = st.columns([1, 1, 2, 1])
    with input_col[0]:
        ph1 = st.empty()
        paid = ph1.selectbox('Who paid?', [n for n in name_list if len(name_list)>=1 and n!="Select All"])
    with input_col[1]:
        ph2 = st.empty()
        amount = ph2.text_input('Amount')
    with input_col[2]:
        ph3 = st.empty()
        for_ = ph3.multiselect('Paid for who?', [x for x in name_list if len(name_list)>2 and x!="-Select name-"])
        if for_ == ['Select All']:
            own = ', '.join([str(elem) for elem in name_list if elem!="-Select name-" and elem!="Select All"])
        else:
            own = ', '.join([str(elem) for elem in for_])
    with input_col[3]:
        ph4 = st.empty()
        item = ph4.text_input('Item/Activity')
        
    btn_col = st.columns([0.6,0.6,2,1,1])
    with btn_col[0]:
        input_btn = st.button("Add")
        if input_btn and paid != '-Select name-' and amount != '' and own != '':
            st.session_state['elem'].append([paid, round(float(amount),2), own, item])
            
    with btn_col[1]:
        delete_btn = st.button("Delete")
        if delete_btn:
            try:
                del st.session_state['elem'][-1]
            except:
                with btn_col[2]:
                    st.write("")
                    st.write("No more rows.")
                    
    input_list = st.session_state['elem']
    
    if len(input_list) >= 1:
    
        st.write('')
        st.write('Edit your value if input wrongly.')
        col2 = st.columns([1,1,1])
        with col2[0]:
            rn = st.selectbox('Which row?', range(len(input_list)))
            if rn is not None and rn != '':
                try:
                    rn = int(rn)
                except:
                    rn = 0
            
        with col2[1]:
            cn = st.selectbox('Which column?', ('-Select column-', 'paid', 'amount', 'for', 'item'))
            if cn == 'paid':
                cname = 0
            elif cn == 'amount':
                cname = 1
            elif cn == 'for':
                cname = 2
            elif cn == 'item':
                cname = 3
            
        with col2[2]:
            ph33 = st.empty()
            if cn == 'paid':
                val = ph33.selectbox('Replace with:', [n for n in name_list if len(name_list)>=1 and n!="Select All" and n!="-Select name-"])
            elif cn == 'for':
                val = ph33.multiselect('Replace with:', [x for x in name_list if len(name_list)>2 and x!="-Select name-"])
                if val == ['Select All']:
                    val = ', '.join([str(elem) for elem in name_list if elem!="-Select name-" and elem!="Select All"])
                else:
                    val = ', '.join([str(elem) for elem in val])
            else:
                val = ph33.text_input('Replace with:')
        
        modify_btn = st.button("Update value")
        if modify_btn and cn != '-Select column-':
            try:
                st.session_state['elem'][rn][cname] = float(val)
            except:
                st.session_state['elem'][rn][cname] = val
        
        df_input = pd.DataFrame(input_list, columns=['paid', 'amount', 'for', 'item'])
        total = df_input['amount'].sum()
        st.header("Raw Data:")
        st.write(df_input)
        
        result = transform_result(df_input)
        # st.header("Result:")
        # st.write(result.style.format("{:.2f}"))
        
        summary_res(total, result)
        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        bottom_col = st.columns([3, 5, 3])
        with bottom_col[1]:
            st.write("---------------End of the page---------------")
