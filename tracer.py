def main():
	print("***** Program Trace Utility *****")
	filename = input("Enter the name of the program file: ")
	words = []
	new_words = []
	traced = False
	try:
		file = open(filename)
		for line in file:
			if '""" DEBUG """' in line:
				words = file.readlines()
				traced = True
				break
			else:
				words = file.readlines()
				traced = False
				break
		if traced == False:
			words = ['""" DEBUG """\n'] + words
			for i in range(len(words)):
				if "def" in words[i]:
					method_name = words[i][4:words[i].find("(") - 1]
					words[i] = words[i] + "\t\"\"\" DEBUG \"\"\";print('" + method_name + "')\n"
			file.close()
			file = open(filename, mode='w')
			for i in words:
				print(i, file=file, end="")
			file.close()
			print("Inserting...Done")
		else:
			for i in range(len(words)):
				if "DEBUG" in words[i]:
					words[i] = ""
			file.close()
			file = open(filename, mode='w')
			for i in words:
				print(i, file=file, end="")
			file.close()
			print("Removing...Done")
	except FileNotFoundError as err:
		print(err)

if __name__ == "__main__":
	main()
	