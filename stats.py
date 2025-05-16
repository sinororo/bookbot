def count_words(path):
    with open(path) as f:
        # reads the file
        file_contents = f.read()
    # counts the words in a file
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")

# def count_chars(path):

#     with open(path) as f:
#     # reads the file
#         file_contents = f.read()

#     file_contents= file_contents.lower()
#     characters_dict = {}

#     for char in file_contents:
#         if char in characters_dict:
#             characters_dict[char] += 1
#         else:
#             characters_dict[char] = 1
#     print(characters_dict)

def sort_count_chars(path):

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
    
    dictionary_list = []

    for key,value in characters_dict.items():
        my_dict = {"char":key, "num":value}
        dictionary_list.append(my_dict)
    
    def sort_on(dict):
        return dict["num"]
    
    dictionary_list.sort(reverse=True, key=sort_on)
    # print(dictionary_list)

    for dict in dictionary_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")

    





        
