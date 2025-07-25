import streamlit as st
import pandas as pd
from functions import get_data, save_data
from deep_translator import GoogleTranslator

df = get_data() # this gives df = st.session_state.df

st.header('Editor')
st.divider()
st.text("In the table below, you can make changes by double-clicking a cell to edit the content inside. " \
"If you would like an easier way to add an english phrase with it's spanish translation, scroll down and use the user inputs.")



edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")
st.session_state.df = edited_df
df = st.session_state.df
st.divider()


# User inputs English phrase 
st.markdown("## ")
col1, col2 = st.columns(2)
col1.text('Type english phrase here: ')
eng = col1.text_area('')

# translation 
def translate():
    return GoogleTranslator(source='en', target='es').translate(eng)
translated = ''
if eng:
    with st.spinner('Translating'):
        translated = translate()

# Output spanish 
col2.text('Spanish Translation:')
col2.markdown('###### ')
if eng:
    col2.text(translated)

# Additional Selection 
category = df['Category'].dropna().unique()
category_choice = st.selectbox('Select a Category:', category, index=None)
note = st.text_input('Add a note (optional): ')
pronunciation = st.text_input('Add a phonetic pronunciation (optional): ')



st.markdown('')
if st.button('Add to translation table'):
    new_id = df.index.max() + 1 if df.index.dtype.kind in "iu" else len(df) # Makes sure that the row is added in a new index 
    new_row = {
        "English": eng,
        "Spanish": translated,
        "Category": category_choice or "",
        "Note": note or "",
        "Pronunciation": pronunciation or "",
    }
    df.loc[len(df)] = new_row # creation of edited df with new row 
    st.session_state.df = df # update session state
st.divider()

st.markdown("# ")
if st.button('Save'): 
    save_data()
    st.toast('Saved to Disk!')