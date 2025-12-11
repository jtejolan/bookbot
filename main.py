from stats import count_words, count_characters, sort_dict

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    chars = count_characters(text)
    sorteds = sort_dict(chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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