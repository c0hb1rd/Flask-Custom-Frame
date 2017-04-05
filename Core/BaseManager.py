from Core.BaseDB import BaseDB

dbConn = BaseDB()


class BaseManager:

    def __init__(self, obj):
        self.table = obj.table()
        self.obj = obj

        self.insertKeyTmp = ", ".join(['`' + k + '`' for k in obj.insertKeys()])
        self.insertValueTmp = ", ".join(["%(" + k + ")s" for k in obj.insertKeys()])

        self.searchTmp = " OR ".join(
            ['`' + k + '`' + " like %(key)s" for k in obj.searchKeys()]
        )

        self.updateTmp = ", ".join(['`' + k + '`' + "=%(" + k + ")s" for k in obj.updateKeys()])

    def getAll(self, searchKey=None):
        if searchKey is None or searchKey == "":
            sql = '''SELECT * FROM `''' + self.table + '` ORDER BY `id` DESC'
            r = dbConn.select(sql)
        else:
            sql = '''SELECT * FROM `''' + self.table + '` WHERE %s ORDER BY `id` DESC' % self.searchTmp
            r = dbConn.select(sql, {'key': "%" + searchKey + "%"})
        return r

    def getAllLimit(self, start, end, searchKey=None):
        if searchKey is None or searchKey == "":
            sql = '''SELECT * FROM `''' + self.table + '` ORDER BY `id` DESC LIMIT %(start)s, %(end)s'
            r = dbConn.select(sql, {'start': start, 'end': end})
        else:
            sql = '''SELECT * FROM `''' + self.table + '` WHERE %s ORDER BY `id` DESC %s' % (self.searchTmp, "LIMIT %(start)s, %(end)s")
            r = dbConn.select(sql, {'key': "%" + searchKey + "%", 'start': start, 'end': end})
        return r

    def getCount(self, searchKey=None):
        if searchKey is None or searchKey == "":
            sql = '''SELECT count(`id`) FROM `''' + self.table + '`'
            r = dbConn.select(sql)
        else:
            sql = '''SELECT count(`id`) FROM `''' + self.table + '` WHERE %s' % self.searchTmp
            r = dbConn.select(sql, {'key': "%" + searchKey + "%"})
        if r.Rows > 0:
            return r.Result[0]['count(`id`)']
        else:
            return r.Rows

    def get(self, objID):
        sql = '''SELECT * FROM `''' + self.table + '''` WHERE `id` = %(objID)s'''
        r = dbConn.select(sql, {'objID': objID})
        return r

    def delete(self, objID):
        sql = '''DELETE FROM `''' + self.table + '''` WHERE `id` = %(objID)s'''
        r = dbConn.execute(sql, {'objID': objID})
        return r

    def update(self, params):
        sql = '''UPDATE `''' + self.table + '''` SET %s WHERE %s''' % (self.updateTmp, '`id` = %(objID)s')
        r = dbConn.execute(sql, params)
        return r

    def add(self, params):
        sql = '''INSERT INTO `''' + self.table + '''`(%s) VALUES(%s)''' % (self.insertKeyTmp, self.insertValueTmp)
        r = dbConn.insert(sql, params)
        return r
