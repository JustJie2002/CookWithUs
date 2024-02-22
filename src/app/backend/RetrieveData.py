import mysql.connector;

class RetrieveData:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
        )