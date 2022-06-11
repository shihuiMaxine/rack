import sqlite3
from sqlite3 import Connection
from sqlite3 import DriverManager
from sqlite3 import ResultSet
from sqlite3 import Statement
import array as arr
import rack.similarity.CosineSimilarityMeasure
import rack.config.StaticData
import rack.dbaccess.ConnectionManager
class AdjacencyScoreProvider:
    #double[][] simscores
    # ArrayList<String> queryTerms
    # HashMap<String, ArrayList<String>> 
    queryTerms = []
    adjacencymap = dict()
    keys=[]
    
    simscores =[[]]


    def AdjacencyScoreProvider (rack, queryTerms):
        rack.queryTerms=queryTerms
        rack.adjacencymap=dict()
        rack.keys=[]

    def collectAdjacentTerms():
        try:
            conn = rack.dbaccess.ConnectionManager.getConnection()
            if Connection.conn != NULL:
                
                for key in rack.queryTerms :
                    getAdjacent = "select distinct Token from TextToken where EntryID in"
                    + "(select EntryID from TextToken where Token='"
                    + key + "') and Token!='" + key + "'"
                Statement.stmt = conn.createStatement()
                ResultSet.results = Statement.stmt.executeQuery(getAdjacent)
                adjacent =[]
                while ResultSet.results.next():
                    token = ResultSet.results.getString("Token")
                    adjacent.add(token)
                rack.adjacencymap.add(key, adjacent)


        except(Exception.exc):
            Exception.exc.printStackTrace()
    def collectAdjacencyScores():
        dimension = rack.adjacencymap.keySet().length()
        rack.keys.addAll(rack.adjacencymap.keySet())
        simscores=[dimension[dimension]]
        
        for i in range (dimension) :
            first = rack.keys[i]
            for j in range (dimension) :
                second = rack.keys[j]
                rack.similarity.CosineSimilarityMeasure.cos = rack.similarity.CosineSimilarityMeasure(rack.adjacencymap[first],rack.adjacencymap[second])
                simscore = rack.similarity.CosineSimilarityMeasure.cos.getCosineSimilarityScore()
                simscores[i][j] = simscore

        return simscores
    def getQueryTermAdjacencyScores():
        rack.collectAdjacentTerms()
        rack.collectAdjacencyScores()
    def main():
        queryTerms =["extract","method","class"]
        AdjacencyScoreProvider.provider = AdjacencyScoreProvider(queryTerms)
        AdjacencyScoreProvider.provider.getQueryTermAdjacencyScores()


    









        

