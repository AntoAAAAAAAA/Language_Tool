import streamlit as st

st.title('My Reflections')
st.divider()



st.text('I completed this project after finishing the Health Literacy App. Like that project, this app wasn’t focused on data analysis but instead prioritized specific user-facing functionality. It was genuinely fun to make. I enjoyed combining several new Streamlit skills into one cohesive tool and seeing how far I’ve come in building interactive web apps.')

st.text('Learning how to use session_state in Streamlit has been incredibly helpful. Creating filter toggles for the main DataFrame and applying masking logic was something I picked up with the help of AI. Using st.data_editor() instead of st.dataframe() was especially useful when implementing the favorites column. That part was tricky, but also really gratifying once I got it to work. As with many Streamlit features, the hardest part was ensuring user inputs remained persistent across page changes and reloads. To solve this, I stored the favorites data in session_state and read from it throughout the app. Another fun challenge was ensuring that favorite selections didn’t disappear when toggling filters—this required careful logic and some creative use of OR conditions to preserve row visibility.')

st.text('One of my favorite parts of the app is the page where users can edit the phrase dataset themselves. While the logic behind it was fairly straightforward, it was satisfying to get it working cleanly. This project was also my first time working with the deep_translator and unicodedata packages. I found deep_translator surprisingly simple to implement and powerful in functionality.')

st.text('This project was relatively simple overall, but it included unique challenges that required thoughtful solutions. I’m happy with how it turned out, and I think there’s a real chance it could be useful in real-world settings. Still, like most of my projects, I don’t expect immediate adoption. These tools are primarily ways for me to practice coding, explore data science principles, and gain hands-on experience with web development.')

st.text('Looking ahead, I’m excited to keep pushing myself. Each project builds on the last—not just in technical ability, but in creativity and design thinking. The Language Access Tool reminded me how fulfilling it is to create something that’s not only functional but purposeful. I hope to keep expanding both the complexity and the impact of my projects in the months to come.')