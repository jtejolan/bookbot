from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
    
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    text = get_book_text(path)
    num_words = count_words(text)
    chars = count_characters(text)
    sorteds = sort_dict(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorteds:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

    
main()