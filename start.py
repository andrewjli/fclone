import sys
import os
from tokeniser import tokenise
from detector import compare

def start():
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	substring = sys.argv[3]

	os.system("perl preprocess.pl " + file1)
	os.system("perl preprocess.pl " + file2)

	tokenise(file1+"p")
	tokenise(file2+"p")

	compare(file1+"t", file2+"t", int(substring))

	# clean intermediate files
	os.remove(file1+"p")
	os.remove(file1+"t")
	os.remove(file2+"p")
	os.remove(file2+"t")

	#print "done"

start()
