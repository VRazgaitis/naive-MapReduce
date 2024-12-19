
"""
This script reads a text file, counts the frequency of each word in the file,
and saves the word count as a JSON file.

The program expects text files to be located in the 'titles/' directory 
and outputs the word count data to the 'counts/' directory. The input file is
selected based on an integer passed as a command-line argument (between 1 and 9),
and the file is expected to be named according to the format '<number>.txt'.
For example, if the number '3' is provided, the script will read 'titles/3.txt'.

Usage:
    Run the script by providing a number between 1 and 9 as a command-line argument:
    $ python map.py <i>
    For example:
    $ python map.py 3

    This will read 'titles/3.txt', count the words, and save the result to 'counts/3.json'.
"""
import json
import os
import argparse
from collections import Counter

def count_words(text_file):
    """
    - Reads a text file from the 'titles/' directory.
    - Counts the occurrences of each word in the file, ignoring case.
    - Saves the word count data as a JSON file in the 'counts/' directory.
    """
    # assume that titles.tar.gz has been unzipped into /titles
    filename = f"titles/"+str(text_file)+".txt"
    word_count = Counter()
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            word_count.update(words)
    json_filename = f"counts/"+str(text_file)+".json"
    files = os.listdir()
    # create the counts/ dir if first completed count
    if "counts" not in files:
        os.mkdir('counts')
    # Write the dictionary to a file as JSON
    with open(json_filename, 'w') as json_file:
        json.dump(word_count, json_file, indent=4) 

if __name__ == "__main__":
    # ensure that a number input has been provided 
    parser = argparse.ArgumentParser()
    parser.add_argument('file_number', type=int, choices=range(1, 10), help="A number between 1 and 9")
    args = parser.parse_args()
    count_words(args.file_number)
        