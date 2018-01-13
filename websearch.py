from urllib import request
import webbrowser as wb

def google(search):
	URL = "http://www.google.com/search?q="
	print(URL + search)
	wb.open(URL + search)
	#http://store.steampowered.com/search/?term=rocket+league