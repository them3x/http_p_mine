class wordlist:

	def __init__(self):
		None

	def organize(self, wordlist):
		try:
			file = open(wordlist)
		except:
			print "File [ "+str(wordlist)+" ] not found"
			exit(0)

		list = set()

		for word in file.readlines():
			list.add(str(word.replace('\n', '')))

		return list
