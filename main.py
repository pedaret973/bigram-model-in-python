import random
import string
#Load the corpus from a text file
def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

#Define the file path for the corpus
file_path = 'text.txt'
corpus = load_corpus(file_path)

#Tokenize the corpus (split into words)
words = corpus.lower().split()

#Create a bigram model (mapping each word to the next word)
bigrams = {}
for i in range(len(words) - 1):
    word, next_word = words[i], words[i + 1]
    if word not in bigrams:
        bigrams[word] = []
    bigrams[word].append(next_word)

#Define a function to generate text based on the bigram model
def generate_sentence(start_word, length=100):
    current_word = start_word.lower()
    sentence = [current_word]
    for _ in range(length - 1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            sentence.append(next_word)
            current_word = next_word
        else:
            break  # No further prediction possible
    return ' '.join(sentence).capitalize() + '.'

#Generate a sentence
while True:
    start_word = input('select a word/letter to start with. ')
    generated_sentence = generate_sentence(start_word)
    print(generated_sentence)
