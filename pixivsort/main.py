from pixivsort.search import Search
from sys import argv, exit
import os

class Main(object):
	
	def __init__(self, argv):
		# Get source and destination directory from
		# commandline arguments
		if len(argv) != 3:
			print "Wrong number of arguments."
			print "Please supply source and target dir."
			exit(1)

		script, src_path, dst_path = argv
		
		if not os.path.exists(src_path):
			print "Source directory does not exist. Exiting..."
			exit(1)
			
		if not os.path.exists(dst_path):
			print "Destination directory does not exist. Exiting..."
			exit(1)
			
		if not os.path.isdir(src_path):
			print "Source directory is not a directory. Exiting..."
			exit(1)
			
		if not os.path.isdir(dst_path):
			print "Destination directory is not a directory. Exiting..."
			exit(1)
	
		# Change these to match naming scheme.
		# Image naming scheme: (<artist id>) <artist> - <title>.<extension>
		self.src_regex = u"(?<=^\()\d*(?=\))"
		# Artist naming scheme: <artist> (<artist id>)
		self.dst_regex = u"(?<=\()\d*(?=\)$)"
		
		self.src_path = src_path
		self.dst_path = dst_path
		
	def run(self):
		search = Search(self.src_path, 
						self.dst_path, 
						self.src_regex, 
						self.dst_regex)

		imagelist = search.find_images()
		artistlist = search.find_artists()
		
		print "imagelist length: %d artistlist length: %d" % (len(imagelist), len(artistlist))
		
		for artist in artistlist:
			print "checking artist with id: " + artist.id
			for image in imagelist:
				
				print "comparing image with artists id: " + image.artist_id
				if artist.id == image.artist_id:
					print "Copying image %s to %s" % (image.path, artist.path)
					image.copy(artist.path)
			
if __name__ == '__main__':
	main = Main(argv)
	main.run()