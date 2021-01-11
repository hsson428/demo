class AedlocationRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'demodb', 'user': 'root', 'password': 'PASSWORD', 'charset': 'utf8' }

    def select_aedlocation_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select buildAddress, buildPlace from aedlocation where buildAddress like %s"
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["buildAddress", "buildPlace"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def select_aedlocation_by_symbol(self, symbol):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select buildAddress, buildPlace from aedlocation where buildAddress like %s"
        cursor.execute(sql, (symbol,))

        row = cursor.fetchone() # 반환 값은 tuple (...)
        keys = ["buildAddress", "buildPlace"]
        
        result = { key:value for key, value in zip(keys, row) }
            
        conn.close()

        return result