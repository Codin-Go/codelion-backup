# bs4 라이브러리에서 BeautifulSoup 기능만 사용하겠다고 작성해주세요.
from bs4 import BeautifulSoup
import requests

url = 'http://www.codelion.net/'
response = requests.get(url)

# BeautifulSoup의 두 번째 재료에 python의 내장 parser를 넣어주세요.
soup = BeautifulSoup(response.text, 'html.parser')