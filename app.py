import streamlit as st
st.set_page_config(page_title='Spanish Access Tool', layout='wide')

home_page = st.Page('home_page.py', title='Home')

pg = st.navigation([home_page])
pg.run()