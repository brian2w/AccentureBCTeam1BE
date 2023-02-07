# nltk converts words into numbers (Which computers can understand) i.e. pre processing

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
## nltk is mainly involved with pre-processing

sentence = "the water is quite heavy today, seems like there will be no more tickets to do"
## stop words -- words you leave and don't analyse i.e. you don't care about them bc they are filler words, or too hard
stop_words = set(stopwords.words("english"))


words = word_tokenize(sentence)
filtered_sentence = []

for w in words: # loops through sentence and adds useful words to filtered sentence
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)




