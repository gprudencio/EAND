''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com
'''

import numpy as np
import matplotlib.pyplot as plt
from eand import eand 

if __name__ == "__main__":
    
    ''' Parameters '''

    Sim = 1                      # Total number of simulations
    MaxIt = 100                  # Maximum number of iterations
    nPop = 50                    # Population size
    nPop2 = np.round(0.2*nPop)   # 20% of population Size
    ndv = 4                      # Number of Decision Variables
    LB = -10**5                  # Lower Bound of Decision Variables
    UB =  10**5                  # Upper Bound of Decision Variables
    
    ''' Simulation '''
    
    # Initialization 
    fitness = np.zeros((1,Sim),dtype=float)          # Fitness values
    NEF = np.zeros((1,Sim),dtype=int)                # Number of function evaluations
    SR = np.zeros((1,Sim),dtype=int)                 # Success rate
    Sim_size = int((nPop+nPop2)*MaxIt+nPop)
    BC = np.zeros((Sim,Sim_size),dtype=float)        # Fitness function over the simulations
    plt_eand = np.zeros((1,Sim_size),dtype=float)    # Fitness function over the simulations

    for k in range(Sim):
        
        # EAND
        # The BestCosts matrix returns the performance of the algorithm during a simulation
        # The variable f returns the number of evaluation functions to reach the fitness known value
        # The variable time returns the CPU time
        BestCosts, BestValue, f, Time = eand(MaxIt, nPop, nPop2, ndv, LB, UB)
        
        fitness[0,k] = BestValue   # Best overall evaluation value over the simulation
        if fitness[0,k] == 0 :     # Verify success rate 
            SR[0,k] = 1
            
        # The matrices NEF and BC store algorithm performance in k simulations
        NEF[0,k] = f
        BC[k,:] = BestCosts[0,:]

    ''' Results '''
    
    print('Result EAND')
    print('Average of fitness value = ',np.mean(fitness))
    print('Standart deviation = ', np.std(fitness))
    print('Average number of evaluation functions = ',np.mean(NEF))
    print('Success rate ', np.mean(SR))
    
    ''' Plot '''
        
    for i in range(Sim_size) :
        plt_eand[0,i] = np.mean(BC[:,i])
        
    plt.semilogy(plt_eand[0,:], markersize=8, color='blue', alpha=0.5)
    plt.xlabel('Function Evaluations')
    plt.ylabel('Best Fitness')
    plt.show()
   
     