import sys, os
import re

try:
    # bibtexdb = open(sys.argv[1]).read()
    bibtexdb = open(os.path.dirname(__file__)+"/jfm_full.bib").read()
except:
    print("Error: specify the file to be processed!")
FILE_NAME = "journalList.txt"
url = "https://gist.githubusercontent.com/FilipDominec/6df14b3424e335c4a47a96640f7f0df9/raw/74876d2d5df9ed60492ef3a14dc3599a6a6a9cfc/journalList.txt"


if not os.path.isfile(FILE_NAME):
    import urllib.request
    urllib.request.urlretrieve(url, FILE_NAME)
rulesfile = open(FILE_NAME)

for rule in rulesfile.readlines()[::-1]:           ## reversed alphabetical order matches extended journal names first
    pattern1, pattern2 = rule.strip().split(" = ")
    # avoid mere abbreviations
    if pattern1 != pattern1.upper() and (' ' in pattern1):
        repl = re.compile(re.escape(pattern1), re.IGNORECASE)
        (bibtexdb, num_subs) = repl.subn(pattern2, bibtexdb)

        if num_subs > 0:
            print("Replaced (%ix) '%s' FOR '%s'" % (num_subs, pattern1, pattern2))
with open(os.path.dirname(__file__)+"/jfm.bib", 'w') as outfile:
    outfile.write(bibtexdb)
    print("Bibtex database with abbreviated files saved into 'jfm.bib'")
