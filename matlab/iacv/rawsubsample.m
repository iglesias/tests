function pixels = rawsubsample(inpic, step)
%RAWSUBSAMPLE Subsample an image by dropping rows and columns.

if nargin < 2
    step = 2;
end

pixels = inpic(1:step:end, 1:step:end);

end

