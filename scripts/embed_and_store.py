import os
import json
from google.cloud import firestore
from sentence_transformers import SentenceTransformer

# Locate the chunks file relative to this script
SCRIPT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
CHUNKS_FILE = os.path.join(PROJECT_ROOT, 'data', 'chunks.jsonl')

# Initialize Firestore client and embedding model
db = firestore.Client()
s2v_model = SentenceTransformer('all-MiniLM-L6-v2')

def main():
    if not os.path.isfile(CHUNKS_FILE):
        print(f"ERROR: chunks file not found at {CHUNKS_FILE}")
        return

    with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            rec = json.loads(line)
            # Compute local embedding
            embedding = s2v_model.encode(rec['content'], convert_to_tensor=False)
            vector_list = embedding.tolist() if hasattr(embedding, 'tolist') else list(embedding)

            # Upsert into Firestore
            doc_ref = db.collection('embeddings').document(rec['id'])
            doc_ref.set({
                'content': rec['content'],
                'source': rec.get('source', ''),
                'vector': vector_list
            })
            print(f"Loaded chunk {rec['id']}")

    print("Finished loading all embeddings to Firestore.")

if __name__ == '__main__':
    main()
