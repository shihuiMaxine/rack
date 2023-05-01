
import math 
class CosineMeasure:
    # def CosineMeasure():
    #     1=1
    def getCosineSimilarity(self,list1,list2):
        cosmeasure = 0.0
        mode1 = self.getMode(list1)
        mode2 = self.getMode(list2)
        upper = 0.0
        for i in range (0,len(list1)):
            upper += list1[i] * list2[i]
        if(mode1>0 and mode2 > 0):
            cosmeasure = upper / (mode1 * mode2)
        return cosmeasure
    
    def  getMode(self,list):
        sum = 0.0
        for i in list:
            sum += i * i
        return math.sqrt(sum)
        

