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

function [BestCosts, BestValue, f, time] = eand(MaxIt, nPop, nPop2, ndv, LB, UB)

    % Initialization    
    nef = 0;                     % Number of evaluation functions
    f = 0;                       % Number of evaluation functions to reach the fitness known value
    X = zeros(nPop,ndv);         % Population X
    Y = zeros(nPop,1);           % Evaluation of X
    M = zeros(nPop,ndv);         % Mutated population M
    MY = zeros(nPop,1);          % Evaluation of M  
    Ydiff = zeros(nPop,1);       % Numerical differentiation of Y
    d = zeros(nPop,1);           % Variable d (Eq. 5)
    BestCosts = zeros(1,((nPop+nPop2)*MaxIt+nPop));     % Save the iteration best evaluation value
    BestValue = inf;             % Best overall evaluation value

    for i = 1:nPop

        X(i,:) = unifrnd(LB, UB, [1 ndv]);  % Initialize the population X 
        X(i,:) = round(X(i,:));             % Handling integer variables
        Y(i,1) = Function(X(i,:));          % Evaluate Y = f(X)  
        nef = nef + 1;                      % Update the number of evaluation functions
        if Y(i,1) < BestValue               % Update the best overall evaluation value 
            BestValue = Y(i,1);               
            f = nef;                        % Number of evaluation functions to reach the fitness known value
        end

        BestCosts(nef) = BestValue;         % Save the best value over the evaluations

    end

    %% EAND main loop

    tic; % Initialize time counter

    for it = 1:MaxIt

        % Global Search Procedure 

        % Numerical differentiation operation    
        for i = 1:nPop 

            % Circular data distribution        
            A = i - 2; 
            B = i - 1; 
            C = i + 1; 
            D = i + 2;
            if i == 1
                A = nPop - 1; B = nPop; 
            elseif i == 2 
                A = nPop;
            elseif i == nPop - 1
                D = 1; 
            elseif i == nPop
                C = 1; D = 2;
            end  

            % Numerical Differentiation (Eq. 2)    
            Ydiff(i,1) = (1/12)*(Y(A,1) - Y(B,1)*8 + Y(C,1)*8 - Y(D,1));

            % Restriction condition (Eq. 4)        
            if Ydiff(i,1) == 0
                Ydiff(i,1) = rand()*((-1)^(randi(2)));
            end 

        end

        % Restriction condiction (Eq. 4)
        if numel(unique(Ydiff)) == 1
            for i = 1:nPop
                Ydiff(i,1) = rand()*((-1)^(randi(2)));
            end
        end

        % Mutation procedure
        for i = 1:nPop         
            d(i,1) = Ydiff(i,1)/mean(abs(Ydiff)); % Variable d (Eq. 5)
            if d(i,1)> 0.9 && d(i,1) < 1.1        % Restriction condiction (Eq. 4)
                d(i,1) = rand();
            end
            M(i,:) = X(i,:) + mean(X)/d(i,1);     % Mutation (Eq. 6)
            M(i,:) = round(M(i,:));               % Handling integer variables
            M(i,:) = eand_limit(M(i,:),LB,UB);    % Constraint handling procedure (Eq. 7)            
            MY(i,1) = Function(M(i,:));           % Evaluate MY = f(M) 
            nef = nef + 1;                        % Update the number of evaluation functions 
            if MY(i,1) < BestValue                % Update the best overall evaluation value
                BestValue = MY(i,1);                       
                f = nef;                          % Number of evaluation functions to reach the fitness known value              
            end 

            BestCosts(nef) = BestValue;           % Save the best value over the evaluations

        end

        % Selection technique 
        [X, Y, Xh, Yh] = eand_selection(X, Y, M, MY, nPop, nPop2, ndv);

        % Local Search Loop       
        [Xh, Yh, BestValue, BestCosts, nef, f] = eand_lsp(Xh, Yh, BestValue, BestCosts, nef, f, nPop2, ndv, LB, UB); 

        % Final selection technique 
        [X, Y] = eand_final_selection(X, Y, Xh, Yh, nPop, nPop2, ndv);


    end

    time = toc; % Finitialize time counter
    
end


