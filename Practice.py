print 'hello world'

def body_centered_cubic():
    x=0.5
    for i in range (0,5):
        y=0.5
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                print x,y,z
                z += 1
            y += 1
        x += 1
    return

body_centered_cubic()