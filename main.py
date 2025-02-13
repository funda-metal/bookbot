#def main():
    #with open("books/frankenstein.txt") as f:
     #   file_contents = f.read()
     #   words = file_contents.split()
     #   print(f"{len(words)}")


#main()

def dict_sort(dict):
    return dict["num"]

def main():
    char_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowercase = file_contents.lower()
        chars = list(lowercase)
        for char in chars:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict
        
main()

def sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"letter": char, "number": count})
    sorted_list = char_list.sort(key=)
    print(sorted_list)

sort(main())