import utility
import traceback

class ContentLoader:
    def __init__(self):
        pass

    def loadFileContent(self,fileName):
        fileContent = ""
        try:
            f = open(fileName)
            fileContent = f.read()
            f.close()


        except:
            print("An exception occurred")

        return fileContent

    def loadFileContentSC(self,fileName):
        content = ""
        try:
            scanner = open(fileName, "r")

            for i in scanner:
                line = i
                content +=i
            scanner.close()
        except:
            print("An exception occurred")

        return content

    def getAllLinesOptList(self,fileName):
        lines = []
        try:
            f = open(fileName)
            fileContent = f.readlines()

            for i in fileContent:
                line = i.strip()
                lines.append(line)

        except:
            traceback.print_exc()

        return lines

    def getAllLines(self,fileName):
        content = ""

        scanner = open(fileName)

        line = scanner.readline()

        for i in scanner:
            content = content + i.strip()+" "
        scanner.close()
        return list(content.split(" "))

sr=ContentLoader()
org_sentence="/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/pp-data/stop-words-english-total.txt"
