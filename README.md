# README

This repository contains code for building and searching text and PDF caches. The provided code consists of three files: `main.py`, `TextCacheBuilder.py`, and `PDFCacheBuilder.py`. Each file serves a specific purpose in the caching and search process.

## main.py

The `main.py` file is the entry point of the program. It performs a search operation on two types of caches: a text cache and a PDF cache. The script takes a search query as input and returns the search results in JSON format.

The main functionalities of `main.py` include:

- `search_text_cache(query, text_cache)`: This function searches for the provided `query` within the `text_cache` dictionary. It performs a case-insensitive search and extracts a snippet of 100 characters starting from the query. The function returns a list of all matching results.

- `search_pdf_cache(query, cache)`: This function searches for the provided `query` within the `cache` dictionary, representing the PDF cache. It performs a case-insensitive search and includes a snippet of the content in the results. The function returns a list of all matching results.

- Example usage: The script takes the search query from the command line arguments. It loads the text cache and PDF cache from their respective pickle files. Then it performs the search operation on both caches, prints the results, converts the results to JSON format, and outputs the JSON string.

## TextCacheBuilder.py

The `TextCacheBuilder.py` file is responsible for building a text cache by extracting visible text from HTML files in a specified directory. The cache is stored in a pickle file.

The main functionalities of `TextCacheBuilder.py` include:

- `extract_visible_text(file_path)`: This function takes a `file_path` as input and reads the HTML content from the file. It utilizes BeautifulSoup to parse the HTML and extract the visible text. The extracted text is cleaned by removing extra spaces and returned as a string.

- `build_cache(directory_path, cache_file)`: This function builds the text cache by iterating over the files in the specified directory. It extracts visible text from HTML files using `extract_visible_text` and saves the cache to a pickle file.

- Example usage: The script sets the `directory_path` and `cache_file_path` variables to the appropriate paths. It continuously builds the text cache by calling `build_cache` function in an infinite loop with a delay of 60 seconds between each execution.

## PDFCacheBuilder.py

The `PDFCacheBuilder.py` file is responsible for building and continuously updating a PDF cache. It extracts text content from PDF files in multiple specified directories using the pdfminer library. The cache is stored in a pickle file.

The main functionalities of `PDFCacheBuilder.py` include:

- `extract_text_from_pdf(file_path)`: This function takes a `file_path` as input and reads the content of the PDF file. It utilizes pdfminer to extract the text content from the PDF and returns it as a string.

- `calculate_file_hash(file_path)`: This function calculates the MD5 hash of the file content to track changes in the PDF files.

- `build_cache(directory_paths, cache_file)`: This function continuously builds and updates the PDF cache. It iterates over the specified `directory_paths` and checks for PDF files. For each file, it calculates the file hash using `calculate_file_hash` and compares it with the hash stored in the cache. If there is a difference or the file is not present in the cache, it extracts the text content using `extract_text_from_pdf` and updates the cache with the new content and hash. The cache is then saved to a pickle file.

- Example usage: The script sets the `directory_paths` and `cache_file_path` variables to the appropriate paths. It continuously builds and updates the PDF cache by calling the `build_cache` function in an infinite loop with a delay of 60 seconds between each execution.

---

Please note that the code provided here is a simplified version, and you may need to modify it to suit your specific requirements. Make sure to provide the appropriate file paths and adjust the code as needed.
