
def count(text):
    count = text.split()
    return len(count)


def charCount(text):
    alphabet = {}
    for i in text:
        to_lower = i.lower()
        if to_lower in alphabet:
            alphabet[to_lower] += 1
        else:
            alphabet[to_lower] =1
    return alphabet

def printReport(book, words, countWords):
    print(f""" --- Begin report of {book} ---
    {words} words found in the document """)
    for key, value in countWords.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")
    
def main():
    
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    words = count(file_contents)
    countWords = charCount(file_contents)
    printReport(path_to_file, words, countWords)
main()