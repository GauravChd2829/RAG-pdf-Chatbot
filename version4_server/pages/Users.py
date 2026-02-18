import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Set light theme by default

# MongoDB config
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "pdf_database"
USER_COLLECTION = "users"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
user_collection = db[USER_COLLECTION]

# Streamlit sidebar
st.set_page_config(page_title="AI FORTRESS", page_icon="🧠")
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"
# Custom CSS for styling
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"
import base64
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
# Apply theme based on session state
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
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:

    st.button("Toggle Dark/Light Mode", on_click=toggle_theme)

st.markdown("<h2 style='color:#4CAF50;'>👥 Registered Users</h2>", unsafe_allow_html=True)

# Fetch user data
users = list(user_collection.find({}, {"_id": 0, "username": 1}))

if not users:
    st.info("No users registered yet.")
else:
    usernames = [u["username"] for u in users if "username" in u]
    
    for username in usernames:
        st.markdown(f"""
        <div class="ai-response">
            <p>👤 <strong>{username}</strong></p>
        </div>
        """, unsafe_allow_html=True)
