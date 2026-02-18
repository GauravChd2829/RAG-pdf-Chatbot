import streamlit as st
import base64
from pymongo import MongoClient
import gridfs

# --- Page Config ---
st.set_page_config(page_title="AI FORTRESS", page_icon="🧠")

# --- MongoDB Config ---
MONGO_URI = "mongodb://localhost:27017"  # Adjust if hosted differently
DB_NAME = "pdf_database"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
domain_collection = db["domain_list"]  # Persistent store for domain names

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# --- Background Image (optional) ---
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
if st.session_state.get("theme", "light") == "dark":
# Custom CSS for Styling
    set_background("black.jpeg")
    st.markdown("""
    <style>
                     p{  font-weight:bold;} 
        h1, h2, h3 {
    color: white !important;
    }
    body {
            background: linear-gradient(135deg, #0D0D0D, #1A1A2E) !important;
        }
    .custom-button {
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        border: none;
        transition: 0.3s;
        text-align: center;
    }
    .login-btn {
        background: linear-gradient(90deg, #38BDF8, #3B82F6);
        color: white;
    }
    .login-btn:hover {
        background: linear-gradient(90deg, #3B82F6, #2563EB);
        transform: translateY(-2px);
    }
    .signup-btn {
        background: linear-gradient(90deg, #34D399, #10B981);
        color: white;
    }
    .signup-btn:hover {
        background: linear-gradient(90deg, #10B981, #059669);
        transform: translateY(-2px);
    }
    label {
        font-size: 25px !important;
        font-weight: bold !important;
        margin-bottom: 8px !important;
        color: white !important;
    }
    [data-testid="stSidebar"]::before {
        content: "📌Navigation";
        font-weight: bold;
        display: block;
        font-size: 25px;
        margin-top: 40px;
        text-align: center;
        color: white;
    }
      [data-testid="stSidebar"] {
        background-color: #211f26 !important;
        font-size: 18px;
        text-align: left !important;
        border-right:2px solid white;
    }
    
    
/* Chat Input Box Styling */
.stChatInput input {
    background-color: #1E1E1E !important;
    color: #FFFFFF !important;
    border: 1px solid #3A3A3A !important;
}

/* Styling for User & AI Messages */
.stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
    background-color: #1E1E1E !important;
    border: 1px solid #3A3A3A !important;
    color: #E0E0E0 !important;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}

.stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
    background-color: #2A2A2A !important;
    border: 1px solid #404040 !important;
    color: #F0F0F0 !important;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}

/* File Uploader Styling */
.stFileUploader {
    background-color: #1E1E1E;
    border: 1px solid white;
    border-radius: 10px;
    padding: 15px;
}

.stFileUploader label {
    color: white !important;
    border-color: white !important;
}

/* Headings */
h1, h2, h3 {
    color: white !important;
}

/* User Question Styling */
.question {
    color: white !important; /* Neon Green Text */
    
    font-size: 18px; /* Readable Size */
    background-color: #1E1E1E !important; /* Dark Background */
    border: 1px solid #3A3A3A !important; /* Subtle Border */
    padding: 10px 20px; /* Balanced Padding */
    padding-let:20px;
    margin: 10px auto; /* Centers the Element */
    display: inline-block; /* Ensures it Wraps Around Content */
    max-width: 90%; /* Prevents Stretching */
    word-wrap: break-word; /* Prevents Overflow Issues */
    border-radius: 25px; /* Rounded Edges */
}

     [data-testid="stSidebar"] {
        background-color: #211f26 !important;
        font-size: 18px;
        text-align: left !important;
        border-right:2px solid white;
    }
    
        .ai-response {
        color: white;  /* Ensures black text */
        background-color: grey;  /* Light background */
        padding: 12px;
        border: 5px solid white;
        border-radius:10px; /* More rounded bubble */
        margin:10px;
        font-size: 16px;
    }
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
else:
    
    set_background("white.jpeg")
    st.markdown("""
    <style>
                   .stAlert {
            background-color: black !important;  /* Black background */
            color: white !important;  /* White text */
            border-radius: 8px;  /* Rounded corners */
            padding: 10px;  /* Add padding */
        }
          body {
            background: linear-gradient(135deg, #0D0D0D, #1A1A2E) !important;
        }
        h1, h2, h3 {
            color: #333333 !important;
        }
        .custom-button {
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            transition: 0.3s;
            text-align: center;
        }
        .question {
            color: #333333 !important;
            font-size: 18px;
            background-color: #F5F5F5 !important;
            border: 2px solid green !important;
            padding: 10px 20px;
            margin: 10px auto;
            margin-bottom:10px;
            display: inline-block;
            max-width: 90%;
            word-wrap: break-word;
            border-radius: 25px;
        }
          [data-testid="stSidebar"] {
        background-color: #211f26 !important;
        font-size: 18px;
        text-align: left !important;
        border-right:2px solid white;
    }
    
    .custom-button {
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        border: none;
        transition: 0.3s;
        text-align: center;
    }
    .login-btn {
        background: linear-gradient(90deg, #1E40AF, #1D4ED8);
        color: white;
    }
    .login-btn:hover {
        background: linear-gradient(90deg, #1D4ED8, #2563EB);
        transform: translateY(-2px);
    }
    .signup-btn {
        background: linear-gradient(90deg, #047857, #065F46);
        color: white;
    }
    .signup-btn:hover {
        background: linear-gradient(90deg, #065F46, #064E3B);
        transform: translateY(-2px);
    }
    label {
        font-size: 22px !important;
        font-weight: bold !important;
        margin-bottom: 8px !important;
        color: black !important;
    }
       [data-testid="stSidebar"] {
        background-color: #211f26 !important;
        font-size: 18px;
        text-align: left !important;
        border-right:2px solid white;
    }
    
    [data-testid="stSidebar"]::before {
        content: "📌Navigation";
        font-weight: bold;
        display: block;
        font-size: 25px;
        margin-top: 40px;
        text-align: center;
        color: white;
    }
                .ai-response {
        color: black;  /* Ensures black text */
        background-color: #f8f9fa;  /* Light background */
        padding: 12px;
        border: 5px solid black;
        border-radius:10px; /* More rounded bubble */
        margin:10px;
        font-size: 16px;
    }

             .question {
        font-weight: bold;
        color: #007bff;
        font-size: 18px;
    }
                   h2, h3 {
        color: #4CAF50; /* Light green heading */
        font-size: 22px; /* Bigger heading */
        font-weight: bold;
    }
                    .stChatInput {
                margin-top:20px;
        border-radius: 12px !important; /* Rounded chat input */
    }


            @media (prefers-color-scheme: dark) {
                .ai-response {
                    color: black;  /* Change text to white in dark mode */
                    background-color: white;  /* Dark background */
                }
            }
                  p{  font-weight:bold;}  
               div.streamlit-expanderHeader {
        background-color: #000000 !important;
        color: white !important;
        font-weight: bold;
    }

    /* Optional: make the expander content area also dark */
    div.streamlit-expanderContent {
        background-color: #111111 !important;
        color: white !important;
    }
    .streamlit-expanderHeader {
        background-color: white;
        color: black; # Adjust this for expander header color
    }
    /* Optional: style inputs inside expander */
    .stTextInput > div > div > input {
        background-color: #222 !important;
        color: white !important;
    }
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

# --- Sidebar ---
with st.sidebar:
    st.button("Toggle Dark/Light Mode", on_click=toggle_theme, key="theme_toggle")
    st.text("Made by VIT")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.pop("username", None)
        st.success("Logged out successfully!")
        st.switch_page("Login.py")
        st.rerun()

# --- Auth Check ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("You must log in first!")
    if st.button("Go to Login"):
        st.switch_page("./Login.py")
    st.stop()

# --- Initialize Domain List from MongoDB ---
if "domains" not in st.session_state:
    st.session_state["domains"] = sorted([doc["name"] for doc in domain_collection.find({})])

# --- Main UI: Domain Selection ---
st.markdown('<div class="selection-container">', unsafe_allow_html=True)
st.markdown('<h1 class="header-text">🔍 Choose Your Domain</h1>', unsafe_allow_html=True)

cols = st.columns(2)
for i, domain in enumerate(st.session_state["domains"]):
    with cols[i % 2]:
        if st.button(domain.capitalize(), key=domain, help=f"Choose {domain} domain", use_container_width=True):
            st.session_state["selected_db"] = domain
            st.switch_page("pages/UploadPDF.py")

st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="manage-domains-container">', unsafe_allow_html=True)


st.markdown('<div class="manage-domains-header">⚙️ Manage Domains</div>', unsafe_allow_html=True)

st.subheader("➕ Add New Domain")
new_domain = st.text_input("Enter new domain name:")

if st.button("Add Domain"):
    new_domain = new_domain.strip().lower()
    if new_domain and new_domain not in st.session_state["domains"]:
        try:
            # Update session and DB
            st.session_state["domains"].append(new_domain)
            domain_collection.insert_one({"name": new_domain})

            # Create domain-specific collections
            collection_names = [
                f"{new_domain}_pdf_database",
                f"{new_domain}_hist",
                f"{new_domain}_test"
            ]

            for name in collection_names:
                col = db[name]
                col.insert_one({"_init": True})
                col.delete_many({"_init": True})

            # Initialize GridFS
            fs = gridfs.GridFS(db, collection=f"{new_domain}_pdf_database")

            st.success(f"✅ Domain '{new_domain}' added with collections: {', '.join(collection_names)}")
            st.success(f"GridFS initialized for collection '{new_domain}_pdf_database'")
            st.rerun()

        except Exception as e:
            st.error(f"❌ Error creating domain: {str(e)}")

    elif new_domain in st.session_state["domains"]:
        st.warning("⚠️ Domain already exists!")
    else:
        st.error("❌ Please enter a valid domain name.")

st.subheader("❌ Delete Existing Domain")
if st.session_state["domains"]:
    domain_to_delete = st.selectbox("Select a domain to delete", st.session_state["domains"])

    if st.button("Delete Domain"):
        try:
            st.session_state["domains"].remove(domain_to_delete)
            domain_collection.delete_one({"name": domain_to_delete})

            collection_names = [
                f"{domain_to_delete}_pdf_database",
                f"{domain_to_delete}_hist",
                f"{domain_to_delete}_test"
            ]

            for name in collection_names:
                if name in db.list_collection_names():
                    db.drop_collection(name)
                    st.success(f"✅ Collection '{name}' deleted.")
                else:
                    st.warning(f"⚠️ Collection '{name}' did not exist.")

            st.rerun()

        except Exception as e:
            st.error(f"❌ Error deleting domain: {str(e)}")
else:
    st.info("ℹ️ No domains available to delete.")

# Close the container
st.markdown('</div>', unsafe_allow_html=True)