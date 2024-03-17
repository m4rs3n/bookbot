def main():
    path_to_book = "books/frankenstein.txt"
    open_book = read_book(path_to_book)
    dict = letter_count(open_book)
    list = (dict_to_list(dict))

    def sort_on(list_item):
        return list_item[1]


    list.sort(key=sort_on, reverse=True)

    def print_report(path_to_book, list):
        print(f"--- Begin report of {path_to_book} ---")
        print(f"{word_count(open_book)} words found in the document\n")

        for item in list:
            if item[0].isalpha():
                print(f"The '{item[0]}' character was found {item[1]} times")
                
        print("--- End report ---")

    print_report(path_to_book, list)


def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(book):
    words = book.split()
    return len(words)


def letter_count(str):
    lowercase_string = str.lower()
    letters_dict = {}
    for letter in lowercase_string:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict


def dict_to_list(dict):
    input_dict = dict
    resultList = list(input_dict.items())
    return resultList


main()
