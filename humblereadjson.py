import json
import re

def readJSON():
	jsonfile = open('humbleresponse.json', 'r')
	jsoncontent = jsonfile.read()
	orderslists = jsoncontent.split('Order:')
	del(orderslists[0])

	ordersjson = []
	for order in orderslists:
		j = json.loads(order)
		ordersjson.append(j)
	return ordersjson

def getProducts(orderlist):
	productList = []
	print("========================")
	for prod in orderlist:
		print (prod['product']['human_name'] + "\n--------------------------")
		for sub in prod['subproducts']:
			print(sub['human_name'])
		print("========================\n")

getProducts(readJSON())