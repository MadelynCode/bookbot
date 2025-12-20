import sys
from stats import num_words, count_char



# gets the text of a book file as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    
    book = get_book_text(path)
    amount = num_words(book)
    # print(f"Found {amount} total words")
    CharacterCount = count_char(book)
    # print(CharacterCount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {amount} total words")
    print("--------- Character Count -------")
    for Char in CharacterCount:
        print(f"{Char}: {CharacterCount[Char]}")
    print("============= END ===============")

main()
