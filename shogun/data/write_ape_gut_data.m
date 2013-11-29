% chimpanzee -> 0
% bonobo     -> 1
% gorilla    -> 2

fm_fid = fopen('fm_ape_gut.txt','w+');
label_fid = fopen('label_ape_gut.txt','w+');

assert(length(ape_gut_meta_id)==length(ape_gut_otus_norm_filt_id));

num_lines = length(ape_gut_meta_id);
num_features = size(ape_gut_otus_norm_filt_features,1);

for i = 1:num_lines
    for j = 1:num_lines
        
        if strcmp(ape_gut_meta_id(i), ape_gut_otus_norm_filt_id(j))
            
%             % DEBUG: uncomment to check that the indices correspond correctly
%             % to each other
%             fprintf('%2d->%2d: %7s %7s\n', i,j, ...
%                 ape_gut_meta_id{i},ape_gut_otus_norm_filt_id{j});

            ape_species = ape_gut_meta_species(i);
            if strcmp(ape_species, 'chimpanzee')
                fprintf(label_fid, '%d\n', 0);
            elseif strcmp(ape_species, 'bonobo')
                fprintf(label_fid, '%d\n', 1);
            elseif strcmp(ape_species, 'gorilla')
                fprintf(label_fid, '%d\n', 2);
            else
                error('Unknown ape species.')
            end
            
            for k = 1:num_features-1 % do not print the last number with white space
                fprintf(fm_fid, '%f ', ape_gut_otus_norm_filt_features(k,j));
            end
            fprintf(fm_fid, '%f', ape_gut_otus_norm_filt_features(end,j));
            fprintf(fm_fid, '\n');
            
            break
        end
    end
end

fclose(fm_fid);
fclose(label_fid);