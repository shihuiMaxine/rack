
from config import StaticData
from dbaccess.ConnectionManager import ConnectionManager
import traceback
class RelevantAPICollector:
    queryTerms=[]

    TOPK_API_THRESHOLD = StaticData.DELTA1

    def __init__(self,queryTerms):
        self.queryTerms = queryTerms


    def collectAPIsforQuery(self):
        tokenmap ={}
        TOPK_API_THRESHOLD = StaticData.DELTA1
        try:
            conn = ConnectionManager().getConnection()
            if conn != None:
                stmt = conn.cursor()
                for texttoken in self.queryTerms:
                    getCodeToken = "select "\
                                   + " ct.Token from CodeToken as ct, TextToken as tt "\
                                   + " where ct.EntryID=tt.EntryID and tt.Token='"\
                                   + texttoken\
                                   + "'"\
                                   + " group by ct.Token order by count(*) desc limit "\
                                   + str(TOPK_API_THRESHOLD)
                    results = stmt.execute(getCodeToken)
                    apis =[]
                    for row in results:
                        token = row[0]
                        apis.append(token)
                    tokenmap[texttoken]=apis
                

        except:
            traceback.print_exc()

        return tokenmap


