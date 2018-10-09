"""Generate Markov text from text files."""

from random import choice


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


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        chain_key = (words[i], words[i +1])
        chain_value = (words[i+2])

        if chain_key not in chains:
            chains[chain_key] = [chain_value]
        else:
            chains[chain_key] += [chain_value]

    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))  # choice(list(chains.keys())) = ('could', 'you')
    value = choice(chains[key])        # chains[key] = ['in', 'in', 'with', 'with']
    words = [key[0], key[1], value]    # Initial line = ['could', 'you', 'in']

    # your code goes here

    # Loop of something
    while True:
        key = (key[1], value)          # ('you', 'in')

        try:
            value = choice(chains[key]) # chains[key] = ['a', 'a']
            words.append(value)
        except KeyError:                # When we reach ('I', 'am?')
            break
            
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print(make_text(chains))
# Produce random text
#random_text = make_text(chains)

#print(random_text)
