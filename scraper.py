from bs4 import BeautifulSoup

file = open("index.html","r")
soup = BeautifulSoup(file, 'lxml')

print(soup.prettify())
