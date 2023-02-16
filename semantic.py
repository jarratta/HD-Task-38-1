"""
Author: Alistair Jarratt
Student ID: AJ22110004854
Task: T40
>> APOLOGIES: FORGOT TO LOAD THE .PY INTO DROPBOX!
Introduction to natural language processing
"""

import spacy

# Create a function using the simple laguage model
def task1_word_similarity_simple():

# use the simple language model
    nlp = spacy.load('en_core_web_sm')

# Check similarity of the words
    word1 = nlp('cat')
    word2 = nlp('monkey')
    word3 = nlp('banana')

#Print the results
    print(f'First word: {word1} Second word: {word2} - Similarity: {word1.similarity(word2)}')
    print(f'First word: {word3} Second word: {word2} - Similarity: {word3.similarity(word2)}')
    print(f'First word: {word3} Second word: {word1} - Similarity: {word3.similarity(word1)}')

# Create a function using the simple laguage model
def task1_word_similarity_complex():

# use the complex language model
    nlp = spacy.load('en_core_web_md')

# Check similarity of the words
    word1 = nlp('cat')
    word2 = nlp('monkey')
    word3 = nlp('banana')

#Print the results
    print(f'First word: {word1} Second word: {word2} - Similarity: {word1.similarity(word2)}')
    print(f'First word: {word3} Second word: {word2} - Similarity: {word3.similarity(word2)}')
    print(f'First word: {word3} Second word: {word1} - Similarity: {word3.similarity(word1)}')

# Create a function to compare words using the simple language model
def vectors_simple():

# Load the simple language model
    nlp = spacy.load('en_core_web_sm')

# Create tokens for the words to be compared and print the results
    tokens = nlp('cat apple monkey banana mouse cheese')
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# Create a function to compare words using the complex language model
def vectors_complex():

# Load the complex language model
    nlp = spacy.load('en_core_web_md')

# Create tokens for the words to be compared and print the results
    tokens = nlp('cat apple monkey banana mouse cheese')
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# Create a function to compare sentances using the simple language model
def sentance_similarity_simple():
    
# Load the simple language model  
    nlp = spacy.load('en_core_web_sm')

# Define the model sentance to compare 
    sentance_to_compare = "'Why is my cat on the car"

# Define the sentances to compare in a list
    sentences = ["where did my dog go",
    "Hello, their is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"]

# Create tokens for the words to be compared and print the results
    model_sentence = nlp(sentance_to_compare)

    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", + similarity)

# Create a function to compare sentances using the complex language model
def sentance_similarity_complex():

# Load the complex language model      
    nlp = spacy.load('en_core_web_md')

# Define the model sentance to compare 
    sentance_to_compare = "'Why is my cat on the car"

# Define the sentances to compare in a list
    sentences = ["where did my dog go",
    "Hello, their is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"]

# Create tokens for the words to be compared and print the results
    model_sentence = nlp(sentance_to_compare)

    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", + similarity)

# Create a menu function to run the various scenarios
def menu():

    menu_select =""

    while menu_select != "q":

            output = f'——————————————————[SELECT AN OPTION]—————————————————————\n'
            output += f'Section a function: \n'
            output += f'a: Word Similarity: Simple Engine \n'
            output += f'b: Word Similarity: Complex Engine  \n'
            output += f'c: Working with vectors: Simple Engine \n'
            output += f'd: Working with vectors: Complex Engine  \n'
            output += f'e: Sentenece Similaity: Simple Engine \n'
            output += f'f: Sentenece Similaity: Complex Engine \n'                
            output += f'q: QUIT the program \n'        
            output += f'—————————————————————————————————————————————————————————\n'
            print (output)

            menu_select = input("Select a function: ").lower()   
            if menu_select in ('a','b','c','d','e','f','q'):
                if menu_select == "a":
                    task1_word_similarity_simple()
                elif menu_select == "b":
                    task1_word_similarity_complex()
                elif menu_select == "c":
                    vectors_simple()
                elif menu_select == "d":
                    vectors_complex()
                elif menu_select == "e":
                    sentance_similarity_simple()
                elif menu_select == "f":
                    sentance_similarity_complex()
                elif menu_select == "q":
                    print("Thank-you learning!")
                    quit()

menu()



########################################_TASK 38_1.1_############################################

# The similiar language model ran however it created the following warning:
#
#[W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give 
#useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and 
#only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.

# The output from the simple model obly compared twi words

#   print(word3.similarity(word1))
# 0.6806929391210822

#But the output from the comlex model was:

# 0.5929930274321619
# 0.40415016164997786
# 0.22358825939615987#

# All the word combinations were compared.  Also the resoult was difernet for the one result from the simple model.

###################################_Task 38_1_2_##################################################

#  The simple model produced a warning:

# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give 
# useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use 
# context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(token1.text, token2.text, token1.similarity(token2))

#Generally the comelx model had better results.  For example

#Simple:
# mouse cat 0.5055392384529114
# mouse apple 0.5927436947822571
# mouse monkey 0.6988571286201477
# mouse banana 0.7421507239341736 <<< Highest
# mouse mouse 1.0
# mouse cheese 0.37378448247909546 <<<< Lowest

# Complex:
# mouse cat 0.5328792929649353 <<<< Highest
# mouse apple 0.2800682783126831
# mouse monkey 0.48655828833580017
# mouse banana 0.18919304013252258 <<<< Lowest
# mouse mouse 1.0
# mouse cheese 0.21466833353042603


###################################_Task 38_1_3_##################################################

# # Once again the code ran but with the same warning message:

# UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give 
# useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and 
# only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.

# The output of the simple mode was:

#   similarity = nlp(sentence).similarity(model_sentence)
# where did my dog go -  0.4255809719575274
# Hello, their is my car -  0.63780741760779
# I've lost my car in my car -  0.500795732031743
# I'd like my boat back -  0.2929248722021074
# I will name my dog Diana -  0.340654217410769

# The putput of the complex model was:
# where did my dog go -  0.5817438469726575
# Hello, their is my car -  0.7765403516324468
# I've lost my car in my car -  0.6228509618436178
# I'd like my boat back -  0.5191908546865404
# I will name my dog Diana -  0.6095949286088317

#The results were different but the highest and lowest were the same but with different similarity ratings:

# Simple:
# where did my dog go -  0.4255809719575274
# Hello, their is my car -  0.63780741760779 <<<<<<<<< Highest
# I've lost my car in my car -  0.500795732031743
# I'd like my boat back -  0.2929248722021074 <<<<<<<<Lowest
# I will name my dog Diana -  0.340654217410769

# Complex:
# where did my dog go -  0.5817438469726575
# Hello, their is my car -  0.7765403516324468 <<<<<<<<<Highest
# I've lost my car in my car -  0.6228509618436178
# I'd like my boat back -  0.5191908546865404 <<<<<<<<<<<< Lowest
# I will name my dog Diana -  0.6095949286088317
