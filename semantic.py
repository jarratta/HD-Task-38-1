########################################_TASK 38_1.1_############################################

# import spacy
# nlp = spacy.load('en_core_web_md')

# word1 = nlp('cat')
# word2 = nlp('monkey')
# word3 = nlp('banana')

# print(word1.similarity(word2))
# print(word3.similarity(word2))
# print(word3.similarity(word1))

# import spacy
# nlp = spacy.load('en_core_web_sm')

# word1 = nlp('cat')
# word2 = nlp('monkey')
# word3 = nlp('banana')

# print(word1.similarity(word2))
# print(word3.similarity(word2))
# print(word3.similarity(word1))


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
import spacy
nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana mouse cheese')
for tokens1 in tokens:
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# import spacy
# nlp = spacy.load('en_core_web_md')

# tokens = nlp('cat apple monkey banana mouse cheese')
# for tokens1 in tokens:
#     for token1 in tokens:
#         for token2 in tokens:
#             print(token1.text, token2.text, token1.similarity(token2))

# Out put of simple model:
# cat cat 1.0
# cat apple 0.7090088129043579
# cat monkey 0.5971202254295349
# cat banana 0.631443202495575
# cat mouse 0.5055392384529114
# cat cheese 0.22862693667411804
# apple cat 0.7090088129043579
# apple apple 1.0
# apple monkey 0.7693575024604797
# apple banana 0.7130810022354126
# apple mouse 0.5927436947822571
# apple cheese 0.23921111226081848
# monkey cat 0.5971202254295349
# monkey apple 0.7693575024604797
# monkey monkey 1.0
# monkey banana 0.7109044194221497
# monkey mouse 0.6988571286201477
# monkey cheese 0.3524942100048065
# banana cat 0.631443202495575
# banana apple 0.7130810022354126
# banana monkey 0.7109044194221497
# banana banana 1.0
# banana mouse 0.7421507239341736
# banana cheese 0.30435097217559814
# mouse cat 0.5055392384529114
# mouse apple 0.5927436947822571
# mouse monkey 0.6988571286201477
# mouse banana 0.7421507239341736
# mouse mouse 1.0
# mouse cheese 0.37378448247909546
# cheese cat 0.22862693667411804
# cheese apple 0.23921111226081848
# cheese monkey 0.3524942100048065
# cheese banana 0.30435097217559814
# cheese mouse 0.37378448247909546
# cheese cheese 1.0

# Outplut from the complex model:
# cat cat 1.0
# cat apple 0.2036806046962738
# cat monkey 0.5929930210113525
# cat banana 0.2235882580280304
# cat mouse 0.5328792929649353
# cat cheese 0.19478504359722137
# apple cat 0.2036806046962738
# apple apple 1.0
# apple monkey 0.2342509925365448
# apple banana 0.6646699905395508
# apple mouse 0.2800682783126831
# apple cheese 0.533275842666626
# monkey cat 0.5929930210113525
# monkey apple 0.2342509925365448
# monkey monkey 1.0
# monkey banana 0.4041501581668854
# monkey mouse 0.48655828833580017
# monkey cheese 0.1834208071231842
# banana cat 0.2235882580280304
# banana apple 0.6646699905395508
# banana monkey 0.4041501581668854
# banana banana 1.0
# banana mouse 0.18919304013252258
# banana cheese 0.5478538870811462
# mouse cat 0.5328792929649353
# mouse apple 0.2800682783126831
# mouse monkey 0.48655828833580017
# mouse banana 0.18919304013252258
# mouse mouse 1.0
# mouse cheese 0.21466833353042603
# cheese cat 0.19478504359722137
# cheese apple 0.533275842666626
# cheese monkey 0.1834208071231842
# cheese banana 0.5478538870811462
# cheese mouse 0.21466833353042603
# cheese cheese 1.0


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

# import spacy
# nlp = spacy.load('en_core_web_sm')

# sentance_to_compare = "'Why is my cat on the car"

# sentences = ["where did my dog go",
# "Hello, their is my car",
# "I\'ve lost my car in my car",
# "I\'d like my boat back",
# "I will name my dog Diana"]

# model_sentence = nlp(sentance_to_compare)

# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", + similarity)

# import spacy
# nlp = spacy.load('en_core_web_md')

# sentance_to_compare = "'Why is my cat on the car"

# sentences = ["where did my dog go",
# "Hello, their is my car",
# "I\'ve lost my car in my car",
# "I\'d like my boat back",
# "I will name my dog Diana"]

# model_sentence = nlp(sentance_to_compare)

# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", + similarity)

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
