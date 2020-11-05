#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:51:17 2020

@author: saroshamomin
"""

import circle

def main():
    my_circle = circle.Circle()    #create circle object
    
    '''another_circle = circle.Circle()'''
    
    #get input from the user
    size = float(input("What is the new size? "))
    color = str(input("What is the new color? "))
    border = float(input("What is the new border? "))
    
    #set the new values to the attributes
    my_circle.set_radius(size) 
    my_circle.set_color(color)
    my_circle.set_border(border)
    
    #print the new values
    print("Radius:", my_circle.get_radius())
    print("Color:", my_circle.get_color())
    print("Border:", my_circle.get_border())
    
    print("The area is:", format(my_circle.calc_area(), '.2f'))  #print area
    
    print("The circumference is:", format(my_circle.calc_circum(), '.2f'))  #print circumference
    
    print(my_circle)
    
main()  #call the method 