def read_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    # count the number of words in the text
    words = text.split()
    return len(words)

def character_count(text):
    # count the number of characters in the text
    char_dict = {}
    for c in text:
        if c.isalpha():
            lower_c = c.lower()
            if lower_c not in char_dict:
                char_dict[lower_c] = 1
            else:
                char_dict[lower_c] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def character_dict_list(char_dict):
    # sort the dictionary by number of times each character appears
    char_list = []
    print(char_dict)
    for key in char_dict:
        char_list.append({"char": key, "num": char_dict[key]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def main():
    # read frankenstein book into memory and then print the contents
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    #print(text)
    print(f"Book contains {word_count(text)} words.")

    character_list = character_dict_list(character_count(text))

    for c in character_list:
        print(c)
        #print(f"The character '{c["char"]}' appears {c["num"]} times.")

if __name__ == "__main__":
    main()

