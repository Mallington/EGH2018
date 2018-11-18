#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:07:40 2018

@author: mathew
"""
from JSONResource import JSONResource as Resource
from Data import Market
class DataStream():
    
    def __init__(self):
        self.companiesResource = Resource('http://egchallenge.tech/instruments')
        self.updates = Resource('http://egchallenge.tech/marketdata/latest')
        self.MARKET = Market(self.companiesResource.RESOURCE_DATA)
        self.MARKET.updateCompanies(self.updates.RESOURCE_DATA)
        
    def update(self):
        self.companiesResource.updateResource()
        self.updates.updateResource()
        
    
    
