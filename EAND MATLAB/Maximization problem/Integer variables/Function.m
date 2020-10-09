% 
% Implementation of Evolutionary Algorithm with Numerical differentiation (EAND) in MATLAB
% 
% Article: Soft Sensors Design in a Petrochemical Process using an Evolutionary Algorithm 
% Journal: Measurement
% Year: 2019
%
% Developer: Gustavo A. P. de Morais
% Contact Info: gustavo_gapm@usp.br, gustavo_gapm@hotmail.com
%
% Avaliation Function: Rastrigin 

function z = Function(x)

    z = 10*length(x) + sum(x.^2) - 10*sum(cos(x.*2*pi));   
      
end
