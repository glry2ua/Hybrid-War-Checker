# HybridWarRAG

## Overview  
Hybrid wars are hard to detect at the begining stages, and harder to fight in the late stages of their implimentation. This project implements a Retrieval-Augmented-Generation (RAG) pipeline to answer “Is my country currently in a hybrid war?” using concrete official-source texts. 

## Structure  
- `data/raw_pdfs/`  
  Raw PDF files to be processed.

- `data/raw_html/`  
  Raw HTML files (if any).

- `scripts/extract_and_clean.py`  
  Extracts text from PDFs/HTML and cleans it.

- `scripts/chunk_text.py`  
  Splits cleaned text into fixed-size chunks for embedding.

- `scripts/embed_and_store.py`  
  Embeds chunks via Vertex AI (or local model) and stores vectors.

## Setup  
```bash
# Install requirements
pip3 install -r requirements.txt

# Step 1: extract & clean
python3 scripts/extract_and_clean.py

# Step 2: chunk text
python3 scripts/chunk_text.py

# Step 3: embed & store
python3 scripts/embed_and_store.py
