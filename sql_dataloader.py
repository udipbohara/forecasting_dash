



# import sqlite3

# # define connection and cursor

# connection = sqlite3.connect('app_data.db')

# cursor = connection.cursor()

# #create stores table

# comm = """CREATE TABLE IF NOT EXISTS consumptions(
#     region TEXT PRIMARY KEY 
#     consumption REAL,
#     date date, 
# )"""



# comm2 = """CREATE TABLE IF NOT EXISTS temperatures(
#     state TEXT PRIMARY KEY, 
#     region TEXT,
#     temperature REAL,
#     FOREIGN KEY (region) REFERENCES consumptions (region)
# )"""


# cursor.execute(comm)


# "INSERT INTO consumptions VALUES (?,?,?)", ()

# connection.commit() 


# '''

# #use objectrocket for heroku
# {
#     “region” : “NY”,
#     “timestamp_ns” : NumberLong(“1451606420000000000”),
#     "states" : ['NY']
#     “forecasts” : {
#         “daily” : {
#                    "last_updated": '2020-08-20',  #show the last updated values (daily for this, then for weekly do weekly)
#                    "values": [98.15664166391042]
#                    }
#         “weekly” : {"last_updated": '2020-08-20',
#                     "values": [85.53066998716453, 2, 3,4,5,6,7]
#                     }
#         “monthly” : {
#                     "last_updated": '2020-08-20',
#                     "values" :[85.53066998716453, 2, 3,4,5,6,7]
#                     }
#         "yearly" : {"last_updated": '2020-08-20',
#                    "values": [85.53066998716453, 2, 3,4,5,6,7,8,9,10]
#     },
#     “temperatures” : {
#         “past” : [12,3,4,5,6,12],
#         “forecast” : [43,1,2,5,6,12],
#         …
#     }
# }
# '''
# #the idea is to build a database, 
# #have forecasts in teh database? and then take it out to front it? to avoid delays?
# # have tables 1 day, 7 days, 1 month, 1 year ready
# # 

# #have tables 
# #have predictions stored in the tables
# #query from the tables for the predictions (faster?)
# #display it to the app after querying


# #sqlFormula = "insert into students (name, age) VALUES (%s, %s)"
# # many lines of data
# # data = [('a',b),
# #         ('c',2)]

# #mycursosr.executemany(sqlformula, students)



