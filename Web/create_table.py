# importing required libraries

import mysql.connector

  

dataBase = mysql.connector.connect(

  host ="localhost",

  user ="root",

  passwd ="",

  database = "hdsd"
)
 
# preparing a cursor object

cursorObject = dataBase.cursor()

  
# creating table 

studentRecord = """CREATE TABLE STUDENT (

                   NAME  VARCHAR(20) NOT NULL,

                   EMAIL VARCHAR(50)

                   )"""

  
# table created
cursorObject.execute(studentRecord) 

  
# disconnecting from server
dataBase.close()