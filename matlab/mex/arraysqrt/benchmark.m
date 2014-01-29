A = (1:1e7).^2;

tic
B = arraysqrt(A);
toc

tic
C = sqrt(A);
toc

tic
D = zeros(size(A));
for i = 1:numel(A)
    D(i) = sqrt(A(i));
end
toc

assert(all(B==C) && all(C==D))