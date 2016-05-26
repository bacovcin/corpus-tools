import sys

# Use a dictionary of dictionary to store tokens to check for duplicates
# Key of first dictionary: First word
# Key of second dictionary: Second word
# Value of second dictionary: Token
tokens = {}

# Remove duplicates from every file in arguments
for arg in sys.argv:
    if arg[-3:] == 'out':
        # Open files
        infile = open(arg)
        outfile = open(arg[:-3]+'psd', 'w')
        start = 0
        write = 0
        lines = infile.readlines()
        # Read all of the lines
        for i in range(len(lines)):
            line = lines[i]
            if '/~*' in line:  # Start of text of token
                token = []
                start = 1
                write = 0
            elif '*~/' in line:  # End of text of token
                # See if token has already been seen
                # If not write out the tree, and add to DoD
                # If it has, don't write out tree
                start = 0
                tokent = ''.join(token[:-1])  # Token as text
                tokenl = tokent.split(' ') + ['', '']  # Token as list
                try:
                    token1 = tokens[tokenl[0]]  # Stored first words
                    try:
                        if tokent not in token1[tokenl[1]]:
                            write = 1
                            tokens[token[0]][tokenl[1]].append(tokent)
                    except:
                        write = 1
                        tokens[tokenl[0]][tokenl[1]] = [tokent]
                except:
                    write = 1
                    tokens[tokenl[0]] = {}
                    tokens[tokenl[0]][tokenl[1]] = [tokent]
            elif write == 1:  # Line contains parts of unseen tree, write out
                outfile.write(line)
            elif start == 1:  # Part of token text, store for later
                token.append(line)
        outfile.close()
