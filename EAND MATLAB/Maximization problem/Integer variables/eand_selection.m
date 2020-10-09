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
% Selection procedure - elitist method to choose the survived individuals

function [X, Y, Xh, Yh] = eand_selection(X, Y, M, MY, nPop, nPop2, ndv)
    
    % Initialization
    Xh = zeros(nPop2,ndv);
    Yh = zeros(nPop2,1);
    P = zeros(2*nPop,ndv);
    C = zeros(2*nPop,1);
    
    % All individuals are ranked together according to their fitness value
    for i = 1:nPop         
        P(i,:) = X(i,:); 
        C(i,1) = Y(i,1);
        P(nPop+i,:) = M(i,:); 
        C(nPop+i,1) = MY(i,1); 
    end   
    [~, indice] = sort(C);        
    
    % The fittest individuals are randomly returned
    m = randperm(nPop);
    
    % New ordenation 
    for i = 1:nPop
        X(i,:) = P(indice(m(i)+nPop),:);
        Y(i,1) = C(indice(m(i)+nPop),1);        
    end
    for i = 1:nPop2
        Xh(i,:) = P(indice(nPop*2 - nPop2 + i),:);    
        Yh(i,1) = C(indice(nPop*2 - nPop2 + i),1);        
    end    
         
end