# -- coding: utf-8 --

from nose.tools import *
from pixivsort.main import Main
import re, os, shutil


def test_arguments():
	"""Test if arguments are read correctly."""
	src_path = u"./test/testsource"
	dst_path = u"./test/testdestination"
	
	argv = ("main.py", src_path, dst_path)
	
	main = Main(argv)
	
	assert main.src_path == src_path
	assert main.dst_path == dst_path

@raises(SystemExit)
def test_missing_arguments():
	"""Test if script exits on too few arguments."""
	src_path = u"./test/testsource"
	
	# First test with too few arguments.
	argv = ("main.py", src_path)
	main = Main(argv)

@raises(SystemExit)
def test_additional_arguments():
	"""Test if script exits on too many arguments."""
	src_path = u"./test/testsource"
	dst_path = u"./test/testdestination"
	
	# First test with too few arguments.
	argv = ("main.py", src_path, dst_path, dst_path)
	main = Main(argv)

@raises(SystemExit)
def test_wrong_src_argument():
	"""Test if script exits when source argument is a file."""
	src_path = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	dst_path = u"./test/testdestination"
	
	# First test with too few arguments.
	argv = ("main.py", src_path, dst_path)
	main = Main(argv)

@raises(SystemExit)
def test_wrong_dst_argument():
	"""Test if script exits when destination argument is a file"""
	src_path = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	dst_path = u"./test/testdestination"
	
	# First test with too few arguments.
	argv = ("main.py", dst_path, src_path)
	main = Main(argv)

def test_run():
	"""Test a full run."""
	src_path = u"./test/testsource"
	dst_path = u"./test/testdestination"
	
	argv = ("main.py", src_path, dst_path)
	
	main = Main(argv)
	main.run()
	
	destfile1 = u"./test/testdestination/rosa (814837)/"
	destfile1 += u"(814837) ろさ - 空と私.jpg"
	assert os.path.exists(destfile1) == True
	destfile2 = u"./test/testdestination/cherrypin (206921)/"
	destfile2 += u"(206921) cherrypin - イラスト集め"
	assert os.path.exists(destfile2) == True
	
	# Copy files back
	shutil.copy2(destfile1, src_path)
	os.remove(destfile1)
	
	shutil.copytree(destfile2, 
					u"./test/testsource/(206921) cherrypin - イラスト集め")
	shutil.rmtree(destfile2)
	
	srcfile1 = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	assert os.path.exists(srcfile1) == True
	srcfile2 = u"./test/testsource/(206921) cherrypin - イラスト集め"
	assert os.path.exists(srcfile2) == True