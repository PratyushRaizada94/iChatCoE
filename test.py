#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        text = correct(word, text, 0.85)
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
        'sorry',
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


def prepare_utterance(utterace):
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


def casual_utterance(sentence):
    '''If utterance is casual reply back accordingly'''

    GREETING_INPUTS = ("hello", "hi", "greetings","hey")
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            print(random.choice(GREETING_RESPONSES))
            print("Hi user, What would you like me to find for you?")
            return True


    WORKQUES_INPUTS = ("sup","sup?", "what's up")
    WORKQUES_RESPONSES = ["Not much"]
    for word in sentence.split():
        if word.lower() in WORKQUES_INPUTS:
            print(random.choice(WORKQUES_RESPONSES))
            print("Just looking up some documents for curious souls :)")
            return True


    THANK_INPUTS = ("thanks", "that's great", "that was helpful")
    THANK_RESPONSES = ["you are welcome", "happy to help :D"]
    for word in sentence.split():
        if word.lower() in THANK_INPUTS:
            print (random.choice(THANK_RESPONSES))
            return True


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

    print("Hi user!")
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





