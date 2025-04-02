"""# import from stats.py
from stats import count_words, count_character, sort_character_no_spaces

# function to get book text using a filepath as input and returns the contens of the file as a string
def get_book_text(filepath):
    with open(filepath, "r") as f:
        book_text = f.read()
    return book_text

# filepath count_words
def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    character_count = count_character(book_text)
    sorted_count = sort_character_no_spaces(character_count)
    print(f"{num_words} words found in the document") 
    print(f"Sorted character count: {sorted_count}")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # print sorted character count with its count
    for char, count in sorted_count.items():
        print(f"{char}: {count}")
        
    print("============= END ===============")
    
main()"""

# import sys
import sys
from stats import count_words, count_character, sort_character_no_spaces
# function to get book text using a filepath as input and returns the contens of the file as a string
def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()
    
def main():
    # check if file path is passed as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath} not found")
        sys.exit(1)
    
    # count words and characters
    num_words = count_words(book_text)
    character_count = count_character(book_text)
    sorted_count = sort_character_no_spaces(character_count)
    
    
    # print results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print sorted character count with its count
    for char, count in sorted_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()