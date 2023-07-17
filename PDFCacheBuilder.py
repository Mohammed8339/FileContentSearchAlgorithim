import os
import time
import pickle
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from concurrent.futures import ThreadPoolExecutor
import hashlib


def extract_text_from_pdf(file_path):
    resource_manager = PDFResourceManager()
    text_buffer = StringIO()
    laparams = LAParams()

    with open(file_path, 'rb') as file:
        interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, text_buffer, laparams=laparams))
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)

        text = text_buffer.getvalue()

    return text


def calculate_file_hash(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        file_hash = hashlib.md5(content).hexdigest()
    return file_hash


def build_cache(directory_paths, cache_file):
    while True:
        cache = {}
        file_hashes = {}

        with ThreadPoolExecutor() as executor:
            futures = []
            for directory_path in directory_paths:
                for filename in os.listdir(directory_path):
                    if filename.endswith(".pdf"):
                        filepath = os.path.join(directory_path, filename)
                        file_hash = calculate_file_hash(filepath)
                        file_hashes[filename] = file_hash

                        if filename not in cache or cache.get(filename, {}).get("hash") != file_hash:
                            future = executor.submit(extract_text_from_pdf, filepath)
                            futures.append((filename, future))

            for filename, future in futures:
                try:
                    text = future.result()
                    file_hash = file_hashes[filename]
                    cache[filename] = {"text": text, "hash": file_hash}
                except Exception as e:
                    print(f"Error reading file: {filename}. {str(e)}")

        with open(cache_file, 'wb') as f:
            pickle.dump(cache, f)
        print("Cache built and saved to file.")

        time.sleep(60)  # Wait for 60 seconds before checking for updates again


# PROVIDE DIRECTORIES HERE DONT FORGET TO PUT THE "r" BEFORE
# THE DIRECTORIES TO PREVENT PYTHON FROM BEING CONFUSED WITH
# THE "\"
directory_paths = [
    r""
]

cache_file_path = "PDF_Cache.pkl"

# Build and continuously update the cache
build_cache(directory_paths, cache_file_path)