def main():

    book_path = "books/frankenstein.txt"
    book_report(book_path)


def word_count(book_contents):
   return (len(book_contents.split()))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_and_counts(book_contents):
    chars_and_counts = {}
    for char in book_contents.lower():
        if char in chars_and_counts:
            chars_and_counts[char] += 1
        elif char not in chars_and_counts:
            chars_and_counts[char]=1

    return chars_and_counts

def book_report(book_path):
    print(f"--- begin report of {book_path} ---")

    text = get_book_text(book_path)

    print(f"{word_count(text)} words found")
    char_counts = get_chars_and_counts(text)
    sorted_chars = dict(sorted(char_counts.items(),key=lambda item: item[1], reverse=True))

    print(sorted_chars)
    for key,value in sorted_chars.items():
        if key.isalpha():
            print(f"letter {key} appears {value} times")
    print("--- end of report ---")


main()

