def count_words(path):
    with open(path) as f:
        # reads the file
        file_contents = f.read()
    # counts the words in a file
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")


# def full_character_count(path):
#     with open(path) as f:
#         # reads the file
#         file_contents = f.read()
    
#     full_text = file_contents.lower()
#     characters_dict = {}
    
#     # print(words)
#     for char in full_text:
#         # print(len(char))
#         characters_dict[char] += len(char)
    
#     return characters_dict

def count_chars(path):

    with open(path) as f:
    # reads the file
        file_contents = f.read()

    file_contents= file_contents.lower()
    characters_dict = {}

    for char in file_contents:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    print(characters_dict)
        
