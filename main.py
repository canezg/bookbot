def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    report = get_report(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']}' times")

    print ("--- End report ---")

def get_report(char_dict):
    sort_list = []
    for ch in char_dict:
        sort_list.append({"char": ch, "num": char_dict[ch]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def sort_on(c):
    return c["num"]


def get_char_dict(text):
    num_char = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in num_char:
            num_char[char] += 1
        else: 
            num_char[char] = 1
    return num_char

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()