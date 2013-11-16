function pixels = binsubsample(inpic)
%BINSUBSAMPLE Smooth an image and then apply raw-subsampling.

prefilterrow = [1 2 1]/4;
prefilter = prefilterrow' * prefilterrow;
presmoothpic = filter2(prefilter, inpic, 'valid');
pixels = rawsubsample(presmoothpic);

end

