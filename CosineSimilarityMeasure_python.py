import array as arr
from ctypes import sizeof
import hashlib
from this import s
import os
from turtle import title
from xxlimited import Null
class CosineSimilarityMeasure :
    cosine_measure =0.0
    title1 = input()
    title2 = input()

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
    def getTokenized_text_content (rack,content):
        tokens  =  arr.array()
        tokenizer  =  content.split()
        #while(tokenizer.hasMoreTokens()):
        for i  in range(0,len(tokenizer)):
            token = tokenizer[i]
            if len(token) != 0:
                tokens.add(token)
        return tokens
    def  getTokenized_text_content_granularized(rack,content):
        #?
        myTokenizer =  MyTokenizer(content)
        tokens  =  myTokenizer.tokenize_code_item()
        return myTokenizer.refine_insignificant_tokens(tokens)


    def getCosineSimilarityScore(rack):
        try:
            for rack.list1 in str:
                if len(str)!= 0:
                    set.add(str)
                    if str in rack.map1:
                        count = int(rack.map1.get(str))
                        count=count+1
                        rack.map1[count]= str
                    else:
                        rack.map1[1]= str
            for rack.list2 in str:
                if len(str) != 0:
                    set.add(str)
                    if str  in rack.map2 :
                        count = int(rack.map2.get(str))
                        count=count+1
                        rack.map2[count]= str
                    else:
                        rack.map2[1]= str
            sqr1  =0.0
            hset1= set()
            hset2 = set()
            for i in range (0,len(rack.set1)):
                hset1.add(rack.set1[i])
            for i in range (0,len(rack.set2)):
                hset2.add(rack.set2[i])

            
            for i in range(0,len(hset1)):
                if int(rack.map1.get(hset1[i])) is Null:
                    val =0
                else:
                    val = int(rack.map1.get([hset1[i]]))
                sqr1=sqr1+val*val

            sqr2  =0.0
        
            for i in range(0,len(hset2)):
                if int(rack.map2.get([hset2[i]])) is Null:
                    val =0
                else:
                    val = int(rack.map2.get([hset2[i]]))
                sqr2=sqr2+val*val
            top_part = 0.0
            for i in range (0,len(hset1)):
                key=""
                key=string(rack.set1.toArray()[i])
                val1=0.0
                val1=double(rack.map1.get(key))
                if rack.map2.get([hset2[i]]) is Null:
                     val2=0.0
                else:
                    val2 = double(rack.map2.get(key))
            cosine_ratio = 0.0
            try:
                cosine_ratio = top_part / (Math.sqrt(sqr1) * Math.sqrt(sqr2))
            except:
                cosine_ratio = 0
            rack.cosine_measure = cosine_ratio

        except:
            print("An exception occurred")
        return rack.cosine_measure
    def get_cosine_similarity_score(rack,granularized,):
        value_return =0.0
        try:
            if len(rack.title1) == 0 or rack.title1==Null:
                return value_return 
            if len(rack.title2) == 0 or rack.title2==Null:
                return value_return 
            if granularized == True:
                parts1 =  rack.getTokenized_text_content_granularized(rack.title1)
            else:
                parts1 =  rack.getTokenized_text_content(rack.title1)
            if granularized == True:
                parts2 =  rack.getTokenized_text_content_granularized(rack.title2)
            else:
                parts2 =  rack.getTokenized_text_content(rack.title2)
            for str in parts1:
                if len(rack.title1) == 0:
                    rack.set1.add(str)
                if str in rack.map1:
                    rack.map1[1]=str
                else:
                    count=0
                    count=rack.map1.get(str)
                    count=count+1
                    rack.map1[count]=str
            for str in parts2:
                if len(rack.title2) == 0:
                    rack.set2.add(str)
                if str in rack.map2:
                    rack.map1[1]=str
                else:
                    count=0
                    count=rack.map2.get(str)
                    count=count+1
                    rack.map2[count]=str
            sqr1  =0.0
            hset1= set()
            hset2 = set()
           
            
            for i in range(0,len(hset1)):
                if rack.set1.toArray()[i] is Null:
                    val =0
                else:
                    val = int(rack.map1.get(rack.set1.toArray()[i]))
                sqr1=sqr1+val*val

            sqr2  =0.0
        
            for i in range(0,len(hset2)):
                if rack.set2.toArray()[i]is Null:
                    val =0
                else:
                    val = int(rack.map2.get(rack.set2.toArray()[i]))
                sqr2=sqr2+val*val
            top_part = 0.0
            for i in range (0,len(hset1)):
                key=""
                key=string(rack.set1.toArray()[i])
                val1=0.0
                val1=double(rack.map1.get(key))
                if rack.map2.get(key)is Null:
                     val2=0.0
                else:
                    val2 = double(rack.map2.get(key))
            cosine_ratio = 0.0
            try:
                cosine_ratio = top_part / (Math.sqrt(sqr1) * Math.sqrt(sqr2))
            except:
                cosine_ratio = 0
            rack.cosine_measure = cosine_ratio
        except:
            print("An exception occurred")
        return rack.cosine_measure
    def  get_cosine_similarity_score(rack,s):
        s=set()
        for  i in range(0,len(s)):
            print(s.toArray()[i] + "\t")
    def load_text_content(fileName):
        content  = input()
        try:
            rootDir = ("./testdata/" + fileName)
        except:
            print("An exception occurred")
        return content
    def main(rack):
        title1 = rack.load_text_content("stack.txt")
        title2 = rack.load_text_content("stack2.txt")
        measure = rack.CosineSimilarityMeasure(title1,title2)
        similarity = measure.get_cosine_similarity_score(True)
        print("Similarity score:" + similarity)


    if __name__ == "__main__":
        main()



                
           
