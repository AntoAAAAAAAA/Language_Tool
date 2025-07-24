import streamlit as st
import pandas as pd
from functions import get_data, save_data

df = get_data() # this gives df = st.session_state.df

# User can make changes and input data into df, then at the end ....

st.session_state.df = df # edited_df

if st.button('Save'):
    st.session_state['df'].to_csv('initial.csv')
    st.success('Saved to Disk')