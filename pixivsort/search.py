import imghdr, os, re
from pixivsort.image import Image

class Search(object):

	def __init__(self, src_path, dst_path, src_regex, dst_regex):
		self.src_path = src_path
		self.dst_path = dst_path
		self.src_regex = src_regex
		self.dst_regex = dst_regex
		
	def find_images(self):
		imagelist = []
		filelist = os.listdir(self.src_path)
		for file in filelist:
			filepath = os.path.join(self.src_path, file)
			if os.path.isfile(filepath):
				if imghdr.what(filepath) != None:
					img = Image(filepath, self.src_regex)
					imagelist.append(img)
			else:
				img = Image(filepath, self.src_regex)
				imagelist.append(img)
				
		return imagelist