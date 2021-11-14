from bs4 import BeautifulSoup

# import lxml
with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)

print(soup.findAll(name="a"))
print(soup.findAll(name="h1", id="name"))
# since class is a keyword use class_
print(soup.findAll(name="h3", class_="heading"))
all_anchor_tags = soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

print(soup.select_one(selector="p a"))
print(soup.select_one(selector="#name"))
print(soup.select_one(selector=".heading"))