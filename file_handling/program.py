def format_text_file(file):
    FILE = open(file, "r+", encoding="utf8")
    text = file.read()

    index = text.find("CHAPTER I.\n")
    text[index:]

    index = text.find("THE END \n")
    text[:index]

    FILE.close()

def add_to_res_file(num_of_lines, num_of_chars):
    file = open("results.txt", "w")
    
    file.write("Number of lines: ")
    file.write(str(num_of_lines))
    file.write("\n")

    file.write("Number of characters: ")
    file.write(str(num_of_chars))
    file.write("\n")
    

def find_num_of_lines(file):
    num_of_lines = 0

    FILE = open(file, "r", encoding="utf8")
    for line in FILE:
        num_of_lines = num_of_lines + 1
    FILE.close()

    print("Number of lines: ", num_of_lines)
    return num_of_lines


def find_num_of_chars(file):
    num_of_chars = 0

    FILE = open(file, "r", encoding="utf8")
    text = FILE.read()
    num_of_chars = len(text)
    FILE.close()

    print("Number of chars: ", num_of_chars)
    return num_of_chars


num_of_lines = find_num_of_lines("text.txt")
num_of_chars = find_num_of_chars("text.txt")
add_to_res_file(num_of_lines, num_of_chars)