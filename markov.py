"""Generate Markov text from text files."""

from random import choice
from sys import argv

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    
    with open(file_path) as file: 
        text = file.read()
        text = text.rstrip("\n")

    return text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:{('Would', 'you'): 0}


        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for i in range(len(words) - n):

        chain_key_lst = []
        counter = 0
        while counter < n:
            chain_key_lst.append(words[i + counter])
            counter += 1

        chain_value = (words[i + n])
        chain_key = tuple(chain_key_lst)

        if chain_key not in chains:
            chains[chain_key] = [chain_value]   # Adding key-value pair
        else:
            chains[chain_key] += [chain_value]  # Updating existing key with additional value

    return chains


def make_text(chains, n):
    """Return text from chains."""

    # Create initial key
    key = choice(list(chains.keys()))   # Pick random key from the list of keys
    #print("=== Initial key:\t", key)
    
    # Get initial word
    value = choice(chains[key])         # Based on 'key', pick random value from list of values associated with 'key'
    #print("=== Initial value:\t", value)
    
    # List of initial words (initial key and value)
    words = list(key)                   # The initial key will always be the first n-words in the sentence
                                        # So, initially, 'words' will be a list of 'key'
    #print("=== Initial words:\t", words)
    
    while True:
        # Add word to words
        words.append(value)    # For the first loop, 'value' is assigned in line 80, or the initial word

        # Get next key
        key = [key[i] for i in range(1,n)]
        #print("--- New key (pre-tuple and value):\t", key)
        
        key = tuple(key + [value])
        #print("+++ New key (post-tuple and value:\t", key)

        # Get new word
        try:
            value = choice(chains[key])

        except KeyError:                # When we reach ('I', 'am?')
            break

    return " ".join(words)


# Call text file in terminal instead
input_path = argv[1]

# n of n-grams
n = 3

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print(random_text)
