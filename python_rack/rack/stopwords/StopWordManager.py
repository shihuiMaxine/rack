
import traceback
import sys
import os
sys.path.insert(0, '/Users/gaoshihui/only_rack/rack-py/rack/utility/')
sys.path.insert(0,'/Users/gaoshihui/only_rack/rack-py/rack/config')
os.system("python /Users/gaoshihui/only_rack/rack-py/rack/config")
from config import StaticData

class StopWordManager:

    def __init__(self):
        self.stopList = []

        self.stopDir = "/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/pp-data/stop-words-english-total.txt"
        self.javaKeywordFile = "/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/pp-data/java-keywords.txt"
        self.CppKeywordFile = "/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/pp-data/cpp-keywords.txt"

        self.loadStopWords()

    def loadStopWords(self):
        try:
            f = open(self.stopDir, "r")
            lines = f.readlines()
            for line in lines:
                word = line.strip()
                self.stopList.append(word)
            f.close()

        except Exception:
            traceback.print_exception(*sys.exc_info())

    def removeSpecialChars(self, sentence):
        regex = " "
        parts = sentence.split(regex)
        refined = ""
        for str in parts:
            refined += str.strip() + " "
        return refined

    def removeTinyTerms(self, sentence):
        regex = " "
        parts = sentence.split(regex)
        refined = ""
        for str in parts:
            if (len(str) >= 3):
                refined += str.strip() + " "
        return refined

    def getRefinedSentence(self, sentence):
        refined = ""
        temp = StopWordManager.removeSpecialChars(self, sentence)
        tokens = temp.split(" ")
        for token in tokens:
            if token.lower() in self.stopList:
                refined += token + " "
        return refined.strip()

    def getRefinedList(self, words):
        refined = []
        for word in words:
            if word.lower() in self.stopList:
                refined.append(word)
        return refined

    def getRefinedList(self, words):
        refined = dict()
        for word in words:
            if word.lower() in self.stopList:
                refined.add(word)
        return refined

def main():
    queryTerms = []

    manager = StopWordManager()
    str = "statement protected java Boolean lang expression Quick Invert operator omits AdvancedQuickAssistProcessor"

    print(manager.getRefinedSentence(str))


if __name__ == "__main__":
    main()
