corpus-tools
============

A set of tools used for working on Penn Treebank style parsed corpora

*** count-wordsi-deep.py ***

Usage: python count-words-deep.py [Target label] [Coding slot] [CorpusSearch coding query output]

This python script runs on the output of a CorpusSearch coding query in the deep format and counts the number of ortho nodes under the larget label(s) (multiple labels can be joined with the :, e.g., NP-SBJ:NP-OB1). This assumes that you are coding CPs and want to target elements in the coding strings sister IP. Other configurations will presumably produce weird results. The coding slot says which column of the coding query to replace with the count (following CorpusSearch practice the column numbers start with 1).

Output: a file concatenating the original query name and the target labels


*** count-words.py ***

Usage: python count-words.py [Target label] [Coding slot] [CorpusSearch coding query output]

This python script runs on the output of a CorpusSearch coding query and counts the number of terminal nodes under the larget label(s) (multiple labels can be joined with the :, e.g., NP-SBJ:NP-OB1). This assumes that you are coding CPs and want to target elements in the coding strings sister IP. Other configurations will presumably produce weird results. The coding slot says which column of the coding query to replace with the count (following CorpusSearch practice the column numbers start with 1).

Output: a file concatenating the original query name and the target labels

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

*** Remove Duplicates ***

Usage: python RemoveDup.py *.out

Running this python script will eliminate any duplicate tokens (i.e. tokens with exactly the same surface content).  This can be used to eliminate duplicate texts amoung the corpora (e.g. between the PPCEME and the PCEEC), as well as only counting formulaic phrase, common in letters, once.  Can only be run on the output of a CorpusSearch query.

*** dummy.q ***

Returns all of the tokens (that have IPs). Useful to create a .out file to run RemoveDup.py on.

*** add-cp.q ***

Adds a CP level around all IPs so that coding queries can target the CP level and still cover matrix IPs.

*** remove-dup-cp.q ***

Should be run after add-cp.q to remove duplicate CP levels created around IPs that already had a CP level above them.
