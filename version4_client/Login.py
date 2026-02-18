import streamlit as st
import bcrypt
import base64
from pymongo import MongoClient
st.set_page_config(page_title="AI FORTRESS", page_icon="🧠")
import re
# MongoDB Setup
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "pdf_database"
USER_COLLECTION = "users"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
user_collection = db[USER_COLLECTION]
if "theme" not in st.session_state:
    st.session_state["theme"] = "dark"
# Initialize session state for theme and authentication if not set
if "login_screen" not in st.session_state:
    st.session_state["login_screen"] = False 
# Function to toggle theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"
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
if st.session_state["theme"] == "dark":
    set_background("black.jpeg")

    st.markdown("""
 <style>
        h1, h2, h3 {
    color: white!important;
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
                     p{  font-weight:bold;} 
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
        color:white;
    }
        [data-testid="stSidebar"] {
        background-color: #211f26 !important;
        font-size: 18px;
        text-align: left !important;
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
    color: white!important;
    border-color: white!important;
}

/* Headings */
h1, h2, h3 {
    color: white!important;
}

/* User Question Styling */
.question {
    color: white!important; /* Neon Green Text */
    
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
    border-right:2px solid white;
    
}
  
    </style>
    """, unsafe_allow_html=True)
else:
    
    set_background("white.jpeg")
    st.markdown("""
    <style>
                     p{  font-weight:bold;} 
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
                    background-color: #1a1a2e !important;

            font-size: 18px;
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
    section[data-testid="stSidebar"] {
        # background-color: #211f26 !important;
        background-color: #211f26 !important;
        border-right: 2px solid white !important;
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
        border-radius: 12px; /* More rounded bubble */
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
                            .stAlert {
            background-color: black !important;  /* Black background */
            color: white !important;  /* White text */
            border-radius: 8px;  /* Rounded corners */
            padding: 10px;  /* Add padding */
        }
    </style>
    """, unsafe_allow_html=True)
with st.sidebar:

    st.button("Toggle Dark/Light Mode", on_click=toggle_theme)

st.sidebar.text("Made by VIT ")

def register_user(username, password):
    """Register a new user with hashed password."""
    if user_collection.find_one({"username": username}):
        return False  # Username already exists

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_collection.insert_one({"username": username, "password": hashed_password})
    return True

def authenticate_user(username, password):
    """Authenticate user using hashed password comparison."""
    user_data = user_collection.find_one({"username": username})
    if user_data and bcrypt.checkpw(password.encode(), user_data["password"]):
        return True
    return False

def main():

    if "login_screen" not in st.session_state:
        st.session_state["login_screen"] = False
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # If logged in, show logout button
    if st.session_state["authenticated"]:
        st.success(f"✅ Logged in as {st.session_state['username']}")

        # Logout Button
        if st.button("🚪 Logout", key="logout_btn"):
            st.session_state["authenticated"] = False
            st.session_state["login_screen"] = False
            st.session_state.pop("username", None)
            st.success("🔓 Logged out successfully!")
            st.rerun()  # Refresh page to go back to welcome screen

    # Redirect immediately if login screen is active
    elif st.session_state["login_screen"]:
        st.markdown('<h1 style="color: #38BDF8; text-align: center;">🔐 AI Fortress Login</h1>', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Login", key="login_btn", help="Log in to your account", use_container_width=True):
                if authenticate_user(username, password):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.success("✅ Login successful! Redirecting...")
                    st.switch_page("pages/Selection.py")
                else:
                    st.error("⚠ Invalid username or password")

        with col2:
            if st.button("Signup", key="signup_btn", help="Create a new account", use_container_width=True):
                if register_user(username, password):
                    st.success("✅ Signup successful! Please log in.")
                else:
                    st.error("⚠ Username already exists! Try a different one.")

    else:
        st.markdown('<h1 style="text-align:left;">🔐 Welcome to AI Fortress </h1>', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: left;">Your secure AI powered platform </h2>', unsafe_allow_html=True)

        # Use `on_click` to persist state change and avoid multiple clicks
        st.button("Login", on_click=lambda: st.session_state.update({"login_screen": True}))

if __name__ == "__main__":
    main()
