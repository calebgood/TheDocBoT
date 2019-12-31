import numpy as np
from sklearn import preprocessing,neighbors,svm
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


train = pd.read_csv('training.csv')
train.replace("?",-999999,inplace=True)

cols= train.columns
cols=cols[:-1]
#print(cols)

X=np.array(train[cols])
y=np.array(train['prognosis'])
print(len(X[0]))

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#clf = neighbors.KNeighborsClassifier(probability=True)
clf = svm.SVC(probability=True)
clf.fit(X_train, y_train)
pickle.dump(clf,open("k_neighbor_model.pickle","wb"))

accuracy = clf.score(X_test, y_test)
print('accuracy:'+str(accuracy*100))

'''
example=np.array([[4,2,1,1,1,2,3,2,1],[8,1,1,1,2,2,3,2,3]])
example=example.reshape(len(example),-1)
predic=clf.predict(example)
print(predic)
'''
