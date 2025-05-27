import json
from google.cloud import firestore
from sentence_transformers import SentenceTransformer
# Initialize local embedding model
s2v_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Firestore
db = firestore.Client()

# Path to your chunks file
with open('data/chunks.jsonl') as f:
    for line in f:
        rec = json.loads(line)
        # Compute embedding locally
        embedding = s2v_model.encode(rec['content'], convert_to_tensor=False)
        vector_list = embedding.tolist() if hasattr(embedding, 'tolist') else list(embedding)
        # Each chunk becomes a document under collection "embeddings"
        db.collection('embeddings').document(rec['id']).set({
            'content': rec['content'],
            'vector': vector_list,
            'source': rec.get('source', '')
        })
print("Finished loading embeddings into Firestore.")