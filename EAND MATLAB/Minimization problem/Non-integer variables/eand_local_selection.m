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
% Local selection procedure - elitist method to choose the survived individuals


function [Xh, Yh] = eand_local_selection(Xh, Yh, Mh, MYh, nPop2, ndv)
   
    % Initialization
    P = zeros(2*nPop2,ndv);
    C = zeros(2*nPop2,1);
    
    % All individuals are ranked together according to their fitness value
    for i = 1:nPop2
        P(i,:) = Xh(i,:);
        C(i,1) = Yh(i,1);
        P(nPop2+i,:) = Mh(i,:);
        C(nPop2+i,1) = MYh(i,1);
    end    
    [~, indice] = sort(C);
    
    % New ordenation
    for i = 1:nPop2
        Xh(i,:) = P(indice(i),:);
        Yh(i,1) = C(indice(i),1);
    end

end
