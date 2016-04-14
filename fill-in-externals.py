<<<<<<< HEAD
import string
import sys
from progressbar import *

def RepresentsInt(s):
	try: 
		int(s)
		return True
        except ValueError:
	        return False

db = {}
infile = open('Eng_Db.txt')
lines = infile.readlines()
infile.close()
cnames = lines[0].rstrip().split(':')[1].split(',')
for line in lines[1:]:
	db[line.split(':')[0]] = line.split(':')[1].split(',')
llist = []
for arg in sys.argv:
	if arg[-3:] == 'ooo':
		infile = open(arg)
		lines = infile.readlines()
		infile.close()
		widgets = ['Lines: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
                   ' ', ETA(), ' ']
		pbar = ProgressBar(widgets=widgets, maxval=len(lines)+1).start()
		for i in range(len(lines)):
			line = lines[i]
			newline = line.rstrip().split(':')
			if RepresentsInt(newline[-1][0]):
				newline = newline[:-2] + [newline[-2]+':'+newline[-1]]
			if newline[0] != 'x':
				for key in db.keys():
					if '_' not in key:
						continue
					else:
						text = key.split('_')[0]
						letnum = key.split('_')[1]
						if text in newline[-1] and newline[0] == letnum:
							a_line = [letnum+'_'+newline[-1].lstrip('_@')]+db[key] + newline[1:-1]
							break
			else:
				for key in db.keys():
					if '_' not in key and key in newline[-1]:			
						a_line = [newline[-1].lstrip('_@')]+db[key] + newline[1:-1]
			try:
				llist.append(a_line)
				pbar.update(i)
			except:
				pbar.update(i)
				continue
		pbar.finish()
		null = []
		for i in range(len(llist[0])):
			null.append(0)
		for list in llist:
			for i in range(len(list)):
				if list[i] != '_':
					null[i] = 1
		newlines = []
		for list in llist:
			string = list[0]
			for i in range(len(list)-1):
				if null[i+1] != 0:
					string = string + '\t' + list[i+1].rstrip('\n')
			newlines.append(string + '\n')
		outfile = open('.'.join(arg.split('.')[:-2])+'.tsv','w')
		outfile.write('ID'+'\t'+'\t'.join(cnames)+'\n')	
		for line in newlines:
			outfile.write(line)
		outfile.close()
=======
import string
import sys
from progressbar import *
db = {}
infile = open('Eng_Db.txt')
lines = infile.readlines()
infile.close()
cnames = lines[0].rstrip().split(':')[1].split(',')
for line in lines[1:]:
	db[line.split(':')[0]] = line.split(':')[1].split(',')
llist = []
for arg in sys.argv:
	if arg[-3:] == 'ooo':
		infile = open(arg)
		lines = infile.readlines()
		infile.close()
		widgets = ['Lines: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
                   ' ', ETA(), ' ']
		pbar = ProgressBar(widgets=widgets, maxval=len(lines)+1).start()
		for i in range(len(lines)):
			line = lines[i]
			idsplit = line.rstrip().split('@')
			newline = idsplit[0].split(':')+[idsplit[1]]
			if newline[0] != 'x':
				for key in db.keys():
					if '_' not in key:
						continue
					else:
						text = key.split('_')[0]
						letnum = key.split('_')[1]
						if text in newline[-1] and newline[0] == letnum:
							a_line = [letnum+'_'+newline[-1],key]+db[key] + newline[1:-1]
							break
			else:
				for key in db.keys():
					if '_' not in key and key in newline[-1]:			
						a_line = [newline[-1],key]+db[key] + newline[1:-1]
			llist.append(a_line)
			pbar.update(i)
		pbar.finish()
		null = []
		for i in range(len(llist[0])):
			null.append(0)
		for list in llist:
			for i in range(len(list)):
				if list[i] != '_':
					null[i] = 1
		newlines = []
		for list in llist:
			string = list[0]
			for i in range(len(list)-1):
				if null[i+1] != 0:
					string = string + '\t' + list[i+1].rstrip('\n')
			newlines.append(string + '\n')
		outfile = open('.'.join(arg.split('.')[:-2])+'.tsv','w')
		outfile.write('ID'+'\t'+'Text'+'\t'+'\t'.join(cnames)+'\n')	
		for line in newlines:
			outfile.write(line)
		outfile.close()
>>>>>>> f0046c7e2ad5cedc61d70c355b8f21c3629b2153
