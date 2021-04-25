"""
@module         : tezz_espr
@title          : Tezz Extractive Summarizer using Page Rank
@author         : Tejas M R
@description    : Implementation of Extractive summarization using python.
@license        : MIT License
@github         : github.com/tezz-io
"""


from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


"""
@type: function
@head: def extract_sentences_from_file(file_name)
@inputs:
    1. file_name: name of the file if it is in the same directory as this file
                    or relative/absolute path to the file
@outputs:
    1. sentences: a python array of all the sentences extracted from the file
"""

def extract_sentences_from_file(file_name):
    # open the file - error is generated if it is invalid
    file = open(file_name, "r")
    
    # read the contents of the file
    file_data = file.readlines()

    return extract_sentences_from_document(file_data[0])

"""
@type: function
@head: def extract_sentences_from_document(document)
@inputs:
    1. document: a long document/string which is a lot of sentences separated by "."
@outputs:
    1. sentences: a python array of all the sentences extracted from the document
"""

def extract_sentences_from_document(document):
    # split the contents of the document using the separator ". "
    # to extract all the sentences
    article = document.split(". ")

    # a python array to store all sentences extracted
    sentences = []

    # iterate through the article
    for sentence in article:
        # print the sentence to preview
        # print(sentence)

        # generate clean sentences
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences

"""
@type: function
@head: def sentence_similarity(sent1, sent2, stopwords=None)
@inputs:
    1. sent1: some sentence
    2. sent2: some other sentence
    3. stopwords: stop words to filter out
@outputs:
    1. 1 - cosine_distance(a, b): mathematical similarity between the sentences
"""

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


"""
@type: function
@head: def build_similarity_matrix(sentences, stop_words)
@inputs:
    1. sentences: a python array of all the sentences extracted from the file
    2. stop_words: stop words are words which are filtered out before or after 
                    processing of natural language data 
@outputs:
    1. similarity matrix: a similarity matrix is a matrix of scores which 
                    express the similarity between two data points
"""

def build_similarity_matrix(sentences, stop_words):
    # no of rows&columns of the similarity_matrix
    num = len(sentences)
    
    # create an empty similarity matrix
    similarity_matrix = np.zeros((num, num))

    # start creating the sikilarity matrix
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], 
                                        sentences[j], stop_words)
    return similarity_matrix

"""
@type: function
@head: generate_summary(sentences, top_n=5)
@inputs:
    1. sentences: the array of sentences
    2. top_n: no of sentences to be in the summary
@outputs:
    1. summarized_text: the summary of all the sentences mathematically
"""

def generate_summary(sentences, top_n=5):
    # stop words to filter
    stop_words = stopwords.words('english')
    
    # empty array of summarized text
    summarized_text = []

    # generate similarity matrix
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)

    # rank sentences in similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    
    # get scores to sort the rank
    scores = nx.pagerank(sentence_similarity_graph)

    # sort the rank
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    n = min(len(ranked_sentences), top_n)
    # pick the top sentences
    for i in range(top_n):
        summarized_text.append(" ".join(ranked_sentences[i][1]))

    # return the summarized_text
    return ". ".join(summarized_text)

"""
@type: function
@head: generate_summary_from_file(file_name, top_n=5)
@inputs:
    1. file_name: the relative/absolute path of the file or the name of
                    the file if it is in the same directory
    2. top_n: no of sentences in the final summary
@outputs:
    1. generate_summary(sentences, top_n): the summarized text
"""

def generate_summary_from_file(file_name, top_n=5):
    sentences = extract_sentences_from_file(file_name)
    return generate_summary(sentences, top_n)

"""
@type: function
@head: generate_summary_from_document(document, top_n=5)
@inputs:
    1. document: a string of sentences.
    2. top_n: no of sentences in the final summary
@outputs:
    1. generate_summary(sentences, top_n): the summarized text
"""
def generate_summary_from_document(document, top_n=5):
    sentences = extract_sentences_from_document(document)
    return generate_summary(sentences, top_n)


"""
Thank you for using tezz_espr. Hope you have a wonderful day.
"""
