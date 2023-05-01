import re
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

class MyTokenizer:
    itemToTokenize = ""


    def __init__(self, item):


        self.itemToTokenize = item

    def tokenize_text_item(self):

        tokenizer = tokenize.tokenizer
        tokenizer.extend(self.itemToTokenize)
        tokens = []
        for i in tokenizer.split():
            token = i
            token.strip()
            if (len(token) != 0):
                smalltokens = self.process_text_item(token)
                for j in smalltokens:
                    token.append(j)
        return tokens

    def tokenize_code_item(self):
        tokens = []
        for i in self.itemToTokenize.split():
            token = i
            token.strip()
            if (len(token) != 0):
                tokenparts = self.process_text_item(token)
                for j in tokenparts:
                    tokens.append(j)
        return tokens

    def refine_insignificant_tokens(self, codeTokens):
        try:
            for token in codeTokens:

                if len(token.strip()) == 1:
                    codeTokens.remove(token)
        except:
            print("An exception occurred")
        return codeTokens

    def remove_code_comment(self, codeFragment):
        modifiedCode = ""
        try:
            pattern = "//.* | (\"(?:\\\\[^\"]|\\\\\"|.)*?\") | (?s)/\\*.*?\\*/"
            pattern = r"//.*"
            modifiedCode = re.sub(pattern, "", codeFragment)
            pattern = r"/\\*.*?\\*/"
            modifiedCode = re.sub(pattern, "", modifiedCode, flags=re.S)
            pattern = r"(\"(?:\\\\[^\"]|\\\\\"|.)*?\")"
            modifiedCode = re.sub(pattern, "", modifiedCode)

        except:
            print("An exception occurred")

        return modifiedCode

    def camel_case_split(self, str):
        camRegex = "([a-z])([A-Z]+)"

        return re.sub(camRegex, "\\1 \\2", str).split(" ")

    def process_text_item(self, bigToken):
        modified = []
        try:
            parts = self.camel_case_split(bigToken)
            # parts = org.apache.commons.lang.StringUtils.splitByCharacterTypeCamelCase(bigToken)
            for part in parts:

                segments = part.split("\\.")
                for segment in segments:
                    if len(segment) >= 2:
                        modified.append(segment)



        except:
            print("An exception occurred")
        return modified
