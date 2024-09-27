# Step 1: Read the file: Use the open() function to open the text file in read mode.
# Read Lines
with open('example_text.txt', 'r') as f:
    text = f.readlines()
    print(text) # returns a list
    print(f.name) # file name
    print(f.mode) # mode (write/read)
    print(f.closed) # is closed?

print(f.closed)

# Step 2: Clean the text: Remove punctuation, convert text to lowercase, and split the text into words.
# Clean File
import string

def clean_text_file(input_filepath, output_filepath):
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile, open(output_filepath, 'w', encoding='utf-8') as outfile:
            for line in infile: # Line is built into the for statement, so I didn't have to define it.
                no_punct = line.translate(str.maketrans('','',string.punctuation)) # Remove punctuation.
                cleaned_line = ' '.join(no_punct.lower().split()) # Make lowercase and remove extra whitespace.
                outfile.write(cleaned_line + '\n') # Write the cleaned line to the outfile on a new line.
    except FileNotFoundError:
        print(f"Error: File not found - '{input_filepath}'")
    except PermissionError:
        print(f"Error: Permission deined for '{input_filepath}' or '{output_filepath}'")
    except Exception as e:
        print(f"An error occurred: {e}")
# The errors are built in, so I didn't have to define them.

clean_text_file('example_text.txt', 'example_text_clean.txt')


# Step 3: Count word frequencies: Create a dictionary to store word frequencies. Iterate through the words, updating the dictionary accordingly.
def count_word_frequencies(filepath):
    word_counts = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()  # Split line into words, remove leading/trailing whitespace
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        return word_counts
    except FileNotFoundError:
        print(f"Error: File not found - '{filepath}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

result = count_word_frequencies('example_text_clean.txt')


# Step 4: Find the top 10 most frequent words: Use the sorted() function with a custom key to sort the dictionary items by frequency in descending order.
if result:
    sorted_word_counts = sorted(result.items(), key=lambda item: item[1], reverse=True) # If I do [0], it sorts alphabetically, but if I do [1], it sorts numerically.
    print(sorted_word_counts)

# Sorted() works like (iterable(required), key, reverse(optional))
# Key argument takes a function that is applied to each item in the iterable before the comparison happens.


# Nested functions:
def count_word_frequencies(filepath):
    word_counts = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()  # Split line into words, remove leading/trailing whitespace
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        def find_top_5_words(word_counts):
            from collections import Counter
            top_5_words = Counter(word_counts).most_common(5)
            return top_5_words
        top_words = find_top_5_words(word_counts)
        return word_counts, top_words
    except FileNotFoundError:
        print(f"Error: File not found - '{filepath}'")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

wordCounts, topWords = count_word_frequencies('example_text_clean.txt') # In this case, wordCounts is a dictionary, and topWords is a list of tuples. 
# If I were to only assign one variable to count_word_frequencies('example_text_clean.txt'), then it would be a tuple with a dictionary, and then a list of tuples. Like this: ({'one': 1, 'two": 2}, [(one, 1),(two, 2)])

if wordCounts:
    print("\nAll word counts:")
    for word, count in wordCounts.items(): # wordCounts.items() produces an iterable (a view object) that yields tuples of (word,count) - and this works because wordCounts is a dictionary
        print(f"{word}: {count}")
    print("\nTop 5 words:")
    for word, count in topWords: # You don't have to iterate through items here because topWords is a list of tuples.
        print(f"{word}: {count}")