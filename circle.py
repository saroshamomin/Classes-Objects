#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:37:26 2020

@author: saroshamomin
"""
import math

class Circle:
    
    def __init__(self):
        self.__radius = 1.0
        self.__border = 2.0
        self.__color = "blue"
    
    def set_radius(self, r):
        self.__radius = r
    
    def set_color(self, color):
        self.__color = color
    
    def set_border(self, border):
        self.__border = border
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    def get_border(self):
        return self.__border
    
    def calc_area(self):
        area = math.pi*self.__radius**2
        return area
            
    def calc_circum(self):
        circumference = 2*math.pi*self.__radius
        return circumference
    
    def __str__(self):
        circle = "The " + self.__color + " circle has radius " + str(self.__radius) + " and border " + str(self.__border)
        return circle
    