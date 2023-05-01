
from similarity.CosineSimilarityMeasure import CosineSimilarityMeasure
from dbaccess.ConnectionManager import ConnectionManager
import traceback

class AdjacencyScoreProvider:

    queryTerms = []
    adjacencymap = dict()
    keys = []
    simscores = [[]]

    def __init__(self, queryTerms):
        self.queryTerms = queryTerms
        self.adjacencymap = dict()
        self.keys = []

    def collectAdjacentTerms(self):
        try:
            conn =  ConnectionManager().getConnection()
            if conn != None:
                for key in self.queryTerms:
                    getAdjacent = ""
                    getAdjacent = 'select distinct Token from TextToken where EntryID in '+ "(select EntryID from TextToken where Token='"+ key + "') and Token!='" + key + "'"

                    stmt = conn.cursor()
                    results = stmt.execute(getAdjacent)
                    adjacent = []
                    for row in results:
                        token = row[0]
                        adjacent.append(token)
                    self.adjacencymap[key] = adjacent

        except:

            traceback.print_exc()

    def collectAdjacencyScores(self):
        dimension = len(self.adjacencymap.keys())
        for key in self.adjacencymap.keys():
            self.keys.append(key)

        simscores = []
        for i in range(0, dimension):
            simscoresr = []
            for j in range(0, dimension):
                simscoresr.append(0.0)
            simscores.append(simscoresr)

        for i in range(0, dimension):
            first = self.keys[i]
            for j in range(i+1, dimension):
                second = self.keys[j]
                cos = CosineSimilarityMeasure(None, None,
                                              self.adjacencymap[first], self.adjacencymap[second])
                simscore = cos.getCosineSimilarityScore()
                simscores[i][j] = simscore

        return simscores

    def getQueryTermAdjacencyScores(self):

        self.collectAdjacentTerms()
        self.collectAdjacencyScores()


def main():
    queryTerms = []

    queryTerms.append("extract")
    queryTerms.append("method")
    queryTerms.append("class")
    provider = AdjacencyScoreProvider(queryTerms)
    provider.getQueryTermAdjacencyScores()


if __name__ == "__main__":
    main()


