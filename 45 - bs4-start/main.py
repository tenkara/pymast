from bs4 import BeautifulSoup 

with open("website.html", 'r', encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))  

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

heading = soup.select_one(selector=".heading")
print(heading)

form_tag = soup.find("input")
max_length = form_tag.get("maxlength")
print(max_length)
