import sys
from stats import get_num_words
from stats import get_char_counter
from stats import sort_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    num_words = get_num_words(sys.argv[1])
    all_chars = get_char_counter(sys.argv[1])
    all_chars = sort_chars(all_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in all_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
