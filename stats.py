def count_words(path):
    with open(path) as f:
        # reads the file
        file_contents = f.read()
    # counts the words in a file
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")