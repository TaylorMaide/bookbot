def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    print_report(num_words, chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path)as f:
        return f.read()

def get_char_count(text):
    char_counts = {}
    lowered = text.lower()
    count = 0
    for char in lowered:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def print_report(word_count, character_count):
    print("--- Begin report of book/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    sorted_char = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def sort_on(dict):
    return dict[0]

main()
