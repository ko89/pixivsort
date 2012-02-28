# -- coding: utf-8 --

from nose.tools import *
from pixivsort.search import Search
from pixivsort.image import Image
import re, os


def test_find_images():
	"""Test search of images."""
	src_regex = re.compile("(?<=^\()\d*(?=\))")
	dst_regex = re.compile("(?<=\()\d*(?=\)$)")
	
	search = Search(u"./test/testsource",
					u"./test/testdestination",
					src_regex,
					dst_regex)
	imglist = search.find_images()
	
	assert len(imglist) == 2
	
	for img in imglist:
		print img.artist_id
		assert img.artist_id in (u"206921", u"814837")

def test_find_artists():
	"""Test search of artists."""
	src_regex = re.compile("(?<=^\()\d*(?=\))")
	dst_regex = re.compile("(?<=\()\d*(?=\)$)")
	
	search = Search(u"./test/testsource",
					u"./test/testdestination",
					src_regex,
					dst_regex)
					
	artistlist = search.find_artists()
	
	assert len(artistlist) == 2
	
	for artist in artistlist:
		assert artist.id in (u"206921", u"814837")