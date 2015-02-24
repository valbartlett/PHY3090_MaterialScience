#!/usr/bin/env python

dt = 0.0001

m = 1.0
g = 9.8
t = 0.0
v = 30.0
h = 10.0

while h>0:
    a = -g
    v = v + a*dt
    h = h + v*dt
    t = t + dt
    print t, h, v, a



 
