import nltk
from nltk.util import bigrams, trigrams, ngrams

sentence = "There are millions of gorgeous lines of prose."
tokens = nltk.word_tokenize(sentence)

bigrams = list(bigrams(tokens))
trigrams = list(trigrams(tokens))
n_four = list(ngrams(tokens, 4))
print(n_four)

tagged_bigrams = [nltk.pos_tag(bigram) for bigram in bigrams]
including = ['NN', 'JJ', 'VB']


def check(bigram):
    for _, cl in bigram:
        result = False
        for cls in including:
            if cls in cl:
                result = True
        if not result:
            return result
    return True


final = [bigram for bigram in tagged_bigrams if check(bigram)]
print(final)