import re
import string

from core import StopWordRemover
from core import TokenStemmer
from stopwords import StopWordManager
from utility import MiscUtility


class TextNormalizer:
    content="// This is a comment - need to be removed" \
               "/* This is a also a comment *"
    def __init__(self,content):
        self.content = content



    def normalizeSimple(self):
        punc = '''\n'''
        content_str = self.content.translate(str.maketrans('', '', string.punctuation))
        content_str=  re.sub(punc, " ", content_str)
        words = self.content.translate(str.maketrans('', '', string.punctuation)).split(" ")
        wordList =[]
        wordList.extend(list(words))
        return MiscUtility.list2Str(wordList)

    def normalizeSimpleCodeDiscardSmall(self) :
        words = self.content.translate(str.maketrans('', '', string.punctuation)).split(" ")
        wordList =[]
        wordList.extend(list(words))
        codeItems = self.extractCodeItem(wordList)
        for i in codeItems:
            wordList.append(i)
        wordList = self.discardSmallTokens(wordList)
        modified = MiscUtility.list2Str(wordList)
        stopManager=StopWordRemover()
        self.content = stopManager.getRefinedSentence(modified)
        return self.content

    def normalizeSimpleCode(self):
        words =  self.content.translate(str.maketrans('', '', string.punctuation)).split(" ")
        # wordList =[]
        wordList=words
        codeOnly =[]
        codeOnly = self.extractCodeItem(wordList)
        for i in codeOnly:
            wordList.append(i)
        return MiscUtility.list2Str(wordList)

    def discardSmallTokens(items):
        temp =[]
        for item in items:
            if(len(item)>2):
                temp.append(item)
        return temp

    def normalizeText(self):
        words = self.content.translate(str.maketrans('', '', string.punctuation)).split(" ")
        wordList = []
        wordList.extend(list(words))
        wordList = self.discardSmallTokens(wordList)
        modifiedContent = MiscUtility.list2Str(wordList)
        stopManager = StopWordManager()
        refined =[]
        refined =stopManager.getRefinedList(wordList)
        temp =[]
        temp = TokenStemmer.performStemming(refined)
        return MiscUtility.list2Str(temp)

    def normalizeTextLight(self):
        words =  self.content.translate(str.maketrans('', '', string.punctuation)).split(" ")
        wordList = []
        wordList.extend(list(words))
        wordList = self.discardSmallTokens(wordList)
        modifiedContent = MiscUtility.list2Str(wordList)
        return modifiedContent

    def extractCodeItem(self,words):
        codeTokens =[]
        for token in words:
            if len(self.decomposeCamelCase(token)>1):
                codeTokens.append(token)

        return codeTokens

    def decomposeCamelCase(self,token):
        camRegex = "([a-z])([A-Z]+)"

        refined = re.sub(camRegex, "\\1 \\2", token).split(" ")
        #ftokens = re.split("\\s+",ftokens)

        return refined

    def decomposeCamelCaseList(self,tokens):
        refined =[]
        # print(tokens)
        for token in tokens:
            # print(token)
            camRegex = "([a-z])([A-Z]+)"
            # replacement = "$1\t$2"
            # for i in token:
                # print(i)
                # if i in  string.ascii_uppercase or i in  string.ascii_lowercase :
            # token = token.replace(i, replacement)
            refined.append(re.sub(camRegex, "\\1 \\2", token).split(" "))

        #     ftokens = token.split(" ")
        #     ftokens_list = list(ftokens)
        # for i in ftokens_list:
        #     refined.append(i)

        return refined



# sr= TextNormalizer()
org_sentence='camelCaseAPPLE'
# sentence=sr.removeStopWords(org_sentence)
# print( TextNormalizer(org_sentence).decomposeCamelCase(org_sentence))