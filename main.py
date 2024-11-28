import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('web-images/bmw.png')
    

with col2:
    st.title('Olwethu Mbane')
    content1 = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
    the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
    """
    st.info(content1)

content2 = '''
Below you can find some apps that I built in python. Feel free to Reach out to me!
'''
st.write(content2)

col3,col4 =st.columns(2)
df = pd.read_csv('data.csv',sep=';')
print(df)

with col3:

    for index, row in df[::2].iterrows():

        st.header((row['title']))
        st.write(row['description'])
        st.image(f'web-images/{row['image']}')
        st.write(f"[source code]({row['url']})")
        

with col4:

    for index, row in df[1::2].iterrows():

        st.header((row['title']))
        st.write(row['description'])
        st.image(f'web-images/{row['image']}')
        st.write(f"[source code]({row['url']})")
