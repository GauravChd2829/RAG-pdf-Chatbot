import streamlit as st
from pymongo import MongoClient
st.set_page_config(page_title="AI FORTRESS", page_icon="🧠")
if "theme" not in st.session_state:
    st.session_state["theme"] = "dark"
# MongoDB Setup
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "pdf_database"
FEEDBACK_COLLECTION = "feedback"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
feedback_collection = db[FEEDBACK_COLLECTION]

# Page Title
st.title("📘 About the Website")
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
        backdrop-filter: blur(10px); /* Adjust blur intensity */
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
        h1, h2, h3 {
    color: white!important;
    }
    p{
                font-weight:bold;
                color:white;}
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
        text-align: left !important;
        border-right:2px solid white;
    }
    
  
    </style>
    """, unsafe_allow_html=True)
else:
    
    set_background("white.jpeg")
    st.markdown("""
    <style>
    p{
                font-weight:bold;}
                .custom-text {
            color: black !important;

        }
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
        border-radius: 12px; /* More rounded bubble */
        font-size: 16px;
        border: 2px solid black;
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
      
        border-radius: 12px !important;
                border:2px solid white!important; /* Rounded chat input */
    }


            @media (prefers-color-scheme: dark) {
                .ai-response {
                    color: black;  /* Change text to white in dark mode */
                    background-color: white;  /* Dark background */
                }
            }
              
    </style>
    """, unsafe_allow_html=True)
with st.sidebar:

    st.button("Toggle Dark/Light Mode", on_click=toggle_theme)
import base64

# Website Description
st.markdown("""
            
    <div class="custom-text">
        <h2>🌟 Welcome to AI Fortress !!!</h2>
        
    <p style='font-size:large;'>This website is designed to help students study various subjects like:</p>
        
        📌 Information Security
        🌐 Internet of Things (IoT)
        🤖 AI-powered Learning
        
        
    We use Specialized Large Language Models (SLLM) to provide interactive learning, 
    Q&A support, and AI-powered explanations.
        
   
        
       🏫 Built by VIT Students
        This project is proudly developed by students of Vellore Institute of Technology (VIT) 
        to enhance digital education and make learning more accessible and engaging.
    </div>
""", unsafe_allow_html=True)


st.sidebar.text("Made by VIT ")

# # Feedback Section
st.markdown("---")
st.markdown("## 📢 We Value Your Feedback!", unsafe_allow_html=True)

st.markdown("""<div class="custom-text">

        Your feedback helps us improve! Please share your thoughts below:
   </div>
""", unsafe_allow_html=True)

# Autofill "Your Name" with the logged-in username
username = st.session_state.get("username", "")

user_name = st.text_input("Your Name", value=username)
user_feedback = st.text_area("Share your experience or any suggestions:")

# Submit Feedback Button
if st.button("Submit Feedback", key="login-btn", help="Click to submit your feedback", use_container_width=True):
    if user_name and user_feedback:
        # Store feedback in MongoDB
        feedback_collection.insert_one({"name": user_name, "feedback": user_feedback})
        st.success("✅ Thank you for your feedback! It has been recorded.")
    else:
        st.warning("⚠ Please fill out both fields before submitting.")
