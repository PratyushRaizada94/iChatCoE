import nltk
import numpy as np
import random
import string # to process standard python strings
import numpy

f=open('corpus.txt','r')
raw=f.read()
raw=raw.lower()# converts to lowercase

nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    vals1 = cosine_similarity(tfidf[-1], tfidf)
    print(vals)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    print(flat)
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

def get_top_3_response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    print(vals)
    idx  = vals.argsort()[0][-2]
    idx1  = vals.argsort()[0][-3]
    idx2 = vals.argsort()[0][-4]
    flat  = vals.flatten()
    flat.sort()
    #print(flat)
    req_tfidf = flat[-2]
    req_tfidf = flat[-3]
    req_tfidf = flat[-4]
    print("flat:",type(flat))
    print("vals:",type(vals))
    print(sum(flat>0.0)-1)
    print(sum(flat))
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you, please specify the sector (health/finance/retail etc. ), technology (ab initio/informatica/tableau etc.) or vertical that you want to search for."
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx] + "\n" + robo_response+sent_tokens[idx1] + "\n" + robo_response+sent_tokens[idx2]
        return robo_response

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(get_top_3_response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")
