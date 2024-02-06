import mysql.connector

class DBhelper:
    try:
        def __init__(self):
            self.conn = mysql.connector.connect(host = "localhost", username="root", password="", database="if0_34980744_collage_details")
            self.mycursor = self.conn.cursor()
    except:
        print("connected to databse")
    else:
        print("some error occured !")