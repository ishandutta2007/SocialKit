import pymysql
#from pymysql import errorcode

# Obtain connection string information from the portal
config = {
  'host':'social-kit.mysql.database.azure.com',
  'user':'root_social_kit@social-kit',
  'password':'Giraffe234',
  'database':'social-kit'
}

# Construct connection string
try:
   conn = pymysql.connect(**config)
   print("Connection established")
except pymysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("SELECT IGU, IGP FROM userTABLE WHERE userID = 1;")
print("Finished selecting list")

conn.commit()
cursor.close()
conn.close()
print("Done.")
  