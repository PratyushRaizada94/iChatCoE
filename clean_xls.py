import pandas as pd

import nltk
import numpy as np
import random
import string # to process standard python strings
from nltk.stem.wordnet import WordNetLemmatizer
from difflib import SequenceMatcher
from nltk.tokenize import RegexpTokenizer
import copy
import random


f=open('chatbot.txt','r')
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
def lemmatize(text):
    """
    Function to lemmatize a text string. 
    Lemmatizing is the process of removing 'ing', 'ly', 'es' etc. suffixes from the test string 
    """

    lem = WordNetLemmatizer()
    return ' '.join(list(map(lambda x: lem.lemmatize(x, 'v'),
                    text.split())))

file_name = "Tree Structure.xlsx"

xls_file = pd.ExcelFile(file_name)
print(xls_file.sheet_names)
df = xls_file.parse('owssvr')
#df = df.loc[df['Item Type'] == "Item"]
df = df[df["Item Type"] != "Folder"]
#print(df)
df = df.replace(np.nan, '', regex=True)
df["Path"] = df["Path"].apply(lambda x: x[50:len(x)].strip())
df["Path"] = df["Path"].apply(lambda x: x.replace('-',' ').replace('/',' ').lower())
df["Extn"] = df["Name"].apply(lambda x: x[x.rindex('.')+1:].lower())
df["Extn"] = df["Extn"].apply(lambda x: "ppt" if x=="pptx" else x)
df["Extn"] = df["Extn"].apply(lambda x: "xls" if x=="xlsx" else x)
df["Extn"] = df["Extn"].apply(lambda x: "doc" if x=="docx" else x)
df["Name"] = df["Name"].apply(lambda x: x.replace('-',' ').replace('_',' '))
df["Name"] = df["Name"].apply(lambda x: x[0:x.rindex('.')].lower())
df["Domain"] = df["Domain"].apply(lambda x: str(x).lower())
df["Technology"] = df["Technology"].apply(lambda x: str(x).lower())
df["Account"] = df["Account"].apply(lambda x: str(x).lower())
#a = lambda x: x[x.rindex('.')+1:]
#print(a("ad.xls"))
from collections import Counter
a = Counter(df["Extn"])
print(dict(a))

#print(df[["Name","Extn","Path"]])
print(sum(a.values()))
print(df.shape)

print(list(df.columns.values))
df.pop("Modified By")
df.pop("Item Type")
df.pop("Modified")
print(df)


df['text'] = df[["Name","Account","Technology","Domain","Path","Extn" ]].apply(lambda x: ' '.join(x), axis=1)
df['text'] = df["text"].apply(lambda x: " ".join(x.split()))
df['text'] = df['text'].apply(lambda x: lemmatize(x))


print(df["text"])
header = ["text"]
df.to_csv('output.csv', columns = header)