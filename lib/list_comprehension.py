#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [a for a in num_list if a % 2 == 0]
    
    return even_nums

print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentence_list):
    exclamation = [ex + '!' for ex in sentence_list]

    return exclamation

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))