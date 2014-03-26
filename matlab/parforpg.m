% Parfor playground.

N = 5;
M = 10;

% The next loop is not executable.

% Presumably, the problem is with indexing slices along one dimension of X
% when these slices are defined using the variable of the parfor.

X = zeros(N*M, 1);

parfor i = 1:M
    X(N*(i-1)+1:N*i) = i*ones(N,1);
end

% On the other hand, this one runs without problems.

% Here, we use another dimension to separate the slices.

X = zeros(N,M);

parfor i = 1:M
    X(:,i) = i*ones(N,1);
end