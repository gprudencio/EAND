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
% Local Search Procedure

function [Xh, Yh, BestValue, BestCosts, nef, f] = eand_lsp(Xh, Yh, BestValue, BestCosts, nef, f, nPop2, ndv, LB, UB)

    % Initialization       
    Mh    = zeros(nPop2,ndv);      % Mutated values from local search
    MYh   = zeros(nPop2,1);        % Evaluation of Mh
    Delta = zeros((nPop2-1),ndv);  % Delta matrix (Eq. 8)
    
    % Local mutation     
    Mh(1,:) = Xh(1,:) + Xh(1,:).*rand*((-1)^(randi(2))); % First element mutation (Eq. 10)
    Mh(1,:) = eand_limit(Mh(1,:),LB,UB);                 % Constraint handling procedure (Eq. 7)    
    MYh(1,1) = Function(Mh(1,:));                        % Evaluate MYh = f(Mh)
    nef = nef + 1;                                       % Update the number of evaluation functions 
    if MYh(1,1) < BestValue                              % Update the best overall evaluation value
        BestValue = MYh(1,1);
        f = nef;                                         % Number of evaluation functions to reach the fitness known value  
    end
    
    BestCosts(nef) = BestValue;                          % Save the best value over the evaluations
      
    for i = 1:(nPop2-1)                                 
        
        Delta(i,:) = Xh(1,:) - Xh(i+1,:);                % Delta matrix (Eq. 8)
        if Delta(i,:) == 0                               % Restriction condition (Eq. 9)
            Delta(i,:) = 1;
        end
        
        Mh(i+1,:) = Xh(i+1,:) + Delta(i,:).*rand*((-1)^(randi(2))); % Other elements mutation (Eq. 11)
        Mh(i+1,:) = eand_limit(Mh(i+1,:),LB,UB);                    % Constraint handling procedure (Eq. 7)        
        MYh(i+1,1) = Function(Mh(i+1,:));                           % Evaluate MYh = f(Mh)
        nef = nef + 1;                                              % Update the number of evaluation functions
        if MYh(i+1,1) < BestValue                                   % Update the best overall evaluation value        
            BestValue = MYh(i+1,1);
            f = nef;                                                % Number of evaluation functions to reach the fitness known value 
        end
        
        BestCosts(nef) = BestValue;                                 % Save the best value over the evaluations
        
    end   
    
    % Local selection technique 
    [Xh, Yh] = eand_local_selection(Xh, Yh, Mh, MYh, nPop2, ndv);
        
end