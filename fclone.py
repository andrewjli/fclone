import sys
import os
import os.path
from tokeniser import tokenise
from detector import compare

def start():
	if sys.version_info[0] >= 3:
		print ("Error: This program is incompatible with Python 3.x")
		sys.exit()
	if len(sys.argv) != 4:
		print "Error: Incorrect number of arguments. Please refer to README.md for more details"
		sys.exit()
	else:
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		substring = sys.argv[3]

	os.system("perl preprocess.pl " + file1)
	os.system("perl preprocess.pl " + file2)

	tokenise(file1+"p")
	tokenise(file2+"p")

	compare(file1+"t", file2+"t", int(substring))

	# clean intermediate files
	if os.path.isfile(file1+"p"):
		os.remove(file1+"p")
	if os.path.isfile(file1+"t"):
		os.remove(file1+"t")
	if os.path.isfile(file2+"p"):
		os.remove(file2+"p")
	if os.path.isfile(file2+"t"):
		os.remove(file2+"t")

	#print "done"

start()
