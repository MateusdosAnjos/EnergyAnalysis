import messageModule as msg
import psycopg2

################################################################################
#                      DATABASE CONNECTION CONSTANTS                           #
################################################################################
DB_HOST = "localhost"
DB_NAME = "COMERC Database"
DB_USER = "postgres"
DB_PASS = "MyDatabase"

################################################################################
#                       DATABASE CONNECTION FUNCTIONS                          #
################################################################################
def connectToDatabase():
    try:
        DATABASE_CONNECTION = psycopg2.connect(
            host = DB_HOST,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        msg.databaseConnected()
        return DATABASE_CONNECTION
    except:
        msg.databaseFailedToConnect()
        return None
    return
