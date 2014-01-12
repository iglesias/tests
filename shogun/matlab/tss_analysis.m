fname = '/home/iglesias/workspace/tests/shogun/data/TSS_example.txt';

fprintf('Loading data....\n')
TSS_example = load(fname);
fprintf('\tdone loading data!\n')

state_seq = TSS_example(:, 2)+1;
feat_mat = TSS_example(:, 3:end);
assert(length(state_seq) == size(feat_mat, 1))

num_elem = length(state_seq);
num_features = size(feat_mat, 2);

%% Split the data into smaller sub-sequences.

% Generate indices to split the long sequence into shorter sequences.
% The length of the new sequences is drawen from an integer Uniform(a,b)
% distribution with both ends included.
%
%       a has been fixed to 1000 as a lower bound for the sequence length.
%       b has been chosen so that the average sequence length gives rise to
%       about 50 sequences.

a = 1000;
b = 26616;

% Upper bound for the number of sequences that will be generated.
ub = 1e6;
lengths = randi([a, b], [1, ub]); 
i = find(cumsum(lengths) > num_elem, 1);
lengths = lengths(1:i);

if sum(lengths) > num_elem
    lengths(end) = num_elem-sum(lengths(1:end-1));
end

fprintf('number of sequences=%d\n', length(lengths))
fprintf('number of states=%d\n', length(unique(state_seq)))
fprintf('number of features=%d\n', num_features)

%% Train HMM

% Here I am using the naming convention used in the HMM code.
nStates = 2;
stateDuration = [];
pD = GaussD;
obsData = feat_mat'; % note the transpose
lData = lengths;

fprintf('Training HMM...\n')
hmm = MakeErgodicHMM(nStates, stateDuration, pD, obsData, lData);
fprintf('\tHMM trained!\n')
[S, logP] = viterbi(hmm, obsData);
fprintf('Decoding sequence of hidden states...\n')

fprintf('1-labels: GT %d and predicted %d\n', sum(state_seq==1), sum(S==1))
fprintf('2-labels: GT %d and predicted %d\n', sum(state_seq==2), sum(S==2))

% Indices in the ground truth sequence of the elements labelled with 2.
A = find(state_seq == 2);
% Same thing but for the predicted sequence.
B = find(S == 2);
% Set difference and evalute the ratio of 2-labels in the GT that are
% definitely right in the predicted sequence.
D = setdiff(A, B);
fprintf('Correct ratio of correct 2-labels %f\n', length(D)*100/length(A));
