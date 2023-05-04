from bs4 import BeautifulSoup
import urllib.request


class Parsa:
    html = ""
    soup = ""
    results = []
    news = []

    def __init__(self, link, file):
        self.link = link
        self.file = file

    def start(self):
        linker = urllib.request.urlopen(self.link)
        self.html = linker.read()
        self.soup = BeautifulSoup(self.html, "html.parser")

    def pars(self):
        self.news = self.soup.find_all("li", class_="liga-news-item")

    def resulter(self):
        for i in self.news:
            title = i.find("span", class_="d-block").get_text(strip=True)
            descr = i.find("span", class_="name-dop").get_text(strip=True)
            link = i.a.get("href")
            self.results.append({
                'title': title,
                'description': descr,
                'href': link,
            })

    def opener_w(self):
        self.file = open(self.file, "w", encoding="utf-8")
        i = 1
        for item in self.results:
            self.file.write(
                f"Нов: {i}\n\nНазв: {item['title']}\nОпис: {item['description']}\nСсыл: {item['href']}\n\n\n")
            i += 1
        self.file.close()

    def lets_go(self):
        self.start()
        self.pars()
        self.resulter()
        self.opener_w()
        print("All done!")
