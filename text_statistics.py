# Header Comments Go Here TODO

from sys import argv
script_name, file_name = argv

#open the file and store by line
text_file = open(file_name, 'r')
lines = text_file.readlines()

#create a list of unformatted words, ie remove trailing punctuation and newlines
words = [w.strip(',:;.\n').lower() for line in lines for w in line.split(' ')]
words = [w for w in words[:] if w != ''] #remove possibly empty words

#create a dictionary containing word:frequency pairs 
word_freq = {}
for word in words :
    word_freq[word] = words.count(word)

#print word, frequency 2-tuples sorted from highest frequency to lowest
for w in sorted(word_freq, key = word_freq.get, reverse = True) :
    print (w, word_freq[w])





