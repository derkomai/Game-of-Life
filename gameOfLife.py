import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import copy

class World:

    def __init__(self, size, interval, initial=None):

        self.size = size
        self.interval = interval

        if initial is None:
            self.cells = [[random.randint(0,1) for j in range(self.size)] for i in range(self.size)]
        else:
            self.cells = initial

        self.fig = plt.figure()
        self.im = plt.imshow(self.cells, interpolation='none', aspect='equal', cmap='binary')
        plt.axis('off')
        

    def simulate(self):

        ani = animation.FuncAnimation(self.fig, self.update, interval=self.interval, blit=True)
        plt.show()


    def checkCell(self, i, j):

        aliveNeighbours = 0
        coordinates = list(range(self.size))

        for deltai in [-1, 0, 1]:
            for deltaj in [-1, 0, 1]:

                if deltai == 0 and deltaj == 0:
                    continue

                if i + deltai in coordinates and \
                   j + deltaj in coordinates:
                    aliveNeighbours += self.cells[i + deltai][j + deltaj]

        if self.cells[i][j] == 0:
            if aliveNeighbours == 3:
                return 1
            else:
                return 0
        else:
            if aliveNeighbours in [2,3]:
                return 1
            else:
                return 0


    def update(self, *args): 

        cellsCopy = copy.deepcopy(self.cells)

        for i in range(self.size):
            for j in range(self.size):
                cellsCopy[i][j] = self.checkCell(i, j)

        self.cells = cellsCopy

        self.im.set_array(self.cells)
        return self.im,


world = World(size=100, interval=50)
world.simulate()