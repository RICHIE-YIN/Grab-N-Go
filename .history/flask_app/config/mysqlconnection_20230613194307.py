import os
import pymysql.cursors
from urllib.parse import urlparse

class MySQLConnection:
    def __init__(self, db):
        url = urlparse(os.getenv('CLEARDB_DATABASE_URL'))
        user = url.username
        password = url.password
        hostname = url.hostname
        db = url.path[1:]

        connection = pymysql.connect(host=hostname,
                                    user=user, 
                                    password=password, 
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
        self.connection = connection
    ...
