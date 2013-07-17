import string
import fileinput
outfile = open('IDList.txt','w')
for line in fileinput.input():
	if 'inID' in line:
		for x in line.split(':')[1].split(' '):
			if '(' in x:
				out = x.lstrip('(')
		outfile.write(out + ':' + line.split(':')[0].lstrip().rstrip() + '\n')
outfile.close()
