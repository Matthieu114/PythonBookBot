from collections import Counter

def count_words(text : str) -> int :
    if not isinstance(text,str):
        raise TypeError("only string arguments are allowed")  
    return len(text.split())


def count_characters(text : str) -> int:
    if not isinstance(text,str):
        raise TypeError("only string arguments are allowed")
    char_count = {}
    concat_text = ''.join(text.lower().split())

    for char in concat_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # can also use the counter function from collections
    # print(Counter(f"{concat_text}\n"))
    return char_count


def read_file(path):
     with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_file(book_path)
    words_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print(f"--- Begin report of {book_path} ---\n")
    print(f"{words_count} found in the document\n")
    for char in char_count:
        print(f"the '{char}' character was found {char_count[char]} times\n")
    print("--- End report ---")

main()