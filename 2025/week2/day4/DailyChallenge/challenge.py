import re
import string
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Text:
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return ("{word} not fount")
        return count
    
# t = Text("hello world hello")
# print(t.word_frequency("hello"))

    def most_common_word():
        pass

            






