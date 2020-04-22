# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:29:36 2020

@author: Saurabh Kumbhar
"""

import turtle

def drawHangman(chance,exitStatus):
    
    if(chance == 7):
        #Step 1
        turtle.circle(50)
        
    if(chance == 6):
        #Step 2
        turtle.right(90)
        turtle.forward(100)
    
    if(chance == 5):
        #Step 3
        turtle.left(60)
        turtle.forward(70)
    
    if(chance == 4):
        #Step 4
        turtle.backward(70)
        turtle.right(120)
        turtle.forward(70)
    
    if(chance == 3):
        #Step 5
        turtle.backward(70)
        turtle.right(120)
        turtle.forward(50)
        turtle.right(90)
        turtle.fd(70)
        
    if(chance == 2):
        #Step 6
        turtle.bk(140)
        
    if(chance == 1):
        #Step 7
        turtle.fd(70)
        turtle.left(90)
        turtle.fd(50)
        turtle.right(90)
        turtle.circle(60)
    
    if(chance == 0):
        #Step 8
        t = turtle.Pen()
        for x in range(180):
            t.forward(1)
            t.left(1)
        t.right(90)
        t.fd(100)

    if(exitStatus == 1):
        turtle.done()