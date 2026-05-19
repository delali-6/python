#This is a program that counts how many times a word appears in a given paragraph regardless of whether its uppercase or lowercase. 
# The user will be prompted to enter a paragraph and a word to search for. The program
#  will then count how many times the word appears in the paragraph and display the result to the user.
paragraph = input("Enter a paragraph: ")
word = input("Enter a word to search for: ")
l_paragraph = paragraph.lower()
word_count = l_paragraph.count(word.lower())
print(f"The word '{word}' appears {word_count} times in the paragraph.")

#This program will count the frequency of each word in a given paragraph 
# and display five of the most common words along with their frequencies. 
# The user will be prompted to enter a paragraph, and the program will process the text 
# to determine the frequency of each word. The results will be displayed in a clear and 
# concise manner, allowing the user to easily identify the most frequently used words in their paragraph.
from collections import Counter
paragraph = input("Enter a paragraph: ")
# Split the paragraph into words and count the frequency of each word
word_counts = Counter(paragraph.split())
# Get the five most common words and their frequencies
most_common_words = word_counts.most_common(5)
for word, count in most_common_words:
    print(f"The word '{word}' appears {count} times in the paragraph.")