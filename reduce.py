"""
Aggregates word counts from multiple JSON files, sorts the words by 
frequency descending, and saves the combined word counts into a new JSON file.

Usage:
Run the script in an environment where the /counts directory contains JSON files.
Each JSON file is expected to contain word counts in the format of a dictionary, where 
keys are words (strings) and values are counts (integers).
"""
import json
import os
from collections import defaultdict, OrderedDict

directory = "./counts"
combined_word_count = defaultdict(int)

# Iterate over all the JSON files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)
        # Open and read each JSON file
        with open(file_path, 'r') as file:
            word_counts = json.load(file)
            # Append the current JSON file counts to combined_word_count
            for word, count in word_counts.items():
                # using defaultdict creates a new key when key not present rather than raising KeyError
                combined_word_count[word] += count
# Sort the dictionary by values (word occurence) in descending order
sorted_word_count = OrderedDict(sorted(combined_word_count.items(), key=lambda item: item[1], reverse=True))
# Save the combined word counts to a new JSON file
output_file = os.path.join(directory, "total_counts.json")
with open(output_file, 'w') as outfile:
    json.dump(sorted_word_count, outfile, indent=4)

print(f"Combined word count has been saved to {output_file}")
