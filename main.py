#def main():
    #with open("books/frankenstein.txt") as f:
     #   file_contents = f.read()
     #   words = file_contents.split()
     #   print(f"{len(words)}")


#main()

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
    print char_dict
            
        
        
main()

