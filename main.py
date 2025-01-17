import numpy as np
from collections import defaultdict

# Step 1: Load the corpus from a text file
def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Step 2: Define the file path for the corpus
file_path = 'text.txt'
corpus = load_corpus(file_path)

# Step 3: Tokenize the corpus (split into words)
words = corpus.lower().split()

# Step 4: Create a bigram model using a dictionary
# Create a mapping of unique words to indices
unique_words = list(set(words))
word_to_index = {word: idx for idx, word in enumerate(unique_words)}
index_to_word = {idx: word for word, idx in word_to_index.items()}

# Initialize a bigram dictionary
bigram_dict = defaultdict(lambda: defaultdict(int))

# Populate the dictionary
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    bigram_dict[current_word][next_word] += 1

# Step 5: Define a function to generate text based on the bigram model
def generate_sentence(start_word, length=100):
    if start_word.lower() not in bigram_dict:
        return "The starting word is not in the corpus."

    current_word = start_word.lower()
    sentence = [current_word]

    for _ in range(length - 1):
        next_word_candidates = bigram_dict[current_word]
        if not next_word_candidates:
            break  # No further prediction possible

        # Convert candidate word counts into probabilities
        total_count = sum(next_word_candidates.values())
        next_word_probs = [count / total_count for count in next_word_candidates.values()]
        next_word = np.random.choice(
            list(next_word_candidates.keys()), p=next_word_probs
        )

        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence).capitalize() + '.'

# Step 6: Generate a sentence
while True:
    start_word = input('What will the starting word be? ')
    generated_sentence = generate_sentence(start_word)
    print(generated_sentence)
