import socket
import streamlit as st

st.title("🔌 IP Address Connection Checker")

ip = st.text_input("Enter IP Address", "8.8.8.8")
port = st.number_input("Enter Port Number", min_value=1, max_value=65535, value=80)

if st.button("Check Connection"):
    try:
        socket.create_connection((ip, port), timeout=5)
        st.success(f"✅ Connection to {ip}:{port} is established.")
    except Exception as e:
        st.error(f"❌ Connection to {ip}:{port} failed: {e}")
