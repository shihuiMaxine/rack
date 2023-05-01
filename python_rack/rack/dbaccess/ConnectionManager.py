import sqlite3
import traceback


class ConnectionManager:

    def __init__(self):
        self.conn = None
        self.db_file ="/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/dbaccess/rack-python.db"


    def getConnection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except:
            traceback.print_exc()
            try:
                self.conn.close()
            except:
                traceback.print_exc()
        return self.conn


manager = ConnectionManager()
conn = manager.getConnection()
print(conn)

