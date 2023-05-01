from similarity import CosineSimilarityMeasure
class LexicalSimilarityProvider:
    queryTerms=[]
    candidates=[]
    simScoreMap=dict()
    

    def __init__(self,queryTerms, candidates):
        self.queryTerms = queryTerms
        self.candidates = candidates
        self.simScoreMap = dict()
    def decomposeCamelCase(self,token):
        camRegex = "([a-z])([A-Z]+)"
        replacement = "$1 $2"
        filtered = token.replaceAll(camRegex, replacement)
        ftokens = filtered.split(" ")
        return ftokens
    def clearTheTokens(self,tokenParts):
        refined = self.StopWordRemover.removeStopWords(tokenParts)
        stemmed = self.TokenStemmer.performStemming(refined)
        return stemmed
    def  normalizeAPIToken(self,apiToken):
        decomposed = self.decomposeCamelCase(apiToken)
        normalized = self.clearTheTokens(decomposed)
        return normalized

    def getLexicalSimilarityScores(self):
        for apiName in self.candidates:
            normalizedTokens = self.normalizeAPIToken(apiName)
            cosMeasure = CosineSimilarityMeasure(None,None,normalizedTokens,self.candidates)
            simScore = cosMeasure.getCosineSimilarityScore()
            if apiName not in self.simScoreMap.containsKey:
                self.simScoreMap[apiName]=simScore
        return self.simScoreMap

def main():
    queryTerms = []

    queryTerms.append("extract")
    queryTerms.append("method")
    queryTerms.append("class")
    list = ["a", "b", "c"]
    provider =LexicalSimilarityProvider(queryTerms,list)
    org_sentence = "This is test"


if __name__ == "__main__":
    main()

