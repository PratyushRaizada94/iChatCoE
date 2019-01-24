#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from difflib import SequenceMatcher
from nltk.tokenize import RegexpTokenizer
import copy
import random


#FIX-ME update vocabulary with the word
vocabulary = [
    'pertain',
    'more',
    'fetch',
    'be',
    'there',
    'do',
    'you',
    'have',
    'any',
    'is',
    'my',
    'on',
    'can',
    'i',
    'get',
    'some',
    'am',
    'look',
    'for',
    'the',
    'to',
    'share',
    'me',
    'of',
    'please',
    'a',
    'very',
    'at',
    'with',
    'relate',
    'sorry',
    'informatica',
    'ab initio',
    'talend',
    'etl',
    'dwt',
    'dwh',
    'rfp',
    'tableu',
    'case',
    'study',
    'video',
    'doccument',
    'link',
    'artefact',
    'hello',
    'hi'
    ]


def lemmatize(text):
    """Function to lemmatize a text string. 
    Lemmatizing is the process of removing 'ing', 'ly', 'es' etc. suffixes from the test string """

    lem = WordNetLemmatizer()
    return ' '.join(list(map(lambda x: lem.lemmatize(x, 'v'),
                    text.split())))


def check_spellings(text):
    """Function to check for typos in the text string.
    It corrects the spelling if it finds some spelling matching to 85% of the lexicon used in the vocabulary"""

    for word in vocabulary:
        text = correct(word, text, 0.7)
    return text


def correct(search_key, text, strictness):
    """This function corrects the spelling in case there is a typo resembling to 85% of the spelling of the matching word"""

    text_copy = copy.deepcopy(text)
    words = text.split()
    for word in words:
        similarity = SequenceMatcher(None, word, search_key)
        if similarity.ratio() > strictness:
            text_copy = text_copy.replace(word, search_key)
    return text_copy


def remove_noise(text):
    """This function is used to filter out the words that are noises and do not convey any important message"""

    text = text.split()
    word = [word for word in text if word not in [
        'pertain',
        'estimate',
        'link',
        'and',
        'more',
        'fetch',
        'be',
        'there',
        'do',
        'you',
        'have',
        'any',
        'is',
        'my',
        'on',
        'can',
        'i',
        'get',
        'some',
        'am',
        'look',
        'for',
        'the',
        'to',
        'share',
        'me',
        'of',
        'please',
        'a',
        'very',
        'at',
        'with',
        'relate',
        'sorry'
        ]]
    return ' '.join(word)


def standardize(text):
    lookup_dict = {
        'rt': 'Retweet',
        'dm': 'direct message',
        'awsm': 'awesome',
        'luv': 'love',
        'doc': 'document',
        'lvl': 'level',
        'plz': 'please',
        'pls': 'please',
        'info': 'information',
        'u': 'you',
        'sry': 'sorry',
        'gr8': 'great'
        }
    new_words = []
    for word in text.split():
        if word in lookup_dict:
            new_words.append(lookup_dict[word])
            continue
        new_words.append(word)
    return ' '.join(new_words)


def prepare_utterance(line):
    """Function to prepare the utterance to a standard text string
    1. Creates deep copy of utterance
    2. Trims the string
    2. Converts text to lower string
    3. Removes punctuations for the text"""

    text = copy.deepcopy(line).strip().lower()
    tokenizer = RegexpTokenizer(r'\w+')
    text = ' '.join(tokenizer.tokenize(text))
    text = standardize(text)
    text = check_spellings(text)
    text = lemmatize(text)
    return text


def listen():
    utterance = input()
    return (utterance)


def prepare_reply():
    pass



def entities_found():
    return True


def confirmed(utterance):
    return True


def fetch_links(entities):
    return ["www.google.com"]


def show_what_found(links):
    print(links)


def clear_entity():
    pass


def discover_entities():
    pass


def apologize():
    print("Sorry I do not understand this. Please elaborate")


def get_bussiness_utterance():
    #check if the utterance is not casual

    utterance = listen()
    while casual_utterance(utterance):
        utterance = listen()
    return utterance


def casual_utterance(sentence,message,input_value):
    '''If utterance is casual reply back accordingly'''

    GREETING_INPUTS = ("hello", "hi", "greetings","hey")
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            #print(random.choice(GREETING_RESPONSES))
            message.insert(INSERT,"Bot: "+random.choice(GREETING_RESPONSES)+"\n")
            #print("Hi user, What can I find for you?")
            message.insert(INSERT,"Bot: "+"Hi user, What can I find for you?"+"\n")
            return True


    WORKQUES_INPUTS = ("sup","sup?", "what's up")
    WORKQUES_RESPONSES = ["Not much"]
    for word in sentence.split():
        if word.lower() in WORKQUES_INPUTS:
            #print(random.choice(WORKQUES_RESPONSES))
            message.insert(INSERT,"Bot: "+random.choice(WORKQUES_RESPONSES)+"\n")
            #print("Just looking up some documents for curious souls :)")
            message.insert(INSERT,"Bot: "+"Just looking up some documents for curious souls :)"+"\n")
            return True


    THANK_INPUTS = ("thanks", "that's great", "that was helpful")
    THANK_RESPONSES = ["you are welcome", "happy to help :D"]
    for word in sentence.split():
        if word.lower() in THANK_INPUTS:
            #print (random.choice(THANK_RESPONSES))
            message.insert(INSERT,"Bot: "+random.choice(THANK_RESPONSES)+"\n")
            return True
    return False


def on_closing():

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        GUI.destroy()

def Enter_Hit(event):

    utter=input_user.get()

    utter = prepare_utterance(utter)
    #print(utter)
    message.config(state=NORMAL,fg="Blue")
    message.insert(INSERT,"User: "+utter+"\n")
    if casual_utterance(utter,message,input_value):
        input_value.set("")
        message.config(state=DISABLED)
   #Handshake starts here
'''
    if (utter=="hi" or utter=="hello"):
        reply="Hello"
        message.insert(INSERT,"Bot: "+reply+"\n")
        input_value.set("")
        message.config(state=DISABLED)
    else:
        reply="Sorry, I did not understand what you just said."
        message.insert(INSERT,"Bot: "+reply+"\n")
        input_value.set("")
        message.config(state=DISABLED)  
'''                                                                                                        


'''
with open('data.txt') as f:
    for line in f:
        text = prepare_utterance(line)

        # standardize the text meassage

        text = standardize(text)

        # Correct the sentence for typos

        text = check_spellings(text)

        # Lemmatize the text

        text = lemmatize(text)

        # Remove noisy words

        text = remove_noise(text)

        # print(line.strip()+" ---------- "+    remove_noise(    lemmatize(   standardize(line.strip().lower())    )    )    )

        print (line.strip() + '\t\t\t\t' + text)
'''

if __name__ == '__main__':

    patience = 4
    entities = []

    print("Application starts...")
    '''
    while True:
        if patience > 0:
            #if utterance is query?
            utterance =  get_bussiness_utterance()
            if entities_found():
                reply = prepare_reply()
                print(reply)
                utterance = listen()
                if confirmed(utterance):
                    links = fetch_links(entities)
                    show_what_found(links)
                else:
                    clear_entity()
                    patience = patience - 1

        else:
            apologize()
            links = fetch_links(entities)
            show_what_found(links)            
            clear_entity()
            patience = 4
    '''
    GUI=Tk()
    GUI.title("Infosys Chatbot")
    input_value=StringVar()
    scrollbar = Scrollbar(GUI)
    scrollbar.pack(side=RIGHT, fill=Y)
    label1=Label(GUI,text="Welcome to Infosys Chatbot!",fg="Red")
    label1.pack(side=TOP,fill=X)
    message=Text(GUI)
    message.pack()
    message.config(state=DISABLED,yscrollcommand=scrollbar.set)
    scrollbar.config(command=message.yview)
    input_user=Entry(GUI,text=input_value)
    user_label=Label(GUI,text="Enter message here:",fg="Red")
    user_label.pack(fill=X)
    input_user.pack(fill=X)
    input_user.bind("<Return>", Enter_Hit)
    GUI.protocol("WM_DELETE_WINDOW", on_closing)
    GUI.mainloop()





