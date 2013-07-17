import string
import sys
db = {}
infile = open('Eng_Db.txt')
lines = infile.readlines()
infile.close()
cnames = lines[0].rstrip().split(':')[1].split(',')
for line in lines[1:]:
	db[line.split(':')[0]] = line.split(':')[1]
llist = []
for arg in sys.argv:
	if arg[-3:] == 'ooo':
		infile = open(arg)
		lines = infile.readlines()
		infile.close()
		for line in lines:
			newline = line.rstrip().split(':')
			if newline[1] != 'x':
				a_line = ['_'.join(newline[:2])] + newline[2:]
			else:
				a_line = [newline[0]] + newline[2:]
			llist.append(a_line)
		null = []
		for i in range(len(llist[0])):
			null.append(0)
		for list in llist:
			for i in range(len(list)):
				if list[i] != '_':
					null[i] = 1
		newlines = []
		for list in llist:
			string = str(str(list[0])+','+db[list[0]]).rstrip()
			for i in range(len(list[1:])):
				if null[i+1] != 0:
					string = string + ',' + list[i+1]
			newlines.append(string + '\n')
		outfile = open(arg.split('.')[0]+'.csv','w')
		outfile.write('Text'+','+','.join(cnames)+'\n')	
		for line in newlines:
			print line
			outfile.write(line)
		outfile.close()
