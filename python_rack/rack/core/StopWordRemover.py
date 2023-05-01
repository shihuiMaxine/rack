from config import StaticData
from utility.ContentLoader import ContentLoader
import stopwords
import string
import re

class StopWordRemover:
    stopwords =[]
    stopDir = "/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/pp-data/stop-words-english-total.txt"

    def __init__(self):
        pass

    def loadStopWords(self):

        lines =[]

        if len(self.stopwords)==0:
            lines = ContentLoader().getAllLines(self.stopDir)

        for line in lines:
            self.stopwords.append(line.strip())
        return None

    def getRefinedSentence(self, sentence):
        

        refined = ""

        parts = sentence.split(" ")
        temp = self.removeSpecialChars(sentence)


        tokens = []
        tokens = temp.split(" ")
        for token in tokens :
            if token.lower() in self.stopwords:
                continue
            else:
                refined += token + " "
        return refined.strip()
    def removeSpecialChars (self,sentence):
        regex = string.punctuation
        parts=[]
        new_string = re.sub(r'[^\w\s]', '', sentence)
        parts = new_string.split(" ")
        refined=""
        for str in parts:
            refined += str.strip() + " "
        return refined
        
    def removeStopWords (self,tokens):
        self.loadStopWords()
        refined =[]
        for token in tokens:
            if token.lower() in self.stopwords:
                continue
            else:
                refined.append(token)
        return refined





