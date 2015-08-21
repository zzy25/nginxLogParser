import getLogInfo as log
import MySQLdb


class mysqlConnector:
    def __init__(self, customerId):
        self.dbUsername = "root"
        self.dbPassword = "amigos02"
        self.dbDatabase = "auto"
        self.dbHost = "localhost"
        self.customerId = customerId

    def startConnection(self):
        self.db = MySQLdb.connect(host=self.dbHost, # your host, usually localhost
                         user=self.dbUsername, # your username
                          passwd=self.dbPassword, # your password
                          db=self.dbDatabase) # name of the data base

    def closeConnection(self):
        self.db.close()

    def insertData(self,info):
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        self.startConnection()

        cur = self.db.cursor()
        # Use all the SQL you like
        cur.execute('INSERT INTO clientes VALUE (%s, "Diego Ragazzi", "ragazzi.d@gmail.com", "eu", 1, "2015-08-21 15:08:43", "nda", 1, "ragazzid", "2015-08-21 15:08:43")', self.customerId)
        self.db.commit()
        cur.close()

        self.closeConnection()



