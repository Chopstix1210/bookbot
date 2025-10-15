from stats import get_book_text, get_char_count, get_num_words, get_sorted_char_dict
import sys


def main():
    try: 
        filepath = sys.argv[1]

        num_words = get_num_words(filepath)
        char_dict = get_char_count(get_book_text(filepath))
        sorted_char_dict = get_sorted_char_dict(char_dict)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        for item in sorted_char_dict:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

    except IndexError as e:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    


main()
