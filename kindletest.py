from lxml import html

f = open("examplekindle.html", "rb")
result = open("kindleoutput.txt", "wb")
content = f.read()
tree = html.fromstring(content)

n = 0

title = tree.get_element_by_id("title" + str(n), None)
author = tree.get_element_by_id("author" + str(n), None)
date = tree.get_element_by_id("date" + str(n), None)
while title is not None:
	outline = "%s;%s;%s;%s\n" % (title.text_content(), author.text_content(), date.text_content(), "Books")
	result.write(outline.encode('utf-8'))
	print(n)
	print(title.text_content())
	print(author.text_content())
	print(date.text_content())
	print ("")
	n +=1
	title = tree.get_element_by_id("title" + str(n), None)
	author = tree.get_element_by_id("author" + str(n), None)
	date = tree.get_element_by_id("date" + str(n), None)