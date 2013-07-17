import string
import sys
from progressbar import *
tokens = []
for arg in sys.argv:
	if arg[-3:] == 'out':
		file = open(arg)
		outfile = open(arg[:-3]+'psd','w')
		start = 0
		write = 0
		widgets = ['Lines: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
                   ' ', ETA(), ' ']
		pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
		lines = file.readlines()
		for i in range(len(lines)):
			line = lines[i]
			if '/~*' in line:
				token = []
				start = 1
				write = 0
			elif '*~/' in line:
				start = 0
				tokent = ''.join(token[:-1])
				if tokent not in tokens:
					write = 1
					tokens.append(tokent)
				else:
					print tokent
			elif write == 1:
				outfile.write(line)
			elif start == 1:
				token.append(line)
			pbar.update(i)
		pbar.finish()
		outfile.close()
