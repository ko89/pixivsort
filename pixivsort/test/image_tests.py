# -- coding: utf-8 --

from nose.tools import *
from pixivsort.image import Image
import re, os

def test_path():
	"""Test path of Image file object."""
	
	path = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, re_pattern)
	assert_equal(img.path, path)
    
def test_regex():
	"""Test regex of Image file object."""

	path = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, re_pattern)
	assert_equal(img.re_pattern, re_pattern)

def test_id_file():
	"""Test id of Image file object."""
	path = u"./test/testsource/(814837) ろさ - 空と私.jpg"
		
	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, re_pattern)
	assert_equal(img.artist_id, u"814837")

def test_id_dir():
	"""Test id of Image directory object."""
	path = u"./test/testsource/(206921) cherrypin - イラスト集め"
	
	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(path, re_pattern)
	assert_equal(img.artist_id, u"206921")

def test_copy_file():
	"""Test copying an Image file object."""
	# If pathnames don't work a switch will be needed
	# using: platform.system() == 'Windows'
	
	sourcefile = u"./test/testsource/(814837) ろさ - 空と私.jpg"
	destpath = u"./test/testdestination"

	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(sourcefile, re_pattern)
	
	img.copy(destpath)
	
	destfile = 	u"./test/testdestination/(814837) ろさ - 空と私.jpg"
	assert os.path.exists(destfile) == True
	
	# Move image back.
	img2 = Image(destfile, re_pattern)
	
	img2.copy(sourcefile)

def test_copy_dir():
	"""Test copying an Image directory object."""
	# If pathnames don't work a switch will be needed
	# using: platform.system() == 'Windows'
	
	# Location of the test directory and the test destination
	sourcefile = u"./test/testsource/(206921) cherrypin - イラスト集め"
	destpath = u"./test/testdestination"

	# Create Image object and move it to the test destination
	re_pattern = re.compile("(?<=^\()\d*(?=\))")
	img = Image(sourcefile, re_pattern)
	img.copy(destpath)
	
	# The directory and it's contents should now be at the test destination
	destfile = 	u"./test/testdestination/(206921) cherrypin - イラスト集め"
	# If not the test fails
	assert os.path.exists(destfile) == True
	
	# Move directory back in place.
	img2 = Image(destfile, re_pattern)
	img2.copy(u"./test/testsource")