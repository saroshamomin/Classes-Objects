#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:37:26 2020

@author: saroshamomin
"""
import math

class Circle:
    
    def __init__(self):
        self.radius = 1.0
        self.border = 2.0
        self.color = "blue"
    
    def calc_area(self):
        area = math.pi*self.radius**2
        return area
            
    def calc_circum(self):
        circumference = 2*math.pi*self.radius
        return circumference
    
