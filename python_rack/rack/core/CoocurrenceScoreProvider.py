

import traceback
from config import StaticData
from dbaccess.ConnectionManager import ConnectionManager



class CoocurrenceScoreProvider :
    queryTerms= []
    keys=[]
    coocAPIMap=dict()
    TOPK_API_THRESHOLD = StaticData.DELTA1
    coocScoreMap=dict()



    def __init__(self,queryTerms):
        self.queryTerms = queryTerms
        self.keys=self.queryTerms
        self.coocAPIMap = dict()
        self.coocScoreMap = dict()


    def getKeyPairs(self):
        temp =[]
        for i in range (0,len(self.keys)):
            first = self.keys[i]
            for j in range (i+1,len(self.keys)):
                second = self.keys[j]
                keypair = first + "-" + second
                temp.append(keypair)

        return temp
    def collectCoocAPIs(self,keypairs):
        try:
            conn = ConnectionManager().conn
            if conn == None:
                conn = ConnectionManager().getConnection()
            if conn != None:
                for keypair in keypairs:
                    
                    parts = keypair.split("-")
                    first = parts[0]
                    second = parts[1]
                    getCocc = 'select '\
                              + ' Token from CodeToken where EntryID in('\
                              + "select EntryID from TextToken where Token='"\
                              + first + "' " + ' intersect '\
                              + " select EntryID from TextToken where Token='"\
                              + second + "')"+ 'group by Token order by count(*) desc limit '\
                              + str(self.TOPK_API_THRESHOLD)

                    stmt = conn.cursor()
                    results = stmt.execute(getCocc)
                    temp =[]
                    for row in results:
                        token = row[0]
                        temp.append(token)

                    self.coocAPIMap[keypair]=temp
            
        except:
            traceback.print_exc()
    def generateCoocScores(self):
        for keypair in self.coocAPIMap.keys():
            apis = self.coocAPIMap.get(keypair)
            length = len(apis)
            for  i in range (0,len(apis)):
                score=0.0
                iLen=0.0
                iLen=i / length
                score = 1 - iLen

                api = apis[i]
                if api in self.coocScoreMap.keys():
                    newScore =0.0
                    newScore = self.coocScoreMap.get(api) + score
                    self.coocScoreMap[api]=newScore
                else:
                    self.coocScoreMap[api]=score
    def normalizeScores(self):
        maxScore = 0.0
        for api in self.coocScoreMap.keys():
            score=0.0
            score = self.coocScoreMap.get(api)
            if score > maxScore:
                maxScore = score
        for api in self.coocScoreMap.keys():
            nScore=0.0
            nScore = (self.coocScoreMap.get(api))/maxScore
            self.coocScoreMap[api]=nScore

    def getCoocScores(self) :
        keypairs = self.getKeyPairs()
        self.collectCoocAPIs(keypairs)
        self.generateCoocScores()
        self.normalizeScores()
        return self.coocScoreMap

def main():
    queryTerms = []


    queryTerms.append("jdk")
    queryTerms.append("file")
    queryTerms.append("copi")
if __name__ == "__main__":

    main()









