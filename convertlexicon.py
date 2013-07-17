import string
import sys
alphabet = []
for char in string.letters:
	alphabet.append(char)
alphabet.append('$')
alphabet.append('+')
for arg in sys.argv:
	if arg[-3:] == 'out':
		oldfile = open(arg)
		newfile = open(str(arg[:-3]+'lex'), 'w')
		for line in oldfile:
			aline = line.split(':')
			newline = aline[0].split(' ')
			for item in newline:
				if len(item) > 0:					
					if item[0] in alphabet:
						newfile.write(str(item + '|'))


