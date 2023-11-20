import streamlit as st
import pandas as pd


st.set_page_config()

#Las dos columnas
col1, col2 = st.columns(2)

with col1: 
    #image = methos creates image
    st.image('images/photo.png', width=400)

with col2:
    st.title('Andrés Lozano')
    content = '''Hi I'm Andrés! I am a linguist with computational skills, working in projects related to narrativity, unit detection and more!!! 
    I did graduate in 2023 with a Master's degree in literature, working with narrativity in games and computational linguistics.
    I have worked with an intership contract in BVMC as an editor with experiece in XML, Indesign and more! 
    Right now I'm working in new projects related to machine learning an unit detections, hope you find this page interesting. 
    '''    
    st.info(content)

content2 = '''Below you can find some of the apps I have built in Python. Feel free to contact me!
'''

st.write(content2)
#We use Pandas to get the content from the CSV. 
col3, emptycol,  col4 = st.columns([1.5, 0.5, 1.5])

#Separator = ;.
df = pd.read_csv('data.csv', sep=';') 


with col3: 
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        #Like in Markdown. I don't like the write result (Change)
        st.write(f'[Source Code]({row["url"]})')


#Partes las columnas por la mitad [0:10], el resto se imprimen aquí. 
with col4: 
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')
