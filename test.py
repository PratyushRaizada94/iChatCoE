import nltk
from nltk.stem.wordnet import WordNetLemmatizer 
from difflib import SequenceMatcher

def lemmatize(text):
	lem = WordNetLemmatizer()
	return(" ".join(list(map(lambda x :lem.lemmatize(x, "v"),text.split()))))

def fuzzy_search(search_key, text, strictness):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        words = line.split()
        for word in words:
            similarity = SequenceMatcher(None, word, search_key)
            if similarity.ratio() > strictness:
                return " '{}' matches: '{}' in line {}".format(search_key, word, i+1)	

def remove_noise(text):
	text = text.split()
	word = [word for word in text if word not in ["pertain","more","fetch","be","there","do","you","have","any","is","my","on","can","i","get","some","am","look","for","the","to","share","me","of","please","a","very","at","with","relate","sorry"]]
	return " ".join(word)

def standardize(text):
	lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love", "doc":"document", "lvl":"level", "plz":"please","pls":"please","info":"information","u":"you","sry":"sorry"}
	new_words = []
	for word in text.split():
		if word in lookup_dict:
			new_words.append(lookup_dict[word])
			continue
		new_words.append(word)
	return " ".join(new_words)

with open("data.txt") as f:
	for line in f:
		print(line.strip()+" ---------- "+    remove_noise(    lemmatize(   standardize(line.strip().lower())    )    )    )

