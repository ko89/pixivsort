#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pixivsort.search import Search
from sys import argv, exit
import os

class Main(object):
    
    def __init__(self, argv):
        # Get source and destination directory from
        # commandline arguments
        if len(argv) != 3:
            print("Wrong number of arguments.")
            print("Please supply source and target dir.")
            exit(1)

        script, src_path, dst_path = argv
        
        try:
            src_path = unicode(src_path)
            dst_path = unicode(dst_path)
        except:
            pass
        
        if not os.path.exists(src_path):
            print("Source directory does not exist. Exiting...")
            exit(1)
            
        if not os.path.exists(dst_path):
            print("Destination directory does not exist. Exiting...")
            exit(1)
            
        if not os.path.isdir(src_path):
            print("Source directory is not a directory. Exiting...")
            exit(1)
            
        if not os.path.isdir(dst_path):
            print("Destination directory is not a directory. Exiting...")
            exit(1)
    
        # Change these to match naming scheme.
        # Image naming scheme: (<artist id>) <artist> - <title>.<extension>
        self.src_regex = "(?<=^\()\d*(?=\))"
        # Artist naming scheme: <artist> (<artist id>)
        self.dst_regex = "(?<=\()\d*(?=\)$)"
        
        self.src_path = src_path
        self.dst_path = dst_path
        
    def run(self):
        search = Search(self.src_path, 
                        self.dst_path, 
                        self.src_regex, 
                        self.dst_regex)

        imagelist = search.find_images()
        artistlist = search.find_artists()
        
        if len(imagelist) == 0 and len(artistlist) == 0:
            print("Error: Nothing found neither in source or destination.")
            print("Maybe you have supplied the paths in the wrong order?")
            print("It should be source path first and destination path second.")
            exit(1)
        
        for artist in artistlist:
            sepparator = "--------------------------------------------"
            artiststring = "%s\nChecking artist with id: %s" % (sepparator, artist.id)
            imagestring = ""
            for image in imagelist:
                if artist.id == image.artist_id:
                    imgpath = image.path.encode("utf-8")
                    artistpath = artist.path.encode("utf-8")
                    
                    image.copy(artist.path)
                    # assemble string for status about copying
                    tempstring = "\n\tCopying image"
                    copystring = "\n\t%s\n\tto\n\t%s" % (imgpath, artistpath)
                    tempstring = tempstring + copystring
                    imagestring = imagestring + tempstring
                    
            if imagestring != "":
                print(artiststring + imagestring)
                    
        print("Finished! Have a nice day.")

#if __name__ == '__main__':
#   main = Main(argv)
#   main.run()
