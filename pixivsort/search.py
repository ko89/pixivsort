import os, re
from pixivsort.image import Image
from pixivsort.artist import Artist

class Search(object):

	def __init__(self, src_path, dst_path, src_regex, dst_regex):
		self.src_path = src_path
		self.dst_path = dst_path
		self.src_regex = src_regex
		self.dst_regex = dst_regex
		
	def find_images(self):
		"""Reads the source path and finds image files and directories.
			Returns a list of all Image file and directory objects."""
		imagelist = []
		filelist = os.listdir(self.src_path)
		for file in filelist:
			filepath = os.path.join(self.src_path, file)
			if os.path.isfile(filepath):
				img = Image(filepath, self.src_regex)
				if img.artist_id != None:
					imagelist.append(img)
			else:
				img = Image(filepath, self.src_regex)
				imagelist.append(img)
				
		return imagelist
	
	def find_artists(self):
		"""Reads the destination path and finds artist directories.
			Returns a list of all Artist directory objects."""
		artistlist = []
		dirlist = os.listdir(self.dst_path)
		for dir in dirlist:
			dirpath = os.path.join(self.dst_path, dir)
			if os.path.isdir(dirpath):
				artist = Artist(dirpath, self.dst_regex)
				if artist.id != None:
					artistlist.append(artist)

		return artistlist