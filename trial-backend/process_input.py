from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pickle


def rem_punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "")
    return(string)

#Returns a set containing suitable symtoms from the given word 
def lang_process(text):
    #process the input properly
    stop_words = set(stopwords.words('english'))
    text=rem_punctuation(text)
    #print(text)
    words=word_tokenize(text)
    filtered_sentence = [w for w in words if not w in stop_words]
    filtered_sentence=set(filtered_sentence)
    #print(text)
    print(filtered_sentence)
    final=[]
    for i in filtered_sentence:
            synonyms=[]
            for syn in wordnet.synsets(i):
                    for l in syn.lemmas():
                            synonyms.append(l.name())
            final.append(synonyms)
    #Flat the list of lists
    fl = []
    for sublist in final:
        for item in sublist:
            fl.append(item)
    fl=list(set(fl))
    fl=[w for w in fl if not w in stop_words]
    print('Test-length:',len(fl))
    #Import the check list to get the symptoms
    checkdict = pickle.load(open("corpus.pickle","rb"))

    def get_key(val): 
        for key, value in checkdict.items(): 
             if val == value: 
                 return key 

    #print(checkdict)
    #Various related symtomns
    pred=set()
    for i in fl:
     for list_values in checkdict.values():
         if i in list_values:
            pred.add(get_key(list_values))
    return pred

if __name__=='__main__':
    with open('sample.txt','rb') as f:
        text=str(f.read())
    print(lang_process(text))
