# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 23:42:34 2014

@author: von

"""

def rpa(p,q):
    '''
    russian peasant algorithm for multiplication
    '''
    r = 0
    if p == 0:
        return 0
    else:
        if p%2 != 0:
            r = r + q
            q = q + q
        else:
            q = q+q
            
    return r + rpa(p/2,q)
        

def rpa_non_recursive(p,q):
    r = 0
    while(p!=0):
        
        if p%2 != 0:
            r = r + q
            q = q + q
        else:
            q = q+q            
        p = p/2
    
    return r
    
    
#testing
print rpa(41,37)
print rpa_non_recursive(37,41)  
print rpa(17,45)
print rpa_non_recursive(17,45) 



