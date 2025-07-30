import sys
from stats import count_words
from stats import count_chars
from stats import sorted_dicts

print("Usage: python3 main.py <path_to_book>")

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    print(f"""============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found {word_count} total words
        --------- Character Count -------""")
    sorted_chars = sorted_dicts(char_count)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"{char}: {num}")
    print(f"============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
