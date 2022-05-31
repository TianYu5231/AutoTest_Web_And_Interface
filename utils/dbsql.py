# coding=utf-8
# @Author: yutian
# @Version: Python 3.7
# @File: dbsql.py
# @Date: 2022/5/30 22:06
# @SoftWare: PyCharm
import pymysql

from common.readyaml import read_yaml
from utils.logger import log


class DBMysql(object):
    """封装mysql"""
    def __init__(self, db_name):
        self.__db_info = read_yaml.load_yml()[db_name]
        self.__host = self.__db_info['host']
        self.__port = self.__db_info['port']
        self.__user = self.__db_info['user_name']
        self.__password = self.__db_info['password']
        self.__database = self.__db_info['db_name']
        try:
            self.__conn = pymysql.connect(host=self.__host, port=self.__port, user=self.__user,
                                          password=self.__password, database=self.__database)
            self.__cursor = self.__conn.cursor()
        except Exception as e:
            log.error('数据库连接错误: {}, \n {}'.format(self.__db_info, e))

    def _close_db(self):
        """关闭数据库"""
        log.info('断开数据库连接')
        self.__cursor.close()
        self.__conn.close()

    def query(self, sql):
        """数据库查询功能"""
        if not sql.startswith('select'):
            log.error('非select语句不能执行query: {}'.format(sql))
        log.info('执行sql:{}'.format(sql))
        try:
            self.__cursor.execute(sql)
        except Exception as e:
            log.error(e)
        query_result = self.__cursor.fetchall()
        log.info('查询结果:{}'.format(query_result))
        self._close_db()
        return query_result


db_domain = DBMysql('learnJDBC')
if __name__ == '__main__':
    db_domain.query('select * from students')
