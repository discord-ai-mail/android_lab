import streamlit as st
import app1 as ap
st.markdown("""<center><h1 style="color:yellow;">SJC KIDDOS</h1></center>""",unsafe_allow_html=True)
org_name="admin"
org_pass="password"
name=st.empty()
passwo=st.empty()
username = name.text_input("Username", placeholder="Enter Username")
password = passwo.text_input("Password", type="password", placeholder="Enter Password")

if st.button("login"):
    if org_name==username:
        if org_pass==password:
            name.empty()
            passwo.empty()
            ap.main()
        else:
            st.error("password is worng contact AKM")
    else:
        st.image("bg.png")
        st.error("username is worng")
