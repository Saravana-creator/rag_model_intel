from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

# Global variables for lazy loading
embedder = None
index = None
chunks_data = None

def load_models():
    global embedder, index, chunks_data
    if embedder is None:
        embedder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    if index is None and os.path.exists("data/embeddings/ncert_index.faiss"):
        index = faiss.read_index("data/embeddings/ncert_index.faiss")
    if chunks_data is None and os.path.exists("data/embeddings/chunks.pkl"):
        with open("data/embeddings/chunks.pkl", "rb") as f:
            chunks_data = pickle.load(f)

def get_answer(query, chunks):
    load_models()
    if index is None:
        return "Please upload an NCERT PDF first to get started with doubt solving.", ""
    
    q_vector = embedder.encode([query])
    D, I = index.search(np.array(q_vector), k=3)
    
    # Use stored chunks if available, otherwise use provided chunks
    source_chunks = chunks_data if chunks_data else chunks
    if not source_chunks:
        return "No NCERT content available. Please upload an NCERT PDF first.", ""
    
    retrieved_chunks = [source_chunks[i] for i in I[0] if i < len(source_chunks)]
    context = "\n\n".join(retrieved_chunks)
    
    # Generate structured NCERT answer
    answer = generate_structured_answer(query, context)
    return answer, context

def generate_structured_answer(question, context):
    """Generate a structured educational answer based on NCERT content"""
    
    # Simple template-based answer generation
    answer_template = f"""📚 **NCERT Solution:**

**Question:** {question}

**Answer based on NCERT textbook:**

{context[:600]}...

**Key Points:**
• This information is directly from your NCERT textbook
• For complete understanding, refer to the full chapter
• Practice similar problems for better comprehension

💡 **Study Tip:** Make sure to understand the concept rather than just memorizing the answer!"""
    
    return answer_template