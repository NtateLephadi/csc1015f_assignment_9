def is_anagram(word, another_word):
    word = list(tuple(word))
    word.sort()
    another_word = list(tuple(another_word))
    another_word.sort()
    return word == another_word

def main():
    words = []
    new_words = []
    anagrams = []    
    print("***** Anagram Finder *****")
    word = input("Enter a word: ")
    try:
        file = open("EnglishWords.txt")
        for line in file:
            if line == "START\n":
                words = file.readlines()
                break
        for text in words:
            text = text[:-1]
            new_words.append(text)   
            
        for text in new_words:
            if is_anagram(word, text) and text != word:
                anagrams.append(text)        
    except FileNotFoundError as err:
        print("Sorry, could not find file 'EnglishWords.txt'.")
    else:
        if len(anagrams) == 0:
            print("Sorry, anagrams of '" + word + "' could not be found.")
            file.close()                        
        file.close()        
        print(str(anagrams))
    
if __name__ == "__main__":
    main()