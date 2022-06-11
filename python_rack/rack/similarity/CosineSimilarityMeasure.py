
import array as arr
from ctypes import sizeof
import hashlib
from turtle import title
class CosineSimilarityMeasure :
    cosine_measure =0.0
    title1= input()
    title2=input()

    set1 = set()
    set2 = set()

    list1  = arr.array()
    list2 = arr.array()

    map1=dict()
    map2=dict()

    def  CosineSimilarityMeasure(rack,title1,title2):
        rack.title1=title1
        rack.title2=title2
        set1 = set()
        set2 = set()


        map1=dict()
        map2=dict()
    def CosineSimilarityMeasure(rack,list1,list2):
        rack.list1=list1
        rack.list2=list2
        set1 = set()
        set2 = set()

        map1=dict()
        map2=dict()
    def getTokenized_text_content (content):
        tokens  =  arr.array()
        tokenizer  =  content.split()
        #while(tokenizer.hasMoreTokens()):
        for i  in range(0,len(tokenizer)):
            token = tokenizer[i]
            if len(token) != 0:
                tokens.add(token)
        return tokens
    def getCosineSimilarityScore():
        try:
            for rack.list1 in str:
                if len(str)!= 0:
                    set.add(str)
                    if str in map1:
                        count = int(map1.get(str))
                        count=count+1
                        map1[count]= str
                    else:
                        map1[1]= str
            for rack.list2 in str:
                if len(str) != 0:
                    set.add(str)
                    if str  in map2 :
                        count = int(map2.get(str))
                        count=count+1
                        map2[count]= str
                    else:
                        map2[1]= str
            sqr1  =0.0
            hset1= set()
            hset2 = set()
            for i in range (0,len(set1)):
                hset1.add(set1[i])
            for i in range (0,len(set2)):
                hset2.add(set2[i])

            
            for i in range(0,len(hset1)):
                if int(map1.get(hset1[i])) is NULL:
                    val =0
                else:
                    val = int(map1.get([hset1[i]]))
                sqr1=sqr1+val*val

            sqr2  =0.0
        
            for i in range(0,len(hset2)):
                if int(map2.get([hset2[i]])) is NULL:
                    val =0
                else:
                    val = int(map2.get([hset2[i]]))
                sqr1=sqr1+val*val




        except:
            print("An exception occurred")


                
           
