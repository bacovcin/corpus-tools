corpus-tools
============

A set of tools used for working on Penn Treebank style parsed corpora

*** only-coding.q from Beatrice Santorini

This CS query file prints only the coding string, giving a .cod.ooo file
suitable for import into e.g. R, or further processing with automated
tools.

*** findlexicon.py ***

Usage: python findlexicon.py [Minimum number of uses] [CorpusSearch lexicon output files]

This python script runs through a lexicon file and will return any word which was used more often than the minimum number of uses argument. This is outputed to a new file with the same name as the input files, but with a .txt extension.  For it to work properly, you need to delete the summary and totals at the top and bottom of the file.

*** convertlexicon.py ***

Usage: python findlexicon.py [CorpusSearch lexicon output files]

This python script runs through a lexicon file and will return a new file which has all of the words from the lexicon file seperated by a pipe, which makes it easy to copy and use in future queries. The output file has a .lex file extension. For it to work properly, you need to delete the summary and totals at the top and bottom of the file.

*** External Coding ***

Usage: CS external.c (or oldeng_external.c) *.ref; CS only-coding.q *.cod; python fill-in-externals.py *.ooo

This set of tools can be used to expand data about the texts in the English corpora.  First one runs external.c or (oldeng_external.c) to ID tag the texts, then one adds whatever relevant internal tagging is necessary.  One generates an .ooo file, and then runs the fill-in-externals.py on the .ooo, which adds in information like year of composition to the file.

*** Remove Duplicates ***

Usage: python RemoveDup.py *.out

Running this python script will eliminate any duplicate tokens (i.e. tokens with exactly the same surface content).  This can be used to eliminate duplicate texts amoung the corpora (e.g. between the PPCEME and the PCEEC), as well as only counting formulaic phrase, common in letters, once.  Coding conventions relating to genre can be found in CodingConventions.txt.
