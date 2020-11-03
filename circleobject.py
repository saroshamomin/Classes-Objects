#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:51:17 2020

@author: saroshamomin
"""

import circle

def main():
    my_circle = circle.Circle()    #create circle object
    
    print("The area is:", format(my_circle.calc_area(), '.2f'))  #print area
    
    print("The circumference is:", format(my_circle.calc_circum(), '.2f'))  #print circumference
    
    
main()  #call the method