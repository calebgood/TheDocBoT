import pandas as pd
df=pd.read_csv('testing.csv')
y=list(df)
#y=[i.replace('_',' ') for i in y]
'''
with open('checkup.txt','r') as f:
    for i in f.readlines():
        y.append(i.replace('_',' '))
'''    
with open('checkup_raw.txt','w') as f:
    for i in y:
        f.write(i+'\n')
