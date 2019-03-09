import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation
import json

file = open('gol.json','r').read()
d = json.loads(file)

ON = 255
OFF = 0
vals = [ON, OFF]

def randommatrix(N): 
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def new(frameNum, img, matrix, N): 
    newmatrix = matrix.copy() 
    for i in range(N): 
        for j in range(N): 
            total = int((matrix[i, (j-1)%N] + matrix[i, (j+1)%N] + 
                         matrix[(i-1)%N, j] + matrix[(i+1)%N, j] + 
                         matrix[(i-1)%N, (j-1)%N] + matrix[(i-1)%N, (j+1)%N] + 
                         matrix[(i+1)%N, (j-1)%N] + matrix[(i+1)%N, (j+1)%N])/255)  
            if matrix[i, j]  == ON: 
                if (total < 2) or (total > 3): 
                    newmatrix[i, j] = OFF 
            else: 
                if total == 3: 
                    newmatrix[i, j] = ON 
  
    img.set_data(newmatrix) 
    matrix[:] = newmatrix[:] 
    return img,


def main(): 
    N = 100
    newInterval = 50
    print('This is Conway\'s Game of LifeIt contain these patterns {} whereas Block,Behive,Loaf,Boat Are Static Patterns Blinker,Toad,Beacon Are Oscillators And Gun,Glider Are Spaceships'.format(str(list(d.keys()))))
    print('\n\nPattern List: ',end='')
    print(list(d.keys()))
    print('\n\nTo Run A Pattern Type Pattern Name From The List For Random Pattern Type Random')  
    k = input('\n\nType Your Pattern Name: ')
    k = k.title()
    matrix = np.array([]) 
    if k in d.keys(): 
        matrix = np.zeros(N*N).reshape(N, N)
        i =10
        j = 10
        a,b = np.array(d[k]).shape
        matrix[i:i+a, j:j+b] = d[k]
  
    else: 
        matrix = randommatrix(N) 
    fig, ax = plt.subplots() 
    img = ax.imshow(matrix, interpolation='nearest') 
    ani = animation.FuncAnimation(fig, new, fargs=(img, matrix, N, ), 
                                  frames = 10, 
                                  interval=newInterval, 
                                  save_count=50)   
    plt.show()

if __name__ == '__main__': 
    main() 
