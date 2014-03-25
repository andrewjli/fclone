from distutils.core import setup
import py2exe

setup(
	name="FClone",
	version="0.1",
	description="A simple code similarity detector for Java source code",
	console=['fclone.py'],
	data_files=[('',[
		'README.md',
		'preprocess.pl'
	])],
)
