# Tezz Extractive Summarizer using Page Rank

## Meta Data

```py
@module         : tezz_espr
@title          : Tezz Extractive Summarizer using Page Rank
@author         : Tejas M R
@description    : Implementation of Extractive summarization using python.
@license        : MIT License
@github         : github.com/tezz-io
```

## Usage

```py
from tezz_espr import generate_summary_from_file, generate_summary_from_document

print("Summary of sample.txt from file:\n")
print(generate_summary_from_file('sample.txt', top_n=2))


print("\n\n\nSummary of sample.txt from the extracted string:\n")
file = open('sample.txt', 'r')
file_data = file.readlines()
print(generate_summary_from_document(file_data[0], top_n=2))
```

## Documentation

### Release functions

#### 1. Generate Summary from file
```py
@type: function
@head: generate_summary_from_file(file_name, top_n=5)
@inputs:
    1. file_name: the relative/absolute path of the file or the name of
                    the file if it is in the same directory
    2. top_n: no of sentences in the final summary
@outputs:
    1. generate_summary(sentences, top_n): the summarized text
```

#### 2. Generate Summary from Document/String
```py
@type: function
@head: generate_summary_from_document(document, top_n=5)
@inputs:
    1. document: a string of sentences.
    2. top_n: no of sentences in the final summary
@outputs:
    1. generate_summary(sentences, top_n): the summarized text
```

### Helper functions

#### 1. Extract sentences from file

```py
@type: function
@head: def extract_sentences_from_file(file_name)
@inputs:
    1. file_name: name of the file if it is in the same directory as this file
                    or relative/absolute path to the file
@outputs:
    1. sentences: a python array of all the sentences extracted from the file
```

#### 2. Extract sentences from document

```py
@type: function
@head: def extract_sentences_from_document(document)
@inputs:
    1. document: a long document/string which is a lot of sentences separated by "."
@outputs:
    1. sentences: a python array of all the sentences extracted from the document
```

#### 3. Calculate sentence similarity using cosine_distance

```py
@type: function
@head: def sentence_similarity(sent1, sent2, stopwords=None)
@inputs:
    1. sent1: some sentence
    2. sent2: some other sentence
    3. stopwords: stop words to filter out
@outputs:
    1. 1 - cosine_distance(a, b): mathematical similarity between the sentences
```

#### 4. Build similarity matrix

```py
@type: function
@head: def build_similarity_matrix(sentences, stop_words)
@inputs:
    1. sentences: a python array of all the sentences extracted from the file
    2. stop_words: stop words are words which are filtered out before or after 
                    processing of natural language data 
@outputs:
    1. similarity matrix: a similarity matrix is a matrix of scores which 
                    express the similarity between two data points
```

#### 5. Generate summary from sentences

```py
@type: function
@head: def generate_summary(sentences, top_n=5)
@inputs:
    1. sentences: the array of sentences
    2. top_n: no of sentences to be in the summary
@outputs:
    1. summarized_text: the summary of all the sentences mathematically
```
