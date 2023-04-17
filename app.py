#!/usr/bin/env python
# coding: utf-8

# In[10]:



import numpy as np
import pandas as pd
import streamlit as st 

def calc(x,y,req):
    x=float(x)
    y=float(y)
    if (req=='+'):
        prediction=x+y
    elif(req=='-'):
        prediction=x-y
    elif(req=='*'):
        prediction=x*y
    elif(req=='/'):
        prediction=x/y
    
    print(prediction)
    return prediction



def main():
    st.title("Calculator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Calculator ML App </h2>
    <p style="color:white;text-align:center;">(use +,-,*,/ for any operation) </p>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    x = st.text_input("X","Type Here")
    y = st.text_input("Y","Type Here")
    req = st.text_input("Provide symbol for any operation","Type Here")
    result=""
    if st.button("Predict"):
        result=calc(x,y,req)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    





