'''Write a program, wordcount.py, that opens a file, and counts how many times each space-separated word occurs in that file. Your program should then print those counts to the screen. 
 python wordcount.py
  seven 4
  Kits, 1
  sack 1 '''
from string import punctuation, whitespace
from sys import argv
from collections import Counter

def count_words():
    '''Count how many times each space-separated word occurs in the file. Convert to lowercase and strip punctuation for consistency. '''
    '''for key, value in my_dict.items():
    print "key = %r, value = %r" % (key, value)'''

    script_name, filename = argv
    word_dict = Counter()

    with open(filename) as my_file:
        for line in my_file:
            word_list = line.split(' ')
            for word in word_list:
                if word != ('' or '\n'):
                    word = word.lower()
                    word = word.strip(whitespace)
                    word = word.strip(punctuation)
                    #if word isn't in dictionary, add word as key to dictionary. Increase value by one regardless
                    # word_count = word_dict.get(word, 0) + 1
                    # word_dict[word] = word_count
                    word_dict[word]+=1
        #print dictionary of words and values with nice format
        for word_key, count in word_dict.iteritems():
            print word_key, count

    print word_dict

count_words()

#count_words("test.txt") 
#count_words("twain.txt")



