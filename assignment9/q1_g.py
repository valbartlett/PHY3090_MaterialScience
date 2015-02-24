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
    a = -(k/m)**.5*x
    v = v + a*dt
    x = x + v*dt
    if ( xprevious > 0) and ( x < 0):
        timeThroughZero.append(t)
    xprevious = x
    t = t + dt
    i=i+1
    #print t, x, v, a

i = 1

while (i < len(timeThroughZero)):
    
    period = timeThroughZero[i+1] - timeThroughZero[i]
    freq = 1/period
    print 'Freq is: ', freq, ' Hz'
     
