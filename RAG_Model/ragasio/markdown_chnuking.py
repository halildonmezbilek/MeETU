import os
import re

def split_markdown(content, min_size=9000, max_size=10000):
    sections = re.split(r'(?<=\n\n)(?=## )', content)
    
    chunks = []
    current_chunk = ''
    
    for section in sections:
        if len(current_chunk) + len(section) > max_size:
            chunks.append(current_chunk.strip())
            current_chunk = section
        else:
            current_chunk += section
            
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def save_chunks(file_path, output_dir, min_size=9000, max_size=10000):
    with open(file_path, 'r') as f:
        content = f.read()

    os.makedirs(output_dir, exist_ok=True)

    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    chunks = split_markdown(content, min_size, max_size)

    for i, chunk in enumerate(chunks, start=1):
        chunk_filename = f"{base_filename}_chunk_{i}.md"
        chunk_path = os.path.join(output_dir, chunk_filename)
        with open(chunk_path, "w") as f:
            f.write(chunk)
        print(f"Saved: {chunk_path}")

def process_all_files(input_dir, output_dir, min_size=65000, max_size=70000):
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing {file_path}")
            save_chunks(file_path, output_dir, min_size, max_size)

input_dir = "/home/halil/Desktop/MeETU/RAG_Model/ragasio/markdowns"
output_dir = "/home/halil/Desktop/MeETU/RAG_Model/ragasio/markdownschunked"
process_all_files(input_dir, output_dir)
