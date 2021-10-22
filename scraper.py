from bs4 import BeautifulSoup
with open("index.html", "r") as fp:
    soup = BeautifulSoup(fp.read() , "html.parser")

    tdList = soup.find_all('td')
    for i in range(len(tdList)):
        dat = str(tdList[i].text).strip()
        print(len(dat))
