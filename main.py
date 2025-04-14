import sys
from stats import word_count, char_count, sorted_count
def get_book_text(book_path: str) -> str:
    """Reads the contents of a book file and returns it as a string."""
    with open(book_path) as book_file:
        return book_file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    """Main function to execute the book reading functionality."""
    book_path = sys.argv[1]  # Replace with your book file path
    book_text = get_book_text(book_path)
    book_sorted = sorted_count(book_text) 
    # Here you can add more functionality to process or display the book text
    print(f"========= BookBot =========\n Analyzing {book_path}...\n")
    print(f"------- Word Count --------\n Found {word_count(book_text)} total words.\n")
    print(f"----- Character Count -----\n ")
    for character, count in book_sorted:
        if character.isalpha():
            print(f" {character}: {count}\n")
    print("===========END=============")
main()