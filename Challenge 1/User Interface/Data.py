#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:12:10 2018

@author: mathew
"""

class Market():
    def __init__(self, marketIDsJSON):
        print("Creating new market")
        self.Companies = []
        for d in marketIDsJSON:
            comp = Company(d)
            self.Companies.append(comp)
        
    def printLatestEpocs(self):
        for comp in self.Companies:
            e =comp.EPOCH_DATA[-1]
            print("Company: ",comp.ID,"Price: ",e.PRICE)
    
    
    def updateCompanies(self, jsonEpochs):
        for comp in self.Companies:
            comp.addEpoch(jsonEpochs)

class Company():
    
    def __init__(self, json):
        self.COMPANY_NAME = json['company_name']
        self.ID = json['id']
        self.INDUSTRY = json['industry']
        self.SYMBOL =json['symbol']
        self.lastUpdate =0
        self.EPOCH_DATA = []
   
    
    def getEpoch(self, JSON,instrumentID):
        return JSON[instrumentID-1]
        
        
    def addEpoch(self, dictionary):
        print("Updating COMPANY: ",self.COMPANY_NAME, ", ID: ",self.ID)
        
        epochJSON = self.getEpoch(dictionary,self.ID )
        if epochJSON['epoch']> self.lastUpdate:
            self.lastUpdate = epochJSON['epoch']
            newEpoch = Epoch(epochJSON)
            self.EPOCH_DATA.append(newEpoch)
        else:
            print("Already had this update")
        
        
        
class Epoch():
    TIMESTAMP = 0;
    PREV_PRICE =0;
    PRICE = 0;
    DELTA_RATIO =0
    TRADING = True #Boolean denotes whether it is trading
    def __init__(self, epochJSON):
        self.TIMESTAMP = epochJSON['epoch']
        self.TRADING = epochJSON['is_trading']
        self.PREV_PRICE= epochJSON['prev_epoch_price']
        self.PRICE = epochJSON['price']