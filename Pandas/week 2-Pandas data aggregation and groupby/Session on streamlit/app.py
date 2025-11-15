import streamlit as st
import pandas as pd
# email=st.text_input("enter email")
# password=st.text_input("enter password")
# gender=st.selectbox("Select Gender",["Male","Female","Others"])


# login_btn=st.button('Login')

# if login_btn:
#     if email=="rajatsingh123@gmail.com" and password=="1234":
#         st.balloons()
#         st.success("Login Successful")
#         st.write(gender)
#     else:
#         st.error("Login Fail")

file=st.file_uploader('Upload a file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())