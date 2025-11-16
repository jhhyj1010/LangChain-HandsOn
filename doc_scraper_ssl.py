import urllib3, requests
import os
import certifi
from urllib3.util.ssl_ import create_urllib3_context
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ctx = create_urllib3_context()
ctx.load_default_certs()

# To fix SSL issues: https://www.geeksforgeeks.org/python/how-to-fix-python-requests-sslerror/

# ctx.options |= 0x4 # Uncomment for legacy server compatibility if needed
urllib3.disable_warnings()
url = "https://api.python.langchain.com/en/latest/langchain_api_reference.html"
with urllib3.PoolManager(ssl_context=ctx) as http:
    #import pdb; pdb.set_trace()
    output_dir = '/tmp/langchain_doc'
    os.makedirs(output_dir, exist_ok=True)
    req = http.request("GET", "https://api.python.langchain.com/en/latest/langchain_api_reference.html")
    # Process req.data with Beautiful Soup
    #import pdb; pdb.set_trace()
    html = req.data
    soup = BeautifulSoup(html, 'html.parser')
    
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']

        # If it's a .html file
        if href.endswith('.html'):
            # Make a full URL if necessary
            if not href.startswith('http'):
                href = urljoin(url, href)

            # Fetch the .html file
            try:
                file_response = requests.get(href, verify=certifi.where()) #http.request('GET', href) #requests.get(href)
            except Exception:
                print(f'Exception raised!')
            else:
                # Write it to a file
                file_name = os.path.join(output_dir, os.path.basename(href))
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(file_response.text)
