#%% 
from nltk import ngrams
from collections import Counter

# 3.4 Bigram language model
corpus = ['<s> I am Sam </s>', '<s> Sam I am </s>',
'<s> I am Sam </s>', '<s> I do not like green eggs and Sam </s>']

#%% 
# implemented with nltk – To check which solution is correct! This does not find the same probability 
# since it implements an unknown token and moves some probability mass to this token
# This is more robust for future cases but in the example the solution below
# might be a bit better. 
from nltk.lm import Laplace
from nltk.lm.preprocessing import padded_everygram_pipeline

text = [['I', 'am', 'Sam'], ['Sam', 'I', 'am',],
['I', 'am', 'Sam'], ['I', 'do', 'not', 'like', 'green', 'eggs', 'and', 'Sam']]

train, vocab = padded_everygram_pipeline(2, text)

# for gen in train:  
#     print(*gen)

lm = Laplace(2)
lm.fit(train, vocab)

print(lm.vocab)
lm.score("Sam", ["am"])
#%%

#%% 
def count_bi_uni_grams(corpus: list):
    '''
    given a corpus and a n calculates the MLE estimates for each N-gram
    returns a counter with the counts of bigrams
    '''
    every_grams = []
    for sentence in corpus: 
        bi_grams = list(ngrams(sentence.split(), n=2))
        uni_grams = sentence.split()

        every_grams.append(bi_grams)
        every_grams.append(uni_grams)

    
    flat_list_bigrams = [item for sublist in every_grams for item in sublist]

    n_grams = Counter(flat_list_bigrams)

    return n_grams
    
def calculate_mle_estimate(pattern: tuple, corpus: list, add_one_smoothing: bool = True):
    '''
    Calculate the mle_estimate of a given sentence 
    '''
    grams = count_bi_uni_grams(corpus)

    V = 0
    if add_one_smoothing:
        for key in grams.keys():
            if type(key) == tuple:
                grams[key] += 1
            else:
                V += 1 
                
        mle_estimate = (grams[pattern]) / (grams[pattern[0]] + V)


    else:
        mle_estimate = (grams[pattern]) / (grams[pattern[0]])


    print(mle_estimate)


calculate_mle_estimate(('am', 'Sam'), corpus=corpus)
# calculate_bigram_MLE(corpus)
# %%

# %% døde ideers land
# Løsning herfra
# https://github.com/Clement25/Speech-and-Language-Processing-ver3-solutions/blob/master/Chapter3.ipynb
# 3.4
sen_wds = []
for sen in corpus:
    sen_wds.append(sen.split())
print(sen_wds)

def add1smooth(sens, pre, cur):
    Vocab = set()
    for sen in sens:
        for wd in sen:
            Vocab.add(wd)
    V = len(Vocab)
    total = target = 0
    for sen in sens:
        for i in range(len(sen)-1):
            if sen[i] == pre:
                total += 1
                if sen[i+1] == cur:
                    target += 1
    return (target+1)/(total+V)
    
print(add1smooth(sen_wds, 'am', 'Sam'))    
# %%
