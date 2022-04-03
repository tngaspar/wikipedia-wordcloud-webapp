import streamlit as st
import cloud
import matplotlib.pyplot as py


st.set_page_config(layout="wide", page_title="Wikipedia WordCloud", page_icon="☁️")

# page setup
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin:0px;'>Wikipedia WordCloud Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin:1px;'>A simple tool to create WordClouds from Wikipedia searches.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin:1px;'>Check out the source code <a href='https://github.com/tngaspar/wikipedia-wordcloud-webapp' target='_blank'>here</a>.</p>", unsafe_allow_html=True)

phrase = st.text_input('Search Word or Phrase', 'wikipedia', help='Write any word or phrase to be searched on Wikipedia')

with st.spinner('Loading...'):
    # plotting
    try:
        wcloud , url= cloud.get_cloud(phrase)
        st.markdown("<p>Page found: <a href="+url+" target='_blank'>"+url+"</a></p>", unsafe_allow_html=True)
    except:
        st.warning(phrase + ' not found. Try another Word or Phrase.')  
        st.stop()
    try:
        image = py.figure(figsize=(20,10), facecolor='k')
        py.imshow(wcloud)
        py.axis("off")
        py.tight_layout(pad=0)
        st.pyplot(image)
    except:
        st.error('An error occurred. Please try again.')  
        st.stop()
