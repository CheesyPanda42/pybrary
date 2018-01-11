from lxml import html
from lxml import etree as ET
import tkinter as tk
from tkinter import ttk
from Tooltip import *
from tkinter import Menu
from tkinter import scrolledtext as scroll
from tkinter import Listbox
from tkinter.ttk import Treeview

#import xml.etree.ElementTree as ET
parser = ET.XMLParser(remove_blank_text=True)
configTree = ET.parse('config.xml', parser = parser)
configRoot = configTree.getroot()

class PybraryGUI():
	def __init__(self):
		# create window
		self.window = tk.Tk()
		self.window.title("Pybrary")
		self.window.minsize(width = 300, height = 300)

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
		print("Tabs")
		self.tabControl = ttk.Notebook(self.window)
		tablist = configRoot.findall('tablist/tab')
		self.tabRefList = []
		for t in tablist:
			tab = ttk.Frame(self.tabControl)
			self.tabRefList.append(tab)
			self.tabControl.add(tab, text = t.attrib['label'])
		self.tabControl.pack(expand = 1, fill = 'both')

		#for tab in self.tabRefList:
		#	labelFrame = ttk.LabelFrame(tab)
		#	labelFrame.config(text = self.tabControl.tab(labelFrame.winfo_parent())['text'])
		#	labelFrame.grid(column = 0, row = 0, padx = 8, pady = 4)


	def setupWidgets(self):
		#probably want treeview, not listbox
		scr_w = 180
		scr_h = 10
		for tab in self.tabControl.winfo_children():
			#scr = scroll.ScrolledText(tab, width = scr_w, height = scr_h, wrap = tk.WORD)
			listbox = Listbox(tab, width = 120)
			listbox.grid(column = 0, row = 0, padx = 20, pady = 10)
			#print(scr.winfo_parent())

			treeview = Treeview(tab)
			treeview['columns'] = ('Title', 'Author')
			treeview.heading('Title', text = "Title")
			treeview.grid(column = 0, row =1)


	def newItem(self):
		print("New item")

	def _quit(self):
		print("Quitting")
		self.window.quit()
		self.window.destroy()
		exit()


def main():
	win = PybraryGUI()
	win.setupGUI()

	datafile = open('humbleoutput.txt','r')
	data = datafile.read().split('\n')
	#print(data)
	for child in win.tabRefList[0].winfo_children()[0].winfo_children():
		print(child)

	scrolltext =  win.tabRefList[0].winfo_children()[0]
	tree = win.tabRefList[0].winfo_children()[1]
	print(scrolltext)
	print(tree)
	for d in data:
		scrolltext.insert(tk.END, d + '\n')
		tree.insert('', 'end', text="", values=(d,""))
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