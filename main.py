import streamlit as st
import cloud
import matplotlib.pyplot as py


st.set_page_config(layout="wide", page_title="Wikipedia Wordcloud", page_icon="☁️")

# page setup
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Wikipedia Wordcloud Generator</h1>", unsafe_allow_html=True)

phrase = st.text_input('Search Word or Phrase', 'Wikipedia', help='Write any word or phrase to be searched on Wikipedia')

with st.spinner('Loading...'):
    # plotting
    wcloud = cloud.get_cloud(phrase)
    image = py.figure(figsize=(20,10), facecolor='k')
    py.imshow(wcloud)
    py.axis("off")
    py.tight_layout(pad=0)
    st.pyplot(image)
