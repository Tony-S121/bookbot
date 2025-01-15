def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_characters(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered not in char_dict.keys():
            char_dict[lowered] = 1
        else:
            char_dict[lowered] += 1

    return char_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    char_count = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


main()