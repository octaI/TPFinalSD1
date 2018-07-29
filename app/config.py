class APP:
    HOST = '0.0.0.0'
    PORT = 8080
    DEBUG = True


class DB:
    DRIVER = "cockroachdb"
    DATABASE = "Election"
    USER = "distribuidos"
    HOST = "roach-ui"
    PORT = 26257
    SETTINGS = {
        'sslmode': 'disable'
    }


class INIT:
    CREATE_CANDIDATES = False 
