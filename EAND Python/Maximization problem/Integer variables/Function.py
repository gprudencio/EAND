''' 
Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in Python
 
Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
Journal: Measurement
Year: 2019

Developer: Gustavo A. P. de Morais
Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com

Avaliation Function: Rastrigin
'''

import numpy as np

def Function(x):
    
    m = np.zeros((1,4))
    z = 0
    for i in range(np.size(x)) :
        m[0,i] = int(x[i])        
        z = z + 10 + (m[0,i])**2 - 10*np.cos(m[0,i]*2*np.pi) 
        
    return z
