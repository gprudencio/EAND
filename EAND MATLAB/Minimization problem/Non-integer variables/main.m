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

clc; clear all; close all;

%% Parameters

Sim = 1;                   % Total number of simulations
MaxIt = 100;               % Maximum number of iterations
nPop = 50;                 % Population size
nPop2 = round(0.2*nPop);   % 20% of population Size
ndv = 4;                   % Number of Decision Variables
LB = -10^5;                % Lower Bound of Decision Variables
UB =  10^5;                % Upper Bound of Decision Variables

%% Simulation

% Initialization
fitness = zeros(1,Sim);                             % Fitness values
NEF = zeros(1,Sim);                                 % Number of function evaluations
SR = zeros(1,Sim);                                  % Success rate
BC = zeros(Sim,((nPop+nPop2)*MaxIt+nPop));          % Fitness function over the simulations
plt_eand = zeros(1,((nPop+nPop2)*MaxIt+nPop));      % Plot analysis

for k = 1:Sim
    
    % EAND
    % The BestCosts matrix returns the performance of the algorithm during a simulation
    % The variable f returns the number of evaluation functions to reach the fitness known value
    % The variable time returns the CPU time
    [BestCosts, BestValue, f, time] = eand(MaxIt, nPop, nPop2, ndv, LB, UB); 
    
    fitness(k) = BestValue;  % Best overall evaluation value over the simulation
    if fitness(k) == 0       % Verify success rate 
        SR(k) = 1;
    end
    
    % The matrices NEF and BC store algorithm performance in k simulations
    NEF(k) = f;    
    BC(k,:) = BestCosts; 
    
end
                                
%% Results

fprintf('Result EAND \n')
fprintf('Average of fitness value = %.4f\n',mean(fitness))
fprintf('Standart deviation = %.10f\n',std(fitness))
fprintf('Average number of evaluation functions = %.4f\n',mean(NEF))
fprintf('Success rate = %d\n\n',mean(SR))

%% Plot

for k = 1:size(BC,2)
    plt_eand(k) = mean(BC(:,k));
end 

figure;
semilogy(plt_eand,'Color',[0,0,1],'LineWidth',2);       
xlabel('Function Evaluations');
ylabel('Best Fitness');
grid on;
