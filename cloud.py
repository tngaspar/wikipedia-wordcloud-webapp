from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import wikipedia
import matplotlib.pyplot as py
import streamlit as st


def create_cloud(content):
    #mask = np.array(Image.open("search1.png"))
    cloud = WordCloud(mode="RGBA" , background_color="rgba(255, 255, 255, 0)", max_words = 300, stopwords = STOPWORDS, height=800, width=1600)
    cloud.generate(content)
    #image_colors = ImageColorGenerator(mask)
    #cloud = cloud.recolor(color_func=image_colors)
    return cloud

def get_content(phrase):
    
    try:
        page = wikipedia.page(phrase, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        page = wikipedia.page(e.options[0])
    return page.content, page.url
    
@st.cache(show_spinner=False)
def get_cloud(phrase):
    content, url = get_content(phrase)
    cloud = create_cloud(content)
    return cloud, url

