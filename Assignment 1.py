
outputFile = open('file.xyz', 'w')

#need to change number to n124 where n is the cumber of 'prints' in a code
outputFile.write('500 \n')
outputFile.write(' \n')
    
def simple_cubic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    return



def simple_tetragonal():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 2
    return



def simple_orthorhombic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3
    return



def body_centered_cubic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0.5
    for i in range (0,5):
        y=0.5
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    return



def body_centered_tetragonal():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 2
    x=1
    for i in range (0,5):
        y=0.5
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 2
    return



def body_centered_orthorhombic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3
    x=1.5
    for i in range (0,5):
        y=1
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3
    return

def face_centered_cubic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0.5
    for i in range (0,5):
        y=0.5
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0
    for i in range (0,5):
        y=0.5
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1
    x=0.5
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 1
        x = x + 1

def face_centered_orthorhombic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3
        
    x=1.5
    for i in range (0,5):
        y=1
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3

    x=0
    for i in range (0,5):
        y=1
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3

    x=1.5
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3

def edge_centered_orthorhombic():
    x=0
    for i in range (0,5):
        y=0
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3
        
    x=1.5
    for i in range (0,5):
        y=1
        for j in range(0,5):
            z=0
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3

    x=0
    for i in range (0,5):
        y=1
        for j in range(0,5):
            z=0.5
            for k in range(0,5):
                #print x,y,z
                outputFile.write('X ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
                z = z + 1
            y = y + 2
        x = x + 3

face_centered_cubic()

outputFile.close()



