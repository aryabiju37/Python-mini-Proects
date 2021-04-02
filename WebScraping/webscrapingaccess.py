from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")
classElements = soup.select(".special")
# print(byClass)
# for el in classElements:
#     print(el.get_text())
# for el in classElements:
#     print(el.name)
# for el in soup.select(".special"):
#     print(el.attrs)

# attr = soup.find("h3")["data-example"]
# print(attr)

# ids = soup.find("div")["id"]
# print(ids)

#.attrs to get all the key-value attributes:
attr = soup.find("div").attrs
print(attr)