from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen("https://www.ua-football.com/sport")
html = req.read()
soup = BeautifulSoup(html, "html.parser")
news = soup.find_all("li", class_="liga-news-item")

results = []
for i in news:
    title = i.find("span", class_="d-block").get_text(strip=True)
    descr = i.find("span", class_="name-dop").get_text(strip=True)
    link = i.a.get("href")
    results.append({
        'title': title,
        'description': descr,
        'href': link,
    })
f = open("pars.txt", "w", encoding="utf-8")
i = 1
for item in results:
    f.write(f"Новость {i}\n\nНазвание: {item['title']}\nОписание: {item['description']}\nСсылка: {item['href']}\n\n******\n")
    i += 1
f.close()