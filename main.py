from stats import get_num_words, get_num_chars, sort_num_chars
import sys

def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()

    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book = get_book_text(path)

    num_words = get_num_words(book)

    #print(f"{num_words} words found in the document")

    num_chars = get_num_chars(book)
    #print(num_chars)

    sorted_dc = sort_num_chars(num_chars)

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    """)
    
    for c in sorted_dc:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['count']}")
    
    print("============= END ===============")


main()