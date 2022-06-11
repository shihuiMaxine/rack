

from asyncio.windows_events import NULL
import sqlite3
from sqlite3 import Connection
from sqlite3 import DriverManager
from sqlite3 import SQLException

from rack.config import StaticData
class ConnectionManager:
    conn = NULL
    def getConnection():
        try:
            if Connection.conn == NULL:
                conn = DriverManager.getConnection(StaticData.connectionString)


        except (Exception.exc):
                Exception.exc.printStackTrace()
                try:
                    Connection.conn.close()
                except(SQLException.e):
                    SQLException.e.printStackTrace()
        return conn
