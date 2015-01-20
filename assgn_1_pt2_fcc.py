rm=2.
e=10.


atom_list = []


na1 = 2
na2 = 2
na3 = 2

print "number of atoms:"
print na1
print "V_total:"

def face_centered_cubic():
    x=0
    for i in range (0,na1):
        y=0
        for j in range(0,na2):
            z=0
            for k in range(0,na3):
                atom_list.append([x,y,z])
                #print x,y,z
                #outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0.5
    for i in range (0,na1):
        y=0.5
        for j in range(0,na2):
            z=0
            for k in range(0,na3):
                atom_list.append([x,y,z])
                #print x,y,z
                #outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0
    for i in range (0,na1):
        y=0.5
        for j in range(0,na2):
            z=0.5
            for k in range(0,na3):
                atom_list.append([x,y,z])
                #print x,y,z
                #outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0.5
    for i in range (0,na1):
        y=0
        for j in range(0,na2):
            z=0.5
            for k in range(0,na3):
                atom_list.append([x,y,z])
                #print x,y,z
                #outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1

face_centered_cubic()

V_total=0.

for coord1 in atom_list:

    for coord2 in atom_list:
        
        d=((coord2[0]-coord1[0])**2. + (coord2[1]-coord1[1])**2. + (coord2[2]-coord1[2])**2.)**(1./2.)
        if d > 0.:
            V= 10.*(((rm/d)**12.)-(2.*(rm/d)**6.))
            V_total=V_total+V

print (V_total/2.)/(na1*na2*na3)
