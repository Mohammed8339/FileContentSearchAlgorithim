import os
import pickle
import json
import sys


def search_text_cache(query, text_cache):
    results = []
    for filename, text in text_cache.items():
        if query.lower() in text.lower():
            start_index = text.lower().index(query.lower())
            snippet = text[start_index:start_index + 100]  # Extract 100 characters starting from the query
            result = {
                "filename": filename,
                "content": snippet
            }
            results.append(result)
    return results


def search_pdf_cache(query, cache):
    results = []
    for filename, data in cache.items():
        text = data["text"]
        if query.lower() in text.lower():
            result = {
                "filename": filename,
                "content": text[:100]  # Include a snippet of the content
            }
            results.append(result)
    return results


# Example usage
if len(sys.argv) > 1:
    search_query = " ".join(sys.argv[1:])
else:
    print("Please provide a search query.")
    sys.exit(1)

text_cache_file_path = "TEXT_Cache.pkl"
pdf_cache_file_path = "PDF_Cache.pkl"

# Load the text cache from file
with open(text_cache_file_path, 'rb') as f:
    text_cache = pickle.load(f)

# Search the text cache
text_search_results = search_text_cache(search_query, text_cache)

# Print text cache search results
# if text_search_results:
#     print("Text Cache Search Results:")
#     for result in text_search_results:
#         print(f"File: {result['filename']}")
#         print(f"Content: {result['content']}")
#         print("-" * 30)
# else:
#     print("No text cache results found.")

# Load the PDF cache from file
with open(pdf_cache_file_path, 'rb') as f:
    pdf_cache = pickle.load(f)

# Search the PDF cache
pdf_search_results = search_pdf_cache(search_query, pdf_cache)

# Print PDF cache search results
# if pdf_search_results:
#     print("PDF Cache Search Results:")
#     for result in pdf_search_results:
#         print(f"File: {result['filename']}")
#         print(f"Content: {result['content']}")
#         print("-" * 30)
# else:
#     print("No PDF cache results found.")

# Convert search results to JSON format
search_results = {
    "text_search_results": text_search_results,
    "pdf_search_results": pdf_search_results
}

# Convert search results to JSON string
json_output = json.dumps(search_results)

# Output JSON string
# print("JSON Output:")
print(json_output)
