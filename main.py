from stats import get_num_words
import sys

def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_letter_count(text)
    sorted = get_sorted(letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("--- End report ---")
    
def sort_on(d):
    return d["num"]

def get_sorted(letters):
    sorted_list = []
    for ch in letters:
        sorted_list.append({"char": ch, "num": letters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letter_count(text):
    lower_case = text.lower()
    letters={}
    for letter in lower_case:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
        
    return(letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
