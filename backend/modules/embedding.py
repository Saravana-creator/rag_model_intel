from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

model=SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
def build_vector_store(chunks):
    embeddings=model.encode(chunks)
    dim=embeddings.shape[1]
    index=faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index,"data/embeddings/ncert_index.faiss")
    
    # Save chunks for retrieval
    with open("data/embeddings/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    
    return index