def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_dict = count_letters(text)
    report(text, book_path, letter_dict)

def words_num(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count +=1
    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letters_dict = {}
    for letter in text.lower():
        if letter in letters_dict:
            letters_dict[letter] += 1 
        else:
            letters_dict[letter] = 1
    return letters_dict

def report(text, book_path, letters_dict):
    print(f"---------- Report of {book_path}---------- ")
    print(f"the number of words found in {book_path} is {words_num(text)}")
    for letter, count in sorted(letters_dict.items()):
        print(f"The letter '{letter}' was found {count} times.")
    print("---------- End of the report ----------")
      
main()
