# https://www.hackerrank.com/challenges/words-score/problem

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    
    for word in words:
        num_vowels = len([x for x in word if is_vowel(x)])
        score += 2 if num_vowels % 2 == 0 else 1
        
    return score