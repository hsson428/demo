class AedlocationRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'demodb', 'user': 'root', 'password': 'PASSWORD', 'charset': 'utf8' }

    def select_aedlocation_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select num, Address from aedlocation where Address like %s"       # where DetailedAddress like %s 추가
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["num", "Address"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def select_aedlocation_by_num(self, num):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select num, DetailedAddress from aedlocation where num = %s"
        cursor.execute(sql, (num,))

        rows = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["num", "DetailedAddress"]
        result = []

        for row in rows:
            row_dict = {key:value for key, value in zip(keys, row)}
            result.append(row_dict)
            
        conn.close()

        return result