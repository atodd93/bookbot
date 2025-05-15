from stats import get_num_words, char_instances, kv_instances

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    filepath = 'books/frankenstein.txt'
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