def count_word_occurrences(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
import word_count
print(word_count.count_word_occurrences(['apple', 'banana', 'apple', 'orange'])) # Output: {'apple': 2, 'banana': 1, 'orange': 1}