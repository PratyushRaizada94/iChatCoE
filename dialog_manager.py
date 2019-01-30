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
    'hi',
    'coffee'
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
        text = correct(word, text, 0.8	)
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
        'in'
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


intent = []
technologies = ["abinitio","informatica"]
sectors = ["health","finance","retail"]

def check_technology():
	print("tech:",intent)
	for tech in technologies:
		if tech in intent:
			return tech
	return False

def check_sector():
	print("sector:",intent)
	for sec in sectors:
		if sec in intent:
			return sec
	return False


while True:
	#global intent
	utterance = input()
	#print(utterance)
	utterance = remove_noise(prepare_utterance(utterance))
	for word in utterance.split():
		if word not in intent:
			intent.append(word)
	print(intent)
	tech  = check_technology()
	sector = check_sector()
	if tech and sector:
		print("fetching links for {} in {} sector".format(tech,sector))
		print(intent)
