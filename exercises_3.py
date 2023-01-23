#%% 
import re
from nltk import ngrams, FreqDist
from collections import Counter

# 3.4 Bigram language model
sens = ['<s> I am Sam </s>', '<s> Sam I am </s>',
'<s> I am Sam </s>', '<s> I do not like green eggs and Sam </s>']

#%% 
# implemented with nltk


#%% 

# print(count_occurences('I am', corpus))

def count_bi_uni_grams(corpus: list):
    '''
    given a corpus and a n calculates the MLE estimates for each N-gram
    returns a dictionary with the counts
    '''
    counter = Counter

    # n_grams = [ngrams(sentence.split(), n=n) for sentence in corpus]
    all_n_grams = []
    for sentence in corpus: 
        bi_grams = list(ngrams(sentence.split(), n=2))
        uni_grams = sentence.split()

        all_n_grams.append(bi_grams)
        all_n_grams.append(uni_grams)

    # print(all_n_grams)
    
    flat_list = [item for sublist in all_n_grams for item in sublist]

    n_grams = Counter(flat_list)

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
                # increasing the count of all the bigrams
                grams[key] += 1
            else:
                # we need to adjust the denominator for when we normalise probabilities!
                V += 1 # increase vocab count so we know what it is! 

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
