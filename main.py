from stats import get_num_words, char_instances, kv_instances
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f"Found {get_num_words(book_text)} total words")
    print('--------- Character Count -------')
    
    char_dict = kv_instances(book_text)
    for entry in char_dict:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()