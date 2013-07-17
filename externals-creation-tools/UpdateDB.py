import sets
import sys
import string
from PTree import *
from progressbar import *

def POSSearch(tree):
	foreign = []
	names = []
	oc = []
	words = []
	if tree.height == 0:
		if tree.content[0] not in  ['*','<'] and tree.name not in [',','.','"',"'",'X','ID','CODE']:
			words.append(tree.content)
			if 'FW' in tree.name:
				foreign.append(tree.content)	
			elif 'NPR' in tree.name:
				names.append(tree.content)
			elif ('VB' in tree.name or (tree.name[0] == 'N' and 'NP' not in tree.name and 'NEG' not in tree.name)
	   		      or tree.name[:3] in ['ADV','A+DJ']):
				oc.append(tree.content)
	else:
		for x in tree.content:
			output = POSSearch(x)
			foreign = foreign + output[0]
			names = names + output[1]
			oc = oc + output[2]
			words = words + output[3]
	return (foreign,names,oc,words)

def findID(tree,ids):
        for child in tree.content:
                if child.name == 'METADATA':
                        for node in child.content:
                                if node.name == 'LETTER':
                                        return node.content.split(':')[0]
                elif child.name == 'ID':
                        id = tree.content[-1].content
                        for key in sorted(ids.keys(), key=lambda s: len(s)*(-1)):
                                if key.lstrip('*').rstrip('*') in id:
                                        return ids[key]
                        else:
                                raw_input('IDError:' + id)

def ParseFiles(argvs,db):
        widgets = ['Files: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
                   ' ', ETA(), ' ']
        pbar = ProgressBar(widgets=widgets, maxval=len(argvs)+1).start()
        for i in range(len(argvs)):
                arg = argvs[i]
                if arg[-3:] in ['ref','psd']:
			#print arg
                        file = open(arg)
                        token = ''
                        for line in file:
				if line == '\n' and 'NP-LOC' in token and 'IP-MAT' not in token:
					token = ''
                                elif line == '\n' and '(ID ' in token:
                                        token = ParseTree(MatchParen(token.lstrip().rstrip())[0][0])
					#print token
					key = findID(token,ids)
					#print key
			                output = POSSearch(token)
					db[key][-2] = db[key][-2] + 1
			                db[key][-1] = [db[key][-1][j]+output[j] for j in range(len(output))]
                                        token = ''
				elif line == '\n':
					token = ''
                                else:
                                        token = token + line.rstrip().lstrip()
		#print i
                pbar.update(i)
        pbar.finish()
        return db

idfile = open('IDList.txt')
idlines = idfile.readlines()
idfile.close()
ids = {}
for line in idlines:
        text = line.rstrip().split(':')
        ids[text[0]] = text[1]

for arg in sys.argv:
	if arg[-3:] == 'txt':
		dbname = arg
		db = {}
		dbfile = open(arg)
		dblines = dbfile.readlines()
		dbfile.close()
		dbout = open(arg + '.bkp', 'w')
		for i in range(len(dblines)):
			line = dblines[i]
			dbout.write(line)
			if i != 0:
				key = line.split(':')[0]
				db[key] = line.split(':')[1].split(',')[:16]
				db[key].append(0)
				db[key].append([[],[],[],[]])
			else:
				firstline = line.split(':')[1].split(',')[:16] + ['Words','OCWords','NamWords','ForWords','Types','OCTypes','NamTypes','ForTypes','Chars','OCChars','NamChars','ForChars','Tokens']
		dbout.close()

db = ParseFiles(sys.argv,db)

dbout = open(dbname,'w')
dbout.write('TextName:'+','.join(firstline)+'\n')
for key in sorted(db.keys()):
	foreign = db[key][-1][0]
	names = db[key][-1][1]
	oc = db[key][-1][2]
	words = db[key][-1][3]
	dbout.write(key+':'+','.join(db[key][:-2])+','+str(len(words))+','+str(len(oc))+','+str(len(names))+','+str(len(foreign))+','+str(len(set([x.lower() for x in words])))+','+str(len(set([x.lower() for x in oc])))+','+str(len(set([x.lower() for x in names])))+','+str(len(set([x.lower() for x in foreign])))+','+str(len([y for x in words for y in x]))+','+str(len([y for x in oc for y in x]))+','+str(len([y for x in names for y in x]))+','+str(len([y for x in foreign for y in x]))+','+str(db[key][-2])+'\n')
dbout.close()
