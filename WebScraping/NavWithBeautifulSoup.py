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
    <li class="special" "super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
""" 
soup = BeautifulSoup(html,"html.parser")
# cntnt = soup.body.contents
# print(cntnt)
#27 and 28 returns the same thing
# print(soup.body.div)
# print(soup.find("div"))
#30 gives all the instances of the div tag
# print(soup.find_all("div"))
# cnt = soup.body.contents[1]
# print(cnt)
# print(type(cnt))
# inner_elts_of_cnt = soup.body.contents[1].contents
# print(inner_elts_of_cnt)

#find by attributes like id, class name etc,id is unique so only find would work, use find_all for class
# d = soup.find(id="first")
# d = soup.find_all(class_ = "special")
# print(d)
#getSiblings
# nxtSiblings = soup.body.contents[1].next_sibling.next_sibling
# print(nxtSiblings)
# data = soup.find(class_="super-special").parent.parent
# print(data)
#find next siblings with find_next_parent
# data1 = soup.find(id="first").find_next_sibling().find_next_sibling()
# print(data1)
# data2 = soup.select("[data-example]")
# print(data2)
# data3 = soup.select("[data-example]")[1].find_previous_sibling()
# print(data3)
#finding the next/previous parent/sibling by tag names:
# data4 = soup.find("h3").find_parent("html")
# print(data4)
# help(data4)
  