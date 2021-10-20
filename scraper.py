from bs4 import BeautifulSoup


# working file.
file = open("index.html","r", encoding="utf-8")
soup = BeautifulSoup(file,"lxml")

print(soup.prettify())
