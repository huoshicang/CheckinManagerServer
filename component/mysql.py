import pymysql
import pymysql.cursors


def GetConn():
    return pymysql.connect(
        host='47.115.206.215',
        user="fondlike",
        password="177155",
        database="gxy",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor  # 设置游标以返回字典格式数据
    )


def QueryDataFetchOne(sql, params=None):
    conn = None
    cur = None
    result = None
    try:
        conn = GetConn()
        cur = conn.cursor()

        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)

        result = cur.fetchone()
    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()
        except pymysql.Error as err:
            result = f"MySQL Error while closing connection: {err}"

    return result


def QueryDataFetchAll(sql, params=None):
    conn = None
    cur = None
    result = None
    try:
        conn = GetConn()
        cur = conn.cursor()

        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)

        result = cur.fetchall()
    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()
        except pymysql.Error as err:
            result = f"MySQL Error while closing connection: {err}"

    return result


def Update(Sql: str, params: tuple):
    conn = None
    cur = None
    message = None
    try:
        conn = GetConn()
        cur = conn.cursor()
        cur.execute(Sql, params)
        conn.commit()
        message = "操作成功"  # 更新成功或添加成功的情况

    except pymysql.Error as e:
        conn.rollback()  # 回滚事务
        message = f"操作失败:{e}"  # 更新失败或添加失败的情况

    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()

        except pymysql.Error as err:
            message = f"MySQL Error while closing connection: {err}"

    return message


def Indate(Sql: str, params: tuple):
    conn = None
    cur = None
    message = None
    try:
        conn = GetConn()
        cur = conn.cursor()
        cur.execute(Sql, params)
        conn.commit()
        message = "操作成功"  # 更新成功或添加成功的情况

    except pymysql.Error as e:
        conn.rollback()  # 回滚事务
        message = f"操作失败:{e}"  # 更新失败或添加失败的情况

    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()

        except pymysql.Error as err:
            message = f"MySQL Error while closing connection: {err}"

    return message
