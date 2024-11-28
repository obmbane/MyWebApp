import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('web-images/bmw.png')
    

with col2:
    st.title('Olwethu Mbane')
    content1 = """
    Realest one out!\n
    Taking over \n
    watch this space
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
        #if index % 2 ==0:
        st.header((row['title']))
        st.write(row['description'])
        st.image(f'web-images/{row['image']}')
        st.write(f"[source code]({row['url']})")
        

with col4:

    for index, row in df[1::2].iterrows():
        #if index % 2 !=0:
        st.header((row['title']))
        st.write(row['description'])
        st.image(f'web-images/{row['image']}')
        st.write(f"[source code]({row['url']})")
