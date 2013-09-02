% load Shogun's stuff to the workspace
modshogun

% load wine data set (it will be stored in a matrix called wine)
load '../data/wine.data'

% separate labels and features from the data
% the labels are in the first column
labels=wine(:,1);
features=wine(:,2:end);

% extract the number of examples and features from data
[n,d]=size(features);

% wrap labels and features into Shogun objects
train_labels=MulticlassLabels(labels');
train_features=RealFeatures(features');

% train LMNN

% number of target neighbours per example
k=5;

lmnn=LMNN(train_features,train_labels,k);
lmnn.set_maxiter(1000)
lmnn.set_correction(15)

init_transform = eye(d);
lmnn.train(init_transform)

% get distance learnt by LMNN
distance=lmnn.get_distance();

% classify training data using KNN
lmnnknn=KNN(k,distance,train_labels);
lmnnknn.train();
output=lmnnknn.apply(train_features);

% compute accuracy
evaluator=MulticlassAccuracy();
evaluator.evaluate(output,train_labels)
