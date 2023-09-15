

import numpy as np
import matplotlib.pyplot as plt


L = 2*np.pi # Length of x
T = 3

# T
dx = 0.1 # Spatial step size h
#dx=1
dt = 0.25 # Time step size t


x = np.arange(0, L+1, dx)
b=np.sin(x)
print(b)
t = np.arange(0, T+1, dt)
U = np.zeros((len(t), len(x)))

U[0,:] = np.sin(x)
U_half_list = {}

prev_half = None
U_values = []


def first_halves(n:int, prev_halves: dict):
    # print(prev_halves, "n = ", n)
    x_axis = list(range(0, len(x)-1))
    for j in x_axis: #2, N
        # Check condition for U[n+0.5,j+0.5]
        U_half = None
        print(n, j)
        if U[n,j+1] <= 0 <= U[n,j]:
            U_half = 0
            print(U[n,j], U[n,j+1])
            print("if1")
        elif U[n,j] + U[n,j+1] <= 0:
            U_half = U[n,j]
            print(U[n,j], U[n,j+1])
            print("if2")
        elif U[n,j] + U[n,j+1] > 0: #and np.isfinite(U[n,j+1]):
            U_half = U[n,j+1]
            print(U[n,j], U[n,j+1])
            print("if3")
        else:    
            U_half = U[n,j]  
   
        if n == 0 and j == 0:
            prev_half = 0   
            U_half_list[f"{j}"] = U_half
 
        if n ==0 and j >= 1:
            prev_half = U_half_list[f"{j-1}"]
            U_half_list[f"{j}"] = U_half
        if n > 0 and j==0:
            prev_half = 0   
            U_half_list[f"{j}"] = U_half
            print(U_half_list, "list")
        if n>0 and j !=0:   
            prev_half = U_half_list[f"{j-1}"]
            U_half_list[f"{j}"] = U_half
        
        U[n+1,j] = U[n,j] + (dx/dt) *(U_half**2 - prev_half**2)
    return U_half_list
        
  
 
def print_plot(U):
   
    T_grid, X_grid = np.meshgrid(t, x, indexing='ij')


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(T_grid, X_grid, U, cmap='magma')
    ax.set_xlabel('Time')
    ax.set_ylabel('Space')
    ax.set_zlabel('')

    plt.show()



def run():
    _first_halves = {}
    for n in range(len(t)-1): 
        print("n inside run", n)
        
        _first_halves = first_halves(n, _first_halves)
    print("U = ", U)
    print_plot(U)
    

run()  