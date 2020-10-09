''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Local selection procedure - elitist method to choose the survived individuals
'''

import numpy as np

def eand_local_selection(Xh, Yh, Mh, MYh, nPop2, ndv) :
    
    # Initialization  
    nPop2, ndv = int(nPop2), int(ndv)      
    P = np.zeros((2*nPop2,ndv),dtype=int)
    C = np.zeros((2*nPop2,1),dtype=float)
    
    # All individuals are ranked together according to their fitness value
    for i in range(nPop2) :
        P[i] = Xh[i]
        C[i] = Yh[i]
        P[nPop2+i] = Mh[i]
        C[nPop2+i] = MYh[i] 
        
    indice = [i[0] for i in sorted(enumerate(C), key=lambda x:x[1])]
   
    for i in range(nPop2) :
        Xh[i] = P[indice[i]].copy()  
        Yh[i] = C[indice[i]] 
    
    return Xh, Yh




