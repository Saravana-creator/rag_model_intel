from fastapi import FastAPI,UploadFile,Form
from fastapi.middleware.cors import CORSMiddleware
from modules.ocr_extraction import extract_text_from_pdf
from modules.text_chunking import chunk_text
from modules.embedding import build_vector_store
from modules.rag_pipeline import get_answer
import os

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "NCERT Doubt Explainer API is running", "description": "Upload NCERT PDFs and ask questions about NCERT content"}

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    try:
        # Validate file type
        if not file.filename.lower().endswith('.pdf'):
            return {"status": "error", "message": "Please upload a PDF file only"}
        
        # Validate file size (max 50MB)
        content = await file.read()
        if len(content) > 50 * 1024 * 1024:
            return {"status": "error", "message": "File too large. Maximum size is 50MB"}
        
        os.makedirs("data/ncert_pdf", exist_ok=True)
        os.makedirs("data/embeddings", exist_ok=True)
        
        pdf_path = f"data/ncert_pdf/{file.filename}"
        with open(pdf_path, "wb") as f:
            f.write(content)
        
        text = extract_text_from_pdf(pdf_path)
        if not text.strip():
            return {"status": "error", "message": "No text could be extracted from the PDF"}
        
        chunks = chunk_text(text)
        build_vector_store(chunks)
        
        return {
            "status": "success", 
            "message": f"PDF processed successfully! Created {len(chunks)} text chunks.",
            "chunks_created": len(chunks)
        }
    except Exception as e:
        return {"status": "error", "message": f"Error processing PDF: {str(e)}"}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        # Validate question
        if not question.strip():
            return {"answer": "Please enter a valid question", "citations": ""}
        
        if len(question) > 1000:
            return {"answer": "Question too long. Please keep it under 1000 characters", "citations": ""}
        
        # Check if FAISS index exists
        if not os.path.exists("data/embeddings/ncert_index.faiss"):
            return {
                "answer": "📚 Please upload an NCERT PDF first using the upload section above to start solving your doubts!", 
                "citations": ""
            }
        
        answer, refs = get_answer(question.strip(), [])
        return {"answer": answer, "citations": refs}
    except Exception as e:
        return {"answer": f"❌ Error processing your question: {str(e)}", "citations": ""}