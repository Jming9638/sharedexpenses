import streamlit as st

def summary_res(total, result):
    t_col = st.columns([0.25,1])
    with t_col[0]:
        st.header("Summary:")
    with t_col[1]:
        st.write("")
        st.write("")
        st.markdown("Total spend: **RM {:.2f}**".format(total))
    st.write('')
    
    max_name = len(max(result.columns, key=len))
    name_space = round(max_name/18, 2) - 0.01
    col = st.columns([name_space, 0.7, 0.4, 0.7, name_space, 1.8])
    for i in result.columns:
        for j in result.index:
            amount = result.loc[j,i]
            if amount > 0:
                with col[0]:
                    st.write("**{}**".format(i))
                with col[1]:
                    st.write("="*15)
                with col[2]:
                    st.write("**RM {:.2f}**".format(amount))
                with col[3]:
                    st.write("="*14+">")
                with col[4]:
                    st.write("**{}**".format(j))
