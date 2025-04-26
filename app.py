import streamlit as st
import app1 as ap

org_name = "admin"
org_pass = "password"
name = st.empty()
passwo = st.empty()

username = name.text_input("Username", placeholder="Enter Username")
password = passwo.text_input("Password", type="password", placeholder="Enter Password")

if st.button("login"):
    if org_name == username:
        if org_pass == password:
            name.empty()
            passwo.empty()
            #ap.main()
            st.title("http://android-akm.streamlit.app/Nagaraju/juju/Pu-error")
        else:
            st.error("Password is wrong. Contact AKM.")
    else:
        st.image("bg.png")
        st.error("Username is wrong.")
