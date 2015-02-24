#!/usr/bin/env python

dt = 0.0001
maxRun = 1000000
k = 1
m = 3.0
t = 0.
v = 0.
x = 2.

i = 0

xprevious = x

timeThroughZero = []

while i < maxRun:
    a = ((1./20.)*x**5)+((-10./12.)*x**4)+((31/6)*x**3)-((30/2)x^2)
    v = v + a*dt
    x = x + v*dt
    if ( xprevious > 0) and ( x < 0):
        timeThroughZero.append(t)
    xprevious = x
    t = t + dt
    i=i+1
    print t, x, v, a
