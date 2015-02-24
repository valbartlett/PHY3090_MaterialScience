#!/usr/bin/env python

dt = 0.0001

alpha = 1
m = 1.0
g = 9.8
t = 0
v = 30
h = 10


while h>0:
    if ( v < 0 ):
        a = -g+(alpha/m)*v**2
    else:
        a = -g-(alpha/m)*v**2
    v = v + a*dt
    h = h + v*dt
    t = t + dt
    print t, h, v, a
