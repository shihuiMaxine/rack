import utility


class ItemSorter:
    def __init__(self):
        pass
    def sortHashMapInt(self,wordMap):
        list =[]
        list=wordMap.keys()
        return list

    def compare (self,o1,o2):

        v2 = list(o2.keys())[0]
        v1 = list(o1.keys())[0]

        return  v1-v2


            
    def  sortHashMapDouble(self,wordMap):
        list3 =[]
        list1 =list(wordMap.values())
        list4 = sorted(list1)
        for i in list4:
            list3.append(str(i))


        map=self.sortHashMap(wordMap)
        list5=list(map.keys())

        return reversed(list5)

    def sortHashMap(self,wordMap):

         v1 = {k: v for k, v in sorted(wordMap.items(), key=lambda item: item[1])}


         return v1


