from bs4 import BeautifulSoup
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a','link_favorsch')

for result in results:
    print(result.get_text(),"\n")