import streamlit as st
import app1 as ap

org_name="123"
org_pass="119@J"
username = st.text_input("Username", placeholder="Enter Username")
password = st.text_input("Password", type="password", placeholder="Enter Password")

if st.button("login"):
    if org_name==username:
        if org_pass==password:
            ap.main()
        else:
            st.error("password is worng contact 22ucs119")
    else:
        st.error("username is worng da")
