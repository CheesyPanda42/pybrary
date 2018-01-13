from lxml import html
from lxml import etree as ET
import tkinter as tk
from tkinter import ttk
from Tooltip import *
from tkinter import Menu
from tkinter import scrolledtext as scroll
from tkinter import Listbox
from tkinter.ttk import Treeview
from tkinter import Scrollbar
from tkinter import messagebox as msg
import re
#import xml.etree.ElementTree as ET
parser = ET.XMLParser(remove_blank_text=True)
configTree = ET.parse('config.xml', parser = parser)
configRoot = configTree.getroot()

class PybraryGUI():
	def __init__(self):
		# create window
		self.window = tk.Tk()
		self.window.title("Pybrary")
		self.window.minsize(width = 600, height = 600)

	def setupGUI(self):
		self.setupMenu()
		self.setupTabs()
		self.setupWidgets()

	def setupMenu(self):
		print("Creating Menus...")
		# Create menu bar
		self.menu_bar = Menu(self.window)
		self.window.config(menu = self.menu_bar)

		# Create menus per menus.xml file
		menulist = configRoot.findall('menubar/menu')

		for m in menulist:
			menu = Menu(self.menu_bar, tearoff = 0)
			itemlist = m.findall('item')
			for i in itemlist:
				callback = getattr(self, i[0].text)
				menu.add_command(label = i.attrib['label'], command = callback)
			self.menu_bar.add_cascade(label = m.attrib['label'], menu = menu)

	def setupTabs(self):
		print("Setting up tabs")
		self.tabControl = ttk.Notebook(self.window)
		tablist = configRoot.findall('tablist/tab')
		self.tabRefList = []
		for t in tablist:
			tab = ttk.Frame(self.tabControl)
			self.tabRefList.append(tab)
			self.tabControl.add(tab, text = t.attrib['label'])
		self.tabControl.pack(expand = True, fill = tk.BOTH)


	def setupWidgets(self):
		#probably want treeview, not listbox
		scr_w = 180
		scr_h = 10
		for tab in self.tabControl.winfo_children():
			# listbox = Listbox(tab, width = 120)
			# listbox.grid(column = 0, row = 0, padx = 20, pady = 10)
			treeview = Treeview(tab)
			treeview['columns'] = ('Title', 'Author', 'Platform')
			treeview.heading("#0", text = "ID")
			treeview.column('#0', minwidth=50, width=50, stretch=False)
			treeview.heading('Title', text = "Title")
			treeview.heading('Author', text = "Author")
			treeview.heading('Platform', text = "Platform")
			treeview.grid(column = 0, row =0, sticky="NSEW", )
			treeview.bind("<Double-1>", self.itemSelected)
			treeview.config(height=25)
			
			scrollbar = Scrollbar(tab)
			scrollbar.grid(column=1, row=0, sticky="NS")
			treeview.config(yscrollcommand = scrollbar.set)
			scrollbar.config(command=treeview.yview)
		#treeCol = self.tabRefList[0].winfo_children()[0].column('#0', minwidth=50, width=50, stretch=False)




	def itemSelected(self, event):
		print(event.widget)
		#item = self.tabRefList[0].winfo_children()[0].selection()
		item = event.widget.selection()
		value = event.widget.item(item, "values")
		#msg.showinfo("Item Selected", "Title: {0}\nAuthor: {1}\nPlatform: {2} ".format(value[0], value[1], value[2]))
		import websearch
		websearch.google(value[0])

	def newItem(self):
		print("New item")

	def _quit(self):
		print("Quitting")
		self.window.quit()
		self.window.destroy()
		exit()

def parseData(data):
	# lines = "____________________________"
	parsedData = []
	itemData = ['','','']
	for d in data:
		temp = d.split(';')
		#print(temp)
		if(temp[0] == ''):
			continue
		itemData[0] = temp[0]
		itemData[1] = temp[1]
		itemData[2] = temp[2]
		parsedData.append(itemData.copy())
	return parsedData


def main():
	win = PybraryGUI()
	win.setupGUI()

	datafile = open('output','rb')
	data = datafile.read().decode().split('\n')
	scrolltext =  win.tabRefList[0].winfo_children()[0]
	tree = win.tabRefList[0].winfo_children()[0]
	_id = 0

	parsedData = parseData(data)

	for d in parsedData:
		tree.insert('', 'end', text=_id, values=(d[0],d[1],d[2]))
		_id += 1

	datafile = open('kindleoutput.txt','rb')
	data = datafile.read().decode().split('\n')
	scrolltext =  win.tabRefList[0].winfo_children()[0]
	tree = win.tabRefList[0].winfo_children()[0]
	_id = 0

	parsedData = parseData(data)

	for d in parsedData:
		tree.insert('', 'end', text=_id, values=(d[0],d[1],d[2]))
		_id += 1

	win.window.mainloop()

if __name__ == '__main__':
	main()


# for menu in menuroot.findall('menu'):
# 		print(menu.attrib['label'])
# 		for item in menu.findall('item'):
# 			print("|--->" + item.attrib['label'])
# 			for child in item.iter():
# 				if child.text is not None:
# 					print("||------>" + child.text)