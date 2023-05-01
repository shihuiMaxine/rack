import os
import sqlite3
import requests, csv
from config import StaticData
import ast
class TokenMapSaver:
    def __init__(self, itemset):
        self.itemset = itemset

    def addTokens(self, entryID, titleTokens, apiTokens):
        conn = None
        try:

            conn = sqlite3.connect("/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/dbaccess/rack-python.db")

            if conn is not None:
                conn.execute("PRAGMA foreign_keys = ON")
                conn.execute("BEGIN TRANSACTION")

                addTextToken = "INSERT INTO TextToken(EntryID, Token) VALUES (?, ?)"
                addCodeToken = "INSERT INTO CodeToken(EntryID, Token) VALUES (?, ?)"

                token_list = ast.literal_eval(titleTokens)
                stripped_token_list = [token.strip() for token in token_list]
                for token in stripped_token_list:
                    conn.execute(addTextToken, (entryID,  token.strip()))


                token_list = ast.literal_eval(apiTokens)
                stripped_token_list = [token.strip() for token in token_list]
                for token in stripped_token_list:
                    # print(token)
                    conn.execute(addCodeToken, (entryID, token))

                conn.commit()
                conn.close()
                print(f"Done: {entryID}")
                print(conn)

        except Exception as e:

            print(e)
            if conn is not None:
                conn.rollback()

    def collectTokens(self):
        try:
            file = open(self.itemset)

            csvreader = csv.reader(file)
            for row in csvreader:
                textTokens = row[5]
                codeTokens = row[3]
                if len(row[4])>2:
                    codeTokens = row[3][0:-1]+", "+  row[4][1:]

                print(codeTokens)
                self.addTokens(row[0], textTokens, codeTokens)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import time
    start = time.time()
    saver = TokenMapSaver("/Users/gaoshihui/rack_py_g/rack_py_g/rack-py-main/rack/core/data_mapping.csv")
    saver.collectTokens()
    end = time.time()
    print(f"Time elapsed: {(end - start)}s")
