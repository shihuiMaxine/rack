
import  array
import  hashlib
class MiscUtility :
    def list2Str(self,list) :
        temp = ""
        for item in list:
            temp += item + " "
        return temp.strip()

    def  extract(self,list1, TOPK):
        temp =[]
        for item in  list1:
            temp.append(item)
            if (len(temp) == TOPK):
                break
        return temp

    def decomposeCamelCase(self,token) :
        refined = []
        camRegex = "([a-z])([A-Z]+)"
        replacement = "$1 $2"
        filtered = token
        for i in filtered:
            if i == camRegex:
                filtered = filtered.replace(i, replacement)
        ftokens = filtered.split()
        for j in ftokens:
            refined.append(j)
        return refined

    def str2List(self,str):
        return list(str.split())

    def list2Array(self,list):
        array =[]
        for index in range (0, len(list)):
            array.append(list[index])

        return array

    def wordcount(self,content):
        if isinstance(content, list):
            words = content
        else:
            words = content.split(" ")


        countmap = dict()
        for word in words:
            if word in countmap.keys():
                count = countmap.get(word) + 1
                countmap[word]=count

            else:
                countmap[word]=1
        return countmap

    def list2Arr(self,list):
        temp =[]

        for i in range (0, len(list)):
            temp.append(list[i])
        return temp






    