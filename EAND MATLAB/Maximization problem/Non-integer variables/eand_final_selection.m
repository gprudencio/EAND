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
% Returns the values from the local selection procedure to the main  population

function [X, Y] = eand_final_selection(X, Y, Xh, Yh, nPop, nPop2, ndv)

    % Initialization
    P = zeros(nPop+nPop2,ndv);
    C = zeros(nPop+nPop2,1);
    n = zeros(1,nPop+nPop2);
    
    % All individuals are ranked together according to their fitness value
    for i = 1:nPop
        P(i,:) = X(i,:); 
        C(i,1) = Y(i,1);        
    end      
    for i = 1:nPop2        
        P(nPop+i,:) = Xh(i,:);
        C(nPop+i,1) = Yh(i,1);
    end  
    [~, indice] = sort(C);     
    for i = 1:(nPop + nPop2)
        n(i) = indice(i);
    end
    
    % The fittest individuals are randomly returned
    m = randperm(nPop);
    m = m + nPop2;
    
    % New ordenation    
    for i = 1:nPop
        X(i,:) = P(n(m(i)),:);
        Y(i,1) = C(n(m(i)),1);        
    end

end