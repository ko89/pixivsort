#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, os, shutil


from distutils import dir_util
from sys import exit

class Image(object):

    def __init__(self, path, re_pattern):
        self.path = path
        self.re_pattern = re_pattern
        
        if os.path.isfile(path):
            # Split path into filename and filepath
            (filepath, filename) = os.path.split(path)
            self.find_id(filename)
            
        elif os.path.isdir(path):
            # Get name of directory
            dirname = os.path.basename(path)
            self.find_id(dirname)
        else:
            print("Warning:\n%s" % self.path)
            #print("Warning:\n%s" % self.path.encode( "utf-8" ))
            print("is neither a file nor a directory. Ignoring...")
            self.find_id(self.path)
        
    
    def find_id(self, filename):
        """Finds artist_id in filename with a regex pattern"""
        match = re.search(self.re_pattern, filename)
        if match:
            self.artist_id = match.group()
        else:
            self.artist_id = None
    
    def copy(self, destination):
        """Copies the image to the given destination
            and deletes the source file."""
        if os.path.isfile(self.path):
            shutil.copy2(self.path, destination)
            os.remove(self.path)
            
        elif os.path.isdir(self.path):
            # As shutil.copytree only copies the contents of
            # the directory to the destination.
            # We need to add the directory name to the destination path.
            dirname = os.path.basename(self.path)
            finaldestination = os.path.join(destination, dirname)
            
            shutil.copytree(self.path, finaldestination)
            #dir_util.copy_tree(self.path, destination)
            shutil.rmtree(self.path)
            
        else:
            print("Error:\n%s" % self.path)
            #print("Error:\n%s" % self.path.encode( "utf-8" ))
            print("is neither a file nor a directory.")
            print("Something must have went very wrong, will now exit...")
            #exit(1)
