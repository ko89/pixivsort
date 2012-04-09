#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Artist(object):

    def __init__(self, path, re_pattern):
        self.path = path
        self.re_pattern = re_pattern
        self.find_id(self.path)
        
    def find_id(self, path):
        """Finds artists id in pathname with a regex pattern"""
        match = re.search(self.re_pattern, path)
        if match:
            self.id = match.group()
        else:
            self.id = None
