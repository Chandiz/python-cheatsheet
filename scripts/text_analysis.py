#!/usr/bin/env python3
"""
Text analysis: lines, words, chars, top N word frequency.
Usage:
  python scripts/text_analysis.py file.txt
  python scripts/text_analysis.py file.txt --top 20
  python scripts/text_analysis.py file.txt --csv word_counts.csv
"""
import argparse
import re
from collections import Counter
import csv

def analyze(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()
    words = re.findall(r"\b\w+\b", text.lower())
    chars = list(text)
    return {
        'lines': len(lines),
        'words': len(words),
        'characters': len(chars),
        'freq': Counter(words)
    }

def write_csv(output, counter):
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['word','count'])
        for w, c in counter.most_common():
            writer.writerow([w, c])

def main():
    p = argparse.ArgumentParser()
    p.add_argument('file')
    p.add_argument('--top', type=int, default=10, help='top N words to show')
    p.add_argument('--csv', help='output csv file for word counts')
    args = p.parse_args()

    res = analyze(args.file)
    print(f"Lines: {res['lines']}")
    print(f"Words: {res['words']}")
    print(f"Characters: {res['characters']}")
    print(f"Top {args.top} words:")
    for w, c in res['freq'].most_common(args.top):
        print(f"{w}: {c}")

    if args.csv:
        write_csv(args.csv, res['freq'])
        print(f"Wrote word counts to {args.csv}")

if __name__ == '__main__':
    main()
