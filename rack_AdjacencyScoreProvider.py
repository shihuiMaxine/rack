import mysql.connector
import array as arr
class AdjacencyScoreProvider:
    #double[][] simscores
    ArrayList<String> queryTerms
    HashMap<String, ArrayList<String>> adjacencymap
    ArrayList<String> keys
    simscores1=[]
    simscores =[]


    def AdjacencyScoreProvider (rack, queryTerms):
        rack.queryTerms=queryTerms
        rack.adjacencymap=adjacencymap
        rack.keys=keys

    def collectAdjacentTerms():
        try:
            conn = ConnectionManager.getConnection()
            if conn != null:
                for queryTerms in keys:
                    getAdjacent = ""
        except:
            print("Something else went wrong")



        

