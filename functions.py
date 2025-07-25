import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('initial.csv', index_col='ID') #st.session_state.df
    df.columns = df.columns.str.strip()  # standardize column names
    df['Template'] = df['Template'].astype(bool) # ensure templates 1/0 value are boolean 
    df['Favorites'] = False # Make an empty Favorites column 
    return df

def get_data():
    if 'df' not in st.session_state:
        base = load_data()
        st.session_state.df = base.copy()
        st.session_state.original_df = base.copy()
    return st.session_state.df

def save_data():
    df = st.session_state["df"]
    if df.index.name is None:
        df.index.name = "ID"
    df.to_csv("initial.csv", index=True, index_label="ID")