
def count(text):
    count = text.split()
    return len(count)






def main():
    
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(count(file_contents))
main()