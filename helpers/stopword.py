# check if a word is a stop word or not

class StopWord:

	def __init__(self):

		words = open('../data/stop_word_list')
		self.stopWords = ''

		for w in words:
			self.stopWords += w[:-1] + ' '

		words.close()

		self.stopWords = self.stopWords[:-1]

	def isStopWord(self, word):

		return self.stopWords.find(word) >= 0 