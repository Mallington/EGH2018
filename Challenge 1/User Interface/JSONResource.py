#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:16:56 2018

@author: mathew
"""
import requests

class JSONResource():
    """ Point class represents and manipulates x,y coords. """
    
    RESOURCE_DATA = ""
    
    def __init__(self, url):
        """ Create a new point at the origin """
        self.URL = url
        self.updateResource()

        
    def updateResource(self):
        self.RESOURCE_DATA = requests.get(self.URL).json()
        

        
