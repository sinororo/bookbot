def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

def count_words(path):
    with open(path) as f:
        # reads the file
        file_contents = f.read()
    # counts the words in a file
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")



# get_book_text("./books/frankenstein.txt")
count_words("./books/frankenstein.txt")

