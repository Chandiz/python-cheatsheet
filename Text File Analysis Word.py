##############  Text File Analysis – Word Counts ###############

##############  Count Words, Lines, Characters  ################

def text_analysis(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # counts
    lines = text.splitlines()
    words = text.split()
    chars = list(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(chars))

# Example
text_analysis("sample.txt")


#################  Frequency of Each Word  ####################

from collections import Counter
import re

def word_frequency(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    # remove punctuation, keep words only
    words = re.findall(r"\b\w+\b", text)

    freq = Counter(words)

    # Top 10 words
    for word, count in freq.most_common(10):
        print(word, ":", count)

# Example
word_frequency("sample.txt")


#######################  Save Word Counts to CSV  #####################

import csv
from collections import Counter
import re

def word_counts_to_csv(filename, output_csv):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r"\b\w+\b", text)
    freq = Counter(words)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        writer.writerows(freq.items())

# Example
word_counts_to_csv("sample.txt", "word_counts.csv")
