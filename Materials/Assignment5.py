x0=0.
v=0.
a=0.
t=0.
dt=0.001

x=0
k=2.0
m=2.0

for i in range(10000):
    f=-k*(x-x0)
    a=f/m
    v=v+a*dt
    x=x+v*dt
    t=i*dt

    print t x



