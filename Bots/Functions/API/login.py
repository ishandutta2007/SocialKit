from API.instagram_private_api import Client
import pymysql


config = {
  'host':'localhost',
  'user':'root',
  'password':'',
  'database':'socialkit'
}

connection = pymysql.connect(**config)

crsr = connection.cursor()

crsr.execute("""SELECT IGU, IGP FROM user
WHERE userID=1""")

lst = crsr.fetchall()

username = str(lst[0][0])
password = str(lst[0][1])

def login():

    api = Client(username, password)
    return api