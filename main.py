import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('web-images/bmw.png')

with col2:
    st.title('Olwethu Mbane')
    content1 = "The Realest One Out"
    st.write(content1)

content2 = '''
Below you can find some apps that I built in python. Feel free to Reach out to me!
'''
st.write(content2)