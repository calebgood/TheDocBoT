import pandas as pd
from brain.utils import lang_process as lg,search
import pickle

def final_verdict(text):
   if text==None:
      return None
   raw_txt=lg(text)
   verdict=[]
   print('Please Enter yes or no for the following:({})'.format(len(raw_txt)))
   a=1
   for i in raw_txt:
      if input(str(a)+'. '+i+'?')=='yes':
         verdict.append(i)
      a+=1
   verdict=[i.replace(' ','_') for i in verdict]
   raw=[]
   with open('checkup_raw.txt','r') as f:
      checklist=[i.replace('\n','') for i in f.readlines()]
   for i in checklist:
      if i in verdict:
         raw.append(1)
      else:
         raw.append(0)
   print(raw)  
   clf=pickle.load(open("k_neighbor_model.pickle","rb"))
   result=clf.predict([raw])
   return result
if __name__=='__main__':
   with open('s.txt','r') as f:
      text=f.read()
   result=final_verdict(text)[0]
   print(result)
   search(result)
