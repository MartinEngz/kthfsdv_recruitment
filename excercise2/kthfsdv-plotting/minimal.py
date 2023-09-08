import numpy as np
import matplotlib.pyplot as plt

class FunctionPlot:
    def __init__(self):
        self.plot()

    def h(self, t):
        lambda_t = 5 * np.sin(2*np.pi * t)
        h_t = 3 * np.pi * np.exp(-lambda_t)
        return h_t
    
    def plot(self):
        self.t_values = [i * 0.01 for i in range(100)]
        self.h_values = [self.h(t) for t in self.t_values]
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.t_values, self.h_values, label='h(t)')
        plt.title('Plot of h(t) = 3 * pi * exp(-lambda(t))')
        plt.xlabel('t')
        plt.ylabel('h(t)')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    plotter = FunctionPlot()
