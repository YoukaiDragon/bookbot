def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    print_report(book_path, word_count, dict_to_list(char_counts))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    lowered_text = text.lower()
    char_counts = dict()

    for c in lowered_text:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    dict_list = list()
    for k in dict:
        dict_list.append({"char": k, "count": dict[k]})
    return dict_list

def print_report(book, word_count, char_count):

    char_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    for c in char_count:
        if c["char"].isalpha():
            print(f"The {c['char']} character was found {c['count']} times")
    print("--- End report ---")
    return

main()