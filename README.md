# 📄 RAG PDF Chatbot (Client-Server Architecture)
A Retrieval-Augmented Generation (RAG) based PDF Chatbot that allows users to interact with PDF documents using natural language queries.
This system extracts content from PDFs, converts it into embeddings, stores it in a FAISS Vector Database, and retrieves relevant context to generate accurate AI-based answers.
This project is implemented using a Client-Server Architecture where the client handles the UI and user interaction, while the server performs document retrieval and response generation.

## 🚀 Features
✅ Upload and store PDF documents as knowledge base<br>
✅ Intelligent document search using FAISS Vector Similarity Search<br>
✅ RAG pipeline for accurate question answering<br>
✅ Domain-based FAISS indexes (Cloud, IoT, Infosec, etc.)<br>
✅ Streamlit-based multi-page UI<br>
✅ Login page for user authentication<br>
✅ Fast and efficient retrieval even for large documents<br>
✅ Clean separation of client and server components<br>

### 🧠 What is RAG?
RAG (Retrieval-Augmented Generation) is an AI technique that improves chatbot accuracy by retrieving relevant information from external documents before generating a response.
Instead of answering purely from model memory, the chatbot:
Retrieves relevant text chunks from the PDF
Feeds them into the LLM prompt
Generates an answer grounded in the document
This reduces hallucinations and increases response reliability.

## 🏗️ Project Architecture
This project is divided into two main modules:

### 📌 Client Side (version4_client)
Handles the UI and user interaction.
Streamlit multipage application
Login page
Chat interface
Sends query to server and displays response

### 📌 Server Side (version4_server)
Handles the complete backend pipeline.
Loads PDF documents
Splits documents into chunks
Generates embeddings
Stores embeddings in FAISS indexes
Retrieves top-k relevant chunks
Generates final response using LLM

##📂 Folder Structure
RAG-pdf-Chatbot/
│
├── version4_client/
│   ├── pages/                 # Streamlit UI pages
│   ├── document_store/        # Client-side stored files
│   ├── Login.py               # Login UI
│   └── ...
│
├── version4_server/
│   ├── pages/                 # Backend pages / modules
│   ├── document_store/
│   │   ├── pdfs/              # Stored PDF documents
│   │   ├── faiss_index_*      # FAISS vector databases
│   ├── Chat2.py               # Main chatbot logic
│   ├── sample.py              # Example script
│   └── Login.py
│
└── README.md

## ⚙️ Tech Stack
### 🔹 Frontend (Client)
Streamlit (UI & Multi-page interface)
Python

### 🔹 Backend (Server)
Python
FAISS (Vector similarity search)
PDF processing libraries (PyPDF / PDFPlumber etc.)
Embedding model (OpenAI / HuggingFace embeddings)
LLM API (GPT / Gemini / etc.)

### 🔹 Database / Storage
FAISS Vector Store
Local Document Storage (PDFs)

### 🔥 How It Works (Pipeline Explanation)
Step 1: PDF Loading
PDF files are stored inside:
version4_server/document_store/pdfs/
The system extracts text from these documents.

### Step 2: Text Chunking
The extracted text is divided into smaller chunks to improve retrieval accuracy.

### Step 3: Embedding Generation
Each chunk is converted into an embedding vector using an embedding model.

### Step 4: FAISS Index Creation
These embeddings are stored in FAISS vector indexes like:
faiss_index_cloud
faiss_index_iot
faiss_index_infosec
These indexes allow very fast similarity-based search.

### Step 5: Query Processing
When a user asks a question:
The query is converted into an embedding
FAISS retrieves the top matching chunks

### Step 6: Answer Generation (RAG)
The retrieved chunks are passed into an LLM prompt, and the final response is generated based on the document content.

## 🖥️ Installation & Setup
### 1️⃣ Clone Repository
git clone https://github.com/GauravChd2829/RAG-pdf-Chatbot.git
cd RAG-pdf-Chatbot

### 2️⃣ Create Virtual Environment
python -m venv venv
Activate:
Windows
venv\Scripts\activate

### 3️⃣ Install Requirements
pip install -r requirements.txt


### ▶️ Running the Project
🟦 Run Server
Go to server folder:
cd version4_server
streamlit run Login.py

🟩 Run Client
Open a new terminal and run:
cd version4_client
streamlit run Login.py

Now the client UI will open in browser and you can start chatting with PDFs.

## 📌 Example Use Case
📄 Upload a PDF like:
Research paper-Resume-Notes-Legal document
Project documentation

### Ask questions like:
"Summarize this document"
"What is the conclusion of the paper?"
"Explain section 2 in simple words"
"Give key points from chapter 4"

The chatbot responds using only relevant PDF context.

## 📊 Applications
✅ Smart Document Assistant
✅ Research Paper Q/A Bot
✅ Legal Document Analyzer
✅ Study Notes Chatbot
✅ Corporate Policy Chatbot
✅ Domain Knowledge Bot (Cloud / IoT / Security)

## 🔮 Future Improvements
Add PDF upload option directly in UI
Deploy on cloud (AWS / Render / Streamlit Cloud)
Enhance MongoDB integration (indexing, schema optimization, Atlas deployment)
Add user session-based memory
Add role-based authentication
Add Docker support

## 👨‍💻 Contributors
Gaurav Chandak
Soham Mondal

## 📜 License
This project is for educational and learning purposes.
You may modify and use it for personal or academic use.

## ⭐ If you like this project
Give it a ⭐ on GitHub to support the work!



