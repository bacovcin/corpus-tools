import string
import sys
alphabet = []
for char in string.letters:
	alphabet.append(char)
alphabet.append('$')
alphabet.append('+')
toknum = int(sys.argv[1])
print toknum
for arg in sys.argv:
	if arg[-3:] == 'out':
		oldfile = open(arg)
		newfile = open(str(arg[:-3]+'txt'), 'w')
		for line in oldfile:
			aline = line.split(':')
			newline = aline[0].split(' ')
			if newline[-1].isdigit():
				if int(newline[-1]) > toknum:
					newfile.write(str(newline[0]+'\n'))
		oldfile.close()
		newfile.close()	


