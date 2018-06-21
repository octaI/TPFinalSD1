class APP:
    HOST = '0.0.0.0'
    PORT = 8080
    DEBUG = True


class DB:
    DRIVER = "cockroachdb"
    DATABASE = "Elections"
    USER = "user"
    HOST = "host"
    PORT = 26257
    SETTINGS = {
        'sslmode': 'disable'
    }
