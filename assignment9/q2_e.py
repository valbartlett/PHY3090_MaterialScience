#!/usr/bin/env python

dt = 0.0001
maxRun = 1000000
k = 1
m = 3.0
t = 0.
v = 30.
x = 10.
alpha = .1

i = 0

xprevious = x

timeThroughZero = []

while i < maxRun:
    a = -(k/m)**.5*x-((alpha/m)*v)
    v = v + a*dt
    x = x + v*dt
    if ( xprevious > 0) and ( x < 0):
        timeThroughZero.append(t)
    xprevious = x
    t = t + dt
    i=i+1
    print t, x, v, a

