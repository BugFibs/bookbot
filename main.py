def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_words(text)
    char_dict = get_char_dict(text)
    sorted_list = get_alpha_list(char_dict)
    # print(text)
    print("---Begin report of books/frankenstein.txt")
    print(f"{num_words} words found in the document.")
    # print(char_dict)
    # print(sorted_list)

    for item in sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")

def get_number_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict 

def sort_on(d):
    return d['num']

def get_alpha_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({'char': char, 'num': char_dict[char] })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

