#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:52:15 2020

@author: saroshamomin
"""

import coin

def main():
    my_coin = coin.Coin()
    
    print("This side is up:", my_coin.get_sideup())
    
    print("I am tossing the coin....")
    my_coin.toss()
    
    print("This side is up:", my_coin.get_sideup())
    
main()