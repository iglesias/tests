load '../data/NBData20.mat'

% Taken arcsinVST.m in MetaDistance. Function to perform feature normalization.
function Xn = arcsinVST(Xtot)
	n = size(Xtot,2);
	Tcnt = sum(Xtot,2);
	%normalization across rows
	Xtot = Xtot./repmat(Tcnt,1,n);

	Xn = asin(sqrt(Xtot));
end


%%% Data preparation from simdriv.m in MetaDistance.
Y = Y20;
X = X20;
X = X(:,1:100);


Xn = arcsinVST(X);

J1 = find(Y==1);
J2 = find(Y==2);
J3 = find(Y==3);
J4 = find(Y==4);
J5 = find(Y==5);

Xn1 = Xn(J1,:);
Xn2 = Xn(J2,:);
Xn3 = Xn(J3,:);
Xn4 = Xn(J4,:);
Xn5 = Xn(J5,:);

n = size(Xn1,1);

Xn1 = Xn1(randperm(n),:);
Xn2 = Xn2(randperm(n),:);
Xn3 = Xn3(randperm(n),:);
Xn4 = Xn4(randperm(n),:);
Xn5 = Xn5(randperm(n),:);

x = [Xn1(1:ceil(n/2),:); Xn2(1:ceil(n/2),:); Xn3(1:ceil(n/2),:); Xn4(1:ceil(n/2),:); Xn5(1:ceil(n/2),:) ];
y = [ones(ceil(n/2),1); 2*ones(ceil(n/2),1); 3*ones(ceil(n/2),1); 4*ones(ceil(n/2),1); 5*ones(ceil(n/2), 1)];

xt = [Xn1(ceil(n/2)+1:n, :); Xn2(ceil(n/2)+1:n, :); Xn3(ceil(n/2)+1:n, :); Xn4(ceil(n/2)+1:n, :); Xn5(ceil(n/2)+1:n,:)];
yt = [ones(n-ceil(n/2), 1); 2*ones(n-ceil(n/2), 1); 3*ones(n-ceil(n/2),1); 4*ones(n-ceil(n/2), 1); 5*ones(n-ceil(n/2), 1)];


%%% Learn a diagonal transformation of the feature space using LMNN

modshogun;

% Wrap labels and features into Shogun objects.
features=RealFeatures(xt');
labels=MulticlassLabels(yt');

k=6;
lmnn=LMNN(features,labels,k);
lmnn.set_maxiter(2);
lmnn.set_diagonal(true);
lmnn.io.set_loglevel(MSG_DEBUG)

lmnn.train(eye(features.get_num_features()));
% imshow(lmnn.get_linear_transform())
stem(diag(lmnn.get_linear_transform()))
