import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import random

ga_data = pd.read_csv('/home/barvin04/Desktop/second_forsk.txt', sep=',',header=None)
#ga_data = pd.read_csv('/home/barvin04/Desktop/simple.txt', sep=',', header=None)

print(ga_data)
print(ga_data.shape)
print(ga_data.head())

X = ga_data.values[:, 3:9]
Y= ga_data.values[:, 9]
print(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

print(X_train)
print(X_test)

clf_gini = DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

clf_gini.predict([[17,-13,509,0,-816,-305]])  #walk
clf_gini.predict([[-43,27,-6,0,-967,-221]])   #abnormal

y_pred = clf_gini.predict(X_test)
print(y_pred)

acc = accuracy_score(y_test, y_pred)*100
print(acc)


print('testing outputs : \n \n \n')
for aNumber in range(20):
    a, b, c, d, e, f= random.randint(-990,990), random.randint(-990,990),random.randint(-990,990),random.randint(-990,990),random.randint(-990,990),random.randint(-990,990)
    print(clf_gini.predict([[a,b,c,d,e,f]]),'  ', a,b,c,d,e,f)#51,30,-8,0,-980,-268 ]  ])
    

for aNumber in range(20):
    a, b, c, d, e, f= random.randint(110,125), random.randint(10,18),random.randint(110,125),random.randint(-990,990),random.randint(230,255),random.randint(230,255)
    print(clf_gini.predict([[a,b,c,d,e,f]]),'  ', a,b,c,d,e,f)

#turn false to true to check for custom data, live input 
while(False):
    ta = str(input())
    ta = ta.split(' ')
    a,b,c,d,e,f= int(ta[0]), int(ta[1]), int(ta[2]), int(ta[3]), int(ta[4]), int(ta[5])
    print(clf_gini.predict([[a,b,c,d,e,f]]), "  ", a,b,c,d,e,f)
#checking whether idle or not on trip and slip dataset
f = open('/home/barvin04/Desktop/GaitAnalysisData/fall_elderly_slip.txt','r')
h = f.readlines()
count=0
for var in range(len(h)):
	line = h[var]
	line=line.strip(';\n')
	line = line.split(',')
	a = int(line[3])
	b= int(line[4])
	c=int(line[5])
	d=int(line[6]) #not
	e=int(line[7])
	f=int(line[8])
	if(clf_gini.predict([[a,b,c,d,e,f]])[0]=='IDLE'):
		print(a,b,c,e,f)
		count = count+1
print(count*100/len(h))
print('accuracy  :', 100-count*100/len(h))
