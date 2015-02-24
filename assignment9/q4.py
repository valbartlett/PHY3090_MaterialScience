#!/usr/bin/env python

dt = 0.0001
maxRun = 100000
m = 3.0
t = 0.
v = 0.
x = 5.5
alpha = 1.
epsilon = 10.
sigma = 5.

i = 0

vprevious = v

timeThroughZero = []

while i < maxRun:
    a = -(1/m)*(24*sigma**6.*epsilon*(x**6. - 2*sigma**6.))/x**13.
    v = v + a*dt
    x = x + v*dt
    if (vprevious > 0) and (v < 0):
        timeThroughZero.append(t)
    xprevious = x
    t = t + dt
    i = i + 1
    print t, x, v, a


