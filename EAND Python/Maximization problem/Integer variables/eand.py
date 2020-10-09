''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com
'''

import numpy as np
import time
from Function import Function
from eand_limit import eand_limit
from eand_selection import eand_selection
from eand_lsp import eand_lsp
from eand_final_selection import eand_final_selection

def eand(MaxIt, nPop, nPop2, ndv, LB, UB) :    
    
    # Initialization    
    MaxIt, nPop, nPop2, ndv = int(MaxIt), int(nPop), int(nPop2), int(ndv)
    nef = 0                                  # Number of evaluation functions
    f = 0                                    # Number of evaluation functions to reach the fitness known value
    X = np.zeros((nPop,ndv),dtype=int)       # Population X
    Y = np.zeros((nPop,1),dtype=float)       # Evaluation of X
    M = np.zeros((nPop,ndv),dtype=int)       # Mutated population M
    MY = np.zeros((nPop,1),dtype=float)      # Evaluation of M  
    Ydiff = np.zeros((nPop,1),dtype=float)   # Numerical differentiation of Y
    d = np.zeros((nPop,1),dtype=float)       # Variable d (Eq. 5)
    Sim_size = int((nPop+nPop2)*MaxIt+nPop)
    BestCosts = np.zeros((1,Sim_size),dtype=float) # Save the iteration best evaluation value
    BestValue = np.NINF                      # Best overall evaluation value
        
    for i in range(nPop) :
        
        X[i] = np.random.uniform(LB, UB, ndv) # Initialize the population X
        X[i] = np.around(X[i])                # Handling integer variables
        Y[i] = Function(X[i])                 # Evaluate Y = f(X) 
        nef += 1                              # Update the number of evaluation functions     
        if Y[i] > BestValue:                  # Update the best overall evaluation value            
            BestValue = Y[i]
            f = nef                           # Number of evaluation functions to reach the fitness known value
        BestCosts[0,(nef-1)] = BestValue      # Save the best value over the evaluations
        
    ''' EAND main loop '''
    
    start = time.time() # Initialize time counter
    time.clock() 
    
    for it in range(MaxIt) :
        
        ''' Global search procedure  '''
        
        ''' Numerical differentiation operation '''        
        for i in range(nPop) : 
            
            # Circular data distribution 
            A = i - 2
            B = i - 1
            C = i + 1
            D = i + 2
            if i == 0:
                A = nPop - 2
                B = nPop - 1           
            elif i == 1:
                A = nPop - 1
            elif i == (nPop - 2):
                D = 0;
            elif i == (nPop - 1):
                C = 0;
                D = 1;    
            
            # Numerical Differentiation (Eq. 2)                    
            Ydiff[i] = (1/12)*(Y[A] - 8*Y[B] + 8*Y[C] - Y[D])
            
            # Restriction condition (Eq. 4)
            if Ydiff[i] == 0:
                Ydiff[i] = np.random.uniform(0, 1)   
            
        # Restriction condiction (Eq. 4)
        if np.size(np.unique(Ydiff)) == 1 :
            for i in range(nPop):
                Ydiff[i] = np.random.uniform(0, 1) 
                
        ''' Mutation procedure '''        
        for i in range(nPop) :
            
            d[i] = Ydiff[i]/np.mean(abs(Ydiff)) # Variable d (Eq. 5)
            if d[i] > 0.9 and d[i] < 1.1 :      # Restriction condiction (Eq. 4)
                d[i] = np.random.uniform(0, 1)
            M[i] = X[i] + np.mean(X)/d[i]       # Mutation (Eq. 6) 
            M[i] = np.round(M[i])               # Handling integer variables
            M[i] = eand_limit(M[i],LB,UB)       # Constraint handling procedure (Eq. 7) 
            MY[i] = Function(M[i])              # Evaluate MY = f(M) 
            nef += 1                            # Update the number of evaluation functions     
            if MY[i] > BestValue:               # Update the best overall evaluation value
                BestValue = Y[i]
                f = nef                         # Number of evaluation functions to reach the fitness known value
            BestCosts[0,(nef-1)] = BestValue    # Save the best value over the evaluations
            
        ''' Selection technique '''
        X, Y, Xh, Yh = eand_selection(X, Y, M, MY, nPop, nPop2, ndv)
        
        ''' Local search procedure '''       
        Xh, Yh, BestValue, BestCosts, nef, f = eand_lsp(Xh, Yh, BestValue, BestCosts, nef, f, nPop2, ndv, LB, UB) 
             
        ''' Final selection technique ''' 
        X, Y = eand_final_selection(X, Y, Xh, Yh, nPop, nPop2, ndv)
                
    
    Time = time.time() - start # Finitialize time counter
    
        
    return BestCosts, BestValue, f, Time


