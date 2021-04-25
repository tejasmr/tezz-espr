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

### sample.txt

In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills.

### output.txt

Summary of sample.txt from file:

Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset



Summary of sample.txt from the extracted string:

Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset
## Documentation

### Release functions

#### 1. Generate Summary from file
```py
@type: function
@head: def generate_summary_from_file(file_name, top_n=5)
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
@head: def generate_summary_from_document(document, top_n=5)
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

#### 2. Extract sentences from document

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
