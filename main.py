def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(" --- Begin report of books/frankenstein.txt --- ")
    print(f"{num_words} words found in the document")
    print("")
    char_counts = get_num_chars(text)
    char_list = convert_to_list(char_counts)
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    my_string = text
    lowered_string = my_string.lower()
    char_count = {}
    for char in lowered_string:
        if char.isalpha():
            if char in char_count:
                char_count[char] = char_count[char] + 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def convert_to_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
        char_list.sort(reverse=True, key=sort_on)
        
    return char_list


main()


