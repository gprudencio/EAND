''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Constraint handling procedure applied after the mutation procedure
'''

import numpy as np

def eand_limit(M,LB,UB) :    
    
    for i in range(np.size(M)) :
        if M[i] > UB :
            M[i] = np.random.uniform(.75*UB, UB, 1)
        elif M[i] < LB :
            M[i] = np.random.uniform(0, .25*UB, 1)  
       
    return M
