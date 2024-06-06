import matplotlib.pyplot as plt

class PlotObject():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        plt.plot(self.x, self.y)