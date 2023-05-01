import hashlib
from core.StopWordRemover import StopWordRemover
from core.TokenStemmer import TokenStemmer
from core.AdjacencyScoreProvider import AdjacencyScoreProvider
from core.RelevantAPICollector import RelevantAPICollector
from core.CoocurrenceScoreProvider import CoocurrenceScoreProvider
from core. APIToken import APIToken
from config import StaticData
from utility.ItemSorter import ItemSorter
import re
import string
import csv

class CodeTokenProvider:
    query = ""
    tokenScoreMap = {}
    MAXAPI = StaticData.MAXAPI
    # ? final
    stemmedQuery = []
    gamma = StaticData.gamma
    KACMap = {}
    KPACMap = {}
    KKCMap = {}

    def __init__(self,query):
        self.query = query
        self.tokenScoreMap = {}
        self.stemmedQuery = []
        self.KACMap = {}
        self.KPACMap = {}
        self.KKCMap = {}


    # @property
    def decomposeQueryTerms(self):
        tempQuery = self.query.lower()
        regex = string.punctuation
        regex= '[?.,\n\t&!()*+,-./:;<=>@[\]^_`{|}~]'
        tokens=re.split('[?.,\n\t&!()*+,-./:;<=>@[\]^_`{|}~ ]', tempQuery)
        numRegex = "\d+"



        refined = StopWordRemover().removeStopWords(tokens)
        stemmed = []

        stemmed = TokenStemmer().performStemming(refined)
        stemmedQuery = []
        a=0
        for token in stemmed:
            if re.match(r'\d+', token):
                continue
            elif len(token) > 0:
                if token in stemmedQuery:
                    a+=1
                else:
                    stemmedQuery.append(token)
        self.stemmedQuery = stemmedQuery


        return self.stemmedQuery

    def collectTokenScores(self,queryTerms):

        adjacent = AdjacencyScoreProvider(queryTerms)

        adjacent.collectAdjacentTerms()
        simscores = adjacent.collectAdjacencyScores()
        keys = []
        keys=list(adjacent.keys)
        collector=RelevantAPICollector(queryTerms)

        tokenmap = {}
        tokenmap = collector.collectAPIsforQuery()

        self.tokenScoreMap = {}
        self.addAssociationFrequencyScores(tokenmap)
        self.addTokenSimilarityScores(keys, simscores, tokenmap)
        self.addDirectCoocScores()
        self.addExtraLayerScoreComputation()

    def collectTokenScoresKAC(self,queryTerms):
        collector=RelevantAPICollector(queryTerms)
        tokenmap = {}
        tokenmap = collector.collectAPIsforQuery()
        # print("tokenmap")
        # print(tokenmap)
        self.tokenScoreMap = {}
        self.addAssociationFrequencyScores(tokenmap)


    def collectTokenScoresKKC(self,queryTerms):
        adjacent = AdjacencyScoreProvider(queryTerms)
        adjacent.collectAdjacentTerms()
        # simscores = [[]]
        simscores = adjacent.collectAdjacencyScores()
        # keys = []
        keys=adjacent.keys
        # print(keys)
        collector=RelevantAPICollector(queryTerms)
        tokenmap = {}
        tokenmap =collector.collectAPIsforQuery()
        self.tokenScoreMap = {}
        self.addTokenSimilarityScores(keys, simscores, tokenmap)

    def collectTokenScoresKPAC(self,queryTerms):
        self.tokenScoreMap = {}
        self.addDirectCoocScores()

    def addTokenSimilarityScores(self,keys, simscores, tokenmap):
        for i in range (0,len(keys)):

            first = keys[i]

            firstapi = tokenmap[first]
            for j in range (0,len(keys)):

                second = keys[j]

                secondapi = tokenmap[second]
                common = self.intersect(firstapi, secondapi)



                simscore = simscores[i][j]


                if simscores[i][j] > self.gamma:

                    for token in list(common):

                        token = token
                        newOldScore = 0.0

                        if token in self.tokenScoreMap:
                            newOldScore = self.tokenScoreMap[token] + simscore
                            self.tokenScoreMap[token] = newOldScore

                        else:
                            self.tokenScoreMap[token] = simscore

                        if token in self.KKCMap:
                            newOldScore = self.KKCMap[token] + simscore
                            self.KKCMap[token] = newOldScore
                        else:
                            self.KKCMap[token] = simscore


    def addAssociationFrequencyScores(self,tokenmap):
        var2 = list(tokenmap.keys())


        for i in var2:
            key = i
            apis = tokenmap[i]
            length = len(apis)
            for i in range(0, length):

                score = 1.00 - (i / float(length))
                api = apis[i]
                newScore = 0.0
                if api in self.tokenScoreMap.keys():
                    newScore = self.tokenScoreMap[api] + score
                    self.tokenScoreMap[api] = newScore
                else:
                    self.tokenScoreMap[api] = score
                if api in self.KACMap:
                    newScore = self.KACMap[api] + score
                    self.KACMap[api] = newScore
                else:
                    self.KACMap[api] = score


    def addDirectCoocScores(self):
        coocProvider= CoocurrenceScoreProvider(self.stemmedQuery)
        coocScoreMap = coocProvider.getCoocScores()

        var3 = list(coocScoreMap.keys())

        for i in var3:

            apiKey = i

            coocScore = coocScoreMap[apiKey]

            if apiKey in self.tokenScoreMap:
                newScore = self.tokenScoreMap[apiKey] + coocScore
                self.tokenScoreMap[apiKey] = newScore
            else:
                self.tokenScoreMap[apiKey] = coocScore

            if apiKey in self.KPACMap:
                newScore = self.KPACMap[apiKey] + coocScore
                self.KPACMap[apiKey] = newScore
            else:
                self.KPACMap[apiKey] = coocScore


    def intersect(self,s1, s2):
        common = set()

        for i in s2:
            if  i in s1:
                common.add(i)

        return common

    def rankAPIElements1(self):

        sorted=ItemSorter().sortHashMapDouble(self.tokenScoreMap)

        rankedAPIs = []
        var3 = sorted
        for i in list(var3):

            rankedAPIs.append(i)
        print("rankedAPIs: ",end=" ")
        print(rankedAPIs)
        return rankedAPIs

    def rankAPIElements2(self,scoreMap):
        sorted=ItemSorter().sortHashMapDouble(scoreMap)
        rankedAPIs = []
        var4 = sorted
        for i in var4:

            rankedAPIs.append(i)
        topRanked = []
        var7 = rankedAPIs
        for j in var7:

            api = j
            if len(api.strip()) > 0:
                topRanked.append(api)
                if len(topRanked) == StaticData.MAXAPI:
                    break
        # print("topRanked")
        return topRanked

    def addExtraLayerScoreComputation(self):
        kacs = self.rankAPIElements2(self.KACMap)

        kacScoreMap = self.getNormScore(kacs)

        kpacs = self.rankAPIElements2(self.KPACMap)
        kpacScoreMap = self.getNormScore(kpacs)
        kkcs = self.rankAPIElements2(self.KKCMap)
        kkcScoreMap = self.getNormScore(kkcs)
        self.addCombinedRankingsV2(kacScoreMap, kpacScoreMap, kkcScoreMap, StaticData.alpha,
                                   StaticData.beta, StaticData.psi)

    def addCombinedRankings(self,kacMap, kpacMap, kkcMap, alpha1, beta1, psi1):
        self.tokenScoreMap = {}
        var10 = list(kacMap.keys())
        key = ""
        score = 0.0
        newScore = 0.0
        for i in var10:

            key =i
            score = kacMap[key]
            score = score * alpha1
        if key in self.tokenScoreMap:
            newScore = self.tokenScoreMap[key] + score
            self.tokenScoreMap[key] = newScore
        else:
            self.tokenScoreMap[key] = score
        var10 = list(kpacMap.keys())

        for i in var10:
            key = i

            score = kpacMap[key]
            score = score * beta1
            if key in self.tokenScoreMap:
                newScore = self.tokenScoreMap[key] + score
                self.tokenScoreMap[key] = newScore
            else:
                self.tokenScoreMap[key] = score
        var10 = list(kkcMap.keys())

        for i in var10:
            key = i
            score = kkcMap[key]

            score = score * psi1
            if key in self.tokenScoreMap:
                newScore = self.tokenScoreMap[key] + score
                self.tokenScoreMap[key] = newScore
            else:
                self.tokenScoreMap[key] = score

    def addCombinedRankingsV2(self,kacMap, kpacMap, kkcMap, alpha1, beta1, psi1):
        self.tokenScoreMap = {}
        var10 = kacMap.keys()
        key = ""
        score = 0.0
        newScore = 0.0
        for i in list(var10):
            key = i

            score = kacMap[key]
            score = score * alpha1
        if key in self.tokenScoreMap:
            newScore = max(self.tokenScoreMap[key], score)
            self.tokenScoreMap[key] = newScore
        else:
            self.tokenScoreMap[key] = score
        var10 = kpacMap.keys()
        for i in list(var10):
            key = i

            score = kpacMap[key]
            score = score * beta1
            if key in self.tokenScoreMap:
                newScore = max(self.tokenScoreMap[key], score)
                self.tokenScoreMap[key] = newScore
            else:
                self.tokenScoreMap[key] = score
        var10 = kkcMap.keys()

        for i in list(var10):
            key =i
            score = kkcMap[key]
            score = score * psi1
            if key in self.tokenScoreMap:
                newScore = max(self.tokenScoreMap[key], score)
                self.tokenScoreMap[key] = newScore
            else:
                self.tokenScoreMap[key] = score


    def getNormScore(self,apis):
        tempMap = {}
        index = 0
        var4 = apis

        for i in var4:
            api = i
            index = index + 1
            score = 1.00 - float(index / len(apis))

            tempMap[api] = score
        return tempMap

    def recommendRelevantAPIs(self,key):
        self.decomposeQueryTerms()
        queryTerms=self.stemmedQuery

        # print(queryTerms)

        if key == "KAC":
            print("KAC: ",end="")
            print(queryTerms)
            self.collectTokenScoresKAC(queryTerms)
        elif key =="KPAC":
            print("KPAC: ", end="")
            print(queryTerms)
            self.collectTokenScoresKPAC(queryTerms)
        elif key =="KKC":
            print("KKC: ", end="")
            print(queryTerms)
            self.collectTokenScoresKKC(queryTerms)
        elif key == "all":
            print("all: ", end="")
            print(queryTerms)
            self.collectTokenScores(queryTerms)

        else:
            self.collectTokenScores(queryTerms)


        apis = self.rankAPIElements1()
        self.KACMap = self.normalizeMapScores(self.KACMap)
        self.KPACMap = self.normalizeMapScores(self.KPACMap)
        self.KKCMap = self.normalizeMapScores(self.KKCMap)
        resultAPIs = []
        suggestedResults = []
        var6 = apis

        for i in var6:
            api = i
            if len(api.strip()):

                atoken = APIToken()
                atoken.token=api
                if api in self.KACMap:
                    atoken.KACScore = self.KACMap[api]

                if api in self.KPACMap:
                    atoken.KPACScore = self.KPACMap[api]

                if api in self.KKCMap:
                    atoken.KKCScore = self.KKCMap[api]

                if api in self.tokenScoreMap:
                    atoken.totalScore = self.tokenScoreMap[api]

                suggestedResults.append(atoken)
                resultAPIs.append(api)

                if len(resultAPIs) == StaticData.MAXAPI:
                    break
        return suggestedResults

    def showAPIs(self,apis):
        var2 = apis

        for i in var2:


            api = i


    def normalizeMapScores(self,tempScoreMap):
        maxScore = 0.00
        var4 = tempScoreMap.keys()
        api = ""
        myscore = 0.00

        for i in var4:
            api =i
            myscore = tempScoreMap[api]
            if myscore > maxScore:
                maxScore = myscore

        var4 = tempScoreMap.keys()

        for i in var4:
            api =i
            myscore = tempScoreMap[api]
            normScore = myscore / maxScore
            tempScoreMap[api] = normScore
        return tempScoreMap

    def discardDuplicates(self,results):
        discardList = []
        i = results.size() - 1
        while i > 0:
            i = i - 1
            low = results[i]
            j = i - 1
            while j >= 0:
                j = j - 1
                high = results[j]
                if low.endsWith(high) or high.endsWith(low):
                    discardList.append(low)

        for c in discardList:
            try:
                results.remove(c)
            except ValueError:
                pass

        return results

def main():
    query = "How do you parse HTML?"


    provider=CodeTokenProvider(query)

    results = ""
    results = provider.recommendRelevantAPIs("all")
    var4 = results


    for i in var4:
        atoken =i


        print(str(atoken.token) + " " +
              str(atoken.KACScore) + " " +
              str(atoken.KPACScore) + " " +
              str(atoken.KKCScore) + " " +
              str(atoken.totalScore))


if __name__ == "__main__":
    main()