from bs4 import BeautifulSoup
import requests

resp = requests.get("https://coinmarketcap.com/")
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    bitok = soup_list[0].find("span")
    print(bitok.text)
