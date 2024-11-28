
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


def main():
    
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(count(file_contents))
    print(charCount(file_contents))
main()