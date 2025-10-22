from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
async def upload_pdf():
    return {"status": "success", "message": "PDF upload functionality will be added after fixing dependencies"}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    return {
        "answer": f"NCERT Answer for '{question}': This is a sample response. Please upload NCERT content first.",
        "citations": "Sample NCERT textbook reference"
    }