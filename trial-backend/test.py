import numpy as np
import pandas as pd
import random
#import time
import pickle


#Test model

clf=pickle.load(open("k_neighbor_model.pickle","rb"))
#print("begin")
#s=time.time()
'''
raw=np.zeros(132)

for _ in range(0):
    a=random.randint(0,131)

raw[22]=1
'''    
df=pd.read_csv('training.csv')
y=df.iloc[:,-1]
#print(y[0])
df.drop(df.columns[[-1]], axis=1, inplace=True)
q=0
for i,j in df.iterrows():
    result=clf.predict([j])[0]
    if y[i]==result:
        q+=1
    else:
        print(false)
print(q)
#e=time.time()
#print("end...","time taken:",e-s)

