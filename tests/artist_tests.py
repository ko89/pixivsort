# -- coding: utf-8 --

from nose.tools import *
from pixivsort.artist import Artist
import re, os


def test_path():
	"""Test path of Artist object."""
	path = u"./tests/testdestination/cherrypin (206921)"
	re_pattern = re.compile("(?<=\()\d*(?=\)$)")
	
	artist = Artist(path, re_pattern)
	assert artist.path == path

def test_id():
	"""Test ID of Artist object."""
	path = u"./tests/testdestination/cherrypin (206921)"
	re_pattern = re.compile("(?<=\()\d*(?=\)$)")
	
	artist = Artist(path, re_pattern)
	assert artist.id == u"206921"
