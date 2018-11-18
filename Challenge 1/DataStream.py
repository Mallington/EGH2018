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
        self.getPrevious()
        self.MARKET.updateCompanies(self.updates.RESOURCE_DATA)
        self.LATEST_EPOCH = 0
        self.UPDATE_AVAILABLE = True
      
    def isUpdateAvailable(self):
        if self.UPDATE_AVAILABLE:
            self.UPDATE_AVAILABLE = False
            return True
        else:
            return False
        
        
    def getPrevious(self):
        
        latestEpoch = self.getLatestEpochValue()
        
        for i in range(latestEpoch-100,latestEpoch+1):
            frame = Resource('http://egchallenge.tech/marketdata/epoch/'+str(i))
            self.MARKET.updateCompanies(frame.RESOURCE_DATA)
            if i%10==0: 
                print(i)
        self.LATEST_EPOCH = latestEpoch
        
    def getLatestEpochValue(self):
        latest = Resource('http://egchallenge.tech/epoch')
        latestEpoch = latest.RESOURCE_DATA['current_epoch']
        return latestEpoch
        
    def update(self):
        latestEpoch = self.getLatestEpochValue()
        if(latestEpoch>self.LATEST_EPOCH):
            self.updates.updateResource()
            self.MARKET.updateCompanies(self.updates.RESOURCE_DATA)
            self.LATEST_EPOCH = latestEpoch
            self.UPDATE_AVAILABLE = True
        
    
    
