# -- coding: utf-8 --

from nose.tools import *
from pixivsort.search import Search
from pixivsort.image import Image
import re, os


def test_find_images():
	src_regex = re.compile("(?<=^\()\d*(?=\))")
	dst_regex = re.compile("(?<=\()\d*(?=\)$)")
	
	search = Search(u"./tests/testsource",
					u"./tests/testdestination",
					src_regex,
					dst_regex)
	imglist = search.find_images()
	
	for img in imglist:
		print img.artist_id
		assert img.artist_id in (u"206921", u"814837")