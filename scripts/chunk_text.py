import glob
import json

INPUT_DIR  = '../data/clean_txt'
OUTPUT_FILE = '../data/chunks.jsonl'
CHUNK_SIZE  = 500  # characters per chunk

def chunkify(text: str, size: int):
    for i in range(0, len(text), size):
        yield text[i:i+size]

def main():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        for txt in glob.glob(f'{INPUT_DIR}/*.txt'):
            raw = open(txt, 'r', encoding='utf-8').read()
            title = txt.split('/')[-1].replace('.txt','')
            for idx, chunk in enumerate(chunkify(raw, CHUNK_SIZE)):
                record = {
                    "id": f"{title}_{idx}",
                    "source": title,
                    "content": chunk
                }
                out.write(json.dumps(record) + '\n')

if __name__ == '__main__':
    main()