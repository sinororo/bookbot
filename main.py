from stats import count_words
from stats import sort_count_chars

print("============ BOOKBOT ============\n" \
"Analyzing book found at books/frankenstein.txt...\n"
"----------- Word Count ----------")

count_words("./books/frankenstein.txt")

print("--------- Character Count -------")

sort_count_chars("./books/frankenstein.txt")

print("============= END ===============")