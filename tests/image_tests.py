# -- coding: utf-8 --

from nose.tools import *
from pixivsort.image import Image
import re, platform, os

def test_path():
	"""This test loads an image file
		and checks if the path is set correctly."""
	
	path = u"./tests/testsource/(814837) ろさ - 空と私.jpg"
	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, pattern)
	assert_equal(img.path, path)
    
def test_regex():
	"""This test loads an image file
		and checks if the regular expression is set correctly."""

	path = u"./tests/testsource/(814837) ろさ - 空と私.jpg"
	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, pattern)
	assert_equal(img.re_pattern, pattern)

def test_id_file():
	"""This test loads an image file
		and checks if the id has been read correctly."""
	path = u"./tests/testsource/(814837) ろさ - 空と私.jpg"
		
	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, pattern)
	assert_equal(img.artist_id, u"814837")

def test_id_dir():
	"""This test loads an image directory
		and checks if the id has been read correctly."""
	path = u"./tests/testsource/(206921) cherrypin - イラスト集め"
	
	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, pattern)
	assert_equal(img.artist_id, u"206921")

def test_copy_file():
	"""This test will copy an image file to a destination
		and check if it arrived."""
	# If pathnames don't work a switch will be needed
	# using: platform.system() == 'Windows'
	
	sourcefile = u"./tests/testsource/(814837) ろさ - 空と私.jpg"
	destpath = u"./tests/testdestination"

	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(sourcefile, pattern)
	
	img.copy(destpath)
	
	destfile = 	u"./tests/testdestination/(814837) ろさ - 空と私.jpg"
	assert os.path.exists(destfile) == True
	
	# Move image back.
	img2 = Image(destfile, pattern)
	
	img2.copy(sourcefile)

def test_copy_dir():
	"""This test will copy a directory to a destination
		and check if it arrived."""
	# If pathnames don't work a switch will be needed
	# using: platform.system() == 'Windows'
	
	# Location of the test directory and the test destination
	sourcefile = u"./tests/testsource/(206921) cherrypin - イラスト集め"
	destpath = u"./tests/testdestination"

	# Create Image object and move it to the test destination
	pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(sourcefile, pattern)
	img.copy(destpath)
	
	# The directory and it's contents should now be at the test destination
	destfile = 	u"./tests/testdestination/(206921) cherrypin - イラスト集め"
	# If not the test fails
	assert os.path.exists(destfile) == True
	
	# Move directory back in place.
	img2 = Image(destfile, pattern)
	img2.copy(u"./tests/testsource")