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
% Constraint handling procedure applied after the mutation procedure

function [L] = eand_limit(L,VarMin,VarMax) 

    Aux = size(L);  
    for j = 1:Aux(2) 
        if L(1,j) > VarMax 
            aux = round(unifrnd(0,0.25*(abs(VarMax)),1));
            L(1,j) = VarMax - aux;
        elseif L(1,j) < VarMin
            aux = round(unifrnd(0,0.25*(abs(VarMax)),1));
            L(1,j) = VarMin + aux;
        end
    end
           
end