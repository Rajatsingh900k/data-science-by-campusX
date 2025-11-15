import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header("Indian startups")
st.subheader("How to build a tycoon?")
st.write("Becaoming a business tycoon ")
st.markdown('- Hello')
st.latex("x^2")
st.code('cout<<"Hello World"')
df=pd.DataFrame({
    "name":['Rajat','Ayush','Anushka'],
    "marks":[50,60,70],
    "package":[4.5,4.5,4.5]
})

st.dataframe(df)

st.metric('Revenue','Rs. 3 lakhs', '-3%')
st.metric('Revenue','Rs. 3 lakhs', '3%')

st.json({
    "name":['Rajat','Ayush','Anushka'],
    "marks":[50,60,70],
    "package":[4.5,4.5,4.5]
})

st.image('./Content/1.png')
# st.video('path') for video
# st.audio('path') for audio

st.sidebar.title("Sidebar title")

col1,col2=st.columns(2)

with col1:
    st.image('./Content/1.png')
with col2:
    st.image('./Content/1.png')

st.error("login failed")
st.success("Login Successful")
st.warning("Hell Naw")
st.info('welcome')

bar=st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)


email=st.text_input("Enter your Email")
num=st.number_input("Enter number")
date=st.date_input("Enter a date")
