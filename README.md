# 🧠 NCERT Doubt Explainer

An AI-powered application to help students solve their NCERT textbook doubts using RAG (Retrieval Augmented Generation).

## Features

- 📚 Upload NCERT PDF textbooks
- 🤖 Ask questions about NCERT content
- 🔍 Get answers based on actual textbook content
- 🌐 Web-based interface
- 📱 Responsive design

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- Tesseract OCR (for image text extraction)

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   python -m uvicorn app:app --reload --port 8000
   ```
   Or use: `start_backend.bat`

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   Or use: `start_frontend.bat`

## Usage

1. **Upload PDF**: Upload your NCERT textbook PDF using the upload section
2. **Ask Questions**: Type your doubt/question in the text area
3. **Get Answers**: Receive structured answers based on the textbook content

## API Endpoints

- `GET /` - Health check
- `POST /upload` - Upload NCERT PDF file
- `POST /ask/` - Ask questions about uploaded content

## Technology Stack

**Backend:**
- FastAPI
- FAISS (Vector Database)
- Sentence Transformers
- PyMuPDF (PDF processing)
- Tesseract OCR

**Frontend:**
- React.js
- Axios
- CSS3

## Project Structure
```
NCERT_DOUBT_EXPLAINER/
├── backend/
│   ├── modules/          # Core processing modules
│   ├── data/            # PDF storage and embeddings
│   ├── app.py           # FastAPI application
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   └── App.css      # Styling
│   └── package.json
└── README.md
```

## Contributing

Feel free to contribute by:
- Adding more language support
- Improving the UI/UX
- Enhancing the RAG pipeline
- Adding more educational features