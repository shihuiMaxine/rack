import math
import numpy as np
from decimal import Decimal
from similarity.MyTokenizer import MyTokenizer

class CosineSimilarityMeasure:
    cosine_measure = 0.0
    title1 = None
    title2 = None

    set1 = set()
    set2 = set()

    list1 = []
    list2 = []

    map1 = dict()
    map2 = dict()

    def __init__(self, title1, title2, list1, list2):
        self.title1 = title1
        self.title2 = title2
        self.list1 = list1
        self.list2 = list2
        self.set1 = set()
        self.set2 = set()

        self.map1 = dict()
        self.map2 = dict()


    def getTokenized_text_content(self, content):

        tokens=content.strip().split()
        return  tokens


    def getTokenized_text_content_granularized(self, content):

        myTokenizer = MyTokenizer(content)
        tokens = myTokenizer.tokenize_code_item()
        return myTokenizer.refine_insignificant_tokens(tokens)

    def getCosineSimilarityScore(self):

        try:
            for str in self.list1:
                if len(str) != 0:
                    self.set1.add(str)
                    if str in self.map1:
                        count = int(self.map1.get(str))
                        count = count + 1
                        self.map1[str] = count
                    else:
                        self.map1[str] = 1
            for str in self.list2:
                if len(str) != 0:
                    self.set2.add(str)
                    if str in self.map2:
                        count = int(self.map2.get(str))
                        count = count + 1
                        self.map2[str] = count
                    else:
                        self.map2[str] = 1

            sqr1 = 0.0
            hset1 = self.set1
            hset2 = self.set2

            for i in range(0, len(hset1)):
                if int(self.map1[list(hset1)[i]]) is None:
                    val = 0
                else:
                    val = int(self.map1[list(hset1)[i]])
                sqr1 = sqr1 + val * val

            sqr2 = 0.0

            for i in range(0, len(hset2)):
                if int(self.map2[list(hset2)[i]]) is None:
                    val = 0
                else:
                    val = int(self.map2[list(hset2)[i]])
                sqr2 = sqr2 + val * val

            top_part = 0.0

            for i in range(0, len(hset1)):
                key = list(self.set1)[i]
                val1 = float(self.map1.get(key))



                if self.map2.get(key) is None:
                    val2 = 0.0

                else:
                    val2 = float(self.map2.get(key))

                top_part = top_part + val1 * val2


            try:
                cosine_ratio = top_part / (math.sqrt(sqr1) * math.sqrt(sqr2))

            except:
                cosine_ratio = 0

            self.cosine_measure = cosine_ratio

        except:
            print("An exception occurred")
        print(self.cosine_measure)

        return self.cosine_measure

    def get_cosine_similarity_score(self, granularized):
        try:

            if len(self.title1) == 0 or self.title1 == None:
                return 0
            if len(self.title2) == 0 or self.title2 == None:
                return 0

            if granularized == True:
                parts1 = self.getTokenized_text_content_granularized(self.title1)
            else:
                parts1 = self.getTokenized_text_content(self.title1)


            if granularized == True:
                parts2 = self.getTokenized_text_content_granularized(self.title2)
            else:
                parts2 = self.getTokenized_text_content(self.title2)
            i = 1
            j = 1

            for str in parts1:

                if len(str) != 0:
                    self.set1.add(str)
                    if str in self.map1:
                        count = int(str(self.map1.get(str)))
                        count = count + 1
                        self.map1[count] = str


                    else:
                        self.map1[i] = str
                        i += 1


            for str in parts2:
                if len(str) != 0:
                    self.set2.add(str)
                    if str in self.map2:
                        count = int(str(self.map2.get(str)))
                        count = count + 1
                        self.map2[count] = str
                    else:
                        self.map2[j] = str
                        j += 1


            hset1 = {}
            hset1 = self.set1
            hset2 = {}
            hset2 = self.set2
            sqr1 = 0.0
            for i in range(0, len(hset1)):


                if [k for k, v in self.map1.items() if v == list(sorted(hset1))[i]][0] != None:
                    val = [k for k, v in self.map1.items() if v == list(sorted(hset1))[i]][0]
                    val = val / val

                else:
                    val = 0
                sqr1 += val * val

            sqr2 = 0.0
            for i in range(0, len(hset2)):
                if [k for k, v in self.map2.items() if v == list(sorted(hset2))[i]][0] != None:
                    val = [k for k, v in self.map2.items() if v == list(sorted(hset2))[i]][0]
                    val = val / val
                else:
                    val = 0
                sqr2 += val * val


            top_part = 0.0

            for i in range(0, len(hset1)):

                key = list(sorted(hset1))[i]

                val1 = [k for k, v in self.map1.items() if v == key][0]

                val1 = "1"
                val1 = Decimal(val1)


                val2 =0.0
                for j in self.map2.keys():
                    if self.map2.get(j) == key:
                        val2=list(self.map2.keys())[0]


                val_sum = val1 * Decimal(val2)

                top_part = top_part + float(val_sum)

            cosine_ratio = 0.0
            try:
                cosine_ratio = top_part / (math.sqrt(sqr1) * math.sqrt(sqr2))
            except:
                cosine_ratio = 0
            self.cosine_measure = cosine_ratio

        except:
            print("An exception occurred")

        return self.cosine_measure

    def show_extracted_tokens(self, s):
        for i in range(len(s)):
            print(np.arrayI(list(s))[i])

    def load_text_content(self, fileName):
        content = ""

        scanner = open(fileName)
        line = scanner.readline()
        try:
            for i in scanner:
                print(i.strip())
                content = content + i.strip() + " "
            scanner.close()

        except:
            print("An exception occurred")
        return content

