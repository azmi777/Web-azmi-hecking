import streamlit as st

st.title("Bot AI Saya")

# Menyimpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kolom input chat
if prompt := st.chat_input("Tulis pesan di sini..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respon bot (sementara masih fake/nggak nyambung ke AI)
    response = f"Kamu bilang: {prompt} (AI belum disambungkan)"
    
    # Tampilkan respon bot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
