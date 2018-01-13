from lxml import html
import requests
import re
import json

f = open("humbleoutput.txt", 'rb')
content = f.read().decode()
o = open('humble.txt', 'wb')

m = '-{26}\r?\n?Item \\d+\n?-{26}\r?\n?'

contentlist = re.split(m,content)
#print(contentlist)
productlist = []
authorList = {}
platformList = {}
softwarelist = ["Steam", "Origin", "Key"]
bookList = ["eBook"]
videoList = ["Video"]

for prod in contentlist:
	x = prod.strip('\r\n').split('\n')
	x.remove('')
	productlist.append(x[1:])

del(productlist[0])
for p in productlist:
	title = p[0].strip(' ')
	author = p[1].strip(' ')
	platform = p[2].strip(' ')
	category = ''
	key = "\w?key\w?"
	steam = "\w?Steam.*(key)?\w?"
	origin = "\w?Origin \w?key\w?"
	#print(p)
	if re.search(steam, platform, flags=re.IGNORECASE):
		platform = "Steam"
	elif re.search(origin, platform, flags=re.IGNORECASE):
		platform = "Origin"
	elif re.search(key, platform, flags=re.IGNORECASE):
		platform = "Key"

	if re.search(steam, author, flags=re.IGNORECASE):
		platform = "Steam"
	elif re.search(origin, author, flags=re.IGNORECASE):
		platform = "Origin"
	elif re.search(key, author, flags=re.IGNORECASE):
		platform = "Key"

	if author in authorList:
		authorList[author] += 1
	else:
		authorList[author] = 1
	if platform in platformList:
		platformList[platform] += 1
	else:
		platformList[platform] = 1

	if platform in platformList:
		category = "Software"
	elif platform in videoList:
		category = "Video"
	elif platform in bookList:
		category = "Books"
	else:
		category = "Other"


	#print("____________________________\nTitle: {0}\nAuthor:{1}\nPlatform:{2}\n____________________________\n".format(title,author,platform))
	#o.write("____________________________\nTitle: {0}\nAuthor:{1}\nPlatform:{2}\n____________________________\n".format(title,author,platform).encode('utf-8'))
	o.write("{0};{1};{2};{3}\n".format(title,author,platform,category).encode('utf-8'))

#print (authorList)
# for a in authorList:
# 	x = a + "; " + str(authorList[a]) + "\n"
# 	o.write(x.encode('utf-8'))
# o.write("\n\n".encode('utf-8'))
# #print (platformList)
# for p in platformList:
# 	x = p + "; " + str(platformList[p]) + "\n"
# 	o.write(x.encode('utf-8'))


# f = open("humblehtml.html", "rb")
# result = open("humbleoutput.txt", "wb")
# content = f.read()
# tree = html.fromstring(content)

# titles = tree.xpath('//h2/text()')
# for title in titles:
# 	result.write(b"%s\n" % str(title).encode('utf-8'))
# 	print(title)

# url = "https://hr-humblebundle.appspot.com/processlogin"

# #username = input("Email: ")
# #password = input("Password: ")
# username = "cprelerson42@gmail.com"
# password = "BigBlueBox11"
# captcha = input("Captcha response: ")
# authy = input("Authy token: ")


# payload = "ajax=true&username={0}&password={1}&recaptcha_challenge_field=&recaptcha_response_field={2}&authy-token={3}".format(username,password,captcha,authy)

# headers = {
#     'X-Requested-By': "hb_android_app",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "f54baf97-9450-7f2a-793d-0dc02d7f079e"
#     }

#response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)

# keys = open("humbleorderslist", 'r')
# keyscontent = keys.read().strip('\n[]{}').split(',')
# #print(keyscontent)
# orderlist = []
# for k in keyscontent:
# 	orderlist.append(k.strip('\n{}[]'))
# keylist = []
# for order in orderlist:
#     keylist.append(order.split(':')[1].strip('\"'))
# #print(keylist)    

    
# responselist = []
# for key in keylist:
#     exurl = "https://hr-humblebundle.appspot.com/api/v1/order/%s" % key
#     print(exurl)
#     exheaders = {
#         'X-Requested-By': "hb_android_app",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "21696e6d-6939-58d2-959b-ab2def84301f"
#         }

#     exresponse = requests.request("GET", exurl, headers=exheaders)

#     responselist.append(exresponse.text)
# responsefile = open("humbleresponse.json", 'w')
# for line in responselist:
#     responsefile.write("Order:\n" + line + "\n")


# # window.Android = {
# #     setCaptchaResponse: function(challenge, response) {
# #         console.log(response);
# #     }
# # }

# geturl = "https://hr-humblebundle.appspot.com/api/v1/user/order"


# getheaders = {
#     'X-Requested-By': "hb_android_app",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "997165f1-4cb1-fe35-a7b6-02936456d70e"
#     }

# response = requests.request("GET", geturl, headers=getheaders)

# print(response.text)

