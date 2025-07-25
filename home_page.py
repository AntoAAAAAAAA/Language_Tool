import streamlit as st
import pandas as pd
import unicodedata
from functions import load_data, get_data, save_data

st.title('Language Access Tool (Spanish)')
st.text('This dashboard was made to help healthcare professionals ease the very common language ' \
'barrier experienced by Spanish-speaking patients in Texas.')
st.divider()

# Load data from initial.csv and put it into df
get_data()
df = st.session_state.df


# Save button will any changes to the 'disk' by changing the csv itself
if st.button('**Save**'):
    save_data()
    st.toast('Saved to Disk')


# Initialize favorites in session_state
if 'Favorites' not in st.session_state:
    st.session_state['Favorites'] = set()
# Load favorites into the dataframe 
df['Favorites'] = df.index.isin(st.session_state['Favorites'])


# Search inputs
templates = st.sidebar.toggle('Only Templates')
note = st.sidebar.toggle('Show Notes')
phon = st.sidebar.toggle('Show Phonetics')
query = st.sidebar.text_input('Search here:')

categories = df['Category'].dropna().unique() #search categories 
chosen_cat = st.sidebar.multiselect('Select Categories', categories)
if not chosen_cat: #sets normal categories as default
    chosen_cat = categories


# Make mask and filter data 
mask = df['Category'].isin(chosen_cat)
if query:
    q_norm = unicodedata.normalize('NFKD', query).casefold()
    mask &= (
    df['English'].str.normalize('NFKD').str.casefold().str.contains(q_norm, regex=False, na=False) |
    df['Spanish'].str.normalize('NFKD').str.casefold().str.contains(q_norm, regex=False, na=False)
    )
# Apply mask for templates toggle 
if templates:
    mask &= df['Template']

# Apply mask to data
view = df.loc[mask].copy()

# Toggle outputs 
if not phon and "Pronunciation" in view.columns:
    view.drop(columns=["Pronunciation"], inplace=True)
if not note and "Note" in view.columns:
    view.drop(columns=["Note"], inplace=True)

# Drop the template column 
view.drop(columns=['Template'], inplace=True)


# Display table unless it is empty 
edited = st.data_editor(
view,
use_container_width=True,
hide_index=True,
column_config={'Favorites': st.column_config.CheckboxColumn(
    label='⭐️',
    help="Click to add/remove from favorites",
    width="small"
)}
)
if view.empty:
    st.info('No results found')

# Persist favourites without losing hidden ones 
new_favs_in_view = set(edited.loc[edited['Favorites']].index) #newly selected favorites 
rows_in_view     = set(edited.index) #rows that the user is looking at 
prev_favs        = st.session_state['Favorites']

st.session_state['Favorites'] = (prev_favs - rows_in_view) | new_favs_in_view 
# (PF - RIV): makes sure that if you uncheck something in the new view, it goes away
# new favs shows what the newly selected favorites are
# the | allows for intersection between the newly edited group of old favs and the group of new favs 

@st.dialog('Are you sure you want to reset data?')
def dialogue():
    st.write('Resetting data will reset your current translations all back to the original dataset that came when this app was first ran.')
    st.write('Press Yes, to continue, otherwise press Cancel.')
    col1, col2, col3, col4 = st.columns(4)
    if col2.button('Yes'):
        st.session_state.df = st.session_state.original_df.copy()
        st.toast('Data Reset to Original Translations')
    if col3.button('Cancel'):
        st.rerun()

if st.button('**Reset Data**'):
    dialogue()
