#  filter_dict.py
#  
# This script filters out words which are not in our corpus.
# It requires a list of the words in the corpus: words.txt

import os
import sys


error = 0
argv_len = len(sys.argv)
if argv_len < 3 or argv_len > 3:
    error = 1




if error == 1:
    print("syntaxe -> python filter_dict.py lexicon_path word_path")
    exit(1)


lexicon_path = sys.argv[1]

word_path = sys.argv[2]




ref = dict()
phones = dict()
try:
    with open(lexicon_path) as f:
        for line in f:
            line = line.strip()
            columns = line.split(" ", 1)
            word = columns[0]
            pron = columns[1]
            try:
                ref[word].append(pron)
            except:
                ref[word] = list()
                ref[word].append(pron)

except FileNotFoundError:
    print("file not found " + lexicon_path)
    exit(1)

# print(ref)

lex = open(lexicon_path, "w")
try:
    with open(word_path) as f:
        for line in f:
            line = line.strip()
            if line in ref.keys():
                for pron in ref[line]:
                    lex.write(line + " " + pron+"\n")
            else:
                print("Word not in lexicon:" + line)
except FileNotFoundError:
    print("file not found " + word_path)
    exit(1)
