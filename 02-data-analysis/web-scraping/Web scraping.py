from bs4 import BeautifulSoup

with open("books.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
#    print(soup.prettify())
    cards = soup.find_all("div", class_="card")
    
    #tags = soup.find("h3")
    #print(tags)