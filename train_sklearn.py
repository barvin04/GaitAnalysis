from sklearn import tree

clf = tree.DecisionTreeClassifier()


filein = open('forsklearn.txt', 'r')
fileh = filein.readlines()

X=[]
Y=[]
for elem in fileh:
    elem =elem.rstrip(']\n').lstrip("['")
    elem = elem.split(',')
    rawdata = elem[0:6]
    for no in range(len(rawdata)):
        rawdata[no] = int(rawdata[no])
    X.append(rawdata)

    classs = elem[6]
    Y.append(classs)

    
#_________classifier_________________ :::

clf = clf.fit(X, Y)
prediction = clf.predict([ [ 17,-13,509,0,-816,-305 ]  ])
print (prediction)
