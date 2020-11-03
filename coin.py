#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:04:02 2020

@author: saroshamomin
"""

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
            
    def get_sideup(self):
        return self.sideup

