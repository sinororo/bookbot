import sys

from stats import count_words
from stats import sort_count_chars


def main():
    
    #check if cli argument was provided:

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============\n" \
    "Analyzing book found at {path}\n"
    "----------- Word Count ----------")

    count_words(path)

    print("--------- Character Count -------")

    sort_count_chars(path)

    print("============= END ===============")


if __name__== "__main__":
    main()

