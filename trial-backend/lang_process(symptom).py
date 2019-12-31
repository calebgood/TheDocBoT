
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pickle
def get_key(val): 
    for key, value in checkdict.items(): 
         if val == value: 
             return key 
  
with open('checkup.txt','r') as f:
        text=f.read()


stop_words = set(stopwords.words('english'))
ref=text.split('\n')
words=[i.split() for i in ref]

for w in words:
    for i in range(len(w)):
        if w[i] in stop_words:
           w[i]=''
N=''
words = [[ele for ele in sub if ele != N] for sub in words] 
print(words)

final={}
for w in range(len(words)):
    synonyms=[]
    for i in words[w]:
        for syn in wordnet.synsets(i):
                for l in syn.lemmas():
                        synonyms.append(l.name())
    final[ref[w]]=set(synonyms)
pickle.dump(final,open("corpus.pickle","wb"))
'''
for i in final.values():
    print(i)

with open('checkup.txt','r') as f:
       check=[i.replace('\n','') for i in f.readlines()]
checkdict={}
for i in check:
        checkdict[i]=i.split()
#print(checkdict)


pred=set()
for tar_lis in final.values():
   for i in tar_lis:
      for list_values in checkdict.values():
         if i in list_values:
            pred.add(get_key(list_values))
     
print(pred)
'''
