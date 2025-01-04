def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(letters)

def get_letter_count(text):
    lower_case = text.lower()
    letters={}
    for letter in lower_case:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
        
    return(letters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
