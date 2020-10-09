''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Returns the values from the local selection procedure to the main  population
'''

import numpy as np

def eand_final_selection(X, Y, Xh, Yh, nPop, nPop2, ndv) :
    
    # Initialization    
    P = np.zeros((nPop + nPop2,ndv),dtype=int)
    C = np.zeros((nPop + nPop2,1),dtype=float)
    indice = np.zeros((nPop,1),dtype=int)
    
    # All individuals are ranked together according to their fitness value
    for i in range(nPop) :
        P[i] = X[i]
        C[i] = Y[i]
    for i in range(nPop2) :
        P[nPop+i] = Xh[i]
        C[nPop+i] = Yh[i]
    
    indice = [i[0] for i in sorted(enumerate(C), key=lambda x:x[1])]
            
    # The fittest individuals are randomly returned
    m = np.random.permutation(range(nPop))
    m = m + nPop2
    
    # New ordenation
    for i in range(nPop) :
        X[i] = P[indice[m[i]]].copy() 
        Y[i] = C[indice[m[i]]]
        
    return X, Y

