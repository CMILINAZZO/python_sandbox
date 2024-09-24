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
# Step 4: Find the top 10 most frequent words: Use the sorted() function with a custom key to sort the dictionary items by frequency in descending order.
# Print the results: Print the top 10 words and their frequencies.
