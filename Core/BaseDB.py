import pymysql

from Config import (
    DB,
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_CHARSET
)


class DBResult:
    Suc = False
    Result = None
    Err = None
    Rows = None

    def __init__(self):
        pass


class BaseDB:
    def __init__(self):
        self.dbConn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB, charset=DB_CHARSET,
                                      cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.dbConn.cursor()
        self.columns = []

    # Return DBResult
    def select(self, sql, params=None):
        r = DBResult()
        try:
            if params is None or len(params) == 0 or type(params) != dict:
                r.Rows = self.cursor.execute(sql)
            else:
                r.Rows = self.cursor.execute(sql, params)
            r.Result = self.cursor.fetchall() if r.Rows != 0 else []
            r.Suc = True
        except Exception as e:
            r.Err = e

        return r

    # Return DBResult
    def execute(self, sql, params=None):
        r = DBResult()
        try:
            if not params:
                r.Rows = self.cursor.execute(sql)
            else:
                r.Rows = self.cursor.execute(sql, params)
            r.Result = self.cursor.fetchall() if r.Rows != 0 else []
            r.Suc = True
            self.dbConn.commit()
        except Exception as e:
            r.Err = e
            self.dbConn.rollback()

        return r

    # Return DBResult
    def insert(self, sql, params=None):
        r = self.execute(sql, params)
        if not r.Suc:
            r.Result = -1
            return r
        r.Rows = self.cursor.execute("SELECT LAST_INSERT_ID()")
        r.Result = self.cursor.fetchone() if r.Rows != 0 else []

        return r

    # Return DBResult
    def getValue(self, sql, params=None):
        r = self.select(sql, params)
        if r.Suc:
            if r.Result:
                r.Result = r.Result[0]
            else:
                r.Result = -1
        return r

