def is_anagram(word, another_word):
	word = list(tuple(word))
	word.sort()
	another_word = list(tuple(another_word))
	another_word.sort()
	return word == another_word

def is_length(word, length_of_word):
	return len(word) == length_of_word

def main():
	words = []
	new_words = []
	anagrams = []   
	anagramsets = []
	print("***** Anagram Set Search *****")
	length_of_words = input("Enter word length:\n")
	print("Searching...")
	filename = input("Enter file name: \n")
	print("Writing results...")
	try:
		file = open("EnglishWords.txt")
		for line in file:
			if line == "START\n":
				words = file.readlines()
				break
		for text in words:
			text = text[:-1]
			new_words.append(text)   

		for i in range(len(new_words)):
			for j in range(len(new_words)):
				if is_length(new_words[i], length_of_words) and is_anagram(new_words[i], new_words[j]) and new_words[i] != new_words[j]:
					anagrams.append(text)
			anagrams.clear()
			if len(anagrams) > 0:
				anagramsets.append(anagrams)
		file.close()
	except FileNotFoundError as err:
		print("Sorry, could not find file 'EnglishWords.txt'.")
	else:
		file = open(filename, "w")
		anagramsets.sort()
		for i in anagramsets:
			print(str(i), file=file)
		file.close()
		print("Done...")
if __name__ == "__main__":
	main()