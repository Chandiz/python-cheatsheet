#!/usr/bin/env python3
"""
Sorting examples. Run to see prints.
"""
def sort_simple():
    nums = [5, 2, 9, 1]
    print("original:", nums)
    nums.sort()
    print("sorted (in-place):", nums)
    nums.sort(reverse=True)
    print("reverse:", nums)

def sort_with_key():
    words = ["banana", "apple", "cherry", "kiwi"]
    print("by length:", sorted(words, key=len))
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    print("sort by age:", sorted(people, key=lambda x: x['age']))

if __name__ == '__main__':
    sort_simple()
    print()
    sort_with_key()
