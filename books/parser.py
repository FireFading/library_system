import requests
import bs4


URL = "https://www.labirint.ru/"
session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Accept-Language': 'en',
}
result = []
res = session.get(url=URL)
res.raise_for_status()
print(res.text)