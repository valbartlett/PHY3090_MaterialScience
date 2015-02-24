#!/usr/bin/env python

dt = 0.0001

alpha = 1
m = 1.0
g = 9.8
t = 0
v = 30
x = 10
a = -9.8

while x>0:
    a = -g
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    print t, x, v, a
