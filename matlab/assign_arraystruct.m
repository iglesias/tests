N = 100; % length of the array
s(N) = struct('x', 0); % initialization
xvalues = 1:N;
W = mat2cell(xvalues, 1, ones(1,N));
[s(:).x] = W{:};
