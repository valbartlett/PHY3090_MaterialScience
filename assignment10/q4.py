#!/usr/bin/env python

dt = 1


me = 5.9726*10**24
Ft = 37*10**6
G = 6.674*10**-11
mr = 7*10**5
mf = 2.1*10**6
re = 6378100
rr = 0.
v = 0.
x = 0.
t = 0.
vexhaust = 2.6*10**3


while mf > 0:
    a = (Ft/(mr+mf))-(G*(mr+mf)*(me))/(re+rr)**2
    mf = mf-(1.42*10**4)
    v = v + a*dt
    rr = rr + v*dt
    t = t + dt
    print t, rr, v, a

