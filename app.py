import streamlit as st
st.set_page_config(page_title='Spanish Access Tool', layout='wide')

home_page = st.Page('home_page.py', title='Home')
edit_page = st.Page('edit_page.py', title='Add Your Own Translations')
reflections_page = st.Page('reflections.py', title='Personal Reflections')

pg = st.navigation([home_page, edit_page, reflections_page])
pg.run()