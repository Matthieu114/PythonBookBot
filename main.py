def count_words(text : str) -> int :
    if not isinstance(text,str):
        raise TypeError("only string arguments are allowed")  
    return len(text.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_count = count_words(file_contents)

main()