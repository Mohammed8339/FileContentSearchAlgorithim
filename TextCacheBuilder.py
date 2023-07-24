import os
import pickle
from bs4 import BeautifulSoup
import time


def extract_visible_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        html_code = file.read()

    soup = BeautifulSoup(html_code, 'html.parser')
    text = soup.get_text(separator=' ')
    text = ' '.join(text.split())  # Remove extra spaces

    return text.strip()


def build_cache(directory_paths, cache_file):
    text_cache = {}

    for directory_path in directory_paths:
        for filename in os.listdir(directory_path):
            if filename.endswith(".php"):
                file_path = os.path.join(directory_path, filename)
                text = extract_visible_text(file_path)
                text_cache[filename] = text

    with open(cache_file, 'wb') as f:
        pickle.dump(text_cache, f)
    print("Text cache built and saved to file.")


# PROVIDE DIRECTORIES HERE DONT FORGET TO PUT THE "r" BEFORE
# THE DIRECTORIES TO PREVENT PYTHON FROM BEING CONFUSED WITH
# THE "\"
directory_paths = [
    r""
]
cache_file_path = "TEXT_Cache.pkl"

while True:
    # Build the text cache
    build_cache(directory_paths, cache_file_path)

    # Delay for 60 seconds
    time.sleep(60)
