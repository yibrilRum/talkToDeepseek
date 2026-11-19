import requests
from bs4 import BeautifulSoup
from googlesearch import search

OLLAMA_HOST = "http://100.71.248.58:11434"
MODEL_NAME = "deepseek"

def google_search(query, num_results=5):
    print(f"Searching google for {query} ...")
    return list(search(query, num_results=num_results))

def get_text_from_url():
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)[:2000]

    except Exception as e:
        return f"[!] Could not fetch {url}: {e}"
