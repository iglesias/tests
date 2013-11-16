close all

% Create checkerboard picture.
pic = repmat([0 1; 1 0], 20, 20);
% Apply raw subsampling with different steps.
rawsub2pic = rawsubsample(pic, 2);
rawsub3pic = rawsubsample(pic, 3);
% Apply binomial subsampling.
binsubpic = binsubsample(pic);

% Display results
showgrey(pic)
title('Checkerboard pattern')

figure
showgrey(rawsub2pic)
title('Rawsubsample with step 2')
unique(rawsub2pic)

figure
showgrey(rawsub3pic)
title('Rawsubsample with step 3')

figure
showgrey(binsubpic)
title('Binomial subsample')
unique(binsubpic)

cascade