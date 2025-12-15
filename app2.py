import streamlit as st
import time

st.title("🚀 My First Deployed App")

st.write("If you can see this on the web, the deployment worked!")

# A simple interactive element
name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}! Welcome to your live website.")
    
    # A simple animation to prove it's running python logic
    if st.button("Launch Rocket"):
        with st.status("Preparing for launch..."):
            st.write("Checking fuel...")
            time.sleep(1)
            st.write("Ignition...")
            time.sleep(1)
        st.balloons()
