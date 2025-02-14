#def main():
    #with open("books/frankenstein.txt") as f:
     #   file_contents = f.read()
     #   words = file_contents.split()
     #   print(f"{len(words)}")


#main()

# Takes a dictionary and returns the value of the 'letter' key.

def dict_sort(dict):
    return dict["letter"]

# Opens the ./books/frankenstein.txt file and reads it.
# Returns a dictionary that includes the characters and their number counts.

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
        
# Takes a dictionary and creates a list of smaller dictionaries.
# Sorts the list alphabetically by the value of the key.

def sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"letter": char, "number": count})
    char_list.sort(key=dict_sort)
    for item in char_list:
        if item["letter"].isalpha(): 
            print(f"The '{item["letter"]}' character was found {item["number"]} times")
    
sort(main())