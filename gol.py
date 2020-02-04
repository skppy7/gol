from time import sleep
import numpy as np
import os

class GoL:
    def __init__(self,size=(20,20), random=True):
        if random:
            self.grid = np.random.randint(0,2,size,dtype=np.bool)
        else:
            self.grid = np.zeros(size,dtype=np.bool)

        self.tempgrid = np.copy(self.grid)
        self.gen = 0
        self.pop = self.grid.sum()

    #this function shows you the evolution of "ite" generations
    def next_gen(self, ite=1, show = True, time=0.1):
        for _ in  range(ite):
            self.gen += 1
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    n = self.neighbors(i,j)
                    if self.grid[i,j]:
                        if not 1<n-1<4:
                            self.tempgrid[i,j] = False
                    elif n == 3:
                        self.tempgrid[i,j] = True
            self.grid = np.copy(self.tempgrid)
            self.pop = self.grid.sum()
            if show:
                self.show_grid(t=time)

    def reset(self):
        self.grid = np.random.randint(0,2,self.grid.shape,dtype=np.bool)

    def neighbors(self,i,j):
        r = [0,2] if i == 0 else [i-1,i+2] if i < self.grid.shape[0] else [i-1,i+1]
        c = [0,2] if j == 0 else [j-1,j+2] if j < self.grid.shape[0] else [j-1,j+1]
        return self.grid[r[0]:r[1],c[0]:c[1]].sum()

    def show_grid(self, t=0):
        os.system('clear')
        for row in self.grid:
            for item in row:
                if item:
                    print('\033[07m  ',end='\033[00m')
                else:
                    print('  ',end='')
            print()
        print('Gen:',self.gen,'\nPop:',self.pop)
        sleep(t)
