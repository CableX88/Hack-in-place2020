# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:54:36 2020

@author: ryanf
"""
class User:
 def __init__(self, fullName, email, campus, year, major, clubsAndOrganizations, canHelp, needHelp, interests): 
  self.fullName = fullName
  self.email = email 
  self.campus = campus
  self.year = year
  self.major = major
  self.clubsAndOrganizations = clubsAndOrganizations
  self.canHelp = canHelp
  self.needHelp = needHelp
  self.interests = interests