''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Local Search Procedure
'''

import numpy as np
from Function import Function
from eand_limit import eand_limit
from eand_local_selection import eand_local_selection

def eand_lsp(Xh, Yh, BestValue, BestCosts, nef, f, nPop2, ndv, LB, UB) :

    # Initialization  
    nPop2, ndv = int(nPop2), int(ndv)
    Mh = np.zeros((nPop2,ndv),dtype=int)            # Mutated values from local search
    MYh = np.zeros((nPop2,1),dtype=float)           # Evaluation of Mh
    Delta = np.zeros(((nPop2-1),ndv), dtype=float)  # Delta matrix (Eq. 8)
    
    ''' Local mutation '''    
    n = np.random.permutation(range(2))
    Mh[0]  = Xh[0] + Xh[0]*(np.random.uniform(0, 1))*((-1)**n[0]) # First element mutation (Eq. 10) 
    Mh[0]  = np.round(Mh[0])             # Handling integer variables
    Mh[0]  = eand_limit(Mh[0],LB,UB)     # Constraint handling procedure (Eq. 7) 
    MYh[0] = Function(Mh[0])             # Evaluate MYh = f(Mh) 
    nef   += 1                           # Update the number of evaluation functions     
    if MYh[0] < BestValue:               # Update the best overall evaluation value
        BestValue = MYh[0]
        f = nef                          # Number of evaluation functions to reach the fitness known value 
    
    BestCosts[0,(nef-1)] = BestValue     # Save the best value over the evaluations
    
    for i in range(nPop2-1) :
        
        Delta[i] = Xh[0] - Xh[i+1]       # Delta matrix (Eq. 8)
        for j in range(ndv) :            # Restriction condition (Eq. 9)
            if Delta[i,j] == 0 :
                Delta[i,j] = 1
                
        n = np.random.permutation(range(2))
        Mh[i+1] = Xh[i+1] + Delta[i]*(np.random.uniform(0, 1))*((-1)**n[0]) # Other elements mutation (Eq. 11)
        Mh[i+1] = np.round(Mh[i+1])          # Handling integer variables
        Mh[i+1] = eand_limit(Mh[i+1],LB,UB)  # Constraint handling procedure (Eq. 7) 
        MYh[i+1] = Function(Mh[i+1])         # Evaluate MYh = f(Mh) 
        nef += 1                             # Update the number of evaluation functions     
        if MYh[i+1] < BestValue:             # Update the best overall evaluation value
            BestValue = MYh[i+1]
            f = nef                          # Number of evaluation functions to reach the fitness known value
        
        BestCosts[0,(nef-1)] = BestValue     # Save the best value over the evaluations
        
    ''' Local selection technique '''    
    Xh, Yh = eand_local_selection(Xh, Yh, Mh, MYh, nPop2, ndv)
    
    return Xh, Yh, BestValue, BestCosts, nef, f    

