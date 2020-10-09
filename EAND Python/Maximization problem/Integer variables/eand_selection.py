''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Selection procedure - elitist method to choose the survived individuals
'''

import numpy as np

def eand_selection(X, Y, M, MY, nPop, nPop2, ndv) :
    
    # Initialization   
    nPop, nPop2, ndv = int(nPop), int(nPop2), int(ndv)
    nPop, nPop2, ndv = int(nPop), int(nPop2), int(ndv)
    Xh = np.zeros((nPop2,ndv),dtype=int)   
    Yh = np.zeros((nPop2,1),dtype=float)    
    P = np.zeros((2*nPop,ndv),dtype=int)
    C = np.zeros((nPop*2,1),dtype=float)
    indice = np.zeros((nPop*2,1),dtype=int)
    
    # All individuals are ranked together according to their fitness value
    for i in range(nPop) :
        P[i] = X[i]
        C[i] = Y[i]
        P[nPop+i] = M[i]
        C[nPop+i] = MY[i] 
        
    indice = [i[0] for i in sorted(enumerate(C), key=lambda x:x[1])]
            
    # The fittest individuals are randomly returned
    m = np.random.permutation(range(nPop))
    
    # New ordenation
    for i in range(nPop) :
        X[i] = P[indice[m[i] + nPop]].copy() 
        Y[i] = C[indice[m[i] + nPop]]
    for i in range(nPop2) :
        Xh[i] = P[indice[nPop*2 - nPop2 + i]].copy()  
        Yh[i] = C[indice[nPop*2 - nPop2 + i]]  
    
    return X, Y, Xh, Yh

 
