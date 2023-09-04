#This code represents a basic Natural Language Processing (NLP) model for generating text based on statistical analysis 
#of trigrams (sequences of three words) from a given text corpus, such as news articles like Reuters.

#The code starts by downloading the Reuters document corpus and initializing some necessary libraries and data structures.

import nltk

nltk.download('reuters')
nltk.download('punkt')

print("downloaded reuters corpus documents for making statistic based basic lang model....")

from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

#Create a statistical language model using trigrams, where it counts the occurrences of the third word given first two words for each trigrams
#These counts of occurences are then converted into probablity given all possible third word that are coming for the first two words of the trigrams. The higehst probable ocuurence word is
#being picked-up for the auto suggested next word

# model{"word1, word2": dic2}
#dic2{"word3": 1, "word4": 2, "word5": 3}
# Let's say model is being asked the next word given, "this is" so the answer is Max(stat_basic_lang_model["this, is"][prob of each possible next words]) = word5

stat_basic_lang_model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in reuters.sents():
	for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
		stat_basic_lang_model[(w1, w2)][w3] += 1

#['being', 'placed']['for'] = ('being', 'placed')['for']/sum(['being', 'placed'])

#The code then transforms the counts into probabilities for each possible third word given the first two words.

for w1_w2 in stat_basic_lang_model:
   total_count = float(sum(stat_basic_lang_model[w1_w2].values()))
   for w3 in stat_basic_lang_model[w1_w2]:
       stat_basic_lang_model[w1_w2][w3] = stat_basic_lang_model[w1_w2][w3]/total_count

#It generates text by starting with two initial words ("today" and "the") and iteratively selecting the next word based on the highest probability of occurrence in the trigrams model. This process continues until a sentence-ending condition is met.

# starting words
text = ["today", "the"]
sentence_finished = False
next_word = None

if tuple(text[-2:]) not in stat_basic_lang_model:
  print("Sorry I am not trained to answer... terminated...")
else:
  while not sentence_finished:
    max_prob_prev = .0
    for word in stat_basic_lang_model[tuple(text[-2:])].keys():
      max_prob_curr = stat_basic_lang_model[tuple(text[-2:])][word]
			# select words that are above the probability threshold
      if max_prob_curr >= max_prob_prev:
        max_prob_prev = max_prob_curr
        next_word = word
        break
    
    text.append(next_word)
    next_word = None
  
    if text[-2:] == [None, None]:
      sentence_finished = True

#The generated text is printed as the output.
print (' '.join([word for word in text if word]))