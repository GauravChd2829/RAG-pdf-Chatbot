import streamlit as st
# Inject custom CSS to style the header
st.markdown("""
    <style>
    /* Style the "⚙️ Manage Domains" header */
    .manage-domains-header {
        background-color: black;
        color: white;
        padding: 10px;
        font-weight: bold;
        font-size: 20px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Now, use a regular container for this header
st.markdown('<div class="manage-domains-header">⚙️ Manage Domains</div>', unsafe_allow_html=True)

# Your other UI components below
st.subheader("➕ Add New Domain")
new_domain = st.text_input("Enter new domain name:")
if st.button("Add Domain"):
    st.write(f"Domain '{new_domain}' added!")  # Placeholder for your logic

st.subheader("❌ Delete Domain")
selected = st.selectbox("Choose", ["iot", "infosec"])
if st.button("Delete"):
    st.write(f"Deleted {selected}")
