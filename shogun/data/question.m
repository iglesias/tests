function str = question(expr,str1,str2)
%
% QUESTION ? operator
%          Simulate the question mark operator of other programming languages.

if expr
    str = str1;
else
    str = str2;
end
