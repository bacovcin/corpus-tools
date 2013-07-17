import string
from PTree import *
import sys
def findID(tree,ids):
        for child in tree.content:
		if child.name == 'METADATA':
			for node in child.content:
				if node.name == 'LETTER':
					return node.content.split(':')[0]
        	elif child.name == 'ID':
			id = tree.content[-1].content
			for key in ids.keys():
				if key.lstrip('*').rstrip('*') in id:
					raw_input(ids[key])
		        	        return ids[key]
			else:
				raw_input(id)

idfile = open('IDList.txt')
idlines = idfile.readlines()
idfile.close()
ids = {}
for line in idlines:
        text = line.split(':')
        ids[text[0]] = text[1]

toklist = ParseFiles(sys.argv)
for key in toklist:
	text = toklist[key]
	for token in text:
		findID(token,ids)
