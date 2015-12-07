# -*- coding: utf-8 -*-

import MySQLdb
import hashlib
from database.db import db


class ApplyDB:

    def __init__(self):
        self.connection = db.get_mysql().connect()
        self.connection.autocommit(True)

    def put(self, names, phones, university, gender):
        if not self.validate(phones):
            return '실패!'

        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT count(DISTINCT `group`) AS group_id FROM `apply`;")

        query = "INSERT INTO `apply` SET `group`='{0}', `name`='{1}', `phone`='{2}', `university`='{3}', `gender`='{4}';"
        group_id = cursor.fetchone()['group_id'] + 1

        cursor.close()
        for i in range(0, len(names)):
            cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(query.format(group_id, names[i], phones[i], university, gender))
            cursor.close()

        return None

    def validate(self, phones):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM `apply` WHERE `phone` IN ("
        for i in range(0, len(phones)):
            query = query + "'" + phones[i] + "', "
        query = query[:len(query) - 2] + ");"
        cursor.execute(query)

        if cursor.rowcount == 0:
            return True
        else:
            return False


apply_db = ApplyDB()
