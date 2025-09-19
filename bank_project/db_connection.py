import pymysql
def db_connection():
    return pymysql.connect(
        host = "localhost",
        user = "root",
        password = "gowthami@123",
        database = "HDFCbank"
        )
print("db connected succesfully")
